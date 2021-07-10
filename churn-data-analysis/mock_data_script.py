import numpy as np
from random import seed
from random import randint

# This is a python script that contains functions that can be used to create mock Rotational Churn data.

# Number of Instances that a user would be present and reused
def instances():
    x = randint(1,15)
    return x

# IMEI Generation
# This function is just a series of converting a 14 digit id to strings and back 
# in order to calculate the 15th digit which is the check digit (cd) to validate the 
# IMEI that has been generated.
def generate_IMEI():
    imei = randint(00000000000000,99999999999999)
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
    imsi = '5150220' + str(randint(00000000,99999999))
    return imsi

# MSISDN Generation
def generate_MSISDN():
    msisdn = '63' + str(randint(1,999))

    if len(msisdn) == 3:
        msisdn+=str(randint(000000000000,999999999999))
    elif len(msisdn) == 4:
        msisdn+=str(randint(00000000000,99999999999))
    elif len(msisdn) == 5:
        msisdn+=str(randint(0000000000,9999999999))

    return msisdn

# Mock Phone Number Function
def generate_PN():
    phone_num = '09' + str(randint(000000000,999999999))
    return phone_num

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











