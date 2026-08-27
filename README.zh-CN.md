# awesome-cs61a

[English](README.md)

一个长期维护、按版本组织的 Berkeley CS61A 自学与工程实践资源库。

本仓库把 Berkeley 的两个课程版本合并为一条学习主线：

- **Spring 2026（`sp26/`）是主线。** 它承载完整的课程学习、Lab、Homework、Project、笔记和测试。
- **Fall 2026（`fa26-supplement/`）是补充。** 它只记录 Gleam、类型与不可变数据、Coding Agents、Browsers 和 Applications 等新增或明显变化的内容。
- **官方资料优先。** 涉及具体版本的内容优先链接 Berkeley 官方页面，并在需要时记录核对日期。
- **可复现优先。** 每个学习结论都应有可运行代码、测试结果、解释或明确的 commit 作为证据。
- **本仓库不是答案镜像。** 它独立维护，不代表 Berkeley，也不应公开复制或受限制的课程答案。

本仓库的目标不只是记录两周学习过程，而是沉淀清晰的资源地图、版本历史、可复现练习和其他学习者可以继续改进的内容。

## 从这里开始

1. 以 [Spring 2026 官方课程页](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) 作为主线。
2. 用 [Fall 2026 官方课程页](https://cs61a.org/fa26/) 和 [官方 syllabus](https://cs61a.org/fa26/syllabus/) 找出需要补充的内容。
3. 先阅读[课程地图](#课程地图)，然后进入 `sp26/`。
4. 阅读周历链接的 [Composing Programs 教材](https://www.composingprograms.com/)。
5. 每个作业先本地运行测试，再标记完成；课程使用 [ok.py](https://github.com/okpy/ok) 进行本地测试。
6. 在 [PROGRESS.md](PROGRESS.md) 记录完成内容、验证方式和剩余问题。

## 课程地图

| 阶段 | 主要内容 | 目录 | 预期证据 |
|---|---|---|---|
| 基础 | 函数、控制流、高阶函数、环境图、抽象 | `sp26/` | 小程序、环境图、测试 |
| 程序结构 | 递归、序列、对象、链表、树 | `sp26/` | Lab、代表性作业、复杂度笔记 |
| 状态与规模 | 调试、可变性、类、继承、惰性求值、生成器、效率 | `sp26/` | 项目代码、Bug 记录、状态图、基准测试 |
| 解释器与数据 | 函数式编程、解释器、SQL、聚合 | `sp26/` | 解释器与 SQL 实验 |
| 可靠性 | 软件测试、程序追踪、伦理、课程总结 | `sp26/` | 回归测试、trace、复盘 |
| AI 时代补充 | Gleam/类型、Coding Agents、浏览器/Web、Applications | `fa26-supplement/` | 原创实验与版本差异笔记 |

重复主题统一放在 `sp26/`。只有 Fall 2026 真正新增或明显改变学习目标的内容才进入 `fa26-supplement/`，避免两套课程互相漂移。

## 仓库目录

```text
awesome-cs61a/
├── README.md                  # 英文默认入口
├── README.zh-CN.md            # 简体中文版
├── PROGRESS.md                # 带日期的进度与验证记录
├── CONTRIBUTING.md            # Issue/PR 与维护规则
├── .gitignore                 # 本地环境忽略项
├── sp26/                      # Spring 2026 完整主线
│   ├── labs/
│   ├── homework/
│   ├── projects/
│   ├── tests/
│   └── notes/
└── fa26-supplement/           # Fall 2026 新增与比较
    ├── gleam/
    ├── coding-agents/
    ├── browsers/
    ├── applications/
    └── notes/
```

顶层目录就是 GitHub 仓库根目录；`sp26/` 和 `fa26-supplement/` 是同一仓库里的目录，不是两个嵌套仓库。

## 什么内容应该放进来

- 在允许的前提下保存自己的课程 starter file 实现、测试和简短说明。
- 记录心智模型、失败尝试、调试模式和复杂度。
- 保存把 CS61A 连接到 Agent 工程、工具调用、状态、评测、SQL 和 Web 应用的原创实验。
- 保存带日期的官方资源链接和可复现的开发环境说明。

不要提交密钥、虚拟环境、大型生成文件、复制的答案、受限课程材料或无关实验。独立 Agent 项目应在有稳定公开地址后再链接，不要把它和课程作业混在一起。

## 公开与私有边界

本项目的长期公共价值在于资源地图、解释、版本比较、可复现工具和原创工程实验，而不是公开作业答案。

| 可以公开 | 保持私有或发布前移除 |
|---|---|
| 官方链接、资源元数据、原创笔记、原创测试、版本差异笔记、原创扩展 | 正在进行或当前课程答案、复制代码、受限 starter files、凭证、私有课程基础设施 |

公开仓库前必须审查所有文件，不能只检查 README。使用 AI 工具或发布任何与作业有关的文件前，应先检查[官方 syllabus](https://cs61a.org/fa26/syllabus/)。

## 进度与维护约定

每次有意义的学习都应留下至少一个可验证产物：

- 可运行代码；
- 本地测试或 `ok` 结果；
- 概念或失败原因说明；
- 聚焦的 Git commit。

使用能说明证据的 commit message，例如：

```text
feat(sp26): complete tree recursion lab
test(sp26): add edge cases for linked-list notes
docs(fa26): compare Gleam and Python data modeling
chore: verify official course links
```

在里程碑更新 [PROGRESS.md](PROGRESS.md)，写明文件、commit ID、测试命令和剩余缺口。每个新学期重新核对官方链接并添加带日期的版本说明，不要无声改写历史记录；保持 `main` 可读可运行，有风险的实验使用短期分支。

## 长期 Roadmap

- [ ] 建立按模块组织的官方讲义、阅读、Lab、项目和工具索引。
- [ ] 维护带日期的 SP26/FA26 差异表，并为未来版本写迁移说明。
- [ ] 加入轻量级链接检查和 Markdown 检查。
- [ ] 加入可在课程外复用、许可证清晰的原创练习扩展。
- [ ] 通过聚焦的 Issue 和 PR 接受社区修正。

个人学习代码只是这个系统的第一轮验证，真正长期的产物是围绕它建立的可维护知识和协作流程。

## 贡献规则

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎提交失效链接、清晰解释、无障碍改进、原创测试和可复现性修复；不要提交复制的代码或 Berkeley 作业完整答案。

## 归属、诚信与许可证

本项目独立维护，不代表 Berkeley 或 CS61A 教学团队。课程材料仍受原始条款约束；使用 AI 工具或发布任何与作业有关的文件前，应先检查[官方 syllabus](https://cs61a.org/fa26/syllabus/)。

本仓库不重新授权 Berkeley 课程材料。本仓库原创内容在审查公开边界后可以单独添加开源许可证；在添加 `LICENSE` 前，不授予原创内容的再使用许可。

## 设计参考

本仓库参考了以下高可见度资源的组织方式，但不会复制其中的答案代码：

- [PKUFlyingPig/CS61A](https://github.com/PKUFlyingPig/CS61A)：作业、Lab、项目、考试分区。
- [InsideEmpire/CS61A-Assignments](https://github.com/InsideEmpire/CS61A-Assignments)：启动、测试、双语说明和免责声明。
- [csfive/composing-programs-zh](https://github.com/csfive/composing-programs-zh)：清晰定位、归属、维护状态、贡献者和许可证。
- [okpy/ok](https://github.com/okpy/ok)：安装、测试、开发和贡献文档。

标准很简单：陌生读者应能理解范围、开始主线、验证结果，并在不依赖私有上下文的情况下改进仓库。
