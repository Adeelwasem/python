number = 76
count = 0
if number == 0:  
    count = 1
else:
    temp_num = abs(number) 
    while temp_num > 0:
        temp_num //= 10  
        count += 1
print(count)