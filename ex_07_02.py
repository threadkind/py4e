# Use the file name mbox-short.txt as the file name

#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475

fname = input("Enter file name: ")
#fname = 'mbox-short.txt'
fh = open(fname)

nums = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x = line.find(":")
    num = float(line[x+1:len(line)])

    nums.append(num)

#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

if len(nums) > 0 :
    total = 0
    lineNum = len(nums)

    for n in nums :
        total = total + n

    average = total / lineNum

    print('Average spam confidence:',average)



