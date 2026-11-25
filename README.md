# 六项备考 Agent Skills

六个可独立安装、独立触发的考试备考 Skill：

| Skill | 覆盖 |
| --- | --- |
| `kaoyan-coach` | 考研路线、择校、政治、英语一/二、数学一/二/三、统考与自命题专业课、复试、调剂 |
| `teacher-qualification-coach` | 教师资格证类别、笔试、科目三、面试、重考和认定准备 |
| `cet4-coach` | 四级笔试、新闻听力、阅读、写作、翻译、四级口语和重考 |
| `cet6-coach` | 六级笔试、讲座听力、复杂阅读、长段翻译、六级口语和刷分 |
| `gongkao-coach` | 国考、省考、事业单位、政治理论、行测模块、申论/综合应用、专业科目和面试 |
| `fakao-coach` | 法考资格、客观题、主观题、年度线、法源版本、案例、文书和计划 |

每个 Skill 都按“先识别考试和版本，再按需读取参考资料”的方式设计。不会把不同考试、不同卷种或不同年份的规则混用。

## 安装

### 直接下载

- [考研 Skill](https://github.com/SunHao9661/kaogong-fakao-skills/releases/download/v2.0.0/kaoyan-coach.skill)
- [教师资格证 Skill](https://github.com/SunHao9661/kaogong-fakao-skills/releases/download/v2.0.0/teacher-qualification-coach.skill)
- [四级 Skill](https://github.com/SunHao9661/kaogong-fakao-skills/releases/download/v2.0.0/cet4-coach.skill)
- [六级 Skill](https://github.com/SunHao9661/kaogong-fakao-skills/releases/download/v2.0.0/cet6-coach.skill)
- [考公 Skill](https://github.com/SunHao9661/kaogong-fakao-skills/releases/download/v2.0.0/gongkao-coach.skill)
- [法考 Skill](https://github.com/SunHao9661/kaogong-fakao-skills/releases/download/v2.0.0/fakao-coach.skill)

### 导入 `.skill`

仓库中的安装包位于 `dist/`：

```text
dist/kaoyan-coach.skill
dist/teacher-qualification-coach.skill
dist/cet4-coach.skill
dist/cet6-coach.skill
dist/gongkao-coach.skill
dist/fakao-coach.skill
```

`.skill` 是 ZIP 格式安装包。可直接导入支持 Agent Skills 的工具。

### 目录安装

```text
~/.codex/skills/kaoyan-coach/
~/.codex/skills/teacher-qualification-coach/
~/.codex/skills/cet4-coach/
~/.codex/skills/cet6-coach/
~/.codex/skills/gongkao-coach/
~/.codex/skills/fakao-coach/
```

## 使用示例

```text
2027 考研英语二和数学三怎么安排 12 周？
初中数学教师资格证科目三怎么准备？
四级 425 算及格吗？
六级讲座听力总是跟不上，给我一个精听流程。
2027 国考行政执法类申论怎么练？
2026 法考客观题多少分合格？
```

## 设计原则

- **独立安装**：六个 Skill 互不作为必需依赖。
- **先路由再作答**：先识别考试、年份、地区、卷种、学段或职位类别。
- **渐进加载**：入口只保留关键约束，详细方法放在对应参考文件。
- **来源分层**：官方材料、用户真题、第三方整理和自编模拟题分开。
- **缺口不猜**：动态政策、院校自命题、地方资格和法源版本无法核实时明确说明。

## 明确边界

- 全国统考考研英语只有英语一、英语二，没有“英语三”；数学有数学一、二、三。
- 教师资格证不是教师招聘、特岗或教师编。
- CET 不设官方及格线；425 是目标点、常见报名或使用门槛。
- 国考、省考、事业单位不是同一套卷。
- 法考不公布试题及参考答案，回忆版不能冒充官方原卷。
- 法考年度合格线不能永久化。
- 本项目不是考试机构官方产品，也不宣称收录全部历史真题。

## 验证

```bash
python3 scripts/validate_skills.py
```

验证内容：

- 六个 `SKILL.md` frontmatter 和名称。
- 所有仓库内 Markdown 链接。
- 六个安装包存在、CRC 正常。
- 包内文件与源目录一致。
- 不包含额外缓存或用户 ZIP。

本次制作的完整验证结果见 [research/validation-report.md](research/validation-report.md)。

系统 Skill 校验器还会分别检查六个目录：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py kaoyan-coach
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py teacher-qualification-coach
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cet4-coach
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py cet6-coach
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py gongkao-coach
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py fakao-coach
```

## 开源许可

本项目使用 [MIT License](LICENSE)。你可以使用、复制、修改、合并、发布、分发、再许可和销售本项目，但需保留版权与许可声明。
