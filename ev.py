from stacks import Stack
def eval(list):   
    op = Stack()
    val = Stack()

    for i in list:
        if type(i)== int:
            val.push(int(val))
        
            
            
        
def hasPrecedence(op1, op2):
    if (op2 == '(' or op2 == ')'):
        return 0
    if ((op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-')):
        return 0
    else:
        return 1
 
   


if __name__ == '__main__':
    n = list(raw_input().split(" "))
    eval(n)
    

    



    
    