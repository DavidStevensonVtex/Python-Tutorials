# Note: match is not supported in Python 3.8, but is supported in Python 3.10
# $ python3 --version
# Python 3.8.10

def minprintf(fmt, *args):
    argindex = 0
    # print("fmt", fmt)
    # for arg in args:
    #     print(argindex, arg)
    #     argindex += 1

    informat = False
    output = ""
    for c in fmt:
        if informat:          
            if c == 'd':
                output += f"{args[argindex]:d}"
                argindex += 1
            elif c == 'f':
                output += f"{args[argindex]:f}"
                argindex += 1
            elif c == 's' or c == 'c':
                output += f"{args[argindex]}"
                argindex += 1
            else:
                output += args[argindex]
            informat = False
        elif c == '%':
            informat = True
            continue
        else:
            informat = False
            output += c
    print(output)

minprintf("%d %f %s %c", 123, 2.34, "abc", 'c')

# $ python3 minprintf.py 
# 123 2.340000 abc c