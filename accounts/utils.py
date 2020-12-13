from django.conf import settings
from time import time
import requests
import json
import os
import uuid


def dataRestictions_handle(name,email,phone, address,university,graduation_Year,cgpa, experiance, current_working_place, applying_in, expected_salary,field_Buzz_Ref, github_url):
    message = ""
    if len(str(name))>256 and len(str(name))<=0:
        message = "Name Length Must be Between 1 and 256"

    elif  len(str(email))>256 and len(str(email))<=0:
        message = "Email Length Must be Between 1 and 256"
    
    elif len(str(phone))>14 and len(str(phone))<=10:
        message = "Phone Length Must be Between 10 and 14"

    elif len(str(address))>512 and len(str(address))<=0:
        message = "Address Length Must be Between 1 and 512"
    
    elif len(str(university))>256 and len(str(university))<=0:
        message = "University's Name Length Must be Between 1 and 256"
    
    elif graduation_Year>2020 and graduation_Year<=2014:
        message = "Graduation Year's Must be Between 2015 and 2020"
    
    elif cgpa>4 and cgpa<=1.99:
        message = "CGPA Must be Between 2.00 and 4.00"

    elif experiance>100 and experiance<0:
        message = "Experiance Must be Between 0 and 100"

    elif len(str(current_working_place))>256 and len(str(current_working_place))<=0:
        message = "Current Working Place's Length Must be Between 1 and 256"

    elif applying_in=="None":
        message = "Select Android or Backend as your interest"

    elif expected_salary>60000 or expected_salary<=14999:
        message = "Expected Salary Must be Between 15000 an 60000"

    elif len(str(field_Buzz_Ref))>256 and len(str(field_Buzz_Ref))<=0:
        message = "Feild Buzz Ref's Length Must be Between 1 and 256"

    elif len(str(github_url))>512 and len(str(github_url))<=0:
        message = "Github URL link's Lenght Must be Between 0 and 512"
    
    return message



def putResume(file_token_id,filename,token):
    url = "https://recruitment.fisdev.com/api/file-object/"+str(file_token_id)+"/"
    # resume_file = convertToBinaryData(filename)
    data=[
        ('file',(filename,open(os.path.join(settings.MEDIA_ROOT, filename),'rb'),'application/pdf'))
    ]
    header={
        'Authorization': f'Token {token}'
    }
    response = requests.put(url,files=data,headers=header)
    return response.json()


def getToken(username,password):
    url = "https://recruitment.fisdev.com/api/login/"
    response = requests.post(url,data={'username':username,'password':password})
    return response.json()



def time_calculation():
    return int(time() * 1000)


def tsyncID_genarator(email):
    id_main = uuid.uuid3(uuid.NAMESPACE_DNS, str(email))
    id_pdf = uuid.uuid3(id_main,str(email))
    return str(id_main),str(id_pdf)


def postData(token,tsync_id,name,email,phone, address,university,graduation_Year,cgpa, experiance, current_working_place, applying_in, expected_salary,field_Buzz_Ref, github_url,tsync_id_pdf,created_time,updated_time):
    url = "https://recruitment.fisdev.com/api/v0/recruiting-entities/"
    data =  {
    "tsync_id": tsync_id,
    "name": name,
    "email": email,
    "phone": phone,
    "full_address": address,
    "name_of_university": university,
    "graduation_year": graduation_Year,
    "cgpa": cgpa,
    "experience_in_months": experiance,
    "current_work_place_name": current_working_place,
    "applying_in": applying_in,
    "expected_salary": expected_salary,
    "field_buzz_reference": field_Buzz_Ref,
    "github_project_url": github_url,
    "cv_file": {
        "tsync_id": tsync_id_pdf
    },
    "on_spot_update_time": updated_time,
    "on_spot_creation_time": created_time
    }
    header = {'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    print("successs")
    response = requests.post(url,data=data,headers=header)
    return response.json()

