
import time
import datetime
from os import system, getcwd, path, makedirs
import os
import smtplib                                              ############ Import the smtp related module to send mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def Sending_Mail(Final_email,Ticket_no,Ticket_Status,Ticket_priority,Final_name,Ticket_description,Status,desc):

    now = datetime.now()
    dt = now.strftime("%A,%d-%B-%y")
    dt=str(dt)

    print("we started")

    SUBJECT = ''' ####### Ticket Assign %s ####### 
        '''%(Status)
    frommail=" asdas"
    gmail_user = '*****@gmail.com'
    gmail_password = '************'
    msg = MIMEMultipart('alternative')
    
    
    body="""
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
    <H2> %s </H2>
    <table>
      <thead>
        <tr>
          <th scope="col" >Ticket Number</th>
          <th scope="col">Status</th>
          <th scope="col">Priority</th>
          <th scope="col">Assignedto </th>
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
    </html>"""%(desc,Ticket_no,Ticket_Status,Ticket_priority,Final_name,Ticket_description)
            
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
