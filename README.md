# awesome-cs61a

[简体中文](README.zh-CN.md)

A concise, version-aware guide to learning Berkeley CS61A and applying it to software engineering and AI agents.

## What readers get

- One coherent learning route instead of scattered CS61A links.
- A complete Spring 2026 baseline plus the important Fall 2026 additions.
- Runnable practice, tests, and notes that explain why each topic matters.
- Version differences and maintenance notes that remain useful after one semester.

## How we build it

1. **Spring 2026 (`sp26/`) is the mainline.** It covers the complete course sequence: abstraction, recursion, data structures, OOP, interpreters, SQL, testing, and tracing.
2. **Fall 2026 (`fa26-supplement/`) is the delta.** It adds only new or substantially changed topics: Gleam, typed/immutable data, Coding Agents, Browsers, and Applications.
3. **Every entry points to an official source.** Every implementation or note records how it was checked.
4. **Original extensions connect the course to real engineering.** Examples include tool calls, state, evaluation, SQL, and Web applications.

## Principles

- **Official first:** prefer primary course sources and record version/date when relevant.
- **No duplicate, no answer mirror:** repeated topics stay in `sp26/`; copied or restricted solutions do not belong here.
- **Reproducible:** code should run, tests should be explainable, and progress should leave evidence.
- **Versioned:** add a dated supplement for a new Berkeley offering instead of silently rewriting history.
- **Small and maintainable:** keep the map clear, links current, and contributions focused.

## Start here

1. [Spring 2026 official course site](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/)
2. [Fall 2026 official course site](https://cs61a.org/fa26/) and [syllabus](https://cs61a.org/fa26/syllabus/)
3. [Composing Programs textbook](https://www.composingprograms.com/)
4. [PROGRESS.md](PROGRESS.md) for our learning progress and a reference for learners who already have programming experience

Run the local tests supplied with each assignment; Berkeley's testing tool is [ok.py](https://github.com/okpy/ok).

## Layout

```text
awesome-cs61a/
├── README.md                  # Default English entry point
├── README.zh-CN.md            # Simplified Chinese version
├── PROGRESS.md                # Dated progress and verification
├── CONTRIBUTING.md            # Contribution rules
├── sp26/                      # Complete Spring 2026 mainline
│   ├── labs/  homework/  projects/  tests/  notes/
└── fa26-supplement/           # Fall 2026 additions and comparisons
    ├── gleam/  coding-agents/  browsers/  applications/  notes/
```

## Contribute and maintain

See [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include broken-link reports, clearer explanations, original tests, accessibility fixes, and reproducibility improvements.

Update [PROGRESS.md](PROGRESS.md) at milestones with the files changed, verification command, and remaining gap. Use focused commits such as `docs(fa26): record Coding Agents version difference`.

## Integrity and attribution

This is an independent project, not affiliated with UC Berkeley. Do not publish copied or restricted course solutions. Check the [official syllabus](https://cs61a.org/fa26/syllabus/) before using AI tools or publishing assignment-related files. Berkeley course materials retain their original terms; no license for original work is granted until a `LICENSE` file is added.
