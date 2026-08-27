# awesome-cs61a

一个面向长期维护的 CS61A 自学资源与工程实践仓库。

This repository combines a complete Berkeley course baseline with an AI-era supplement. It is designed to help a new learner start quickly, understand why each resource exists, verify their work, and contribute improvements over time—not merely to store one student's homework.

## Repository promise

- **Spring 2026 (`sp26/`) is the mainline.** It is the complete learning sequence for programming abstraction, recursion, data structures, objects, interpreters, SQL, testing, and tracing.
- **Fall 2026 (`fa26-supplement/`) is the supplement.** It records only the meaningful additions or changes: Gleam, typed/immutable data, Coding Agents, Browsers, and Applications.
- **Official sources come first.** Every version-sensitive recommendation links to the Berkeley course page and records the date checked.
- **Reproducibility matters.** A learning claim should be backed by runnable code, a test result, an explanation, or a focused commit.
- **This is not a solution mirror.** The repository is independent, unaffiliated with Berkeley, and must not expose course answers or copied code.

## Start here

1. Follow the [Spring 2026 official course site](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) as the main syllabus.
2. Use the [Fall 2026 official course site](https://cs61a.org/fa26/) and [Fall 2026 syllabus](https://cs61a.org/fa26/syllabus/) to identify the supplement.
3. Read the [course map](#course-map), then begin in `sp26/`.
4. Read the [Composing Programs textbook](https://www.composingprograms.com/) sections linked from the weekly calendar.
5. Run the local tests supplied with each assignment; [ok.py](https://github.com/okpy/ok) is the Berkeley testing tool used by the course.
6. Record completed work and evidence in [PROGRESS.md](PROGRESS.md).

## Course map

| Stage | Main topics | Where to work | Expected evidence |
|---|---|---|---|
| Foundations | Functions, control, higher-order functions, environments, abstraction | `sp26/` | Small programs, environment diagrams, tests |
| Program structure | Recursion, sequences, objects, linked lists, trees | `sp26/` | Labs, representative homework, complexity notes |
| State and scale | Debugging, mutation, classes, inheritance, lazy evaluation, generators, efficiency | `sp26/` | Project code, bug reports, state diagrams, benchmarks |
| Interpreters and data | Functional programming, interpreters, SQL, aggregation | `sp26/` | Interpreter/SQL experiments and queries |
| Reliability | Software testing, tracing, ethics, final review | `sp26/` | Regression tests, traces, final retrospective |
| AI-era extension | Gleam/types, Coding Agents, Browsers/Web, Applications | `fa26-supplement/` | Original experiments and version-difference notes |

Repeated material stays in `sp26/`. A topic enters `fa26-supplement/` only when Fall 2026 introduces something genuinely new or substantially changes the learning objective. This prevents two copies of the same course from drifting apart.

## Repository layout

```text
awesome-cs61a/
├── README.md                  # Public scope, learning map, and maintenance contract
├── PROGRESS.md                # Dated progress and verification log
├── CONTRIBUTING.md            # Issue/PR and contribution rules
├── .gitignore                 # Python, Gleam, Web, and local-secret exclusions
├── sp26/                      # Spring 2026 complete mainline
│   ├── labs/
│   ├── homework/
│   ├── projects/
│   ├── tests/
│   └── notes/
└── fa26-supplement/           # Fall 2026 additions and comparisons
    ├── gleam/
    ├── coding-agents/
    ├── browsers/
    ├── applications/
    └── notes/
```

The top-level folder is the GitHub repository root. `sp26/` and `fa26-supplement/` are directories inside one repository, not nested repositories.

## Public and private boundary

The long-term public value of this project is the maintained map, explanations, version comparisons, reproducible tooling, and original engineering experiments. It is not the publication of assignment answers.

| Public when ready | Keep private or remove before publishing |
|---|---|
| Official links, resource metadata, original concept notes, tests written by us, version-difference notes, original extensions | Solutions to active/current assignments, copied solutions, restricted starter files, credentials, private course infrastructure |

If a course assignment is included for personal practice, keep the entire working repository private until it is safe and permitted to publish. Before making this repository public, audit every file—not just the README—for copied or restricted material.

## How to maintain it

Every resource entry or change should answer four questions:

1. What problem does this resource solve?
2. Which course version and audience is it for?
3. What was checked, and on what date?
4. What is the license or attribution requirement?

Use focused commits such as:

```text
docs(sp26): clarify recursion learning path
docs(fa26): record Coding Agents version difference
test(sp26): add edge cases for linked-list notes
chore: verify official course links
```

Update [PROGRESS.md](PROGRESS.md) at milestones with files, commit IDs, test commands, and remaining gaps. At the start of a new Berkeley term, add a dated version note and update links; do not silently rewrite historical work. Keep `main` readable and working, and use short topic branches for experiments that may break the mainline.

## Contribution policy

See [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include broken-link reports, clearer explanations, accessibility improvements, original tests, and reproducibility fixes. Do not submit copied or completed solutions to Berkeley assignments.

## Long-term roadmap

The repository becomes more useful as it accumulates maintained, reusable knowledge rather than more personal files:

- [ ] Build a module-by-module index of official lectures, readings, labs, projects, and local tooling.
- [ ] Keep a dated SP26/FA26 difference table and add a short migration note for each future offering.
- [ ] Add lightweight link and Markdown checks so broken resources are found early.
- [ ] Add original, license-compatible practice extensions that can be reused outside the course.
- [ ] Accept community corrections through issues and focused pull requests, with a source URL and verification date.

The learning implementation in `sp26/` is the first test of this system. The durable public artifact is the map, the explanations, and the maintenance process built around it.

## Attribution, integrity, and license

This is an independent study project and is not affiliated with or endorsed by UC Berkeley or the CS61A teaching staff. Course materials remain subject to their original terms. The [official syllabus](https://cs61a.org/fa26/syllabus/) should be checked before using AI tools or publishing any assignment-related file.

The repository does not relicense Berkeley course materials. Original work created here may receive a separate open-source license after the public/private boundary has been reviewed. Until a `LICENSE` file is added, no license to reuse original work is granted.

## Design references

The repository structure was informed by high-visibility resources, while deliberately avoiding their solution code:

- [PKUFlyingPig/CS61A](https://github.com/PKUFlyingPig/CS61A) — course-area separation (`hws`, `labs`, `projects`, `exams`).
- [InsideEmpire/CS61A-Assignments](https://github.com/InsideEmpire/CS61A-Assignments) — onboarding, local testing, bilingual explanation, and disclaimer.
- [csfive/composing-programs-zh](https://github.com/csfive/composing-programs-zh) — concise scope, attribution, maintenance status, contributors, and license information.
- [okpy/ok](https://github.com/okpy/ok) — installation, testing, development, and contribution documentation for course infrastructure.

The standard we are aiming for is simple: a stranger should be able to understand the scope, start the mainline, verify a result, and improve the repository without needing private context.
