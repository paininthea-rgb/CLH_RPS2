# look at a temperature and figure out what state water is in - solid, liquid or gas

# set the temperature first - and turn our text input into a number => that's what int() does
temp = input("enter a temperature: ")

if temp < 4:
	print("water is frozen - a solid")
elif temp > 4 and temp < 100:
	print("water is liquid")
elif temp >= 100:
	print("water is a gas")

