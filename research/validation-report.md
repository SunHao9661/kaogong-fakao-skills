# 六项备考 Skill 验证报告

验证日期：2026-11-25

结论：六个源目录和六个 `.skill` 安装包均通过机械验证；关键考试规则通过内容契约检查。

## 源目录

```text
kaoyan-coach/
teacher-qualification-coach/
cet4-coach/
cet6-coach/
gongkao-coach/
fakao-coach/
```

共 78 个文件。

## 系统 Skill 校验

对六个目录分别运行：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>
```

结果：6/6 通过。

检查项包括：

- frontmatter。
- `name` 与目录一致。
- 命名格式。
- 未完成脚手架占位。

## 仓库验证

运行：

```bash
python3 scripts/validate_skills.py
```

结果：

```text
Validation passed: 6 skills, all links, and 6 installable archives.
```

检查项包括：

- 六个 `SKILL.md`、`README.md`、`references/`、`examples/cases.md`。
- 所有仓库内 Markdown 相对链接。
- 六个安装包存在。
- ZIP CRC。
- 包内每个文件与源目录逐字节一致。
- 包内无意外缓存文件。

## 内容契约检查

| Skill | 关键规则 | 结果 |
| --- | --- | --- |
| `kaoyan-coach` | 英语一/二区分；明确没有全国统考英语三；数学一/二/三区分 | 通过 |
| `teacher-qualification-coach` | 报告分 120、70 合格；笔试 2 年、合格证明 3 年；教资与教师招聘分离 | 通过 |
| `cet4-coach` | 125 分钟、57 题、710 分；不设官方及格线；新闻听力结构 | 通过 |
| `cet6-coach` | 130 分钟、57 题、710 分；讲座听力；150 词写作；180—200 字翻译 | 通过 |
| `gongkao-coach` | 政治理论独立；申论三类；省考先锁省份；事业单位不套公务员卷 | 通过 |
| `fakao-coach` | 2026 客观题线 180；2026 主观题线待官方公告；不公布试题答案；法源时间点 | 通过 |

## 安装包

| 文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `dist/kaoyan-coach.skill` | 22517 | `89a9784be10985596ae5a13b1d3e4e4ad5fc53caf34bf26fc6d150c53cba9fe4` |
| `dist/teacher-qualification-coach.skill` | 16797 | `12def96e413c533e028b76d6de61d553f16b0ac42d9d7d79aed8142ea6bc54f4` |
| `dist/cet4-coach.skill` | 15106 | `1b5a1789595e9bd03cf569ce4969945811d3c46039f1c54a563267657edb2a4a` |
| `dist/cet6-coach.skill` | 14824 | `b419fae02a190e35893fae1011cb184531a018cd80359ccf182b5fa0b58da0bb` |
| `dist/gongkao-coach.skill` | 23806 | `9a685502f63d4ef68b1a7a57ea3016de90aa618ae984184cb60beabcc3fbc2c7` |
| `dist/fakao-coach.skill` | 20790 | `d9396e96b8713ba29f6fd3de41783173c5a77723e239d023740e52d5e05c4c77` |

## 发布前整库审计

审计范围：README、MIT License、GitHub Actions、验证脚本、六个 Skill 源目录、六个安装包、研究底稿和未跟踪文件边界。

结果：

- 必须修复：无。
- 已修复：README 增加六个 `v2.0.0` Release 直链。
- 已修复：旧视频分析增加范围说明，避免仍被理解为仓库只有两个 Skill。
- 已修复：忽略用户保留的三个历史 ZIP，防止误提交。
- 已修复：移除一个当时无法解析域名的法院来源链接，保留最高人民法院官方入口。
- 已清理：验证过程生成的 `__pycache__`，不会提交。

外部来源抽查：

- 61 个唯一链接完成访问检查。
- 可公开访问的官方页面返回 200。
- 部分 NEEA、司法部、最高检页面对自动请求返回 403 或 302，这是网站反爬或跳转行为；此前人工抓取已验证正文。
- 一个无法解析的重复法院站点链接已删除。

最终测试：

- 六个系统 Skill 校验通过。
- 仓库验证脚本通过。
- 六个 ZIP CRC 通过。
- 将六个 ZIP 解压后再次执行系统 Skill 校验，6/6 通过。
- 六个关键考试规则契约检查通过。

## 未执行或不在范围内的操作

- 未安装到 `~/.codex/skills/`；当前交付是仓库源目录和 `.skill` 安装包。
- 未发布 GitHub Release。
- 未内置完整历史题库。
- 未修改用户已有的以下未跟踪 ZIP：
  - `dist/gongkao-coach_01.zip`
  - `dist/fakao-coach_01.zip`
  - `dist/gongkao-exam-coach.zip`

## 时效说明

- 2027 考研、2027 国考和 2026 法考规则是当前制作时点的官方快照。
- 报名时间、考试结构、年度线、地方资格和法源变化应在使用时重新核验。
- Skill 已把这些内容设计为“年度快照”，没有写成永久规则。
