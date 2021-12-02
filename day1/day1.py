file = open("day1input.txt", "r")

lines = file.readlines()
result = 0
count = 0
list = []
for line in lines:
    line = int(line)
    list.append(line)
    count += 1
# print(count)
index = 1
while index < len(list):
    if list[index-1] < list[index]:
        result += 1
    index += 1

i2 = 3
result2 = 0
while i2 < len(list):
    rolling1 = list[i2-3] + list[i2-2] + list[i2-1]
    rolling2 = list[i2-2] + list[i2-1] + list[i2]
    if rolling1 < rolling2:
        result2 += 1
    print(f'index {i2}, rolling1 {rolling1}, rolling2 {rolling2}')
    i2 += 1
print(count)
print(f'part 1 answer: {result}, part 2 answer: {result2}')