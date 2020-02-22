def is_prime(num):
    """ 
    INPUT: A number
    OUTPUT: A print statement whether or not the print statement is prime
    """
    for n in range(2,num):
        if num % n ==0:
            print("not prime")
            break
    else:
        print("The number is prime")
is_prime(50)

def square(num):
    result = num**2
    return result

square(4)

def even(num):
    return num%2 ==0
even(53)

def reverse(rev):
    return rev[::-1]
reverse("Daniel")


  
