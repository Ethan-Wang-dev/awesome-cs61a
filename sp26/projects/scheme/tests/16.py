test = {
  'name': 'Problem 16',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (solution-code '(define (factorial n) (if (= n 0) 1 (* n _____))) '(factorial (- n 1)))
          (define (factorial n) (if (= n 0) 1 (* n (factorial (- n 1)))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (solution-code '(define (len s) (if (null? s) 0 (+ 1 _____))) '(len (cdr s)))
          (define (len s) (if (null? s) 0 (+ 1 (len (cdr s)))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (solution-code '(define (sum s) (if (null? s) 0 (+ (car s) (sum (cdr s))))) '(sum (cdr s)))
          (define (sum s) (if (null? s) 0 (+ (car s) (sum (cdr s)))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (solution-code '(define (power b n) (if (= n 0) 1 (* b _____))) '(power b (- n 1)))
          (define (power b n) (if (= n 0) 1 (* b (power b (- n 1)))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (solution-code '(define (count-even s) (if (null? s) 0 (+ (if (even? (car s)) 1 0) _____))) '(count-even (cdr s)))
          (define (count-even s) (if (null? s) 0 (+ (if (even? (car s)) 1 0) (count-even (cdr s)))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (solution-code '(define (member-of x s) (if (null? s) #f (if (equal? x (car s)) #t _____))) '(member-of x (cdr s)))
          (define (member-of x s) (if (null? s) #f (if (equal? x (car s)) #t (member-of x (cdr s)))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
