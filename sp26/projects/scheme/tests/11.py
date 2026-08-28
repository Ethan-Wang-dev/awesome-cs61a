test = {
  'name': 'Problem 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define y 1)
          e8964e1ed0bd9300da7e470e362a919c
          # locked
          scm> (define f (mu (x) (+ x y)))
          3d7c962867998a3bb3bb3acf6178a0fd
          # locked
          scm> (define g (lambda (x y) (f (+ x x))))
          8f64929776745634a5ee9a83f3a90e8a
          # locked
          scm> (g 3 7)
          3f006794a0b556ae60c95c5d021df148
          # locked
          """,
          'hidden': False,
          'locked': True,
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
          scm> (define h (mu () x))
          h
          scm> (define (high fn x) (fn))
          high
          scm> (high h 2)
          2
          scm> (define (f x) (mu () (lambda (y) (+ x y))))
          f
          scm> (define (g x) (((f (+ x 1))) (+ x 2)))
          g
          scm> (g 3)
          8
          scm> (mu ())
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
