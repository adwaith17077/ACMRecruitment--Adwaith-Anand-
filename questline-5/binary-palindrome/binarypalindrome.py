def binarypalindrome(n):
    if n[::-1]==n:
        print(int(n,2),',',n,'is a binary palindrome')
    else:
        print(int(n,2),',',n,'is not a binary palindrome')

x=format(9,'04b')
binarypalindrome(x)

x=format(10,'04b')
binarypalindrome(x)
    
