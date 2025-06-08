import sys

lenn = len(sys.argv)
print(lenn)
if (lenn == 1):
    print()
elif (lenn != 2):
    print("AssertionError: more than one argument is provided")
else:
    # print(type(sys.argv[1]))
    try:
        nbr = int
    except:

print(sys.argv)