#  look at the temperature and figure out what state water is in - solid, liquid or gas

#set the temperature first
temp = int(input("enter the temperature:"))

if temp < 4:
	print("water is frozen - a solid")

elif temp > 4 and temp < 100:
	print("Water is in liquid form")

elif temp >= 100:
	print("Water is a gas")

else:
	print("you didn't enter the number")
