; Twice

(print 2)
(print (print 2))
(begin (print 2) (print 2))
(define (twice expr) (list 'begin expr expr))
(twice (print 2))
(twice '(print 2))
(eval (twice '(print 2)))

(define-macro (twice expr) (list 'begin expr expr))
(twice (print 2))

(define-macro (second expr) (car (cdr expr)))

; Repeat

; Return a list containing expr n times.
;
; scm> (repeated-expr 4 '(print 2)) 
; ((print 2) (print 2) (print 2) (print 2))
(define (repeated-expr n expr)
  (if (zero? n) nil (cons expr (repeated-expr (- n 1) expr))))

; Evaluate expr n times and return the last value.
;
; scm> (repeat (+ 1 2) (print 5))
; 5
; 5
; 5
; scm> (repeat 3 (+ 2 3))  ; (+ 2 3) is evaluated 3 times, but only the last value is returned
; 5
(define-macro (repeat n expr)
  (cons 'begin (repeated-expr (eval n) expr)))


(define (repeated-expr n expr)
  `((define (repeater k)
       (if (= k 1) ,expr (begin ,expr (repeater (- k 1)))))
    (repeater ,n)))

(define (repeated-call n f)
  (if (= n 1) (f) (begin (f) (repeated-call (- n 1) f))))

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr)))

; For

(define (map fn vals) 
  (if (null? vals) 
      () 
      (cons (fn (car vals)) 
            (map fn (cdr vals)))))

(map (lambda (x) (* x x)) '(2 3 4 5))

(define-macro (for sym vals expr)
  (list 'map (list 'lambda (list sym) expr) vals))

(define-macro (for sym vals expr)
  `(map (lambda (,sym) ,expr) ,vals))

(for x '(2 3 4 5) (* x x))

(define-macro (for-no-quote sym vals expr)
  `(map (lambda (,sym) ,expr) ',vals))

(for-no-quote x (2 3 4 5) (* x x))