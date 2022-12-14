(define (my-filter pred s) 
        (cond ((null? s) nil)
              ((pred (car s)) 
                       (cons (car s) (my-filter pred (cdr s))))
              (else (my-filter pred (cdr s)))
        )
)


(define (interleave lst1 lst2)
        (cond ((null? lst1)
                      lst2)
              ((null? lst2)
                      lst1)
              (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
        )
)

(define (accumulate joiner start n term)
        (if (= n 0)
            start
            (begin (define result (joiner start (term n)))
                   (accumulate joiner result (- n 1) term))
        )
)

(define (no-repeats lst)
        (define helper (lambda (s filtered-lst)
                (cond ((null? s) filtered-lst)
                      ((> (last-element filtered-lst) (car s))
                              (begin (define result (append filtered-lst (list (car s))))
                                     (helper (cdr s) result)))
                      (else (helper (cdr s) filtered-lst))))
        )
        (helper (cdr lst) (list (car lst)))
)

(define (last-element lst)
        (if (null? (cdr lst))
        (car lst)
        (last-element (cdr lst)))
)
