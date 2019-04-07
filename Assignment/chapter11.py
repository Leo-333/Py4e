import re

fname = input("Enter your file name:")
if len(fname)<1:
    fname = 'regex_sum_42.txt'
handle = open(fname)
sum = 0
count = 0
for line in handle:
    numlist = re.findall('[0-9]+', line)
    for num in numlist:
        sum = sum + int(num)
        count += 1
print(count, sum)
    