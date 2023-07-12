def div(a,b,c=None,d=None):
    if a == 0 or b == 0 or c == 0 or d == 0:
        string = "inf"
        return string
    else:
        return a / b / c / d
