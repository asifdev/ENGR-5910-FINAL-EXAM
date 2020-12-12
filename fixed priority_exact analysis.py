#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 02:36:15 2020

@author: MD Asif Khan
"""
# implementation of Fixed Priority – Exact Analysis

# import necesssary library
import numpy as np
import math

# array containing tasks
input = np.array([[2, 5], [2,4], [2,10]])

#  Task number for which worst-case response time will be calculated
task_number = 3



# printing initial arrays 
print("List of tasks", input) 
  
# convert into 1D array 
result = input.flatten() 
  

#array containing execution times
C_array = []
#array containing Period
T_array = []
    

for i in range(len(result)):

    #seperate execution times
    if i%2 ==0:
#        
        C_array.append(result[i])
    else:
#        
        #seperate Periods
        T_array.append(result[i])

initial_max_job = 0

for ele in range(0, task_number):

    initial_max_job = initial_max_job + C_array[ele]
    # printing total value
print("initial_max_job: ", initial_max_job)


#Function to calculate worst case response time
def calcualte_wcrt(max_num):
      
  updated_job = 0
  out = 0
  for ele in range(0, task_number - 1):
      max_job = math.ceil((max_num / float(T_array[ele])))
      updated_job +=max_job * C_array[ele]
  new_initial_max_job = C_array[task_number - 1] + updated_job
  out = new_initial_max_job

  #comparing with previous step of wcrt
  if out != float(max_num):
      print('Not equal', max_num)
      calcualte_wcrt(out)
  else:
      print('Equal Found!', max_num)

#call the recusrive function 
calcualte_wcrt(initial_max_job)

    
    



