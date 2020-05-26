from LinkedList import *


# lex functions create tokens into Linked List
def lex(command):
    i = 0
    length = len(command)
    checkToken = ""
    myList = LinkedList()
    while i < length:
        if command[i] is not '(' and command[i] is not ')' and command[i] is not ',':
            checkToken = checkToken + command[i]
        else:
            if checkToken is not "":
                myList.insertBack(checkToken)
            checkToken = ""

        i = i + 1

    while myList.counter > 1:
        myList.calculate(myList.head)

        if myList.head.Value is -1:
            return "invalid expression"

    return myList.head.Value
