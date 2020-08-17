hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
overtime = r * 1.5

pay = 0

if h <= 40 :
	pay = h*r

else :
	pay = 40 * r
	h = h - 40
	pay = pay + (h * overtime)

print(pay)