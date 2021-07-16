from random import randint
import datetime
import random
import numpy as np
import pandas as pd

# This is a python script that contains functions that can be used to create mock Rotational Churn data.

# Number of Instances that a user would be present and reused
def instances():
    x = randint(1,25)
    return x

# IMEI Generation
# This function is just a series of converting a 14 digit id to strings and back 
# in order to calculate the 15th digit which is the check digit (cd) to validate the 
# IMEI that has been generated.
def generate_IMEI():
    
    while len(imei) != 14:
        imei = randint(10000000000000,99999999999999)
        imei = list(str(imei))
        
    a = imei.copy()

    for i in range(len(a)):
        x = 0
        if i%2 != 0:
            x = int(a[i])
            a[i] = x*2
        a[i] = str(a[i])

    a = ''.join(a)

    a = list(a)
    for i in range(len(a)):
        a[i] = int(a[i])

    cd = list(str(sum(a)))
    if int(cd[len(cd)-1]) < 10:
        cd = 10 - int(cd[len(cd)-1])

    imei.append(cd)

    for i in range(len(imei)):
        imei[i] = str(imei[i])

    imei = ''.join(imei)

    return imei

# IMSI Generation
# For the IMSIs, we will be using this 7 digit 5150220 number as a prefix to randomized 
# values. The prefix is a country code + network code identifier for Philippines' Globe Telcom
def generate_IMSI():
    imsi = '5150220' + str(randint(10000000,99999999))
    return (imsi)

# MSISDN Generation
def generate_MSISDN():
    msisdn = str(randint(100000000,999999999))
    return (msisdn)

# Mock Phone Number Function
def generate_PN():
    phone_num = '09' + str(randint(100000000,999999999))
    return (phone_num)

# Yes or No Randomizer
def generate_YN():
    yn = randint(0,1)
    
    if yn == 0:
        yn = 'yes'
    else:
        yn = 'no'

    return yn

# Cell Tower Generation
def generate_cell_tower(yn):
    if yn == 'yes':
        cell_tower = 'T{}'.format(randint(1,10395))
    else:
        cell_tower = 'NS' # NS = No Service/No cell tower was used, because no call or text was utilized
    return cell_tower

# Random Date Generation (from 2019 - 2021)
def generate_date():
    x = np.random.choice(pd.date_range('2019-01-01','2021-01-01'), 1)
    return x[0]

def generate_apps():
    apps = ['youtube'
                ,'facebook'
                ,'messenger'
                ,'chrome'
                ,'twitch'
                ,'viber'
                ,'gcash'
                ,'paypal'
                ,'discord'
                ,'twitter'
                ,'netflix'
                ,'spotify'
                ,'lazada'
                ,'shopee'
                ,'YT Music'
                ,'reddit'
                ,'paymaya'
                ,'grab']
    x = randint(4,len(apps)-1)
    
    random.shuffle(apps)
    apps = apps[:x]
    apps = ', '.join(apps)
    
    return apps

# Number of Hrs Spent on... Something Generation
def generate_num_of_hrs():
    num_of_hrs = round(random.uniform(0.18, 22.8), 1)
    return num_of_hrs

# Average Monthly Load Generation (? this might be changed)
def generate_avg_load():
    return randint(11,473)
    
# Mobile Data Usage Generation
def generate_md_usage():
    x = round(random.uniform(0.1, 5.0), 2)
    return x

# Active Time Generation
def generate_active_time():
    x = randint(0,1)
    if x == 0:
        return 'day'
    else:
        return 'night'
    
    




















