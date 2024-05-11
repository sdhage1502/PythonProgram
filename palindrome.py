def palindroome(string1):
    return string1==string1[::-1]
str1=input("Enter a number:")
if palindroome(str1):
    print("is palindrome")
else:
    print("is not palindrome")


