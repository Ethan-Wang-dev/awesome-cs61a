test = {
  'name': 'Problem 12',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          362a13f62b8278cff7410c0d72fbb640
          # locked
          # choice: #t
          # choice: #f
          # choice: SchemeError
          scm> (and 1 #f)
          dee55ab436bc219727575ed9b83ed831
          # locked
          # choice: 1
          # choice: #t
          # choice: #f
          scm> (and (+ 1 1) 1)
          e9c72ee24bf5f0040e3f510cd1634fbe
          # locked
          scm> (and #f 5)
          dee55ab436bc219727575ed9b83ed831
          # locked
          scm> (and 4 5 (+ 3 3))
          68bf08aa7c411511f0a9af3cac39f793
          # locked
          scm> (not (and #t #f 42 (/ 1 0)))
          362a13f62b8278cff7410c0d72fbb640
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (not (and #f))
          #t
          scm> (and 3 2 #f)
          #f
          scm> (and 3 2 1)
          1
          scm> (and 3 #f 5)
          #f
          scm> (and 0 1 2 3)
          3
          scm> (define (true-fn) #t)
          true-fn
          scm> (and (true-fn))
          #t
          scm> (define x #f)
          x
          scm> (and x #t)
          #f
          scm> (eq? (and #t)  #t)
          #t
          scm> (eq? (or #t) #t)
          #t
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          x
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      #f
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          #f
          scm> x
          11
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (and #t #t #t #t))
          no-mutation
          scm> no-mutation
          (lambda () (and #t #t #t #t))
          scm> (no-mutation)
          #t
          scm> no-mutation ; `and` should not cause mutation
          (lambda () (and #t #t #t #t))
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
          scm> (or)
          dee55ab436bc219727575ed9b83ed831
          # locked
          # choice: #t
          # choice: #f
          # choice: SchemeError
          scm> (or (+ 1 1))
          725437f086fad00d39b3b3621cfe9fef
          # locked
          # choice: 2
          # choice: #t
          # choice: #f
          scm> (not (or #f))
          362a13f62b8278cff7410c0d72fbb640
          # locked
          scm> (define (zero) 0)
          e27c97d7c851b7768c287eed5f76e62c
          # locked
          scm> (or (zero) 3)
          fd0160de2f72728a572c943666b1d89b
          # locked
          scm> (or 4 #t (/ 1 0))
          9871f5a05c2faba882ad6bd9ba1b836e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (or 5 2 1)
          5
          scm> (or 0 1 2)
          0
          scm> (or #f (- 1 1) 1)
          0
          scm> (or 'a #f)
          a
          scm> (or (< 2 3) (> 2 3) 2 'a)
          #t
          scm> (or (< 2 3) 2)
          #t
          scm> (define (false-fn) #f)
          false-fn
          scm> (or (false-fn) 'yay)
          yay
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          #f
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     #t
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          #t
          scm> x
          11
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (or #f #f #f #f))
          no-mutation
          scm> no-mutation
          (lambda () (or #f #f #f #f))
          scm> (no-mutation)
          #f
          scm> no-mutation ; `or` should not cause mutation
          (lambda () (or #f #f #f #f))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (greater-than-5 x) (if (> x 5) #t #f))
          greater-than-5
          scm> (define (other y) (or (greater-than-5 y) #f))
          other
          scm> (other 2)
          #f
          scm> (other 6) ; test for mutation
          #t
          scm> (define (other y) (and (greater-than-5 y) #t))
          other
          scm> (other 2)
          #f
          scm> (other 6) ; test for mutation
          #t
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
