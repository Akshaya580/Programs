def check_palindrome(s):
    if s == s[::-1]:
        return "TRUE"
    else:
        return "FALSE"
s=input().strip()
print(check_palindrome(s))
