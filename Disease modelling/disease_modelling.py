#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 21:16:02 2021

@author: 01lore01
"""


import random
import pandas as pd
import numpy as np


N = 1000 # size of population
R0 = 1.0 # infection number
AVG_TIME_OF_INFECTION = 7 # average number of days of infection
IMMUNITY = 360 # average number of days of immunity
MAX_DAY = 250 # days simulated
START_SICK = 0.01 # percentage of population that is initially sick




class Person():
    """ Creates an instance of a person in the population. """
    def __init__(self, n, age, sick = 0):
        self.n = n
        self.age = age
        self.infected_now = sick
        self.has_been_infected = sick
        self.was_infected = 0
        self.time = 0
        self.immune = 0
        
        
    def time_of_infection(self):
        """ Determines individual time 
            of infection. """
        return int(random.normalvariate(AVG_TIME_OF_INFECTION, AVG_TIME_OF_INFECTION*0.2))
        

    def infected_now(self):
        """ Indicates whether a person is
            infected right now. """
        print("check")
        if self.has_been_infected and (not self.immune):# check 
            print("OK1")
            if self.time > (self.was_infected + self.time_of_infection()):
                self.immune = 1
                print("OK2")
                return 0
            else:
                return 1
        return 0
            
    
    def has_been_infected(self):
        """ Indicates whether or not 
            a person has been infected. """
        self.was_infected = self.time
        print(self.was_infected)
        return 1
    
    
    def check_alive(self):
        """ Checks if person is alive.
            If not alive, removes person 
            from list_of_patients. """
        if self.infected_now:    
            if 75 > self.age > 65:
                if random.random() > 0.98**(1/AVG_TIME_OF_INFECTION):
                    list_of_patients.pop(self.n)
                    return False
            elif 85 > self.age >= 75:
                if random.random() > 0.94**(1/AVG_TIME_OF_INFECTION):
                    list_of_patients.pop(self.n)
                    return False
            elif self.age >= 85:
                if random.random() > 0.91**(1/AVG_TIME_OF_INFECTION):
                    list_of_patients.pop(self.n)
                    return False
            else:
                if random.random() > 0.999**(1/AVG_TIME_OF_INFECTION):
                    list_of_patients.pop(self.n)
                    return False
            return True
        return True

    
    



def set_time(list_of_patients, day):
    """ Updates patient.time to current
        day for all patients. """
    for patient in list_of_patients:
        patient.time = day
    return list_of_patients


def total_sick(list_of_patients):
    """ Calculates the total number of 
        infected people right now. """
    number_of_sick = 0
    for patient in list_of_patients:
        if patient.infected_now:
            number_of_sick += 1
    return number_of_sick


def update_indices(list_of_patients):
    """ Updates indices when patients
        have been removed from 
        list_of_patients (diseased). """
    for index, patient in enumerate(list_of_patients):
        patient.n = index
    return list_of_patients


def check_day(day):
    """ Executes changes for a given
        day and returns total number 
        of infected people"""
    number_of_sick = total_sick(list_of_patients)
    sick = 0
    index = 0
    while (sick <= int(R0*number_of_sick/AVG_TIME_OF_INFECTION)) and (index < len(list_of_patients)):
        if (not list_of_patients[index].infected_now) and (not list_of_patients[index].immune):
                list_of_patients[index].infected_now
                list_of_patients[index].has_been_infected
                #print(list_of_patients[index].infected_now)
                sick += 1
        index += 1
    for patient in list_of_patients:
        update_indices(list_of_patients)
        patient.check_alive()
    return total_sick(list_of_patients)


def total_alive():
    """ Checks how many patients are 
        alive right now. """
    alive = 0
    for index, patient in enumerate(list_of_patients):
        if patient.check_alive():
            alive += 1
        else:
            list_of_patients.pop(index)
    return alive
        

def total_immune():
    """ Checks how many patients are
        immune right now. """
    immune = 0
    for patient in list_of_patients:
        if (patient.was_infected + patient.time_of_infection()) < day:
            patient.immune = 1
            immune += 1
    return immune


list_of_patients = []
for n in range(N):
    sick = 0
    if random.random() > (1-START_SICK):
        sick = 1
    patient = Person(n, random.randint(0, 90), sick)
    list_of_patients.append(patient)    
    

    
day = 0
while day < MAX_DAY:
    list_of_patients = set_time(list_of_patients, day)
    print(day, check_day(day), total_alive(), total_immune())
    day += 1
    
    
# Assert that total_alive() == len(list_of_patients) for all i in range(1000)


def main():
    day = 0
    while day < MAX_DAY:
        # update all variables
        
        
        
        # print 
        
        
        
        
        
        
        day += 1


if __name__ == '__main__':
    pass
        

        




        