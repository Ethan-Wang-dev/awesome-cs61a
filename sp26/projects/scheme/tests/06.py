test = {
  'name': 'Problem 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eval_all(Link(2, nil), env)
          725437f086fad00d39b3b3621cfe9fef
          # locked
          # choice: 2
          # choice: SchemeError
          >>> eval_all(Link(4, Link(5, nil)), env)
          9a3da8c3f3291f1ba3284a28cfeb60f8
          # locked
          # choice: 4
          # choice: 5
          # choice: (4 5)
          # choice: SchemeError
          >>> eval_all(nil, env) # return None (meaning undefined)
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> s = Link(1, Link(2, Link(3, nil)))
          >>> eval_all(s, env)
          3
          >>> s     # The list should not be mutated!
          Link(1, Link(2, Link(3)))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (+ 2 3) (+ 5 6))
          8a45d840829a1008ef79013f7d8df6fd
          # locked
          scm> (begin (define x 3) x)
          71373a588b7d2da6b021a6a9cb2a416f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 30 '(+ 2 2))
          231e95c67da5138d11a0d1b68ee03d92
          # locked
          # choice: (+ 2 2)
          # choice: '(+ 2 2)
          # choice: 4
          # choice: 30
          scm> (define x 0)
          344572bfd411ffe1bccc40e3e63b0726
          # locked
          scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
          e8964e1ed0bd9300da7e470e362a919c
          # locked
          scm> x
          e9c72ee24bf5f0040e3f510cd1634fbe
          # locked
          scm> y
          725437f086fad00d39b3b3621cfe9fef
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 30 'hello)
          hello
          scm> (begin (define x 3) (cons x '(y z)))
          (3 y z)
          scm> (begin (define x 3) (cons x '(x z)))
          (3 x z)
          scm> (begin (+ 1 2) nil)
          ()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1))
          ....        (define x (+ x 10))
          ....        (define x (+ x 100))
          ....        (define x (+ x 1000)))
          x
          scm> x
          1111
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 0 1 2 0)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin (print 3) (+ 2 3) (print 6))
          3
          6
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
