(define (fact n)      (if (= n 1) 1 (* n (fact (- n 1)))))
(define (fact-expr n) (if (= n 1) 1 (list '* n (fact-expr (- n 1)))))
(fact-expr 5)
(eval (fact-expr 5))

(define (is-*-call expr)   (and (list? expr) (equal? '* (car expr))))

(define (flatten-nested-* expr) 
  (if (not (list? expr)) expr
    (let ((expr (map flatten-nested-* expr)))
    	(print expr)
      (if (is-*-call expr)
	  			(apply append (map (lambda (e) (if (is-*-call e) (cdr e) (list e) )) expr))
	 				expr))))

(flatten-nested-* '(* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8)))))

(define (print-evals-noif expr)
  (if (list? expr)
			(map print-evals-noif expr))
  (print expr '=> (eval expr)))

(print-evals-noif '(* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8)))))

(define (print-evals expr)
  (if (list? expr)
      (if (equal? (car expr) 'if)
	  			(begin
  	    		(print-evals (car (cdr expr)))
	   				(if (eval (car (cdr expr)))
	      				(print-evals (car (cdr (cdr expr))))	      
	      				(print-evals (car (cdr (cdr (cdr expr)))))))
					(map print-evals expr)))
  (print expr '=> (eval expr)))
  
(define expr '(* 2 (if (> 2 (+ 1 1)) (+ 3 4) (* 5 6))))

(print-evals expr)

; Quasiquotation

(define (fact-exp n)
  (if (= n 0) 1 `(* ,n ,(fact-exp (- n 1)))))

