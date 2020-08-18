#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emaildict = {}

for line in handle :
    if not line.startswith("From") : continue
    l = line.split(' ')

    if len(l) > 2 :
        email = line.split(' ')[1]
        try :
        	emaildict[email] = emaildict[email] + 1
        except :
        	emaildict[email] = 1

    num = 0
    e = ''

    for key in emaildict.keys() :
    	if emaildict[key] > num :
    		e = key
    		num = emaildict[key]

print(e, num)