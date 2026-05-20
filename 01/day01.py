with open('albert_input.txt', 'r') as file:
    lines = file.readlines()

total = 0
string = ''

for num, line in enumerate(lines):
    print(num, line)

    l = 0
    r = len(line) - 1

    while not line[l].isnumeric():
        l += 1

    while not line[r].isnumeric():
        r -= 1

        
    total += int(line[l] + line[r])


print(total)






total = 0

digits = {'one': 1, 
          'two': 2,
          'three': 3,
          'four': 4,
          'five': 5,
          'six': 6,
          'seven': 7,
          'eight':8,
          'nine':9,
          '1':1,
          '2':2,
          '3':3,
          '4':4,
          '5':5,
          '6':6,
          '7':7,
          '8':8,
          '9':9
          }

for line in lines:
    l = 0
    r = len(line) - 1

    left_digit = 0
    right_digit = 0

    while left_digit == 0:
        for i in range(1,6):
            substring = line[l:l+i]
            
            if substring in digits.keys():
                left_digit = digits[substring]
                break
        l += 1

    
    while right_digit == 0:
        for i in range(1,6):
            substring = line[r:r+i]
            
            if substring in digits.keys():
                right_digit = digits[substring]
                break
        r -= 1

    total += left_digit*10 + right_digit

print(total)