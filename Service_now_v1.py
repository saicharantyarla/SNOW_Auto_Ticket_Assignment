#!/usr/bin/env python
from sys import path
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import os
from datetime import date
from datetime import datetime


try:

    def Shift_working(Excel_Filename,day,date,shift_time,flag1,sheetName):
    
        c_name=[]
        c_no=[]
        c_email_id=[]
        c_team_name=[]
        one_shift=[]
        second_shift=[]
        third_shift=[]
  
        #print (Excel_Filename)
        if flag1 == "FALSE":
            ############################################################################
            ##########send a mail to create a monthly roaster ########################
            print("Update the Excel sheet in specified format")
        else:    
            
            Excel = pd.ExcelFile(Excel_Filename)
            Sheet_names= Excel.sheet_names
            count=len(Sheet_names)
            #print (Sheet_names)
            for sheet_name1 in Sheet_names:
                print(sheet_name1)
                if sheet_name1 == sheetName:
                    a= pd.read_excel(Excel, sheet_name="%s"%(sheet_name1))
                    
                    
                    list_col=list(a.columns.values.tolist())
                    print(list_col)
                    
                    b=a[a["Date"] == date]                 
                    day=int(day)
                    day=day-1
                    print("Hii")
                    
                    
                    for i in list_col:
                        print("hello")
                        print(i)
                        print(type(b[i][day]))
                        if (b[i][day] == 1):
                            print("ee")
                            
                            
                            one_shift.append(i)
                            print("The values return are {0}".format(one_shift))
                        if (b[i][day] ==2):
                            second_shift.append(i)
                            
                        if (b[i][day] ==3):
                            third_shift.append(i)
                
                    
                if sheet_name1 in "Contact_info":
                    Contactinfo= pd.read_excel(Excel, sheet_name="%s"%(sheet_name1))
                    Col_list=list(Contactinfo.columns.values.tolist())
                    index_Len=len(Contactinfo.index)
                    index_Len=list(range(0,index_Len))
                    for i in Col_list:
                        for j in index_Len:
                            if i == "Contact":
                                c_name.append(Contactinfo[i][j])
                            if i == "Cell":
                                c_no.append(Contactinfo[i][j])
                            if i == "Email-Address":
                               c_email_id.append(Contactinfo[i][j])
                            if i == "Team Name":
                                
                                c_team_name.append(Contactinfo[i][j])
                       
                      
                    
            if shift_time == "first":
                
                print("the shift is %s "%(one_shift))
                print(c_name)
                print(c_no)
                print(c_email_id)
                print(c_team_name)
                return one_shift,c_name,c_no,c_email_id,c_team_name
                
            if shift_time == "second":
                return second_shift,c_name,c_no,c_email_id,c_team_name
                #print(second_shift)
                #print(c_name)
                #print(c_team_name)
            if shift_time == "third":
                return third_shift,c_name,c_no,c_email_id,c_team_name    
                
            
                 
except Exception as e:
    
    print(str(e))

