# Python program showing
# a use of raw_input()
from symbol import argument

from pip._vendor.distlib.compat import raw_input

# Input command in command line
inp = raw_input("Enter value for compressed string : ")


# Function that checks that the input does not have any
# inappropriate values
def errorCheck(comInput):
    countDel = 0

    inpArray = []

    for val in comInput:
        # Check to see if first value is a number
        # Check to see if there are any upper case letters in string
        # Check correct delimiter
        if val.isnumeric() or val.islower() or val == "[" or val == "]":
            inpArray.append(val)
        else:
            print("Incorrect input value")
            inpArray = []
            break

    return inpArray


officialInput = errorCheck(inp)
delIndex = officialInput.index("[")
# print(x)
# print(delIndex)

print("Length of array is: ")
print(len(officialInput))


# Function that check the indices of brackets
def idxDelimiterCheck(inp, delimiter):
    # Initiate index list as empty
    bracList = []
    countBrac = 0
    # Count the number of delimeter in the input
    count = inp.count(delimiter)
    # While loop that
    while count > 0:
        # Search
        idx = [i for i, n in enumerate(inp) if n == delimiter][countBrac]
        # Increment to bracket count to new index
        countBrac += 1
        # Error checking for the output correct results
        # print("Count Bracs:")
        # print(countBrac)
        # print(idx)
        # Append the value of the index the delimiter to an array
        bracList.append(idx)

        # Decrement count until no more value are found
        count -= 1
        # print(count)
    return bracList


# List of indices of open and close brackets
idxBracOpen = idxDelimiterCheck(officialInput, '[')
idxBracClose = idxDelimiterCheck(officialInput, ']')

print(idxBracOpen)
print(idxBracClose)


# b = 10[ab]
# Function that checks the location of each open and close Bracket
# to determine the best way to create a solution
def checkBrackLoc(lstOpen: list, lstClose: list) -> [list, int]:
    totLst = []
    # Check if bracket list are equal
    # Same number of open and close brackets
    if len(lstOpen) == len(lstClose):
        # Simplest case scenario
        # ex. 10[ab]
        if len(lstOpen) == 1:
            if lstOpen[0] < lstClose[0]:
                return [[lstOpen[0], lstClose[0]], 0]
            else:
                print("Incorrect Bracket Placement")
        elif len(lstOpen) > 1:
            for i in range(0, len(lstOpen)):
                # Case if open and close bracket are in parallel
                # Ex. 2[a]10[b]
                if lstOpen[i] < lstClose[i] < lstOpen[i + 1]:
                    for j in range(0, len(lstOpen)):
                        # Joining open bracket list and close bracket list
                        totLst.append([lstOpen[j], lstClose[j]])
                        # Sorting list of Integers in ascending
                        # totLst.sort()
                    return [totLst, 1]
                # Case where one repetition can occur inside the other
                # Ex. 2[3[a]b]
                elif lstOpen[i] < lstClose[i] and lstOpen[i + 1] < lstClose[i]:
                    lstOpen.sort(reverse=1)
                    for j in range(0, len(lstOpen)):
                        # Joining open bracket list and close bracket list
                        totLst.append([lstOpen[j], lstClose[j]])
                        # Sorting list of Integers in ascending
                        # totLst.sort()
                    return [totLst, 2]
                else:
                    return [[0], -1]
    else:
        print("Incorrect Bracket Amount")


bracArray = checkBrackLoc(idxBracOpen, idxBracClose)
print(bracArray[0])
print(bracArray[1])

switchVal = int(bracArray[1])
argBracArray = bracArray[0]


# Function that executes
# Simplest case scenario
# ex. 10[ab]
# print(numString(x, bracArray))
def singleStringNumber(argumentArray, inputValue):
    numArray = []  # Array that store number values
    for i in range(0, argumentArray[0]):
        numArray.append(inputValue[i])
    print(numArray)
    # Join number to create a string
    num = ''.join(map(str, numArray))

    # Try to convert string to a number
    try:
        num = int(num)

    except ValueError:
        print("Not a number")

    else:
        # Defining the number of times character is repeated
        num = int(num)
        # print(num)

    alpArray = []  # Array that store the alphabet values
    for j in range(argumentArray[0] + 1, argumentArray[1]):
        alpArray.append(inputValue[j])
    # Characters being repeated
    print(alpArray)
    # Joining the characters between the open and close bracket
    alp = ''.join(map(str, alpArray))
    # Printing the joined characters
    # print(alp)

    # Printing the repeated characters (alp) based
    # on value num
    print("Output:")
    print(alp * num)


