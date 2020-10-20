'''Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisor of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5
2 is a divisor of20
3 is not a divisor of 20
…
5 is a divisor of 20'''
def integer():
    try:
        apples = int(input("How many apples have Harry got?:"))
        min_number = int(input("Enter a minimum number:"))
        max_number = int(input("Enter a maximum number:"))
        if min_number>max_number:
            print("min_number can't be greater than max_number")
        if min_number!= max_number:
            for num in range(min_number, max_number+1):
                if apples%num==0:
                    print(f"{num} is divisor of {apples} ")
                else:
                    print(f"{num} is not a divisor of {apples}")
        elif min_number==max_number:
            print("This is invalid range as min_num is equal to max_num.")
            for num in range(min_number, max_number+1):
                if apples%num == 0:
                    print(f"{num} is divisor of {apples} ")
                else:
                    print(f"{num} is not a divisor of {apples}")

    except ValueError:
        print("Accept intergers value only!")
        integer()
integer()




