<style>
/*.red{*/
/*color: goldenrod;*/
/*}*/

h1{
color: indianred;
}
h1:hover{
color:goldenrod;
}
h2{
color:darkseagreen;
}
h3{
color:lightseagreen;
}
p{
font-size: 1.8rem;
}
li{
font-size: 1.8rem;
}
td{
font-size: 1.4rem;;
}
th{
font-size: 1.4rem;;
}

</style>
# Msc CSE2017
## 1. A strange question stating that if an algorithm needs 21 steps for a 7 x 7 matrix multiplication, how many steps would it need for an n x n matrix multiplication?

Let us consider that for each row.dot(column) we have to do the same thing, and we have to do this for each row.column() pair - so it seems like each dimension would give you 21 / 7 = 3 steps, since you have 7 row.column() pairs needing a total of 21 steps.

so for n*n matrix multiplication, we actually need 3n steps.

## 2. Explain the algorithm of how computers perform division.

Division algorithms in digital designs can be divided into two main categories. Slow division and fast division.

### Slow Division

The simplest slow methods all work in basically the following way. Take the number to be divided (number or dividend) and subtract the divisor from it. Do this recursively with the result of each subtraction until the remainder is less than the divisor. This leftover amount is the remainder. The amount of iterations is the quotient. i.e.

    If we wantto divide 7 by 3:
        1. 7 - 3 = 4
        2. 4 - 3 = 1
        3. 1 < 3
Thus, the answer is 2 remainder 1.

### Fast Division

While slow division is easy to understand, it requires repetitive iterations. There exists various "fast" algorithms, but they all rely on estimation.

Consider the Goldschmidt method:
```
I'll make use of the following:
Q = N/D
This method works as follows:
    1. Multiply N and D with a fraction F in such a way that D approches 1.
    2. As D approaches 1, N approaches Q
```
This method uses binary multiplication which is done via iterative addition. It is also used in modern AMD CPUs.

## 3. Describe the Bottlenecks of greedy AI algorithms.
A greedy algorithm is a simple, intuitive algorithm that is used in optimization problems. The algorithm makes the optimal choice at each step as it attempts to find the overall optimal way to solve the entire problem.




