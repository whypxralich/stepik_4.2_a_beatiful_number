#stepik_4.2_a_beatiful_number 

a = int(input())
if 1000<=a<=9999 and (a%7==0 or a%17==0):
    print ("YES")
else:
    print("NO")