from random import randint
import datetime
import random
import numpy as np
import pandas as pd

# This is a python script that contains functions that can be used to create mock Rotational Churn data.

class _id_generation():
    # Number of Instances that a user would be present and reused
    def instances():
        x = randint(1,25)
        return x

    # IMEI Generation
    # This function is just a series of converting a 14 digit id to strings and back 
    # in order to calculate the 15th digit which is the check digit (cd) to validate the 
    # IMEI that has been generated.
    def generate_IMEI():
        imei = []
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


class _mock_behavior():
    # Yes or No Randomizer
    def generate_YN():
        yn = randint(0,1)
        
        if yn == 0:
            yn = 'yes'
        else:
            yn = 'no'

        return yn
    
    # Random Date Generation
    def generate_date(s):
        #x = np.random.choice(pd.date_range('2019-01-01','2021-01-01'), 1)
        
        if s == 0: # churner date generation
            x = pd.date_range(start='2017-08-15', end='2019-04-05').to_pydatetime().tolist()
        elif s == 1: # rotational churner date generation
            x = pd.date_range(start='2019-04-19', end='2020-12-07').to_pydatetime().tolist()
            
        return x
    
    def generate_weeks(s):
        generated_dates = _mock_behavior.generate_date(s)
        dates = []
        x = 7
        while len(dates) == 0:
            for i in range(len(generated_dates)):
                if x == 0:
                    dates.append(generated_dates[i])
                    x = 6
                else:
                    x-=1
        
        if s == 0:
            start, end = _mock_behavior.generate_week_start_end()
        return dates[start:end]

    def generate_rc_weeks(w,l):
        c_end = datetime.datetime.strptime(w, '%Y-%m-%d')
        start = c_end + datetime.timedelta(weeks=4)
        end = start + datetime.timedelta(weeks=l)
        generated_dates = pd.date_range(start, end).to_pydatetime().tolist()
        
        dates = []
        
        x = 7
        while len(dates) == 0:
            for i in range(len(generated_dates)):
                if x == 0:
                    dates.append(generated_dates[i])
                    x = 6
                else:
                    x-=1
        
        return dates
    
    def generate_week_start_end():
        start = randint(0,54)
        end = randint(64,84)
        return start, end

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

    def generate_credit_load():
        credit = [20,30,50,70,90,100,150,200,300,500,800,1000]
        return random.choice([0,random.choice(credit)])
        
    # Mobile Data Usage Generation
    def generate_md_usage():
        x = round(random.uniform(5.0, 9.0), 2)
        return x

    def generate_promos():
        return randint(0,randint(1,6))

    # Active Time Generation
    def generate_active_time():
        activity_time = [0,1,2]
        return random.choice(activity_time)


class mock_data_generation():
    def mock_churner_data():
        weeks = _mock_behavior.generate_weeks(0)

        ids = _id_generation.generate_IMEI()
        IMEIs = []
        credits_loaded = []
        num_hrs = []
        mdu = []
        promos = []
        times = []
        active = []

        for _ in range(len(weeks)):
            IMEIs.append(ids)

            credit = _mock_behavior.generate_credit_load()
            hrs = _mock_behavior.generate_num_of_hrs()
            md_usage = _mock_behavior.generate_md_usage()
            promo = _mock_behavior.generate_promos()
            active_time = _mock_behavior.generate_active_time()
            activity = credit + hrs + md_usage + promo + active_time

            credits_loaded.append(credit)
            num_hrs.append(hrs)
            mdu.append(md_usage)
            promos.append(promo)
            times.append(active_time)

            if activity == 0:
                active.append(1)
            else:
                active.append(0)

        for i in range(len(weeks)):
            if i == len(weeks)-4 or i == len(weeks)-3 or i == len(weeks)-2 or i == len(weeks)-1:
                credits_loaded[i] = 0
                num_hrs[i] = 0
                mdu[i] = 0
                promos[i] = 0
                times[i] = 0
                active[i] = 1

        return weeks, IMEIs, credits_loaded, num_hrs, mdu, promos, times, active

    def mock_rc_data(w,l,df):
        weeks = _mock_behavior.generate_rc_weeks(w,l)
        ids = _id_generation.generate_IMEI()
        IMEIs = []
        credits_loaded = []
        num_hrs = []
        mdu = []
        promos = []
        times = []
        active = []
        
        for _ in range(len(weeks)):
            IMEIs.append(ids)
        
        for i in range(len(df.columns)):
            # change credits loaded
            credits = df[df.columns[i]].values.tolist()
            credit_list = [0,20,30,50,70,90,100,150,200,300,500,800,1000]
            
            for i in range(len(credits)):
                cl_pos = randint(credit_list.index(credits[i])+randint(1,2),credit_list.index(credits[i])-randint(1,2))#randint(0,)
                if cl_pos <= 0:
                    cl_pos = 0
                credits_loaded.append(credit_list[cl_pos])
            
        
        #    col_vals = df[df.columns[i]].value_counts().reset_index().to_numpy().tolist()
        #    val_sh = [x[1] for x in col_vals]
        #    random.shuffle(val_sh)
        #    for j in range(len(col_vals)):
        #        col_vals[j][1] = val_sh[j]

        
        return weeks, IMEIs, credits_loaded, num_hrs, mdu, promos, times, active









# Cell Tower Generation
#def generate_cell_tower(yn):
#    if yn == 'yes':
#        cell_tower = 'T{}'.format(randint(1,10395))
#    else:
#        cell_tower = 'NS' # NS = No Service/No cell tower was used, because no call or text was utilized
#    return cell_tower    




















