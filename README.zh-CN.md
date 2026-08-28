# awesome-cs61a

[English](README.md)

一个简洁、按版本组织的 Berkeley CS61A 自学与工程实践指南，帮助读者把课程知识应用到软件工程和 AI Agent。

## 读者能得到什么

- 一条由高价值 CS61A 资源组成的连贯学习路线。
- 完整的 Spring 2026 主线，以及 Fall 2026 的重要新增内容。
- 可运行的练习、测试和解释性笔记，说明每个主题为什么重要。
- 能跨学期继续使用的版本差异记录和维护信息。

## 我们怎么做

1. **Spring 2026（`sp26/`）是主线。** 覆盖抽象、递归、数据结构、OOP、解释器、SQL、测试和程序追踪。
2. **Fall 2026（`fa26-supplement/`）记录差异。** 只补充 Gleam、类型与不可变数据、Coding Agents、Browsers 和 Applications 等新增或明显变化的主题。
3. **每条资料都指向官方来源。** 每份实现或笔记都记录验证方式。
4. **用原创扩展连接真实工程。** 例如工具调用、状态、评测、SQL 和 Web 应用。

## 原则

- **官方优先：** 优先使用一手课程资料，必要时记录版本和核对日期。
- **范围聚焦：** 重复内容统一放在 `sp26/`，所有内容保持原创或明确归属。
- **可复现：** 代码应能运行，测试应能解释，进度应留下证据。
- **有版本：** 每个新学期添加带日期的补充，保留完整学习历史。
- **小而可维护：** 保持地图清晰、链接有效、贡献聚焦。

## 从这里开始

1. [Spring 2026 课程资料镜像](https://lr2933.github.io/cs61a-spring-2026/) 和 [Berkeley 原始课程页](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/)
2. [Fall 2026 官方课程页](https://cs61a.org/fa26/) 和 [syllabus](https://cs61a.org/fa26/syllabus/)
3. [Composing Programs 教材](https://www.composingprograms.com/)
4. [SP26 作业与项目索引](sp26/ASSIGNMENTS.md)：查看每项任务要打开的文件和本地测试命令
5. [PROGRESS.md](PROGRESS.md)：查看我们自己的学习进度，也为有编程基础的学习者提供参考

先运行一次 `python3 sp26/tools/course.py doctor`，之后按照[作业与项目索引](sp26/ASSIGNMENTS.md)中的命令测试。Berkeley 使用的测试工具是 [ok.py](https://github.com/okpy/ok)。

## 目录

```text
awesome-cs61a/
├── README.md                  # 默认英文入口
├── README.zh-CN.md            # 简体中文版
├── PROGRESS.md                # 带日期的进度与验证记录
├── CONTRIBUTING.md            # 贡献规则
├── sp26/                      # Spring 2026 完整主线
│   ├── ASSIGNMENTS.md         # 编辑文件与本地测试命令
│   ├── labs/  homework/  projects/  tests/  notes/
│   └── tools/                 # 清单与本地工作流脚本
└── fa26-supplement/           # Fall 2026 新增与比较
    ├── gleam/  coding-agents/  browsers/  applications/  notes/
```

## 贡献与维护

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎提交失效链接、清晰解释、原创测试、无障碍修复和可复现性改进。

在里程碑更新 [PROGRESS.md](PROGRESS.md)，写明修改文件、验证命令和剩余缺口。使用聚焦的 commit，例如 `docs(fa26): record Coding Agents version difference`。

## 诚信与归属

本项目依据 Berkeley 官方课程资料独立维护，并保留课程材料的原始归属和条款。内容发布遵循官方 syllabus；原创内容将在适合复用时添加许可证。
