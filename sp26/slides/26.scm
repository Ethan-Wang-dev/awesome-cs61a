; Call expressions

(+ 1 2 3 4)
(+)
(*)
(- 12)
(- 20 1 2 3 4 5)
(+ 2 (* 2 (+ 3 (* 2 2 2 2 3 3 7))))
(number? 12)
(integer? 3.3)
(zero? 2)

; How Scheme changes programs

(define (a-plus-abs-b a b) ((if (< b 0) - +) a b))

; Lambda

((lambda (g y) (g (g y))) (lambda (x) (+ x 1)) 3)

(define (f g)
  (lambda (y) (g (g y))))
((f (lambda (x) (* x x))) 3)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Sierpinski by drawing lines or filling or negating region
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (repeat k fn)
    (if (> k 0)
        (begin (fn) (repeat (- k 1) fn))
        nil))

;; Repeats the following 3 times: calls FN and turns left 120
(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))))

;; Sierpinski filled fractal
(define (sier-filled d level)
  (if (= level 1)
    (begin
      (begin_fill)
      (tri (lambda () (fd d)))
      (end_fill))
    (tri (lambda () (sier-filled (/ d 2) (- level 1)) 
                    (fd d)))))

;; Sierpinski line fractal
(define (sier-line d level)
  (tri (lambda () 
          (if (> level 1) 
              (sier-line (/ d 2) (- level 1))
             'pass)
          (fd d))))

;; Sierpinski line edge fractal
(define (sier-line-edge d level)
  (if (= level 1)
    (tri (lambda ()
          (fd (/ d 2))
          (lt 60)
          (fd (/ d 2))
          (fd (/ d -2))
          (rt 60)
          (fd (/ d 2))))
    (tri (lambda ()
            (sier-line-edge (/ d 2) (- level 1))
            (fd d)))))

;; Sierpinsky negative space fractal
(define (sier-negative d level)
  (fd (/ d 2))
  (lt 60)
  (sier-filled (/ d 2) 1)
  (rt 60)
  (back (/ d 2))
  (if (> level 1)
      (tri (lambda ()
              (sier-negative (/ d 2) (- level 1))
              (fd d)))))
;(speed 0)
;(rt 90)
;(bk 200)
;;; uncomment one of the following four
;(sier-filled 400 2)
;(sier-line 400 2)
;(sier-line-edge 400 2)
;(sier-negative 400 2)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Sierpinski chaos game
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;; Some random functions since neither Scheme nor Turtle had them

(define seed 123456)

(define (rand)
  (set! seed (modulo (+ (* 1103515245 seed) 12345) 2147483648))
  seed)

(define (randint low high)
  (+ low (modulo (rand) (+ 1 (- high low)))))

;;; Some standard scheme functions

(define (list-ref lst n)
  (if (= n 0)
      (car lst)
      (list-ref (cdr lst) (- n 1))))

(define (cadr lst) (car (cdr lst)))

;;; Some 2D graphics helpers

(define (x pt) (car pt))
(define (y pt) (cadr pt))

(define (goto-xy vertex)
  (goto (x vertex) (y vertex)))

(define (midpoint p q)
  (list (/ (+ (x p) (x q)) 2)
        (/ (+ (y p) (y q)) 2)))

(define (centered-filled-circle radius)
  (rt 90)
  (fd radius)
  (lt 90)
  (begin_fill)
  (circle radius)
  (end_fill)
  (rt 90)
  (back radius)
  (lt 90))

;;; Sierpinsky chaos setup code (three corners)

(define triangle-height (* 200 (/ (sqrt 3) 2)))
(define v1 (list -200 (- triangle-height)))
(define v2 (list 0       triangle-height))
(define v3 (list  200 (- triangle-height)))

(define vertices (list v1 v2 v3))

(define (random-vertex)
  (list-ref vertices (randint 0 2)))

;;; Chaos game for some number of iterations

(define (chaos iterations current-point)
  (if (= iterations 0)
      'done
      (let ((next (midpoint current-point (random-vertex))))
        (penup)
        (goto-xy next)
        (pixel (x next) (y next) "#000000")
        ;(pendown)
        ;(centered-filled-circle 2)
        (chaos (- iterations 1) next))))

;;; Sierpienski chaos game
;;; https://en.wikipedia.org/wiki/Chaos_game

(define (sier-chaos n)
  (clear)
  (pu)
  (hideturtle)
  (speed 0)
  (color "#FF0000")
  (goto-xy v1)
  (centered-filled-circle 10)
  (color "#007F00") ;; I find bright green too bright
  (goto-xy v2)
  (centered-filled-circle 10)
  (color "#0000FF")
  (goto-xy v3)
  (centered-filled-circle 10)
  (color "#000000")
  ;(pixelsize 3)
  (chaos n '(0 0)))

;(sier-chaos 5000)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Sierpinski using XOR
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;; Some scheme functions

;; map dyadic FN over LST1 and LST2 
;; Requires lst1 and lst2 are equal length
(define (map2 fn lst1 lst2)
  (if (null? lst1)
    '()
    (cons (fn (car lst1) (car lst2))
          (map2 fn (cdr lst1) (cdr lst2)))))

;; Add ELT to the last element of the list LST
(define (add-to-end elt lst)
  (if (null? lst)
    (list elt)
    (cons (car lst) (add-to-end elt (cdr lst)))))

;; xor says exactly one of A,B are true (i.e., they're not equal)
(define (xor a b)
  (not (equal? a b)))

;;; Sierpinski-specific routines

;; Return the next Sierpinski row
(define (next-sier row-vals)
  (map2 xor (cons #f row-vals) (add-to-end #f row-vals)))

;; Draw the correct row
(define (circle-sier-row-helper row-vals)
  (if (not (null? row-vals))
    (begin
      (if (car row-vals)
        (centered-filled-circle 10))
      (fd 20)
      (circle-sier-row-helper (cdr row-vals)))))

;; Move to the correct row then call the helper to draw it
(define (circle-sier-row row-num row-vals)
  (pu)
  (color "#000000") ;; I find bright green too bright
  (goto-xy v2)  
  (setheading 210)
  (fd (* 20 row-num)) ;; assume row 0 starts
  (setheading 90)
  (circle-sier-row-helper row-vals))

;; Sierpinski triangle with circles based on XOR
(define (circle-sier row-max)
  (define (circle-sier-helper row-num row-vals)
      (if (not (= row-num row-max))
          (begin
            (circle-sier-row row-num row-vals )
            (circle-sier-helper (+ row-num 1) (next-sier row-vals)))))
  (circle-sier-helper 0 (list True)))

(speed 0)
(circle-sier 32) ;; 32 is the full triangle
