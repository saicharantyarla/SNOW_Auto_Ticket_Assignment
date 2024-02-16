#Need to install requests package for python
#easy_install requests
import requests
from datetime import datetime
import smtplib                                              ############ Import the smtp related module to send mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime



def Sending_Mail(Final_email,Ticket_number,description,status):

    now = datetime.now()
    dt = now.strftime("%A,%d-%B-%y")
    dt=str(dt)

    print("we started")

    SUBJECT = ''' ####### Ticket P1 Status ####### 
        '''
    frommail=" asdas"
    gmail_user = 'saicharantyarla@gmail.com'
    gmail_password = 'Saicharan123$'
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
    <H2> Ticket Status </H2>
    <table>
      <thead>
        <tr>
          <th scope="col" >Ticket Number</th>
          <th scope="col">Status</th>
          <th scope="col">Priority</th>
          
          <th scope="col">Description </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <strong class="Ticket_no">%s</strong>
            <td class="Status">%s</td>
            <td class="Priority">%s</td>
            <td class="Assigned_to">%s</td>
            <td class="Assigned_to">%s</td>
            </td>
        </tr>
        </tbody>
    </table>
    </html>"""%(Ticket_number,status,priority,description)
            
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
        return "Success"
        
    except Exception as e:
        print ("Email sending failed due to: {0}".format(e))
        return "Failure"




def testing(Ticket_sysID)
    try:    
        url = 'https://lntinfotechdemo7.service-now.com/api/now/table/incident/{0}?sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=number%2Cstate%2Cassignment_group%2Csys_id%2Cassigned_to%2Cpriority%2Cshort_description'.format(Ticket_sysID)

        # Eg. User name="admin", Password="admin" for this code sample.
        user = 'sai.charan'
        pwd = 'Charan123$'

        # Set proper headers
        headers = {"Content-Type":"application/json","Accept":"application/json"}



        # Do the HTTP request
        response = requests.patch(url, auth=(user, pwd), headers=headers  )

        # Check for HTTP codes other than 200
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            exit()

        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        if data['result']['state'] == 'In Progress':
            Ticket_number=data['result']['number']
            description=data['result']['short_description']
            status=data['result']['state']
            priority=data['result']['priority']
            if data['result']['priority'] =='1 - Critical':
                time.sleep(100)
                res=Sending_Mail(Final_email,Ticket_number,description,status)
            elif data['result']['priority']== '2 - High':
                time.sleep(160)
                res=Sending_Mail(Final_email,Ticket_number,description,status)
   
        else:
            print("sucess")
            
    except Exception as e:
        
        print(str(e))        
        
    