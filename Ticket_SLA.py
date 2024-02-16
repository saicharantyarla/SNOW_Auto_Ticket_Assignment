#Need to install requests package for python
#easy_install requests
import requests
from datetime import datetime
import smtplib                                              ############ Import the smtp related module to send mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


# Set the request parameters
url = 'https://lntinfotechdemo7.service-now.com/api/now/table/incident?sysparm_query=active%3Dtrue%5Eassignment_group.nameSTARTSWITHTesting_CITI%5Estate%3D2%5EORstate%3D3%5EORstate%3D1&sysparm_display_value=true&sysparm_exclude_reference_link=false&sysparm_fields=number'

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
ticket=[]
ticket_number=[]
business_per=[]
for index in range(len(data['result'])):
    ticket.append(data['result'][index]['number'])

print(ticket)

url1 = 'https://lntinfotechdemo7.service-now.com/api/now/table/task_sla?sysparm_query=stage%3Din_progress%5EORstage%3Dpaused&sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=task%2Cbusiness_percentage'


# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url1, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data1 = response.json()


for index in range(len(data1['result'])):
    ticket_number.append(data1['result'][index]['task'])
    business_per.append(data1['result'][index]['business_percentage'])

#print(ticket_number)
Final_ticket=[]
Final_per=[]
count=0
for i in ticket:
    count=count+1
    for j in ticket_number:
        if i==j:
            Final_ticket.append(i)
            index=ticket_number.index(i)
            #print(business_per[index])
            Final_per.append(business_per[count])
allLines1=""    
print("we entered here")
print(Final_ticket)
print(Final_per)

for k in Final_per:

    
    if float(k.replace(",","")) > 80:
        #print(k)
        index=Final_per.index(k)
        ticket_number=Final_ticket[index]

        beginning="<tr>"
        bodyE3 ="<td class='Ticket_no'> " + ticket_number + " </td>"
        
        bodyE3+="<td class='Status'> " + k + "</td>"
        end="</tr>"
        allLines1+=beginning+bodyE3+end
        

################################ HTML #############################################
now = datetime.now()
dt = now.strftime("%A,%d-%B-%y")
dt=str(dt)

print("we started")

SUBJECT = ''' ####### Ticket List to BREACH ####### 
    '''
frommail=" asdas"
gmail_user = 'saicharantyarla@gmail.com'
gmail_password = 'Saicharan123$'
Final_email='saicharan.tyarla@lntinfotech.com'
msg = MIMEMultipart('alternative')


body ="""
<html>	
<style>
table {
  border-collapse: separate;
  border-spacing: 0;
  color: #4a4a4d;
  font: 14px/1.4 "Helvetica Neue", Helvetica, Arial, sans-serif;
}
th,
td {
  padding: 10px 15px;
  vertical-align: middle;
  
}
thead {
  background: #395870;
  background: linear-gradient(#49708f, #293f50);
  color: #fff;
  font-size: 11px;
  text-transform: uppercase;
}

td {
  border-bottom: 1px solid #cecfd5;
  border-right: 1px solid #cecfd5;
}
td:first-child {
  border-left: 1px solid #cecfd5;
}
.Ticket_no {
  color: #395870;
  display: block;
}
.text-offset {
  color: #7c7c80;
  font-size: 12px;
}
.Status,
.Priority {
  text-align: center;
}
.Assigned_to {
  text-align: center;
}


</style>

<H2> The Ticket Details Nearing Breach </H2>
<table>
  <thead>
    <tr>
      <th scope="col" >Ticket Number</th>
      <th scope="col">Business Elapsed percentage</th>
      
    </tr>
  </thead>
  <tbody>
  %s
  </tbody>
</table>
</html>"""%(allLines1)
        
to = ['saicharan.tyarla@lntinfotech.com','saicharan189@gmail.com']        
    # Prepare actual message
sent_from = gmail_user
part1="""From: %s 
To: %s 
Subject: %s the send email ID is %s

""" %(sent_from, ", ".join(to), SUBJECT,Final_email)
part1 = MIMEText(part1, 'plain')

part2 = """
%s
""" %body
part2 = MIMEText(part2, 'html')


msg.attach(part1)
msg.attach(part2)

try:
    client = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    client.ehlo()
    client.login(gmail_user, gmail_password)
    client.sendmail(sent_from, to, msg.as_string())
    client.close()
    print ("Email sent")
   
    
except Exception as e:
    print ("Email sending failed due to: {0}".format(e))
    
