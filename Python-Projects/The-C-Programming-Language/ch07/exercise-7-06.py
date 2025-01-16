# Exercise 7-6. Write a program to compare two files, 
# printing the first line where they differ.

import sys

def main():
    if (len(sys.argv) < 3):
        print("Usage: python3 exercise-7-06.py file1 file2")
        exit(1)
    
    linenumber = 1
    file1 = file2 = None
    try:
        file1 = open(sys.argv[1], "rt")

        try:
            file2 = open(sys.argv[2], "rt")

            while line1 := file1.readline():
                line2 = file2.readline()
                if line1 != line2:
                    print("Lines are different at line #", linenumber)
                    print(sys.argv[1], line1, end="")
                    print(sys.argv[2], line2, end="")
                    break
                linenumber += 1
        except PermissionError:
            print("Permission denied:", sys.argv[2])
        except FileNotFoundError:
            print("File not found:", sys.argv[2])
        finally:
            if file2 is not None:
                file2.close()
    except PermissionError:
        print("Permission denied:", sys.argv[1])
    except FileNotFoundError:
        print("File not found:", sys.argv[1])
    finally:
        if file1 is not None:
            file1.close()

main()

# $ python3 exercise-7-06.py file1.txt file2.txt
# Lines are different at line # 3
# file1.txt Different line
# file2.txt The rain in Spain falls mainly in the plain.