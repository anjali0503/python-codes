# Exercise 3: Given a string, display only those characters which are present at an even index number.

def printEveIndexChar(str):
    for i in range(0, len(str)-1, 2):
        print("index[",i,"]", str[i] )

input_Str = "python"
print("Orginal String is ", input_Str)

print("Printing only even index chars")
printEveIndexChar(input_Str)


#output

Orginal String is  python
Printing only even index chars
index[ 0 ] p
index[ 2 ] t
index[ 4 ] o
