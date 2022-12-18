#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:57:54 2022

@author: adrianamachado
"""

def get_day(day, is_leap): 
    
    '''
    From Codewars
    Determine the date given the number of days into the year and if the year is a leap year or not.
    '''
    
    leap_year_days_month_dict = {'January': (31, 31), 'February': (29, 60), 'March': (31, 91), 
                                 'April': (30, 121), 'May': (31, 152), 'June': (30, 182), 
                                 'July': (31, 213), 'August': (31, 244), 'September': (30, 274),
                                 'October': (31, 305), 'November': (30, 335), 'December': (31, 366)}
    
    year_days_month_dict = {'January': (31, 31), 'February': (28, 59), 'March': (31, 90), 
                            'April': (30, 120), 'May': (31, 151), 'June': (30, 181), 
                            'July': (31, 212), 'August': (31, 243), 'September': (30, 273),
                            'October': (31, 304), 'November': (30, 334), 'December': (31, 365)}
    month = ''
    print_day = 0
    
    if is_leap == True:
        
        for i in range(len(leap_year_days_month_dict)):
            keys = list(leap_year_days_month_dict)
            value = leap_year_days_month_dict[keys[i]]
            eom = value[0]
            m_days = value[1]
            if day > m_days:
                pass
            else:
                month = keys[i]
                if m_days-day == 0:
                    print_day = eom
                else:
                    prev_sum = 0
                    for v in range(i):
                        prev_sum += leap_year_days_month_dict[keys[v]][0]
                    print_day = day - prev_sum
                            
                break

    else:
        
        for i in range(len(year_days_month_dict)):
            keys = list(year_days_month_dict)
            value = year_days_month_dict[keys[i]]
            eom = value[0]
            m_days = value[1]
            if day > m_days:
                pass
            else:
                month = keys[i]
                if m_days-day == 0:
                    print_day = eom
                else:
                    prev_sum = 0
                    for v in range(i):
                        prev_sum += year_days_month_dict[keys[v]][0]
                    print_day = day - prev_sum
                            
                break

    
    return f'{month}, {print_day}'
    
get_day(41, False)