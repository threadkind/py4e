#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

timecount = {}

for line in handle :
    if not line.startswith("From") : continue
    l = line.split(' ')

    if len(l) > 2 :
        email = line.split(' ')[1]
        time = line.split(' ')[6]
        hr = time.split(':')[0]

        try :
        	timecount[hr] = timecount[hr] + 1
        except :
        	timecount[hr] = 1

for key in sorted(timecount.keys()) :
	print(key, timecount[key])



