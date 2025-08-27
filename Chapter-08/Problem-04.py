def factorial(n):
    if n == 1 or n == 0 :
      return 1
    else:
        return n + factorial(n-1)
    
a = factorial(int(input(f"Enter the number: ",)))
print(a)