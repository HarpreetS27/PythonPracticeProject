def reverse(num):
    rev = 0
    while num > 0:
        reminder = num % 10
        rev = (rev * 10) + reminder
        num = int(num / 10)
    return rev


isPalindrome = False


def check_palindrome(val1, val2):
    global isPalindrome
    if val == val2:
        isPalindrome = True
    else:
        isPalindrome = False


test_cases = int(input("Enter the number of test cases"))
for i in range(test_cases):
    val = int(input("Enter the values you want to check : "))
    rever = reverse(val)
    check_palindrome(val, rever)
    if isPalindrome:
        print("This is already a palindrome")
    else:
        while not isPalindrome:
            val += 1
            rever = reverse(val)
            check_palindrome(val, rever)
        print(f"The next palindrome for this number is {val}")

