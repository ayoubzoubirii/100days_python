bill = input("welcome to the tip calculator ! \n what was the total bill ? : ")
tip = int(input("how much tip would you like to give ? 10 ,12 , or 15 ? :"))
num_people = int(input("How many peappel to split the bill ? :"))
persentage = (tip/100)*float(bill)
pay = round(((float(bill) + persentage)/ num_people),2) 
print(f"Each person should pay {pay} MAD ")