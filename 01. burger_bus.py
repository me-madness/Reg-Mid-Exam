#First task from MidExam

city_numbers = int(input())
profit = 0
totalProfit = 0

for i in range(1, city_numbers + 1):
    profit = 0
    city_name = str(input())
    owner_income = float(input())
    owner_expenses = float(input())
    profit = owner_income - owner_expenses
    if i % 3 == 0:
       profit -= owner_expenses / 2
    elif i % 5 == 0:
       profit = (owner_income * 0.9) - owner_expenses
       if i % 3 == 0:
           profit += owner_expenses / 2 
    print(F"In {city_name} Burger Bus earned {profit:.2f} leva.")
    totalProfit += profit
    
print(f"Burger Bus total profit: {totalProfit:.2f} leva.")    
    
    
# 3 
# Sofia
# 895.67
# 213.50
# Plovdiv
# 2563.20
# 890.26
# Burgas
# 2360.55
# 600.00
# 5
# Lille
# 2226.00
# 1200.60
# Rennes
# 6320.60
# 5460.20
# Reims
# 600.20
# 452.32
# Bordeaux
# 6925.30
# 2650.40
# Montpellier
# 680.50
# 290.20