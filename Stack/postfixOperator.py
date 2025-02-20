from stack import Stack


def precedence(operator):
    if operator in "+-":
        return 1
    elif operator in "*/":
        return 2
    return -1  # Default for invalid input

def nextToken(s):
    token=""
    if len(s)>0:
        if s[0] in "+-*/":
            token=s[0]
            s=s[1:]
        else:
            while len(s)>0 and s[0] not in "+-*/":
                token += s[0]
                s = s[1:]
    return token, s


def toPostfix(formula):
    ans=[]
    s=Stack(1000)

    token,formula=nextToken(formula) # Get first token

    while token:
        if token in "+-*/":
            while not s.isEmpty() and precedence(s.peek()) >= precedence(token):
                ans.append(s.pop()) # Pop higher/equal precedence operators
            s.push(token) # Push the current operator onto the stack
        else:
            ans.append(token) # If number, add it to output
        token,formula=nextToken(formula) # Get next token
        # print(token, formula)
    print(s)
    while not s.isEmpty():
        ans += [s.pop()] # Pop remaining operators
    return ans

def processPostfix(postfixTokens):
    s=Stack(1000)
    for t in postfixTokens:
        if t in "+-*/":
            op2=s.pop() # Right operand
            op1=s.pop() # Left operand
            print(op2, op1)
            if t=="+":
                ans=op1+op2
            elif t=="*":
                ans = op1 * op2
            elif t=="-":
                ans = op1 - op2
            elif t=="/":
                ans= op1 / op2
            s.push(ans)
        else:
            s.push(int(t))

    return s.pop()

string1 = "3+5*2-8/4"
postfix= toPostfix(string1)
print(postfix)
result=processPostfix(postfix)
# print(result)
