#!/usr/bin/env python
from sys import path
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import os
from datetime import date
from datetime import datetime,timedelta
import Service_now_v1
import api_call2
import api_call3
import api_call4
import mail

def Excel_Filtration(flag,team_name,Ticket_sysID,Ticket_priority,Ticket_no,Ticket_Status,Ticket_description):

    try:

        def file_date(flag):
            from datetime import date,datetime,timedelta
            
            # Fteching the data automatically from the Excel sheet with the current date time format
            flag=flag.upper()
            if flag == "TRUE":
                today = date.today()
                date=today.strftime("%Y-%m-%d")
                day=today.strftime("%d")
                Filename_Format="D:\CITI_GROUP\SNOW_AUTO TICKET_ASSIGN\ICG_ROSTER_TIBCO_"
                year=today.strftime("%Y")
                month =today.strftime("%b")
                str1=month+"_"+year+".xlsx"
                Excel_Filename=Filename_Format+str1
                sheetName="Tibco_{0}{1}".format(month,year)
                if os.path.exists(Excel_Filename):
                    flag1="TRUE"
                else:
                    flag1="FALSE"
                return Excel_Filename,day,date,flag1,sheetName
            else:
            # Same as above but for the third shift 
                date=(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
                Filename_Format="D:\CITI_GROUP\SNOW_AUTO TICKET_ASSIGN\ICG_ROSTER_TIBCO_"
                day=(datetime.now() - timedelta(1)).strftime('%d')
                year=(datetime.now() - timedelta(1)).strftime('%Y')
                month=(datetime.now() - timedelta(1)).strftime('%b')
                str1=month+"_"+year+".xlsx"
                Excel_Filename=Filename_Format+str1
                sheetName="Tibco_{0}{1}".format(month,year)
            
                if os.path.exists(Excel_Filename):
                    flag1="TRUE"
                else:
                    flag1="FALSE"
                return Excel_Filename,day,date,flag1,sheetName 
                
                
        # This Module is used based on the description and team division. This will return the names and email_id and team name
        def Final_values(shift,c_name,c_no,c_email_id,c_team_name,flag,team_name):
            names=[]
            email_id=[]
            t_name=[]
            
            #print("came")
            #print(shift)
            #print(c_name)
            for i in shift:
                for j in c_name:
                    if i == j:
                        names.append(j)
                        id=c_name.index(j)
                        k=c_email_id[id]
                        l=c_team_name[id]
                        email_id.append(k)
                        t_name.append(l)
                        #print(email_id)
                        #print(t_name)
                        
            # This flag is returned on basis of the description came from the API that matches the servername in excel sheet
            if flag=="TRUE":
                t_names1=[]
                names1=[]
                email_id1=[]
                #print("Entered")
                for j in team_name:
                    id = 0 
                    for i in t_name:
                        #print(i)
                        if i==j:
                            t_names1.append(i)
                           # print(t_names1)
                            id=t_name.index(i)
                            #print(id)
                            k=email_id[id]
                            l=names[id]
                            email_id1.append(k)
                            names1.append(l)
                        id =id+1    
                return names1,email_id1,t_names1
            else:    
                return names,email_id,t_name
               
                
                                
        now = datetime.now()
        time=now.strftime("%H")    
        time=int(time)
        
        if time >= 6 and time < 14:
            print("1st shift")
            shift_time="first"
            Excel_Filename,day,date,flag1,sheetName=file_date('TRUE')
            shift,c_name,c_no,c_email_id,c_team_name=Service_now_v1.Shift_working(Excel_Filename,day,date,shift_time,flag1,sheetName)
            print("the shift is {0}".format(shift))
            names,email_id,t_name=Final_values(shift,c_name,c_no,c_email_id,c_team_name,flag,team_name)
        elif time >= 14 and time < 22:
            print("2nd shift")
            shift_time="second"
            Excel_Filename,day,date,flag1,sheetName=file_date('TRUE')
            shift,c_name,c_no,c_email_id,c_team_name=Service_now_v1.Shift_working(Excel_Filename,day,date,shift_time,flag1,sheetName)
            names,email_id,t_name=Final_values(shift,c_name,c_no,c_email_id,c_team_name,flag,team_name)
        elif (time >= 22 and time < 24):
            shift_time="third"
            print("3rd shift")
            Excel_Filename,day,date,flag1,sheetName=file_date('FALSE')
            shift,c_name,c_no,c_email_id,c_team_name=Service_now_v1.Shift_working(Excel_Filename,day,date,shift_time,flag1,sheetName)
            names,email_id,t_name=Final_values(shift,c_name,c_no,c_email_id,c_team_name,flag,team_name)
        elif (time >= 1 and time < 6):
            shift_time="third"
            print("3rd shift")    
            Excel_Filename,day,date,flag1,sheetName=file_date('FALSE')
            shift,c_name,c_no,c_email_id,c_team_name=Service_now_v1.Shift_working(Excel_Filename,day,date,shift_time,flag1,sheetName)
            names,email_id,t_name=Final_values(shift,c_name,c_no,c_email_id,c_team_name,flag,team_name)
        else:
            shift_time="third"
            print("3rd shift") 
            Excel_Filename,day,date,flag1,sheetName=file_date('FALSE')
            shift,c_name,c_no,c_email_id,c_team_name=Service_now_v1.Shift_working(Excel_Filename,day,date,shift_time,flag1,sheetName)
            names,email_id,t_name=Final_values(shift,c_name,c_no,c_email_id,c_team_name,flag,team_name)
            

        print("##################### Next details ###################")
        #The below Module will return the Final Name and Email ID of that person to whom we can assign the ticket
        Final_name,Final_email,Final_team=api_call3.assign_Ticket(names,email_id,t_name)
        #print("Final Name")
        print(Final_name)
        print(Final_email)
        print(Final_team)
        Final_email=Final_email[0]
        Final_name=Final_name[0]
        #print("############ updated one ###############")
        #print(Final_name)
        #print(Final_email)
        #print(Ticket_no)
        #print(Ticket_Status)
        #print(Ticket_priority)
        #print(Ticket_description)
        
        #Checking the user availability in the Service now  
        Final_name=api_call2.User_check_Servicenow(Final_email)
        
        if Final_name == "No Value":
            print("The User Doesnot Exists {0}".format(Final_email))
            exit()
            return "Failed "," Failed","Failed"
            
        else:    
            
            # To assign the Ticket to the particluar person
            Status=api_call4.Assign_Ticket(Ticket_sysID,Final_name,Ticket_no)
            
            if Status=="Successful":
                if Ticket_priority == "1 - Critical" or Ticket_priority == "2 - High":
                    #Final_email.append("Dl.com")
                    desc="High Priority Critical Incident Ticket has assigned to you with below details:"
                    #Final_name=Final_name[0]
                    ExitCode=mail.Sending_Mail(Final_email,Ticket_no,Ticket_Status,Ticket_priority,Final_name,Ticket_description,Status,desc)
                    
                else:
                    desc="Low Priority Incident Ticket has assigned to you with below details:"
                    ExitCode=mail.Sending_Mail(Final_email,Ticket_no,Ticket_Status,Ticket_priority,Final_name,Ticket_description,Status,desc)
                
            else:
                Status=="Failure"
                if Ticket_priority == "1 - Critical" or Ticket_priority == "2 - High":
                    #Final_email.append("Dl.com")
                    desc="High Priority Critical Ticket and Unable to assign it to you. Please login to the ITSM tool and accept it"
                    ExitCode=mail.Sending_Mail(Final_email,Ticket_no,Ticket_Status,Ticket_priority,Final_name,Ticket_description,Status,desc)
                else:
                    desc="Low Priority Ticket and Unable to assigned it to you with below details"
                    ExitCode=mail.Sending_Mail(Final_email,Ticket_no,Ticket_Status,Ticket_priority,Final_name,Ticket_description,Status,desc)            
            
        return Final_name,Final_email,Final_team
    except Exception as e:
        
        print(str(e))