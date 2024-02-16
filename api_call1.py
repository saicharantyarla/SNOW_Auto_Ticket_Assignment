#Need to install requests package for python
#easy_install requests
import requests
import Service_now_v2
import pandas as pd

try:

    # Set the request parameters
    url = 'https://lntinfotechdemo7.service-now.com/api/now/table/incident?sysparm_query=assignment_group%3Ddb194c10db484410ad13f52ebf961952%5Eassigned_toISEMPTY&sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=number%2Cstate%2Csys_created_by%2Cshort_description%2Csys_class_name%2Cpriority%2Cassigned_to%2Csys_id'



    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'sai.charan'
    pwd = '*********'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )

    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    print(data)
    
    if data['result']:

        ########## From Ticket description trying to fetch the team details #######################
        def Ticket_description_known(description,Server_name,team_name):
            flag="False"

            tem_name=[]
            for i in Server_name: 
                if i in description:
                    id = Server_name.index(i)
                    tem_name.append(team_name[id])
                    flag="True"
            team_name=tem_name
            team_name = list(dict.fromkeys(team_name))
            print("Hi")
            print(team_name)
            print(flag)
            return team_name,flag   # This will return flag as True if service name is identified in the description of the ticket


        ################################ Read the Description of the incident ticket and Analyse ##################################
        for index in range(len(data['result'])):
            Server_name=[]
            team_name=[]
            #print("#################### Ticket #############")
            # Get the server vs team mapping file from the Excel sheet 
            Excel = pd.ExcelFile('D:\CITI_GROUP\SNOW_AUTO TICKET_ASSIGN\TIBCO_SERVER_TEAM_MAPPING.xlsx')
            Sheet_names= Excel.sheet_names
            count=len(Sheet_names)
            for sheet_name1 in Sheet_names:
                if sheet_name1 == "Server_team_mapping":
                    a= pd.read_excel(Excel, sheet_name="%s"%(sheet_name1))
                    Col_name_list=a.columns.values.tolist()
                    index_Len=len(a.index)
                    index_Len=list(range(0,index_Len))
                    for i in Col_name_list:
                        for j in index_Len:
                            if i == "Server_name":
                                Server_name.append(a[i][j])
                            if i == "Team_Name":
                                team_name.append(a[i][j])
            # The above code will read the file and store the details in the Server_name , team_name variables                    
            print("The Server and team mapping is :")
            print(Server_name)
            print(team_name)
            # Checking whether the ticket is not assigned to anyone 
            if data['result'][index]['assigned_to']=='' and data['result'][index]['state']=='Active' or data['result'][index]['state']=='New':
                Ticket_sysID=data['result'][index]['sys_id']
                Ticket_priority=data['result'][index]['priority']
                Ticket_no=data['result'][index]['number']
                Ticket_Status=data['result'][index]['state']
                Ticket_description=data['result'][index]['short_description']
                description=data['result'][index]['short_description']
                
                team_name,flag=Ticket_description_known(description,Server_name,team_name)
                if flag == "True":
                    print(team_name)
                    Final_name,Final_email,Final_team=Service_now_v2.Excel_Filtration(flag,team_name,Ticket_sysID,Ticket_priority,Ticket_no,Ticket_Status,Ticket_description)
                else:
                    team_name=[]
                    Final_name,Final_email,Final_team=Service_now_v2.Excel_Filtration(flag,team_name,Ticket_sysID,Ticket_priority,Ticket_no,Ticket_Status,Ticket_description)                
                    
    
except Exception as e:
    print(str(e))
