#write a program to check wether a given string is a palindrome or not.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1] 
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

#write a program to check wether a given string is a palindrome or not.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1] 
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')   
else:
    print(f'"{string}" is not a palindrome.')   