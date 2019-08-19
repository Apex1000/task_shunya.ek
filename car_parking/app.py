#! /usr/bin/python3

### may work only on linux
import os
import sys
import time


car_parking=[[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
availablety = 12
bike_parking=['available','available','available']
localtime = time.asctime( time.localtime(time.time()) )

while True:
    button_press=input("""
    Library parking Total slots for car is 12 
    Press button A for car parking  
    Press button E for exit --------->> """,)
    if button_press == 'A':
        if availablety > 0 :
            for i in range(len(car_parking)):
                for j in range(len(car_parking[i])):
                    if car_parking[i][j] == 0:
                        print("			","Your slot number is", str(i+1)+str(j+1)+'A'  ) 
                        car_parking[i][j]=str(i+1)+str(j+1)+'A'
                        availablety = availablety - 1
                        # print (car_parking)
                        time.sleep(5)
                        os.system('clear')
                        break
                break
        else:
            print ('Sorry! No space available. Park outside.')
            time.sleep(5)
            os.system('clear')
    
    else:
        flag = 0
        os.system('clear')
        check=input(" \n   Enter slot number :")
        for i in range (len(car_parking)):
            for j in range(len(car_parking[i])):
                if check == car_parking[i][j]:
                    flag = 1
                    break
            break
        if flag == 1:
            car_parking[i][j] = 0
            availablety = availablety + 1
            print("			","Bye Bye")
            time.sleep(5)
            os.system('clear')
        else:
            print("			","Sorry this spot is not Available.")


