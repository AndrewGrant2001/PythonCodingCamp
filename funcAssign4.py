def fib(term):
   if term <= 1:
       return term
   else:
       return(fib(term - 1) + fib(term - 2))


num = int(input("Enter i-th term: "))
print(f'When term = {num}, we have the sum = {fib(num)}')