def handle_choice(integerA):
    match integerA:
        case 1:
            print("integerA = 1")
        case 2:
            print("integerA = 2")
        case 3:
            print("integerA = 3")
        case _:
            print("integerA is not 1,2, or 3")

for i in range(4):
    print(i)
    handle_choice(i)

# $ python match-statement.py 
# 0
# integerA is not 1,2, or 3
# 1
# integerA = 1
# 2
# integerA = 2
# 3
# integerA = 3