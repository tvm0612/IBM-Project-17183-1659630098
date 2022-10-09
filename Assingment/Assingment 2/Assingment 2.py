import random
while(True):
    temp=random.randrange(0,100)
    humid=random.randrange(0,100)
    print("Temperature: ",temp," Humidity: ",humid)
    if (temp>90 or temp<80) and humid>60:
        print("------Dangerious!!!------")
        break
