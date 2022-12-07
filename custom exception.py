number=10
try:
    i_num=int(input("enter a number:"))
    if i_num <number:
        raise ValueTooSmallError
    elif i_num>number:
        raise ValueTooLargeError
except ValueTooSmallError:
        print("This value is too small,try again!")
except ValueTooLargeError:
        print("This value is too large,try again!")
        print("rest of the code")