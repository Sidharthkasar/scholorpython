age1 = int(input("Enter Your Age : "))
price = int(input("Enter Price : "))

price_in_rupees = (price*84.89)

if age1 >=0 and age1 < 17:
    print (" Your Age is too Small" )
elif age1 >= 18 and age1 < 30:
    print (price_in_rupees, " is your ticket price" )
elif age1 > 30 and age1 < 50:
    print (price_in_rupees, " is your ticket price")
else:
    print ("You Got A free Entry")
