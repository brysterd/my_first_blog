nums = [1,2,3,1]
counter = {}

for number in nums:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)