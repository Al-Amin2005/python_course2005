prodect_name1 = "mouse"
prodect_name2 = "keyboard"


quan1 = 2
quan2 = 3

price1 = 500
price2 = 800

total_price1 = price1*quan1
total_price2 = price2*quan2

discount = 5
total = total_price1 + total_price2

total_after_discount = total - (total*discount)/100

print(total)
print(total_after_discount)

print(total_price1,total_price2)