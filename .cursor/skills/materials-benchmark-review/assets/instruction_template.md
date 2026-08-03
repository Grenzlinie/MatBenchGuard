# <Task title>

> Authoring rule: the solver cannot see `paper/paper.md`. Include every paper-reported fact, parameter, formula, and method step that is necessary to define the scientific target or keep the workflow unambiguous. Do not invent paper-unreported execution settings. Do not turn the task into information extraction, formula substitution, or a solution tutorial.

## Problem background

说明材料体系、科学问题和计算意义；不要要求阅读论文，不要泄露被评分答案。

## Approach

给出论文支持且定义目标所必需的方法、公式、固定条件和步骤。明确哪些网格、软件、求解器或收敛选择由 solver 决定。删除任何内容前确认不会造成中间产物消失、Workflow 断裂或题意歧义。

## Reproduction target

定义目标量、体系、条件、范围、单位和预期绝对值/关系类型。直接复现使用适用的 paper Gold；smoke/改条件必须说明为什么 paper relation 仍适用。若要求多套条件，为每套条件公开稳定 `condition_group_id` 和完整参数签名；不要把多组缩成“任选一组”。

## Assets

- `<resource role>`：`bundled file / public URL / runtime-provided / allowed equivalent`。
- 若无需外部资源，写 `No external assets are required.`

不可替代数据、模型、势、固定结构快照或特定代码必须有真实取得方式。论文只给成分、晶系/空间群、晶格参数或建模方法时，应把这些信息完整写入题面并允许 solver 构建/优化结构；不要因为没有 CIF 而虚构资产要求。不要暴露只对内部平台有意义的镜像或挂载细节。

## Workflow steps

### Step 1: <scientific purpose>

- Role: `scored` / `checked_result` / `process`
- Required input: <题面输入或前一步产物>
- Action boundary: <必须完成的科学操作；不替 solver 规定论文未给的唯一实现>
- Paper-backed fixed information: <必要公式、参数、方法步骤>
- Solver-selectable choices: <实现、网格、收敛等>
- Output file: `/app/outputs/<file>`
- Downstream consumer: <后续 step/checker；不能是孤立产物>
- Contract: <format、schema、单位、主键、基数、枚举>
- Scoring: <如何作为核心 Gold 或可选公开结果检查被验证>

## Output files

在计算前创建 `/app/outputs`，写入所有 scored artifacts；Enhanced 如需额外结果检查，也必须在此公开：

- `/app/outputs/<file>`

## Output contract

### <file>

- path: `/app/outputs/<file>`
- format: `<format>`
- purpose: `scored` / `checked_result`
- target policy: `paper_direct` / `unique_recompute` / `paper_supported_relation`
- condition groups: <公开全部必需 `condition_group_id`、每组完整条件签名，以及该行/记录如何标识所属组>
- rows/cardinality: <exact or justified range>
- primary key: <if tabular>
- schema: <fields, types, units, enums>
- scientific meaning: <为何正确求解必然产生；若是 Enhanced，checker 如何廉价重算/交叉检查>

## Self-check before finishing (optional, not scored)

只给 shape、有限值、主键和内部关系自检；不要追加标准解法教程。

## How you are scored

说明 verifier 检查的公开 artifacts、绝对值/关系/不变量与组件权重。Baseline 可以只比较 Gold；Enhanced 的 Gold 必须占 60--80%，轻量结果检查占 20--40%。多条件组任务要声明全部组都会被检查；Gold 和精确容差可以隐藏，提交要求不能隐藏。
