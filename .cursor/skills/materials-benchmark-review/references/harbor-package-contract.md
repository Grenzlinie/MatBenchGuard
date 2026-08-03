# Harbor 题包与文件角色

## 1. Paper2Arm profile

```text
paper-xxx/
├── instruction.md                # 唯一 solver-visible 题面
├── paper/paper.md                # 仅供 Author/Review/Repair
├── manifest.json
├── steps.json                    # Workflow 的结构化镜像
├── resources.json                # 资源声明/部署映射
├── task.toml
├── environment/
├── tests/
│   ├── grading_spec.json
│   ├── checker.py
│   ├── test.sh
│   └── Gold/fixture
└── solution/                     # Review/Repair 完全排除
```

本 profile 固定输出根目录为 `/app/outputs`。`test.sh` 必须向 `/logs/verifier/reward.txt` 或 `reward.json` 写数值 reward。

## 2. 可见性与权威顺序

| 文件 | solver 可见 | Review/Repair 可读 | 角色 |
|---|---:|---:|---|
| `instruction.md` | 是 | 是 | 科学题面和公开输出合同 |
| `paper/paper.md` | 否 | 是 | 科学事实、Gold、关系和参数来源 |
| `steps.json` 等派生视图 | 否 | 是 | 实现题面，不得补题 |
| `resources.json` | 否 | 是 | 资源身份、locator 和部署映射 |
| `tests/**` | 否 | 是 | 隐藏验收、Gold、精确容差 |
| `solution/**` | 否 | 否 | 完全排除 |

冲突处理顺序：论文裁决科学事实；先修/重写 `instruction.md`；再同步派生视图；最后生成 grading、Gold、checker 和 test。

## 3. 题面不是文献阅读任务

`paper.md` 不会交给 solver。题面不得写“阅读原文”“查看 Fig./Table/Section”“根据 paper.md 补参数”或“复述作者结论”。Author 必须先从论文抽取自包含科学问题，把论文已给且完成任务必需的对象、条件、步骤、公式、参数、数据、单位和输出要求直接写入题面。

论文 locator 只留在 reviewer-side provenance，不能成为 solver action。

## 4. 必要信息与 solver agency

题面必须明确：

- 科学对象、目标量、体系和固定条件；
- 论文给出的关键方法、公式、参数和步骤；
- 哪些执行细节由 solver 选择或收敛；
- Workflow 每步的输入、输出和依赖；
- 每个公开文件/checkpoint 的路径、格式、schema、单位、主键、基数和枚举；
- 评分关注绝对值、关系、趋势还是内部一致性。

若任务要求多组体系/条件/参数，题面还必须公开完整组集合、稳定组标识和每组条件签名。checker 可为不同组使用不同隐藏 Gold/容差，但不能隐藏“哪些组必须提交”，也不能把多组要求缩成任选一组。

“自包含”不等于给出标准答案教程，也不等于替论文补参数。论文未报告的执行细节不是不可复现证据；checker 应用容差、收敛或不变量接受合法实现差异。

## 5. Assets 与可获得性

题面 `Assets` 必须让外部 Agent 知道必需资源的身份和取得方式：

- `BUNDLED`：文件随题包/工作目录提供；
- `PUBLIC_URL`：给出稳定公开 locator；
- `RUNTIME_PROVIDED`：环境明确提供；
- `GENERIC_EQUIVALENT`：允许等价工具或独立重实现。

内部镜像 ID、挂载细节和平台 API 不必暴露。若数据或特定代码不可替代，且没有任何上述取得方式，题包拒绝。若论文方法足以独立实现，则原作者代码不是必需资产。若论文通过成分、晶系/空间群、晶格参数或构造方法定义结构，solver 可自行建模时，CIF/POSCAR 也不是必需资产；只有评分依赖不可重建的固定原子级 realization 时才必须提供结构文件。临时网络错误只说明当前无法验证，不能冒充永久不可用。

## 6. 拿走论文测试

删除 `paper/` 后，题面仍应是一道完整的计算、建模或分析题；删除任何被保留的 Workflow step 或中间产物后，若下游输入断裂或题意变得有歧义，则该内容属于必要合同，不能以“减少引导”为由删除。
