**1**
in the interative method we need to perform a loop and iterate through every element
first I assigned a variable with empty string let it be 'r'. and made a loop which iterates through every character in the string 
and to the variable r i added the string character in the loop 
ie,

    for i in s:
        r=i+r
this stores the characters in the loop and pushes it back so we get reversed string


**2**
recursive method is easy because you just have to assign a variable to input the string reversed by string slicing ie, let a variable be r then 
we can assign r=s[::-1]  {let s be a string} it will return the string reversed
