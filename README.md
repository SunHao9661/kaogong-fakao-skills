# 考公 × 法考 Agent Skills

公开仓库：<https://github.com/SunHao9661/kaogong-fakao-skills>

两个功能同构、科目独立的备考 Skill：

- **gongkao-coach**：公务员考试与考编，覆盖行测、申论和结构化面试。
- **fakao-coach**：国家统一法律职业资格考试，覆盖客观题、主观题和各部门法。

两个 Skill 都支持单题解析、模块训练、模拟卷、备考规划、错题复盘和考场策略。所有自编内容都会标注为模拟题；考试结构、时政、法条和程序期限要求查询官方最新来源。

## 立即下载

- [下载考公 Skill](dist/gongkao-coach.skill)
- [下载法考 Skill](dist/fakao-coach.skill)
- [阅读视频与公考 Skill 分析](VIDEO_ANALYSIS.md)

`.skill` 文件是 ZIP 格式的技能包，可直接交给支持 Agent Skills 的工具导入，也可解压后放入 Skills 目录。

## 安装

### 方式一：导入 `.skill`

在支持 `.skill` 导入的 Agent 中选择对应文件：

```text
dist/gongkao-coach.skill
dist/fakao-coach.skill
```

### 方式二：目录安装

解压后，把两个目录放进 Agent 的 Skills 根目录。以 Codex 为例：

```text
~/.codex/skills/gongkao-coach/
~/.codex/skills/fakao-coach/
```

### 方式三：下载源码

```bash
git clone https://github.com/SunHao9661/kaogong-fakao-skills.git
cp -R kaogong-fakao-skills/gongkao-coach ~/.codex/skills/
cp -R kaogong-fakao-skills/fakao-coach ~/.codex/skills/
```

## 使用

安装后直接使用自然语言：

```text
这道资料分析怎么做，给我最短步骤和易错点。
根据我的正确率和每天 3 小时，排一份 8 周考公计划。
按当年大纲出一套自编法考混合模拟题，标明不是官方真题。
批改这份法考主观题答案，按争点、法源、事实适用和结论反馈。
```

## 功能结构

| 能力 | 考公 | 法考 |
| --- | --- | --- |
| 单题解析 | 行测与申论 | 客观题与案例 |
| 模块训练 | 资料、数量、言语、判断、常识 | 民法、刑法、程序、行政、商经知、理论、三国法 |
| 模拟组卷 | 行测/申论 | 客观题/主观题 |
| 规划复盘 | 阶段计划、错题归因 | 客观主观协同、批改重写 |
| 真实性控制 | 真题/模拟题区分 | 法律/司法解释/学理观点区分 |

## 仓库结构

```text
.
├── gongkao-coach/
│   ├── SKILL.md
│   ├── README.md
│   ├── examples/
│   └── references/
├── fakao-coach/
│   ├── SKILL.md
│   ├── README.md
│   ├── examples/
│   └── references/
├── dist/
│   ├── gongkao-coach.skill
│   └── fakao-coach.skill
├── scripts/
│   └── validate_skills.py
└── VIDEO_ANALYSIS.md
```

## 验证

本地运行：

```bash
python3 scripts/validate_skills.py
```

校验内容包括：

- `SKILL.md` frontmatter。
- 名称格式和必需字段。
- 所有仓库内 Markdown 链接。
- 两个 `.skill` 安装包是否存在且内容完整。

GitHub Actions 会在每次提交后自动执行同一检查。

## 开源许可

本项目使用 [MIT License](LICENSE)。你可以使用、复制、修改、合并、发布、分发、再许可和销售本项目，只需保留版权与许可声明。

## 使用边界

- 本项目是备考训练工具，不是官方考试机构产品。
- 自编题目不会冒充官方真题。
- 官方考试信息以国家公务员局、地方组织/人社部门、司法部及当年考试大纲为准。
- 法条序号、程序期限和司法观点未核实时不会给出精确值。
- 法考内容用于考试学习，不构成正式法律意见。

## 参考与独立性

视频与公开仓库分析见 [VIDEO_ANALYSIS.md](VIDEO_ANALYSIS.md)。本项目保留同类“技能包 + 按需知识文件 + 实战示例”的产品结构，但工作流、参考资料和实现文本均为独立编写，与视频作者及原仓库无隶属关系。
