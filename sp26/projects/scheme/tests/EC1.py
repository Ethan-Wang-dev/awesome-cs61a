test = {
  'name': 'EC 1',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 1)
          344572bfd411ffe1bccc40e3e63b0726
          # locked
          scm> (let ((x 5))
          ....    (+ x 3))
          e379be012ed2005e67131f006b7f6085
          # locked
          scm> x
          e9c72ee24bf5f0040e3f510cd1634fbe
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (let ((a 1) (b a)) b)
          487e5d855a4749c37e82d995b26091f7
          # locked
          # choice: SchemeError
          # choice: 1
          # choice: x
          # choice: y
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (let ((x 5))
          ....    (let ((x 2)
          ....          (y x))
          ....        (+ y (* x 2))))
          4a4f11fb032ec2b75309dac59b3b3254
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (let ((a 2) (a 3)) (+ a a)) ; how should we catch something like this?
          487e5d855a4749c37e82d995b26091f7
          # locked
          scm> (let ((y 2 3)) (+ y y)) ; should this be an allowable form?
          487e5d855a4749c37e82d995b26091f7
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (square x) (* x x))
          square
          scm> (define (f x y)
          ....    (let ((a (+ 1 (* x y)))
          ....          (b (- 1 y)))
          ....        (+ (* x (square a))
          ....           (* y b)
          ....           (* a b))))
          f
          scm> (f 3 4)
          456
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
          >>> # Incorrectly formatted bindings
          >>> bindings = Link(Link('x', Link(2, nil)), Link(Link('y', nil), nil)) # equivalent to ((x 2) (y))
          >>> make_let_frame(bindings, global_frame)
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Improper formals list - used same variable name twice
          >>> bindings = Link(Link('x', Link(2, nil)), Link(Link('x', Link(3, nil)), nil)) # equivalent to ((x 2) (x 3))
          >>> make_let_frame(bindings, global_frame)
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> bindings = Link(Link('x', Link(2, nil)), Link(Link('y', Link(3, nil)), nil)) # equivalent to ((x 2) (y 3))
          >>> f1 = make_let_frame(bindings, global_frame)
          >>> f1.lookup('x')
          2
          >>> bindings # make sure bindings isn't mutated
          Link(Link('x', Link(2)), Link(Link('y', Link(3))))
          """,
          'hidden': False,
          'locked': False,
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
          scm> (define x 3)
          x
          scm> (define y 4)
          y
          scm> (let ((x (+ y 2))
          ....       (y (+ x 2)))
          ....      (cons x (cons y nil)))
          (6 5)
          scm> (let ((x 'hello)) x)
          hello
          scm> (let ((a 1) (b 2) (c 3)) (+ a b c))
          6
          scm> (define z 0)
          z
          scm> (let ((a (define z (+ z 1)))) z)
          1
          scm> (let ((x 1)
          ....       (y 3))
          ....    (define x (+ x 1))
          ....    (list x y))
          (2 3)
          scm> (let ((a 1 1)) a)
          SchemeError
          scm> (let ((a 1) (2 2)) a)
          SchemeError
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
