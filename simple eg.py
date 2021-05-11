# Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum

def sum_or_multiplication_of(num1,num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2
print("result",sum_or_multiplication_of(40,2))



# output
result 80
