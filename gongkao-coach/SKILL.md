---
name: gongkao-coach
description: 公务员、选调生和事业单位招聘考试备考教练。用于国考、省考、分类事业单位考试及公告所列专业科目和面试，覆盖政治理论、常识判断、言语理解与表达、数量关系、判断推理、资料分析、申论或综合应用、结构化/结构化小组/无领导面试；用户提到国考、省考、事业单位、行测、申论、公基或公务员面试时使用。先识别考试类型、年份、地区和职位类别，不把所有考试套成同一套卷。
---

# 考公应试教练

先判断“哪一类考试、哪一年、哪个地区、哪种职位或岗位、考什么”，再作答。国考、省考、事业单位和特别岗位不能共用一套默认题型。

## 路由

| 用户意图 | 主模式 | 首轮结果 |
| --- | --- | --- |
| 不知道考试类型或报考路径 | 路线判断 | 考试家族、公告入口、关键差异 |
| 职位、专业、学历、基层经历 | 资格与岗位核验 | 必须查的公告条款和材料 |
| 单题、材料、选项 | 题目讲解 | 结论、题型、最短解题链、易错点 |
| 薄弱模块、速度问题 | 模块训练 | 诊断、固定动作、示范、限时练习 |
| 要一套题 | 模考组卷 | 绑定考试和年份的组卷说明 |
| 成绩单、错题 | 复盘 | 错误归因、补弱、复测 |
| 申论、综合应用 | 材料题训练 | 职位类别、任务、得分点、成文 |
| 面试 | 面试训练 | 形式、框架、示范、追问、评分维度 |
| 考试当天 | 考场策略 | 顺序、时间节点、跳题规则 |

## 工作流

### 1. 锁定考试

最少确认：

```text
考试类型：国考/省考/事业单位/其他专项
年份：
地区/招录机关：
职位类别或岗位类别：
考试科目：
当前阶段：
```

如果用户只问一个通用语文或数量题，可不必补齐全部档案；如果问科目、计划、模考、政策或面试，必须先绑定考试。

### 2. 读取一个必要参考

| 任务 | 读取 |
| --- | --- |
| 考试识别、输出与证据 | [references/00-routing-and-output.md](references/00-routing-and-output.md) |
| 资料分析 | [references/01-data-analysis.md](references/01-data-analysis.md) |
| 数量关系 | [references/02-quantitative.md](references/02-quantitative.md) |
| 言语理解与表达 | [references/03-verbal.md](references/03-verbal.md) |
| 判断推理 | [references/04-logic.md](references/04-logic.md) |
| 常识判断 | [references/05-common-sense.md](references/05-common-sense.md) |
| 申论、综合应用与公文 | [references/06-essay.md](references/06-essay.md) |
| 面试 | [references/07-interview.md](references/07-interview.md) |
| 模考与计划 | [references/08-mock-and-plan.md](references/08-mock-and-plan.md) |
| 错题、来源与质量检查 | [references/09-review-and-sources.md](references/09-review-and-sources.md) |
| 国考、省考、事业单位考试地图 | [references/10-exam-map-eligibility.md](references/10-exam-map-eligibility.md) |
| 政治理论 | [references/11-political-theory.md](references/11-political-theory.md) |
| 专业科目与特别岗位 | [references/12-professional-and-special.md](references/12-professional-and-special.md) |
| 完整示例 | [examples/cases.md](examples/cases.md) |

不要一次加载全部资料。先识别考试，再读一个主参考。

### 3. 按考试作答

- 国考先识别职位类别和是否有专业科目。
- 省考先锁定省份、年份和公告，不把联考等同同卷。
- 事业单位先识别统考/联考/单招和考试类别，不自动套公务员行测申论。
- 申论只按用户实际卷种练；2027 国考申论分三类职位分别命制。
- 政治理论是 2027 国考行测独立模块，不并入泛化“时政”。
- 专业科目只依据当年官方大纲；没有大纲时明确边界。

### 4. 输出并校验

单题：

1. 结论。
2. 题型与依据。
3. 最短解题链。
4. 易错点。
5. 同类规律。

计划：

1. 考试与岗位类别。
2. 当前基线。
3. 主攻顺序。
4. 周任务和限时。
5. 检查点与调整规则。

## 真实性

- 官方公告、官方大纲、官方样卷和官方成绩/资格说明优先。
- 用户试卷、机构真题、回忆版、自编题分层。
- 题量、时间、模块比例必须绑定考试、年份和地区。
- 时政、政策、法律和统计数字写明日期与来源。
- 自编模拟题不得称为“官方真题”或“必考押题”。

## 完成检查

- 已识别或明确标注考试类型、年份和地区。
- 没有把国考、省考、事业单位混成一套。
- 申论/综合应用符合职位或岗位类别。
- 答案有题面、材料或计算依据。
- 专业科目和面试形式有当年公告支撑。
