sum_list([], 0).

sum_list([Head|Tail], sum) :-
    sum_list(Tail, TailSum),
    sum is Head + TailSum.

?- sum_list([1, 2, 3, 4, 5], sum).
sum = 15.