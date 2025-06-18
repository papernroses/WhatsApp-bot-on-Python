# twilio
# date time Module
# time module
# 1. twilio client setup
# 2.user inputs
# 3.scheduling time
# 4.sent message


# step-1 installing required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time


#step-2 twilio credentials
account_sid='ACd4221d8c29b77d8a794a894113e74d9e'
auth_token='af443f424ece6228745f005954770ed9'
client =Client(account_sid,auth_token)


#step-3 design and send message function
def send_message(recipient_number,message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent succesfully! Message SID{message.sid}")
    except Exception as e:
        print("An error occured")


#step-4 user input
name=input('Enter the recipient name= ')
recipient_number =input("Enter the recipinet whatsapp number with country code (e.g, +123): ")
message_body =input(f'enter the message you want to send to {name}: ')


#step-5 parse date/time and calculate delay
date_str=input('Enter the date to send the message (YYYY-MM-DD): ')
time_str=input('Enter the time to send the message (HH:MM in 24 hour format): ')

#datetime
schedule_datetime=datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime=datetime.now()

#caluclate delay
time_difference=schedule_datetime-current_datetime
delay_seconds=time_difference.total_seconds()

if(delay_seconds<=0):
    print("The time has passed.Please enter a future time.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}. ")

    #wait until the scheduled time
    time.sleep(delay_seconds)

    #send message
    send_message(recipient_number,message_body)