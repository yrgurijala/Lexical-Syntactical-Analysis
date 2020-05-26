def add(lista, listb):
    remainder = None
    addList1 = LinkedList()

    refNodea = lista
    refNodeb = listb

    while refNodea.isnotempty() or refNodeb.isnotempty():
        if refNodea.isnotempty() is False:
            a = 0
            b = refNodeb.head.Value
        elif refNodeb.isnotempty() is False:
            b = 0
            a = refNodea.head.Value
        else:
            a = refNodea.head.Value
            b = refNodeb.head.Value

        addition = str(int(a) + int(b))

        if remainder is not None:
            addition = str(int(a) + int(b) + remainder)

        if len(addition) is 2:
            addList1.insertBack(addition[1])
            remainder = int(addition[0])
        else:
            addList1.insertBack(addition)
            remainder = None

        refNodea.deletehead()
        refNodeb.deletehead()

    if remainder is not None:
        addList1.insertBack(remainder)

    return addList1


def multiply(lista, listb):
    multList = LinkedList()
    multList1 = LinkedList()
    checkSecondRow = 0

    refNodea1 = lista
    refNodeb1 = listb

    while refNodea1.isnotempty():
        remainder = None
        a = refNodea1.head.Value
        check = refNodeb1.counter
        check1 = 0
        while check1 != check:
            b = refNodeb1.returnValue(check1)
            multiplication = str(int(a) * int(b))

            if remainder is not None:
                multiplication = str(int(a) * int(b) + remainder)

            if len(multiplication) is 2:
                multList1.insertBack(multiplication[1])
                remainder = int(multiplication[0])
            else:
                multList1.insertBack(multiplication)
                remainder = None

            check1 = check1 + 1

        refNodea1.deletehead()

        if remainder is not None:
            multList1.insertBack(remainder)

        for i1 in range(checkSecondRow):
            multList1.insertfront(0)

        checkSecondRow = checkSecondRow + 1
        multList = add(multList1, multList)
        multList1.clearList()

    return multList


class Node:
    def __init__(self, value):
        self.Value = value
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def insertfront(self, value):
        newNode = Node(value)
        newNode.nextNode = self.head
        self.head = newNode
        self.counter = self.counter + 1

    def insertBack(self, value):
        newNode = Node(value)
        newNode.nextNode = None
        self.counter = self.counter + 1

        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head

        while lastNode.nextNode:
            lastNode = lastNode.nextNode

        lastNode.nextNode = newNode

    def deletehead(self):
        if self.head is None:
            return
        refNode = self.head
        self.head = refNode.nextNode
        self.counter = self.counter - 1

    def clearList(self):
        self.head = None
        self.counter = 0

    def isnotempty(self):
        if self.head is None:
            return False
        return True

    def returnValue(self, a):
        refNode = self.head

        for i2 in range(a):
            refNode = refNode.nextNode

        return refNode.Value

    def dispay(self):
        refNode = self.head

        while refNode is not None:
            print(refNode.Value)
            refNode = refNode.nextNode

    def calculate(self, node):
        refNode = node

        if refNode is not None:
            refNode1 = refNode.nextNode

            if refNode1 is not None:
                refNode2 = refNode1.nextNode

                if refNode2 is None:
                    self.head.Value = -1
                    return

                if refNode.Value[0] is not 'm' and refNode.Value[0] is not 'a':
                    self.calculate(refNode1)
                    return
                if refNode1.Value[0] is 'm' or refNode1.Value[0] is 'a':
                    self.calculate(refNode1)
                    return
                if refNode2.Value[0] is 'm' or refNode2.Value[0] is 'a':
                    self.calculate(refNode2)
                    return

                aList = LinkedList()
                bList = LinkedList()

                if refNode1.Value[0] is 'b':
                    self.head.Value = -1
                    return

                i = 0
                while i < len(refNode1.Value):
                    aList.insertfront(refNode1.Value[i])
                    i += 1

                i = 0
                while i < len(refNode2.Value):
                    bList.insertfront(refNode2.Value[i])
                    i += 1

                if refNode.Value[0] is 'm':
                    ansList = multiply(aList, bList)
                else:
                    ansList = add(aList, bList)

                refNode.Value = ""

                i = 0
                while i < ansList.counter:
                    refNode.Value = str(ansList.returnValue(i)) + refNode.Value
                    i += 1

                refNode.nextNode = refNode2.nextNode
                self.counter -= 2
