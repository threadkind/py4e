#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_902892.txt"
handle = open(name)

count = 0

for line in handle :
	x = re.findall('[0-9]+', line)

	if len(x) > 0 :
		for num in x :
			count = count + int(num)

print(count)