# CS61A Spring 2026 Mainline

The complete course track for building a strong programming foundation. This directory uses the [Spring 2026 course-site archive](https://lr2933.github.io/cs61a-spring-2026/) for source material and turns each topic into code, tests, and notes that can be revisited later. The [Berkeley-hosted archive](https://www-inst.eecs.berkeley.edu/~cs61a/sp26/) is the original course site.

## Coverage

- Functions, control, higher-order functions, environments, and abstraction
- Recursion, sequences, objects, linked lists, and trees
- Debugging, mutation, classes, inheritance, lazy evaluation, generators, and efficiency
- Functional programming, interpreters, SQL, aggregation, software testing, and tracing

## Directory map

```text
ASSIGNMENTS.md  # Exact homework/project edit targets and test commands
labs/          # Course labs and local experiments
homework/      # Spring 2026 homework starters and tests
projects/      # Hog, Cats, Ants, Scheme, and contest projects
notes/         # Mental models, debugging patterns, and complexity
resources/     # External course-material links and provenance notes
tests/         # Workflow tests and regression checks
tools/         # Assignment manifest and local CLI
```

Course slides, study guides, discussion worksheets, and lab PDFs stay at their source links. The programming starters and local tests are organized under [`ASSIGNMENTS.md`](ASSIGNMENTS.md); [`resources/README.md`](resources/README.md) keeps the external entry points together.

## Working method

1. Get the lecture and reading materials from the official course page.
2. Open the assignment target from [`ASSIGNMENTS.md`](ASSIGNMENTS.md), implement it independently, and run its local tests.
3. Add a short note covering the key idea, one failed attempt, and the verification command.
4. Update the repository-level [PROGRESS.md](../PROGRESS.md) after a milestone.

Run `python3 tools/course.py list` to see every edit target, `python3 tools/course.py doctor` to check setup, and `python3 tools/course.py test <id>` to run one assignment.

The companion [`../fa26-supplement/`](../fa26-supplement/) directory extends this mainline with Fall 2026 topics such as Coding Agents, Browsers, and Applications.
