(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car cdr(s)))

(define (caddr s) (car cdr(cdr s)))

(define (ascending? asc-lst) 
        (cond ((null? (cdr asc-lst)) #t)
              ((> (car asc-lst) (car (cdr asc-lst))) #f)
              (else (ascending? (cdr asc-lst)))))

(define (square n) (* n n))

(define (pow base exp) 
        (cond ((or (= exp 1) (= base 1)) base) 
              ((even? exp) (square (pow base (/ exp 2))))
              (else (* (square (pow base (/ (- exp 1) 2))) base))))
