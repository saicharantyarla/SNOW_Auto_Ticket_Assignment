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
    pwd = 'Charan123$'

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
except Exception as e:
    print(str(e))
