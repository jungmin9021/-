
input_data = input().split(' ')

hour = int(input_data[0])
minute = int(input_data[1])

minute -= 45
if minute < 0:
    minute += 60
    hour -= 1
    #만약 10 10 면
    # 10 -35
    # 9 25
    if hour < 0:
        hour = 23
        
print(str(hour) + ' ' + str(minute))
