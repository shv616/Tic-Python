import random 
import time
import sys
import datetime
import os

def callnumber(name,phone):
    
    a = datetime.datetime.now()
    print('Calling to ',phone)
    print('For end call, press Enter')
    input() 
    b = datetime.datetime.now()
    c = 'Call Duration = '+ str(b - a)[:7]
    a = 'Call Time = '+ str(a)[:19]
    f = open("call_log.txt","a")
    f.write(name),f.write(', '),f.write(phone),  f.write('\n')
    f.write(a),   f.write('\n' )
    f.write(c),   f.write('\n\n' )
    f.close()
    print(a)
    print(c)
	
	
def add_phone_book(name,phone) :   
    f = open("phone_book.txt","a")
    f.write(name ), f.write(':' ) , f.write(phone)
    f.write('\n' )
    f.close()
	
	
def phone_book():    
   
    if os.path.exists("phone_book.txt")== False :
        f = open("phone_book.txt","w")
        f.close
    
    f = open("phone_book.txt","r")
    for x in f:
        print(x)
    f.close()
	
	
def call_to(name):
    f = open("phone_book.txt","r")
    d = 0
    for x in f:
        col=x.find(':')
        if x[:col] == name :
            phone = x[col+1:-2]
            callnumber(name,phone)
            d = 1
    f.close        
    if d == 0 :
        print('This name is not exist in phone book')
        y = input('Do you want to add this contact Y/N : ')
        if y == 'y' or y == 'Y' :
            input_data()
  
  
  
  
  
def input_data():
    name = input('Enter Name: ')
    
    if os.path.exists("phone_book.txt")== False :
        f = open("phone_book.txt","w")
        f.close

    f = open("phone_book.txt","r")
    d = 0
    for x in f:
        col=x.find(':')
        if x[:col] == name :
            d = 1
    f.close
    
    if d == 1 :
        print('This name is exist, pls enter new name')
        y = input('Do want enter new name Y/N : ')
        if y == 'y' or y == 'Y':
            input_data()


    if d == 0 :
        phone = input('Enter Phone Number: ')
        add_phone_book(name,phone)
		



def show_log():
    
    if os.path.exists("call_log.txt")== False :
        f = open("call_log.txt","w")
        f.close
        
    f = open("call_log.txt","r")
    for i in f:
        print(i)
    f.close()
	
	
	
def my_phone():
    
    k = input(' Welcome\n 1-Show contact\n 2-Add contact\n 3-Call\n 4-Show log\n 5-Exit\n')
    
    if k == '1':
        phone_book()
       
    if k == '2':
        input_data()
        
    if k == '3':
        name = input('Enter the name : ')
        call_to(name)
        
    if k == '4':
        show_log()
