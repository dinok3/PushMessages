# Notification App!

## Description 
Simple Django application that uses Pushover application to send notifications that you create.
You can do all the CRUD operations and search for past notifications.

## Note
Pushover has a 30-day free trial. After expiration you will have to purchase and license Pushover account.

## Installation
```
git clone https://github.com/krivke/PushMessages.git
cd PushMessages
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Install Pushover and create an account on your phone to receive notifications.
On [Pushover website](https://pushover.net/) you will find your user key that you need to add into:

settings.py: 
```
USER = "your user key"
```


![Brief look at the app](https://github.com/krivke/PushMessages/tree/master/main/static/images/)


