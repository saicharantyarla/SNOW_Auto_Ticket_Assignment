#Need to install requests package for python
#easy_install requests
import requests
def assign_Ticket(names,email_id,team_name):

    try:
        import requests

        # Set the request parameters
        url = 'https://lntinfotechdemo7.service-now.com/api/now/table/incident?sysparm_query=assignment_group%3Ddb194c10db484410ad13f52ebf961952&sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=number%2Cstate%2Csys_class_name%2Cpriority%2Cassigned_to'

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
        #print("The Json data is {0}".format(data))
        #print("The names returned are .. {0}".format(names))

        final_list=[]
        for i in names:
            count=0
            for index in range(len(data['result'])):
                if data['result'][index]['assigned_to']==i and data['result'][index]['state'] == 'In Progress':
                    if data['result'][index]['priority']== '1 - Critical' or data['result'][index]['priority']== '2 - High':
                        count=count+1000
                    else:
                        count=count+1
            final_list.append(count)
        print("#############################")    
        print("The final list is {0}".format(final_list))
            
        n=min(final_list)
        Final_name=[]
        Final_email=[]
        Final_team=[]
        Final_name.append(names[final_list.index(min(final_list))])
        
        
        id=names.index(Final_name[0])
        k=email_id[id]
        Final_email.append(k)
        Final_team.append(team_name[id])
        
        
        return Final_name,Final_email,Final_team
    except Exception as e:
        print(str(e))
      
           