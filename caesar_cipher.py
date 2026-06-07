print ('-'*45)

print ('Welcome to Caesar Cipher encode/decoder')

print ('-'*45)

ende = input("Would you like to encode or decode?").lower()

print ('-'*45)

result = ""

if ende == "encode":

    message = input("Please enter the prompt you would like to encode")
    print ('-'*45)
    while True:
        try:
            shifts = int(input("Please enter the number of shifts."))
            break
        except ValueError:
            print ("Not a number please try again")

    for char in message:
            if char.isalpha():
                if char.isupper():
                    offset = 65
                    number = ord(char) - offset
                    shifted = (number + shifts ) % 26 + offset
                    letter = chr(shifted)
                    result += letter
                elif char.islower():
                    offset = 97
                    number = ord(char) - offset
                    shifted = (number + shifts) % 26 + offset
                    letter = chr(shifted)
                    result += letter
                else:
                    result += char
    

elif ende == "decode":
        message = input("Please enter the prompt you would like to decode")
        print ('-'*45)

        try:
            shifts = int(input("Please enter the number of shifts."))
        except ValueError:
                print ("Not a number please try again")

        for char in message:
            if char.isalpha():
                if char.isupper():
                    offset = 65
                    number = ord(char) - offset
                    shifted = (number - shifts) % 26 + offset
                    letter = chr(shifted)
                    result += letter
                elif char.islower():
                     offset = 97
                     number = ord(char) - offset
                     shifted = (number - shifts) % 26 + offset
                     letter = chr(shifted)
                     result += letter
            else:
                result += char


print ('-'*45)
print (result)
