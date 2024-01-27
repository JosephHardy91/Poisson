#poisson regression example

#e.g. events per some unit of time
#e.g. number of births per day

#best for count data
#data may be sparse (lots of zeros); gamma ray events, for example

#there is a rate lambda that is assumed to drive generation of the count data observed
#the rate is assumed to be a function of the predictors
#the rate is assumed to be a poisson random variable

#https://timeseriesreasoning.files.wordpress.com/2021/06/d50a9-1npldr72r5lcw5eq9ijzo7w.png
#Px(k) = (lambda*t)^k * exp(-lambda*t) / k!
#Px(k) is the probability of observing k events in time t
#lambda is the rate of events per unit time
#k is the number of events observed
#exp is the exponential function
#k! is the factorial of k
#t is the period of time over which the events are observed

data_folder_path = r"C:\Users\Joe\Documents\Python Scripts\Data\2017 Monthly Bike Count Totals for East River Bridges"

import random
import math,statistics
import numpy as np



#print('RANDOM_N,INTER_ARRIVAL_TIME,EVENT_ARRIVAL_TIME')
ARRAY_SIZE = 2**20
print(ARRAY_SIZE)
mean_arrival_rates = np.zeros(ARRAY_SIZE)
for i in range(ARRAY_SIZE):
    _lambda = 5
    _num_total_arrivals = 150
    _time_tick = 1
    _num_arrivals_in_unit_time = np.zeros(_num_total_arrivals)
    _num_arrivals = 0
    _arrival_time = 0
    for j in range(_num_total_arrivals):
        #Get the next probability value from Uniform(0,1)
        p = random.random()

        #Plug it into the inverse of the CDF of Exponential(_lamnbda)
        _inter_arrival_time = -math.log(1.0 - p)/_lambda

        #Add the inter-arrival time to the running sum
        _arrival_time = _arrival_time + _inter_arrival_time

        #Increment the number of arrival per unit time
        _num_arrivals = _num_arrivals + 1
        if _arrival_time > _time_tick:
            _num_arrivals_in_unit_time[j] = _num_arrivals
            _num_arrivals = 0
            _time_tick = _time_tick + 1

        #print it all out
        #print(str(p)+','+str(_inter_arrival_time)+','+str(_arrival_time))
    mean_arrival_rates[i] = _num_arrivals_in_unit_time.mean()

    # print('\nNumber of arrivals in successive unit length intervals ===>')
    # print(_num_arrivals_in_unit_time)

    # print('Mean arrival rate for sample:' + str(sum(_num_arrivals_in_unit_time)/len(_num_arrivals_in_unit_time)))

print("Mean arrival rates average:", mean_arrival_rates.mean())
print("Mean arrival rates standard deviation:", mean_arrival_rates.std())