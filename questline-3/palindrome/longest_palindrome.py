s = 'ebbaabad' #Example input string
l=[]
  
for i in range(len(s)):
    # Odd-length palindromes
    left1, right1 = i, i
    while left1 >= 0 and right1 < len(s) and s[left1] == s[right1]:
        so=s[left1:right1+1]
        left1 -= 1
        right1 += 1
        l.append(so)
 
    # Even-length palindromes
    left2, right2 = i, i + 1
    while left2 >= 0 and right2 < len(s) and s[left2] == s[right2]:
        se=s[left2:right2+1]
        left2 -= 1
        right2 += 1
        l.append(se)

m=0
for i in l:
    if len(i)>m:
        longestpalindrome=str(i)
        m=len(i)
print(longestpalindrome)
