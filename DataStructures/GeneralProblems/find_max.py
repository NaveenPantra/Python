def find_max(num1, num2):
    if num1 < num2:
        maxi = -1
        # range(num1, num2) --> num1 ......... num2 - 1
        # range(num1, num2 + 1) --> num1 ......... (num2 + 1 - 1)
        for num in range(num1, num2 + 1):
            # For multiple of 5 --> num % 5 == 0
            # For Two digit number --> num // 100 == 0
            if num % 5 == 0 and num // 100 == 0 and mulThree(num) % 3:
                maxi = max(maxi, num)
        return maxi


def mulThree(num):
    sumDigit = 0
    while num > 0:
        last = num % 10
        sumDigit += last
        num /= 10
    return sumDigit


print(f"{find_max(10, 15)}")
