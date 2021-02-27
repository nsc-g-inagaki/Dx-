num = input('値？:')
num = float(num)

if num %2 != 0:
	print('規格外')
elif 2 <= num <= 5:
	 print('規格内')
elif 6 <= num <= 20:
	print ('規格外')
elif 20 < num:
	 print ('規格内')
elif 1 <= num <=100:
	 print('対象外')

