# awesome-cs61a

[简体中文](README.zh-CN.md)

A concise, version-aware guide to learning Berkeley CS61A and applying it to software engineering and AI agents.

## What readers get

- One coherent learning route built from the most useful CS61A resources.
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
- **Focused scope:** repeated topics stay in `sp26/`, with original work and clear attribution throughout.
- **Reproducible:** code should run, tests should be explainable, and progress should leave evidence.
- **Versioned:** add a dated supplement for each new Berkeley offering and preserve the learning history.
- **Small and maintainable:** keep the map clear, links current, and contributions focused.

## Start here

1. [Spring 2026 course archive](https://lr2933.github.io/cs61a-spring-2026/) and [Berkeley original site](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/)
2. [Fall 2026 official course site](https://cs61a.org/fa26/) and [syllabus](https://cs61a.org/fa26/syllabus/)
3. [Composing Programs textbook](https://www.composingprograms.com/)
4. [SP26 assignment index](sp26/ASSIGNMENTS.md) for the exact homework/lab/project files and local test commands
5. [PROGRESS.md](PROGRESS.md) for our learning progress and a reference for learners who already have programming experience

Run `python3 sp26/tools/course.py doctor` once, then use the assignment-specific commands in [the index](sp26/ASSIGNMENTS.md). Berkeley's testing tool is [ok.py](https://github.com/okpy/ok).

## Layout

```text
awesome-cs61a/
├── README.md                  # Default English entry point
├── README.zh-CN.md            # Simplified Chinese version
├── PROGRESS.md                # Dated progress and verification
├── CONTRIBUTING.md            # Contribution rules
├── sp26/                      # Complete Spring 2026 mainline
│   ├── ASSIGNMENTS.md         # Edit targets and local test commands
│   ├── labs/  homework/  projects/  tests/  notes/
│   └── tools/                 # Manifest and local workflow CLI
└── fa26-supplement/           # Fall 2026 additions and comparisons
    ├── gleam/  coding-agents/  browsers/  applications/  notes/
```

## Contribute and maintain

See [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include broken-link reports, clearer explanations, original tests, accessibility fixes, and reproducibility improvements.

Update [PROGRESS.md](PROGRESS.md) at milestones with the files changed, verification command, and remaining gap. Use focused commits such as `docs(fa26): record Coding Agents version difference`.

## Integrity and attribution

This is an independent project with attribution to the official Berkeley course sources. Publication follows the course syllabus and preserves the original terms of Berkeley materials. Original work will receive a license when the repository is ready for reuse.
