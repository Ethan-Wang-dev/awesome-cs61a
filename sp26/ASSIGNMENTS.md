# CS61A Spring 2026 Assignments

This is the code-first index for the Spring 2026 mainline. Open the listed edit target, read the official instructions, implement one question at a time, and run the local command.

The workspace keeps the starter files and tests needed for local practice. Solutions, course media, and discussion/lab documents remain at the linked course pages.

## Homework

| ID | Focus | Edit target | Local test | Instructions |
| --- | --- | --- | --- | --- |
| [HW01](homework/hw01/) | Functions and control | `homework/hw01/hw01.py` | `python3 sp26/tools/course.py test hw01` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw01/) |
| [HW02](homework/hw02/) | Higher-order functions | `homework/hw02/hw02.py` | `python3 sp26/tools/course.py test hw02` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw02/) |
| [HW03](homework/hw03/) | Recursion and tree recursion | `homework/hw03/hw03.py` | `python3 sp26/tools/course.py test hw03` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw03/) |
| [HW04](homework/hw04/) | Sequences, data abstraction, and trees | `homework/hw04/hw04.py` | `python3 sp26/tools/course.py test hw04` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw04/) |
| [HW05](homework/hw05/) | Generators | `homework/hw05/hw05.py` | `python3 sp26/tools/course.py test hw05` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw05/) |
| [HW06](homework/hw06/) | OOP, linked lists, and mutable trees | `homework/hw06/hw06.py` | `python3 sp26/tools/course.py test hw06` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw06/) |
| [HW07](homework/hw07/) | Scheme fundamentals | `homework/hw07/hw07.scm` | `python3 sp26/tools/course.py test hw07` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw07/) |
| [HW08](homework/hw08/) | Scheme evaluation practice | `homework/hw08/hw08.scm` | `python3 sp26/tools/course.py test hw08` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw08/) |
| [HW09](homework/hw09/) | Programs as data and macros | `homework/hw09/hw09.scm` | `python3 sp26/tools/course.py test hw09` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw09/) |
| [HW10](homework/hw10/) | SQL and data queries | `homework/hw10/hw10.sql` | `python3 sp26/tools/course.py test hw10` | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw10/) |
| [HW11](homework/hw11/) | Finale surveys and reflection | Reading entry; no code file | — | [course page](https://lr2933.github.io/cs61a-spring-2026/hw/hw11/) |

## Projects

| ID | Focus | Edit target | Local test | Instructions |
| --- | --- | --- | --- | --- |
| [Hog](projects/hog/) | Simulation, higher-order functions, and debugging | `projects/hog/hog.py` | `python3 sp26/tools/course.py test hog` | [course page](https://lr2933.github.io/cs61a-spring-2026/proj/hog/) |
| [Cats](projects/cats/) | Python program design and typing | `projects/cats/cats.py` | `python3 sp26/tools/course.py test cats` | [course page](https://lr2933.github.io/cs61a-spring-2026/proj/cats/) |
| [Ants](projects/ants/) | Object-oriented design and simulation | `projects/ants/ants.py` | `python3 sp26/tools/course.py test ants` | [course page](https://lr2933.github.io/cs61a-spring-2026/proj/ants/) |
| [Scheme](projects/scheme/) | Interpreter implementation | `projects/scheme/scheme_classes.py`, `scheme_eval_apply.py`, `scheme_forms.py` | `python3 sp26/tools/course.py test scheme` | [course page](https://lr2933.github.io/cs61a-spring-2026/proj/scheme/) |
| [Scheme Contest](projects/optional/scheme-contest/) | Recursive art | `projects/optional/scheme-contest/contest.scm` | `python3 sp26/tools/course.py test scheme-contest` | [course page](https://lr2933.github.io/cs61a-spring-2026/proj/scheme_contest/) |

Scheme Contest is optional. It uses the Scheme interpreter from the main project and keeps its entry under `projects/optional/`.

## Useful commands

```bash
# Show every assignment and its edit target
python3 sp26/tools/course.py list

# Check the local Python and starter setup
python3 sp26/tools/course.py doctor

# Run one question through Berkeley's local ok runner
python3 sp26/tools/course.py test hw01 -- --question a_plus_abs_b
```

The command adds `--local`, `--nointeract`, and `--score` automatically. Tests run from the assignment directory and do not require Berkeley authentication.

## Provenance

The starter packages were imported from the [Spring 2026 course archive repository](https://github.com/LR2933/cs61a-spring-2026). Their archive URLs are recorded in [`tools/assignments.json`](tools/assignments.json), together with the course-page URL and editable paths.
