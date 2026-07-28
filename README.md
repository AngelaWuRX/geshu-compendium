# Fullstack AI Engineer Notes Vault

## 一、它到底是什么

这不是：

* 课堂笔记博客
* 收藏链接的网站
* AI自动生成的知识库
* 为了显得懂很多而堆概念的portfolio

它应该同时是四样东西：

**你的第二大脑**
存下课程、项目、debug过程和技术判断。

**工程手册**
以后忘记怎么设计auth、streaming、queue、RAG或evaluation时，可以回来直接查。

**可运行的实验室**
读者不只看代码，还能改参数、运行、破坏和观察结果。

**能力证明**
别人点进来，看到的不只是“学过React和LLM”，而是你能从数据库、API、前端交互一直做到模型调用、评估和部署。

网站的核心句可以是：

> Notes, experiments, and production patterns for building fullstack AI systems.

---

## 二、课程是输入，不是网站导航

你私下可以继续按学校课程存档：

```text
courses/
  cs101/
  databases/
  operating-systems/
  machine-learning/
  distributed-systems/
  web-development/
```

但公开网站重新组织成能力地图：

```text
foundations/
frontend/
backend/
data/
systems/
ai-engineering/
production/
projects/
```

例如数据库课里的内容，不只留在“Database Course”。

它会被拆到：

* Data Modeling
* Indexes and Query Plans
* Transactions
* Connection Pooling
* Vector Search
* Database-backed Queues
* Multi-tenant Data Isolation

机器学习课则会被拆到：

* Optimization
* Embeddings
* Classification
* Calibration
* Evaluation
* Distribution Shift
* Training vs Inference
* Retrieval Systems

这样网站不是“我修过哪些课”，而是“我已经建立了哪些工程能力”。

---

# 三、一级知识结构

## 1. Foundations

所有后续系统都依赖的底层东西。

* Python
* TypeScript
* Data structures and algorithms
* Git and version control
* Linux and shell
* Processes and concurrency
* Networking
* HTTP
* Security fundamentals
* Probability and statistics
* Linear algebra
* Optimization

这里不追求重新写一本教材。

只记录对工程真正有影响的部分。

比如学概率时，不只写Bayes公式，而是连接到：

* classifier confidence
* spam filtering
* ranking
* hallucination detection
* online experiments
* model evaluation

## 2. Frontend Engineering

* React mental model
* Server and client components
* State management
* Forms and validation
* Streaming UI
* Optimistic updates
* Accessibility
* Design systems
* Performance
* Browser storage
* Offline behavior
* Testing

AI产品特有的前端内容单独强调：

* token streaming
* partial structured output
* tool-call progress
* interrupt and resume
* citation rendering
* message branching
* human approval UI
* long-running task state
* generated artifact previews

## 3. Backend Engineering

* API design
* Authentication and authorization
* Background jobs
* Queues
* Webhooks
* Rate limiting
* Caching
* Idempotency
* File uploads
* Real-time systems
* Observability
* Error handling
* API testing

每一篇都不能只停在“怎么写”。

还要回答：

* 为什么需要它
* 什么时候不需要
* 它会在哪里失败
* 如何测试
* 如何观察生产状态
* 如何恢复

## 4. Data Systems

* PostgreSQL
* Schema design
* Transactions
* Indexing
* Query planning
* Migrations
* Object storage
* Redis
* Event logs
* Analytics
* Vector databases
* Hybrid search
* Data retention
* Privacy and deletion

AI系统的数据结构需要单独记录：

```text
users
conversations
messages
runs
tool_calls
artifacts
documents
chunks
embeddings
evaluations
feedback
usage_events
```

不能只会把所有东西塞进一个`messages` JSON字段。

## 5. AI Engineering

这是网站最核心的一层。

### Model interfaces

* text generation
* structured generation
* streaming
* tool calling
* multimodal input
* model routing
* fallback
* retries
* context management

### Prompt systems

* prompt anatomy
* system and developer instructions
* few-shot examples
* prompt versioning
* structured prompts
* prompt injection
* context conflicts

### Retrieval

* document ingestion
* chunking
* embeddings
* metadata filters
* keyword search
* hybrid retrieval
* reranking
* context assembly
* citation grounding

### Agents

* tools
* planning
* state
* memory
* approval
* retries
* termination
* durable execution
* agent evaluation

