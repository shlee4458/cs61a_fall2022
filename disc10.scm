; Q1 fib num
(define (vir-fib n)
        (if (= n 1)
        1
        (+ n (vir-fib (- n 1))))
)

; Q2 list
(define with-list (list (list 'a 'b) 'c 'd '(e)))

(define with-quote (list (list (quote a) (quote b)) (quote c) (quote d) (list (quote e))))


(define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)


(define with-cons (cons helpful-list another-helpful-list))
(draw with-cons)


; Q3 list-concat
(define (list-concat a b)
        (if (null? a)
            b
            (cons (car a) (list-concat (cdr a) b)))
)

; Q4 map
(define (map-fn fn lst)
        (if (null? lst)
            nil
            (cons (fn (car lst)) (map-fn fn (cdr lst))))
)

(define fn (lambda (x) (* x 2)))

; Q5 remove
(define (remove item lst)
        (filter (lambda (x) (not (= x item))) lst)
)