# Function that executes
# Case if open and close bracket are in parallel
# Ex. 2[a]10[b]
def seriesStringNumber(argumentArray, inputValue):
    num = ""
    alp = ""
    numArray = []  # Array that store number values
    alpArray = []  # Array that store the alphabet values
    intList = []
    startIdx = 0
    for lst in argumentArray:
        print(lst)
        for i in range(startIdx, lst[0]):
            num = num + inputValue[i]
            # print(num)

            # print(inputValue[i])
        numArray.append(num)
        print(numArray)
        for num in numArray:
            # Try to convert string to a number
            try:
                num = int(num)

            except ValueError:
                print("Not a number")

            else:
                num = int(num)
        intList.append(num)
        # print(intList)
        startIdx = lst[1] + 1
        num = ""

        for j in range(lst[0] + 1, lst[1]):
            alp = alp + inputValue[j]
        alpArray.append(alp)
        print(alpArray)
        alp = ""
        # Map and repeat characters (alp) based
        # on value num
        result = list(map(lambda z, y: z * y, alpArray, intList))
        # result = map(lambda z, y: z * y, alpArray, intList)

        # Join output to one complete string
        s = ""
        joinedResult = s.join(result)
    print("Output:")
    print(joinedResult)


def insideStringNumber(argumentArray, inputValue):
    count = 0
    num = ""
    alp = ""
    numArray = []  # Array that store number values
    alpArray = []  # Array that store the alphabet values
    intList = []
    startIdx = argumentArray[1][0] + 1
    diff = argumentArray[1][1] - argumentArray[0][1]
    for lst in argumentArray:
        print(lst)
        for i in range(startIdx, lst[0]):
            num = num + inputValue[i]
            # print(num)

            # print(inputValue[i])
        numArray.append(num)
        print(numArray)
        for num in numArray:
            # Try to convert string to a number
            try:
                num = int(num)

            except ValueError:
                print("Not a number")

            else:
                num = int(num)
        intList.append(num)
        # print(intList)
        startIdx = 0
        num = ""
        if count == 0:
            for j in range(lst[0] + 1, lst[1]):
                alp = alp + inputValue[j]
                alpArray.append(alp)
            print(alpArray)
            alp = ""
            # Map and repeat characters (alp) based
            # on value num
            result = list(map(lambda z, y: z * y, alpArray, intList))
            # result = map(lambda z, y: z * y, alpArray, intList)
        else:
            # Ex.2[3[a]b]
            if diff > 1:
                for j in range(argumentArray[0][1] + 1, lst[1]):
                    del alpArray[0]
                    del intList[0]
                    alp = result[0] + inputValue[j]
                    alpArray.append(alp)
                    # Map and repeat characters (alp) based
                    # on value num
                    result = list(map(lambda z, y: z * y, alpArray, intList))
            # Ex.2[3[a]]b
            else:
                for j in range(argumentArray[1][1] + 1, len(inputValue)):
                    del alpArray[0]
                    del intList[0]
                    alp = alp + inputValue[j]
                    alpArray.append(result[0])
                    alpArray.append(alp)
                    intList.append(1)
                    # print("Made it")
                alp = ""
                result = list(map(lambda z, y: z * y, alpArray, intList))
        # Join output to one complete string
        s = ""
        joinedResult = s.join(result)
        count += 1
    print("Output:")
    print(joinedResult)



# Function to repeat strings
# Switcher is dictionary data type here
def repeatStrings(argumentVal, argumentArray, inputValue):
    if argumentVal == 0:
        singleStringNumber(argumentArray, inputValue)
    elif argumentVal == 1:
        seriesStringNumber(argumentArray, inputValue)
    elif argumentVal == 2:
        insideStringNumber(argumentArray, inputValue)
    else:
        print("Can't Repeat Strings!! Invalid Method")


repeatStrings(switchVal, argBracArray, officialInput)
# singleStringNumber(argBracArray)