### Evaluation

* golden datasets
* rubric-based evaluation
* deterministic checks
* LLM judges
* retrieval metrics
* regression testing
* latency and cost
* human feedback
* failure taxonomies

### Safety and reliability

* prompt injection
* data leakage
* permission boundaries
* tool validation
* output validation
* sandboxing
* rate limits
* audit trails
* graceful degradation

## 6. Production Engineering

这一部分会把你和只会做demo的人真正分开。

* Deployment
* CI/CD
* Environments
* Secrets
* Logging
* Metrics
* Tracing
* Cost tracking
* Feature flags
* Incident response
* Load testing
* Model migrations
* Data migrations
* Rollbacks
* SLOs

---

# 四、你的notes不该长得像课堂抄写

每一篇正式note使用统一结构。

## Note Template

### 1. The Problem

先讲它在解决什么。

不要以定义开头。

例如不是：

> A queue is a data structure that follows FIFO.

而是：

> Your API accepted a request that takes eight minutes to finish. The browser may disconnect, the server may restart, and the user still expects a result. What owns the work now?

然后才引出queue。

### 2. Mental Model

用一句足够准确的话建立模型。

> A queue separates accepting work from executing work.

或者：

> Streaming does not make generation faster. It makes partial progress observable.

### 3. Minimal Build

给出最小可运行版本。

代码必须完整到读者能真正运行，而不是只放关键三行。

### 4. What Breaks

这是最重要的一节。

例如queue文章里写：

* worker crashes after completing work but before acknowledging
* job runs twice
* poison messages
* queue backlog
* database and queue state disagree
* user cancels after execution starts

### 5. Production Version

把最小demo升级成真实系统：

* validation
* authentication
* retries
* idempotency
* observability
* cleanup
* rate limits
* tests

### 6. Live Lab

让读者自己操作：

* 改并发数
* 人为制造延迟
* 关闭worker
* 重复发送请求
* 查看trace
* 比较不同配置

### 7. Build Challenge

不是选择题，而是小型工程任务。

例如：

> Add cancellation without allowing a cancelled job to publish its result.

### 8. Decision Record

记录你自己的判断：

> I would use a database-backed queue below this scale because operational simplicity matters more than theoretical throughput.

这类内容特别有价值，因为它展示的不是知识，而是工程判断。

### 9. References

只放你真正使用过的：

* 官方文档
* 论文
* 源码
* 技术规范
* 高质量工程文章

---

# 五、不同类型的内容

网站里不要所有东西都叫“notes”。

## Concepts

解释一个模型。

例如：

* How HTTP streaming actually works
* What an embedding represents
* Why database indexes speed up reads
* Tokens, context windows, and attention

## Patterns

解决一种反复出现的工程问题。

例如：

* Idempotent webhook handling
* Streaming structured model output
* Human approval before tool execution
* Durable agent state
* Hybrid retrieval

## Labs

可以直接运行和修改的实验。

例如：

* Compare chunk sizes on retrieval quality
* Simulate retry storms
* Visualize an embedding space
* Break a naive rate limiter
* Measure token streaming latency

## Build Logs

记录你真实做项目的过程。

包括错误决定，而不只是最后成果。

例如：

* Why I replaced my vector database
* Rebuilding chat persistence
* My first agent loop never stopped
* Cutting inference cost by 43%
* What failed during the first 100 users

## Postmortems

这是很强的portfolio内容。

模板：

```text
Incident
Impact
Timeline
Root cause
Contributing factors
Detection failure
Resolution
Preventive changes
What I misunderstood
```

即使是个人项目，也可以认真做postmortem。

## Projects

每个完整项目必须连回notes。

项目不是孤立展示页，而是知识图谱中的真实验证。

例如一个AI研究助手项目可以关联：

* document ingestion
* chunking
* hybrid search
* reranking
* streaming
* citations
* evaluation
* observability
* authentication

---

# 六、网站页面

## Home

首页不要塞满文章。

只放：

* 你是谁
* 你正在构建什么
* 当前重点领域
* 最近更新的notes
* 一张工程能力地图

首页简介可以是：

> I’m building toward fullstack AI engineering: frontend interfaces, backend systems, data infrastructure, model integration, evaluation, and production reliability.
>
> This site is my live notebook—part field manual, part laboratory, and part record of what broke along the way.

## Learn

