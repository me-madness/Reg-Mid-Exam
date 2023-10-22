# Third task from MidExam

price_rating = input().split(", ")
entry_point = input()
type_of_items = input()
left_site = []
right_site = []
for price in price_rating:
    if price <= entry_point:
        left_site.append(price)
        print(left_site)
    else:
        right_site.append(price)    

print(left_site)
print(right_site)        
# sum_of_price_ratings = 0
# left_site_cheap_sum = 0
# left_site_expensive_sum = 0
# right_site_cheap_sum = 0 
# right_site_expensive_sum = 0 

# for price in price_rating:
#     if type_of_items == "cheap":
#         if price < entry_point:
#             left_site_cheap_sum += int(price)    
#         else:
#             right_site_cheap_sum += int(price)
#     elif type_of_items == "expensive":
#         if price >= entry_point:
#             left_site_expensive_sum += int(price)
#         else:
#             right_site_expensive_sum += int(price)
            
            
                        
# if left_site_cheap_sum >= right_site_cheap_sum:
#     print(f"Left - {left_site_cheap_sum}")   
# else:    
#     print(f"Right - {right_site_cheap_sum}")

# 1, 5, 1
# 1
# cheap