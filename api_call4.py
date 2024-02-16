#Need to install requests package for python
#easy_install requests
import requests

def Assign_Ticket(Ticket_sysID,Final_name,Ticket_no):

    try:
        # Set the request parameters
        url = 'https://lntinfotechdemo7.service-now.com/api/now/table/incident/{0}?sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=number%2Cstate%2Cassignment_group%2Csys_id%2Cassigned_to'.format(Ticket_sysID)

        # Eg. User name="admin", Password="admin" for this code sample.
        user = 'sai.charan'
        pwd = '******************'

        # Set proper headers
        headers = {"Content-Type":"application/json","Accept":"application/json"}

        data={"assigned_to":Final_name,"state":'In Progress'}
        data=str(data)

        # Do the HTTP request
        response = requests.patch(url, auth=(user, pwd), headers=headers , data=data )

        # Check for HTTP codes other than 200
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            exit()

        # Decode the JSON response into a dictionary and use the data
        data = response.json()
       # print("###################return #############")
        #print(Final_name)
        #print(data)
        
        if data['result']['assigned_to']== Final_name and data['result']['state'] == 'In Progress' and data['result']['number'] == Ticket_no:
            
            Status="Successful"
            #print("success")
            
        else:
            Status="Failure"
            #print("Failure")
        return Status    
    except Exception as e:
        Status="Failure"
        return Status
        
        
        