按照能力路径浏览：

```text
Foundations
Fullstack Systems
AI Applications
AI Infrastructure
Production
```

## Notes

全部正式文章。

支持按照：

* topic
* difficulty
* status
* language
* project
* course source

筛选。

## Labs

所有可运行实验。

每个lab标明运行环境：

* Browser Python
* Browser Node
* Local Docker
* Cloud API required

## Projects

不是简单截图。

每个project页面展示：

* problem
* system design
* architecture diagram
* important decisions
* live demo
* repository
* evaluation
* failures
* related notes

## Now

你目前正在学什么、构建什么。

比传统blog更适合live vault。

## Changelog

例如：

```text
2026-07-27
Rewrote the retry section in Durable Agent Runs.
Added a failure simulation to the queue lab.
Corrected the explanation of PostgreSQL isolation levels.
```

这能让整个网站真的像活的notebook，而不是发布后不再更新的文章坟场。

---

# 七、内容状态

每篇note都有状态。

## Seed

只有问题、链接和零散想法。

不公开，或者明显标记未整理。

## Working

已经有基本解释和代码，但仍可能变化。

## Stable

你认为已经足够准确，可以被别人依赖。

## Production-tested

对应方法已经在真实项目里使用，并且有测试、监控或实际数据支持。

页面顶部可以显示：

```text
Status: Working
Last tested: 2026-07-20
Runtime: Node.js
Project: AI Support Agent
```

这比简单写“updated recently”更有工程味。

---

# 八、Live Notebook体验

不要让每个页面都变成完整IDE。

交互必须服务于概念。

## Python内容

适合：

* embeddings visualization
* probability
* evaluation metrics
* chunking experiments
* retrieval ranking
* simple ML models
* data analysis

页面内放：

```text
Explanation
Editable code cell
Run button
Output
Small challenge
Reset
```

## TypeScript和React内容

适合：

* streaming UI
* state machines
* API handlers
* tool-call rendering
* validation
* React behavior

先使用轻量内嵌editor。

只有真正需要完整Node环境的lab，再启用浏览器runtime。

## 真实模型调用

不要把API key放进浏览器。

页面调用你自己的服务端endpoint。

每个公开实验必须：

* 限制调用次数
* 限制最大tokens
* 不允许任意tool execution
* 对输入输出做验证
* 显示估算成本
* 可以切换到mock模式

---

# 九、搜索和AI助手

第一版只做普通搜索。

标题、正文、标签、代码符号和项目名称都可以检索。

先不要急着加“Ask my notes”。

因为一个知识库如果普通搜索都不好用，接一个聊天框只会把问题藏起来。

后面再加AI助手，并且要求它：

* 只回答vault已有内容
* 明确引用具体note和section
* 区分你的观点和外部事实
* 找不到时直接说找不到
* 可以生成学习路径
* 可以对比两个工程方案
* 不替你偷偷改正文

---

# 十、仓库结构

```text
vault/
  app/
    notes/
    labs/
    projects/
    now/
    changelog/
    api/
  content/
    foundations/
    frontend/
    backend/
    data/
    ai-engineering/
    production/
  courses/
    private/
  components/
    note/
    code/
    diagrams/
    labs/
  experiments/
    python/
    typescript/
  projects/
  public/
  scripts/
    validate-links/
    build-search-index/
    check-code/
    generate-changelog/
  tests/
```

`courses/private`保存原始课堂材料。

`content`保存重新写过的公开知识。

不要直接把课堂笔记原封不动发布。

---

# 十一、每篇note的frontmatter

```yaml
title: Durable Agent Runs
summary: Persisting and resuming long-running AI workflows safely.
status: working
difficulty: intermediate
topics:
  - agents
  - queues
  - state-machines
  - reliability
course_sources:
  - distributed-systems
projects:
  - research-agent
runtime:
  - typescript
  - postgresql
last_tested: 2026-07-20
```

这样未来能自动生成：

* 课程到能力的映射
* 项目相关知识
* 学习路径
* 过期内容提醒
* 技术栈页面
* changelog

---

# 十二、第一批不要写太多

第一版只做十二篇真正完整的内容。

## Foundations

1. How an HTTP request moves through a fullstack application
2. Async execution, concurrency, and parallelism
3. Database transactions through real failure cases

## Fullstack

4. Authentication is identity plus authority
5. Streaming responses from server to UI
6. Background jobs and idempotency

