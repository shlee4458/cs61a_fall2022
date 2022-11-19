`(if ,condition ,if-true ,if-false)

; Q3 if program
(define (if-program condition if-true if-false)
        `(if ,condition ,if-true ,if-false)

; Q4 power 
(define (pow-expr n p)
        (if (= p 0) 1
                `(* ,(pow-expr n (- p 1)) ,n))
)

; Q5 Swap
(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (swap expr)
    (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
        (if (> (eval second) (eval first))
                (cons op (cons second (cons first rest)))
                expr)
    )
)

; Q6 Make Or
(define (make-or expr1 expr2)
        `(let ((v1 ,expr1))
        (if v1 v1 ,expr2)
        )
)

; Q7 Make-Make or
(define (make-make-or)
        `(define (make-or expr1 expr2) `(let ((v1 ,expr1)) (if v1 v1 ,expr2)))
)