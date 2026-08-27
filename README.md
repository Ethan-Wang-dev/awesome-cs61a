# awesome-cs61a

[简体中文](README.zh-CN.md)

An independent, maintained, version-aware guide to learning Berkeley CS61A and applying its ideas to software engineering and AI agents.

This repository combines two Berkeley offerings into one learning track:

- **Spring 2026 (`sp26/`) is the mainline.** It provides the complete sequence of lectures, labs, homework, projects, notes, and tests.
- **Fall 2026 (`fa26-supplement/`) is the supplement.** It records only meaningful additions or changes: Gleam, typed and immutable data, Coding Agents, Browsers, and Applications.
- **Official sources come first.** Version-sensitive claims link to Berkeley and include a checked date when appropriate.
- **Reproducibility matters.** A learning claim should have runnable code, a test result, an explanation, or a focused commit.
- **This is not a solution mirror.** It is independent, unaffiliated with Berkeley, and must not expose copied or restricted solutions.

The repository is meant to outlive one person's two-week study sprint. The durable output is a clear resource map, version history, reproducible practice, and improvements that another learner can reuse.

## Start here

1. Follow the [Spring 2026 official course site](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) as the main syllabus.
2. Use the [Fall 2026 official course site](https://cs61a.org/fa26/) and [syllabus](https://cs61a.org/fa26/syllabus/) to identify the supplement.
3. Read the [course map](#course-map), then begin in `sp26/`.
4. Read the [Composing Programs textbook](https://www.composingprograms.com/) sections linked from the weekly calendar.
5. Run each assignment locally before marking it complete. The course uses [ok.py](https://github.com/okpy/ok) for local testing; follow the official assignment page for the exact command.
6. Record what was completed, how it was verified, and what remains in [PROGRESS.md](PROGRESS.md).

## Course map

| Stage | Main topics | Where | Expected evidence |
|---|---|---|---|
| Foundations | Functions, control, higher-order functions, environments, abstraction | `sp26/` | Small programs, environment diagrams, tests |
| Program structure | Recursion, sequences, objects, linked lists, trees | `sp26/` | Labs, representative homework, complexity notes |
| State and scale | Debugging, mutation, classes, inheritance, lazy evaluation, generators, efficiency | `sp26/` | Project code, bug reports, state diagrams, benchmarks |
| Interpreters and data | Functional programming, interpreters, SQL, aggregation | `sp26/` | Interpreter and SQL experiments |
| Reliability | Software testing, tracing, ethics, final review | `sp26/` | Regression tests, traces, retrospectives |
| AI-era extension | Gleam/types, Coding Agents, Browsers/Web, Applications | `fa26-supplement/` | Original experiments and version-difference notes |

Repeated topics stay in `sp26/`. A topic enters `fa26-supplement/` only when Fall 2026 introduces something genuinely new or substantially changes the learning objective. This prevents two copies of the same course from drifting apart.

## Repository layout

```text
awesome-cs61a/
├── README.md                  # English public entry point
├── README.zh-CN.md            # Simplified Chinese version
├── PROGRESS.md                # Dated progress and evidence log
├── CONTRIBUTING.md            # Issue/PR and maintenance rules
├── .gitignore                 # Local environment exclusions
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

## What belongs here

- Personal implementations of permitted course starter files, with tests and short explanations.
- Concept notes about mental models, failed attempts, debugging patterns, and complexity.
- Original experiments connecting CS61A ideas to Agent engineering, tool calls, state, evaluation, SQL, and Web applications.
- Dated links to official resources and a reproducible development environment.

Do not add credentials, virtual environments, large generated files, copied solutions, restricted course material, or unrelated experiments. A separate Agent project may be linked after it has a stable public URL; it should not be mixed into course assignments.

## Public/private boundary

The durable public value is the maintained map, explanations, version comparisons, reproducible tooling, and original engineering experiments—not assignment answers.

| Public when ready | Keep private or remove before publishing |
|---|---|
| Official links, resource metadata, original notes, original tests, version-difference notes, original extensions | Active/current assignment solutions, copied code, restricted starter files, credentials, private course infrastructure |

Before making the repository public, audit every file, not only this README. Course rules and AI-use requirements are defined by the [official syllabus](https://cs61a.org/fa26/syllabus/).

## Progress and maintenance contract

Every meaningful study session should leave a verifiable artifact:

- runnable code;
- a local test or `ok` result;
- a note explaining a concept or failure; or
- a focused Git commit.

Use focused commit messages, for example:

```text
feat(sp26): complete tree recursion lab
test(sp26): add edge cases for linked-list notes
docs(fa26): compare Gleam and Python data modeling
chore: verify official course links
```

Update [PROGRESS.md](PROGRESS.md) at milestones with files, commit IDs, test commands, and remaining gaps. At the start of a new Berkeley term, re-check official links and add a dated version note instead of silently rewriting historical work. Keep `main` readable and working; use short topic branches for risky experiments.

## Long-term roadmap

- [ ] Build a module-by-module index of official lectures, readings, labs, projects, and tooling.
- [ ] Maintain a dated SP26/FA26 difference table and migration notes for future offerings.
- [ ] Add lightweight link and Markdown checks.
- [ ] Add original, license-compatible practice extensions reusable outside the course.
- [ ] Accept community corrections through focused issues and pull requests.

The personal learning implementation is the first test of this system. The durable artifact is the maintained knowledge and process built around it.

## Contribution policy

See [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include broken-link reports, clearer explanations, accessibility improvements, original tests, and reproducibility fixes. Do not submit copied or completed solutions to Berkeley assignments.

## Attribution, integrity, and license

This is an independent study project and is not affiliated with or endorsed by UC Berkeley or the CS61A teaching staff. Course materials remain subject to their original terms. Check the [official syllabus](https://cs61a.org/fa26/syllabus/) before using AI tools or publishing any assignment-related file.

This repository does not relicense Berkeley course materials. Original work created here may receive a separate open-source license after the public/private boundary has been reviewed. Until a `LICENSE` file is added, no license to reuse original work is granted.

## Design references

The organization was informed by high-visibility resources, while deliberately avoiding their solution code:

- [PKUFlyingPig/CS61A](https://github.com/PKUFlyingPig/CS61A) — separation of homework, labs, projects, and exams.
- [InsideEmpire/CS61A-Assignments](https://github.com/InsideEmpire/CS61A-Assignments) — onboarding, local testing, bilingual explanation, and disclaimer.
- [csfive/composing-programs-zh](https://github.com/csfive/composing-programs-zh) — concise scope, attribution, maintenance status, contributors, and license information.
- [okpy/ok](https://github.com/okpy/ok) — installation, testing, development, and contribution documentation for course infrastructure.

The standard is simple: a stranger should be able to understand the scope, start the mainline, verify a result, and improve the repository without private context.
