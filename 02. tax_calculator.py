# Second task from MidExam

vehicles = input().split(">>")
total_tax_collected = 0

for vehicle in vehicles: 
   total_tax_to_pay = 0
   new_vehicle = vehicle.split()
   car_type = new_vehicle[0]
   years = int(new_vehicle[1])
   miles = int(new_vehicle[2])
   if car_type == "family":
      total_tax_to_pay = (50 - 5 * years) + ((miles // 3000) * 12)
      total_tax_collected +=total_tax_to_pay
      print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")    
   elif car_type == "heavyDuty":
      total_tax_to_pay = (80 - 8 * years) + ((miles // 9000) * 14)
      total_tax_collected +=total_tax_to_pay
      print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")      
   elif car_type == "sports":
      total_tax_to_pay = (100 - 9 * years) + ((miles // 2000) * 18)
      total_tax_collected +=total_tax_to_pay
      print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.") 
   else:
      print("Invalid car type.")
      
    
print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")    
# family 3 7210>>van 4 2345>>heavyDuty 9 31000>>sports 4 7410
# family 5 3210>>pickUp 1 1345>>heavyDuty 7 21000>>sports 5 9410>>family 3 9012    