outBalance = float(input('Enter the outstanding balance on your account: '))
apr = float(input('Enter your anual percentage rate as a decimal: '))
mpr = apr/12.0
newBalance = outBalance
low = newBalance / 12
high = (outBalance * (1 + mpr) ** 12)/12
#payment = 0
while (high - low) > 0.005:
	payment = round((low + high)/2.0, 2)
	for m in range(1, 13):
		newBalance = round(newBalance * (1 + mpr) - payment, 2)
		if newBalance < 0:
			break
	if newBalance < 0:
		high = payment
	else:
		low = payment
	print(newBalance)
	if (high - low) > 0.005:
		newBalance = outBalance
print('RESULT')
print('Monthly payment to pay off debt in 1 year:', payment)
print('Number of months needed:', m)
print('Balance: ', newBalance)
