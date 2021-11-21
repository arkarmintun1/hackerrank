import re

# Input - an array of integers
# Output - decimal values of each fraction for positive, negative and zero elements


def plusMinus(arr):
    positive = 0
    negative = 0
    neutral = 0
    length = len(arr)
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            neutral += 1
    print(positive/length)
    print(negative/length)
    print(neutral/length)


plusMinus([-4, 3, -9, 0, 4, 1])
# Output
# 0.500000
# 0.333333
# 0.166667

plusMinus([1, 2, 3, -1, -2, -3, 0, 0])
# Output
# 0.375000
# 0.375000
# 0.250000


# Input - an array of integers
# Output - min and max values that can be calculated by summing exactly four of the five integers
def miniMaxSum(arr):
    min = sum(arr)
    max = 0
    for i, val in enumerate(arr):
        total = 0
        for j, value in enumerate(arr):
            if(j != i):
                total += value
        if(total < min):
            min = total
        if(total > max):
            max = total
    print(min, max)


miniMaxSum([1, 2, 3, 4, 5])
# Output - 10 14

miniMaxSum([7, 69, 2, 221, 8974])
# Output - 299 9271


# Input - Time in 12 hour AM/PM format
# Output - Time in 24 hour format
def timeConversion(s):
    morning = re.findall('AM$', s)
    evening = re.findall('PM$', s)
    hour = s[:2]
    minute = s[3:5]
    second = s[6:8]
    if morning:
        if hour == "12":
            return f"00:{minute}:{second}"
        return f"{hour}:{minute}:{second}"
    if evening:
        if hour == "12":
            return f"{hour}:{minute}:{second}"
        return f"{int(hour)+12}:{minute}:{second}"


timeConversion("07:05:45PM")
# Output - 19:05:45
