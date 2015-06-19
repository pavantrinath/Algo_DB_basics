from Stacks import Stack

def prefixeval(list):
        values = Stack()

        for token in list[::-1]:
            if token in "0123456789":
                values.push(int(token))

            else:
                if token in "()":
                    continue
                else:
                    op1 = values.pop()
                    op2 = values.pop()
                    result = calculate(token,op1,op2)
                    values.push(result)
        return values.pop()


        print values

def postfixeval(list):
        values = Stack()

        for token in list:
            if token in "0123456789":
                values.push(int(token))

            else:
                if token in "()":
                    continue
                else:
                    op1 = values.pop()
                    op2 = values.pop()
                    result = calculate(token,op1,op2)
                    values.push(result)
        return values.pop()


        print values

def calculate(op,op1,op2):
    if op =="*":
        return op1 * op2
    else:
        if op == "/":
            return op1/op2
        else:
            if op=="+":
                return op1 + op2
            else:
                return op1 - op2






if __name__ == '__main__':

    n = list(raw_input().split(" "))
    print postfixeval(n)