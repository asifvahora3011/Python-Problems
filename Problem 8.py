'''Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number
and put one of the values (randomly generated) as wrong.Rohan Das did this to fool his classmates and make them commit
a mistake in a test. You cannot tolerate this!Rohan das is a fraud by nature. Rohan Das wrote a python function to print
a multiplication table of a given number and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it
to the screen! If the table is correct, your function returns None'''
import random
def multiplication(num):
    wrong=random.randint(0,9)
    table = [i*num for i in range(1,11)]
    table[wrong]= table[wrong]+ random.randint(0,10)
    return table
def isCorrect(table,number):
    for i in range(1,11):
        if table[i-1] != i*number:
            return i-1
    return None
if __name__ == '__main__':
    number = int(input("Enter a number:"))
    myTable = multiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable,number)
    print(f"The table is wrong at index {wrongIndex}")