'''You are given a list that contains some numbers. You have to print a list of next palindromes only if
the number is greater than 10; otherwise, you will print that number.
Input:
[1, 6, 87, 43]
Output:
[1, 6, 88, 44]'''
'''Author - Asif
Date - 19-10-2020
Purpose - Return a next palindrome if number is greater than 10 else return actual number.'''
def next_palindrome(n):
        n = n+1
        while not is_palindrome(n):
            n+=1
        return n
def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__ == '__main__':
    num = int(input("How many elements you want to add:"))
    mylist=[]
    for i in range(num):
        numbers = int(input("Enter numbers in your list:\n"))
        mylist.append(numbers)
    new_list=[]
    for item in mylist:
        if item > 10:
            n = next_palindrome(item)
            new_list.append(n)
        else:
            new_list.append(item)
    print(f"Next palindromes list for numbers greater than 10 in {mylist} is {new_list}")

