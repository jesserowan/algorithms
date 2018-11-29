def parensValid(string):
    open = 0
    closed = 0
    for x in range (len(string)):
        if string[x] == "(":
            open += 1
        elif string[x] == ")":
            closed += 1
        if closed > open:
            return False
    if closed == open:
        return True
    else:
        return False

print(parensValid("Y(3(p)p(3)r)s"))
print(parensValid("N(0(p)3"))
print(parensValid("N(0)t )0(K"))