## AI

7. From prompt to model response
8. Structured output and validation
9. Embeddings and semantic retrieval
10. Building a minimal RAG pipeline

## Production

11. Evaluating an AI feature before shipping
12. Observability for model-backed applications

再配两个完整项目：

* AI research assistant
* AI workflow or agent application

这已经足够构成一个很强的第一版。

不要一开始迁移所有课程。

否则会花几个月整理旧内容，却没有形成自己的工程体系。

---

# 十三、最终效果

核心问题应该是：

> What problem does this solve, how do I build it, and how does it fail in production?

这才是Fullstack AI Engineer版本。

---

# 十四、目前实现到哪一步

上面十三节是设计文档，不是现状。这一节说明**哪些已经建好、哪些还是空的**，
免得把计划当成成果。

## 技术栈的决定

**前端继续用 MkDocs Material，不迁到 Next.js。**

§10 的目录结构（`app/`、`api/`）暗示的是一个 JS 应用，但这个仓库已经有三样
不该丢的东西：79 篇笔记、一套手调的设计系统、以及一条把私有 Obsidian vault
安全发布出去的转换管线（`scripts/sync_vault.py` + `vault_manifest.toml`）。

§8 要求的「页面调用自己的服务端 endpoint」不需要重写前端就能做到：静态页面
加一小段 JS，去 `fetch()` 一个 FastAPI 后端。这个判断和 `backend/README.md`
里已经写下的结论一致，代价（GitHub Pages 只能托管静态文件，所以后端要第二个
部署目标）也在那里说清楚了。

## 已经建好的骨架

```text
docs/
  index.md                首页，按 §6 重写
  now.md  changelog.md    Now 页 + 变更日志
  learn/                  五条学习路径（§6）
  notes/
    index.md              全部正式笔记 + 标签索引
    foundations/ frontend/ backend/
    data/ ai-engineering/ production/    ← §3 的能力地图
    data-structures/ algorithms/
    machine-learning/ networks/          ← 原有 79 篇，归入 Reference
  labs/ build-logs/ postmortems/
  projects/
  _templates/             五个内容类型模板，不参与构建

frontend/overrides/
  partials/note-meta.html  状态条：status / difficulty / runtime / last tested
```

两套分类**故意交叉**：`notes/` 下的文件夹是**能力**（一篇笔记归属哪里），
`learn/` 是**阅读顺序**（跨文件夹，不拥有任何页面）。所以
「Database transactions」在 §12 里属于 Foundations 路径，文件却放在
`notes/data/`——因为 §3 的能力地图才决定归档位置。

## 状态系统

每篇笔记的 frontmatter 里带 `status`，主题会渲染成页面顶部的状态条：

| 状态 | 含义 |
|---|---|
| `seed` | 只有问题和零散想法，还不值得读 |
| `working` | 有解释和代码，但可能还会变 |
| `stable` | 足够准确，别人可以依赖 |
| `production-tested` | 已在真实项目里跑过，有测试或监控支撑 |

带 `runtime` 但没有 `last_tested` 的页面会显示 *never*——这是故意的，
「有代码但从没跑过」正是读者需要知道的事。

## 还没有做的

- **十二篇正文**。目前全是 `seed` 状态的骨架：有问题陈述、有 `What Breaks`
  清单，没有正文。这是下一步真正的工作。
- **Labs 的运行时**。模板和运行环境分级写好了，实验一个都没有。
- **按 status / difficulty / runtime 筛选**。标签索引（`<!-- material/tags -->`）
  是真的能用的；多维筛选需要生成 JSON 加一个前端组件，故意没有做一半。
- **AI 助手**。按 §9，普通搜索先做好。
- **旧笔记迁移**。按 §12，79 篇课程笔记留在 Reference 分支，URL 没有变，
  内容一个字没动。

## 本地运行

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve            # http://127.0.0.1:8000/geshu-compendium/
.venv/bin/mkdocs build --strict   # CI 跑的就是这个，必须是绿的
python3 scripts/sync_vault.py     # 从 vault 重新生成 Reference 分支
```

部署后在
[geshu-compendium](https://angelawurx.github.io/geshu-compendium/)。

内容采用 [CC BY-NC-SA 4.0](LICENSE-CONTENT)，站点代码 [MIT](LICENSE)。
