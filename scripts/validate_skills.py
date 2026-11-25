#!/usr/bin/env python3
"""Validate the six Skill packages and their downloadable archives."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = (
    "kaoyan-coach",
    "teacher-qualification-coach",
    "cet4-coach",
    "cet6-coach",
    "gongkao-coach",
    "fakao-coach",
)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
IGNORED_PACKAGE_FILES = {".DS_Store", "Thumbs.db"}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter is not closed")

    values: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        if not raw_line.strip() or raw_line[:1].isspace():
            continue
        if ":" not in raw_line:
            raise ValueError(f"Invalid frontmatter line: {raw_line}")
        key, value = raw_line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def source_files(root: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name in IGNORED_PACKAGE_FILES:
            continue
        relative = path.relative_to(root).as_posix()
        files[relative] = path.read_bytes()
    return files


def check_skill(skill_name: str) -> list[str]:
    errors: list[str] = []
    root = ROOT / skill_name
    skill_file = root / "SKILL.md"

    if not skill_file.is_file():
        return [f"{skill_name}: missing SKILL.md"]
    if not (root / "README.md").is_file():
        errors.append(f"{skill_name}: missing README.md")
    if not (root / "references").is_dir():
        errors.append(f"{skill_name}: missing references directory")
    if not (root / "examples" / "cases.md").is_file():
        errors.append(f"{skill_name}: missing examples/cases.md")

    text = skill_file.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_name}: {exc}"]

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if name != skill_name or not NAME_RE.fullmatch(name):
        errors.append(f"{skill_name}: invalid or mismatched name '{name}'")
    if not description:
        errors.append(f"{skill_name}: missing description")
    if len(description) > 1024:
        errors.append(f"{skill_name}: description exceeds 1024 characters")

    for markdown in root.rglob("*.md"):
        for target in LINK_RE.findall(markdown.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#")):
                continue
            target_path = (markdown.parent / target.split("#", 1)[0]).resolve()
            if not target_path.exists():
                errors.append(f"{markdown.relative_to(ROOT)}: missing link target {target}")

    archive = ROOT / "dist" / f"{skill_name}.skill"
    if not archive.is_file():
        errors.append(f"{skill_name}: missing {archive.relative_to(ROOT)}")
        return errors

    expected_files = source_files(root)
    expected_archive_names = {
        f"{skill_name}/{relative}" for relative in expected_files
    }
    try:
        with zipfile.ZipFile(archive) as bundle:
            names = set(bundle.namelist())
            missing = expected_archive_names - names
            extra = {
                name
                for name in names
                if name not in expected_archive_names
                and not name.endswith("/")
                and Path(name).name not in IGNORED_PACKAGE_FILES
            }
            if missing:
                errors.append(
                    f"{skill_name}: archive missing {', '.join(sorted(missing))}"
                )
            if extra:
                errors.append(
                    f"{skill_name}: archive contains unexpected files "
                    f"{', '.join(sorted(extra))}"
                )
            if bundle.testzip() is not None:
                errors.append(f"{skill_name}: archive CRC check failed")

            for relative, source_bytes in expected_files.items():
                archive_name = f"{skill_name}/{relative}"
                if archive_name not in names:
                    continue
                if bundle.read(archive_name) != source_bytes:
                    errors.append(
                        f"{skill_name}: archive file differs from source: {relative}"
                    )
    except zipfile.BadZipFile:
        errors.append(f"{skill_name}: archive is not a valid ZIP")

    return errors


def main() -> int:
    errors: list[str] = []
    for skill_name in SKILLS:
        errors.extend(check_skill(skill_name))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validation passed: "
        f"{len(SKILLS)} skills, all links, and {len(SKILLS)} installable archives."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
