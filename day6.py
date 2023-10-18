'''#Hanoi problem
def toh(n,s,a,d):
    if n>0:
        toh(n-1,s,d,a)
        print(s,d)
        toh(n-1,a,s,d)
n=int(input("enter no of rings"))
toh(n,'A','B','C')
o/p:2
A B
A C
B C

3
A C
A B
C B
A C
B A
B C
A C'''
# paranthesis code
'''class day6:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        res=[]
        def backtrack(opencount=0,closecount=0):
            if opencount==closecount==n:
                res.append("".join(l))
            if opencount<n:
                l.append('(')
                backtrack(opencount+1,closecount)
                l.pop()
            if closecount<opencount:
                l.append(")")
                backtrack(opencount,closecount+1)
                l.pop()
            return res
        return backtrack()'''
'''#
paranthesis
def generateParenthesis(n):
    def backtrack(combination, open_count, close_count):
        if len(combination) == 2 * n:
            result.append(combination)
            return
        if open_count < n:
            backtrack(combination + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(combination + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    return result

# Test cases
n = int(input())
print(generateParenthesis(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]'''
'''
valid parenthesis
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack

# Test cases
s1 = input()
print(isValid(s1))  # Output: True'''


