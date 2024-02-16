#Need to install requests package for python
#easy_install requests
import requests
def User_check_Servicenow(Final_email):
    try:
        #Final_email='saicharan.tyarla@lntinfotech.com'
        # Set the request parameters
        url = 'https://lntinfotechdemo7.service-now.com/api/now/table/sys_user?sysparm_query=active%3Dtrue%5Eemail%3D{0}&sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=user_name%2Cname%2Cemail'.format(Final_email)

        # Eg. User name="admin", Password="admin" for this code sample.
        user = 'sai.charan'
        pwd = '************'

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
        print("came here")
        print("THE DATA IS %s"%(data))
        if data['result'] and data['result'][0]['email'] == Final_email:
            assign_Name=data['result'][0]['name']
            #print(assign_Name)
            return assign_Name
        else:
            print("No value")
            return "No Value"
    except Exception as e:
        print(str(e))
        


