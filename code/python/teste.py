def userprint(umessage):
    finalmsg = f"The inputed user message is: {umessage}"
    return finalmsg

option = input("1 - for till certain number\n2 - print inputed message\nOption: ")
if option == "1":
    number = int(input("Enter a number: "))
    for nmb in range(number):
        print(nmb)
if option == "2":
    muser = input("Enter a message: ")
    print(userprint(muser))
