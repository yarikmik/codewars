"""
Create a function named divisors/Divisors that takes an integer n > 1
and returns an array with all of the integer's divisors(except for 1 and the number itself),
from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#)
(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""


# def divisors(integer):
#     arr = []
#     i = 2
#     while i < integer:
#         if integer % i == 0:
#             arr.append(i)
#         i += 1
#     return arr if len(arr) > 0 else f'{integer} is prime'

def divisors(integer):
    return [i for i in range(2, integer) if integer % i == 0] or f'{integer} is prime'

print(divisors(14))
