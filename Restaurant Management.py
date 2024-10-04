#!/usr/bin/env python
# coding: utf-8

# In[1]:


#RMS Restaurant Management System
user_bill=0
def welcome_user():
    #Welcome user
    print('Welcome to Moonlight Cafe')

def display_menu():
    global menu
    menu={'latte':200,'drip coffee':180,'cappuccino':300}
    #Display Menu
    print('Menu')
    print('*'*20)
    for i in menu:
        print(i.title(),menu[i])
    print('*'*20)

def take_order():
    global user_order
    #Take order
    user_order=input('Please place your order here')

def preparing_order():
    global user_bill
    #Prepare Order
    print('Preparing your',user_order.title())
    import time
    time.sleep(2)
    user_bill=user_bill+menu[user_order]
def serve_order():
    #Serve Order
    print('Your',user_order,'is ready!')
    print('Please enjoy!')

def display_bill():
    global user_bill
    #Display Bill
    #user_bill=(menu[user_order])
    print('Your Total Bill',user_bill)

def verify_bill():
    global user_pay,user_bill
    #Take Payment
    user_pay=int(input('Please pay your bill here:'))
    #Verify Payment
   
    while user_pay<user_bill:
        print('Payment Unsuccessful!')
        user_bill=user_bill-user_pay
        print('Please pay remaining',user_bill)
        user_pay=int(input('Please pay your bill here:'))
       

    if user_pay>user_bill:
        print('Payment Successful!')
        print('Here is your change',user_pay-user_bill)
    else:
        pass

def thank_user():
    #Thank user
    print('Thank you for visiting Moonlight Cafe!')
    print('Please come back soon!')
def order_process():
    display_menu()
    take_order()
    if user_order.lower() in menu:
        preparing_order()
        serve_order()
        user_rep=input('Do you want to order anything else?')
        while user_rep.lower()=='yes':
            repeat_order()
            user_rep=input('Do you want to order anything else?')
        display_bill()
        verify_bill()
        thank_user()
    else:
        print('Invalid Order')
        order_process()
def repeat_order():
    display_menu()
    take_order()
    if user_order.lower() in menu:
        preparing_order()
        serve_order()
    else:
        print('Invalid Order')
        repeat_order()

welcome_user()
order_process()


# In[ ]:




