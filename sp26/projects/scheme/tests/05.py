test = {
  'name': 'Problem 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'b4aa547bac1b887dfd7387940e9b4a0a',
          'choices': [
            r"""
            Link('quote', Link(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Link(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> do_quote_form(Link(3, nil), global_frame)
          71373a588b7d2da6b021a6a9cb2a416f
          # locked
          >>> do_quote_form(Link('hi', nil), global_frame)
          7416b5e74e5b93f7c641ed723332329a
          # locked
          >>> expr = Link(Link('+', Link('x', Link(2))))
          >>> do_quote_form(expr, global_frame) # Make sure to use Link notation
          794b71f6db0ce00c40ebf39e9ca9b174
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> ''hello
          (quote hello)
          # choice: (quote hello)
          # choice: hello
          # choice: (hello)
          # choice: (quote (quote (hello)))
          scm> (quote (1 2))
          (1 2)
          scm> (car '(1 2 3))
          1
          scm> (cdr '(1 2))
          (2)
          scm> (cons 'car '('(4 2)))
          (car (quote (4 2)))
          scm> (eval (cons 'car '('(4 2))))
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> ''hello
          (quote hello)
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
