from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import json

from . utils import *
from . form import *
from . cookie import *
from . decorators import *
from . models import userDetails



list_of_response=[]
### login view 
@is_authenticated ### check weather user loged in or not
def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        res = getToken(username,password)
        token = res['token']
        setCookie(request,'token',token)
        return redirect('home')
    context ={}
    return render(request,'login.html',context)



@unAthenticated ### check uer is unauthenticated
def home(request):
    # print(request.user)
    list_of_response.clear()
    message=[]
    form_class = ApplicantInfo()
    token = getCookie(request,'token')
    if request.method=="POST":
        form_class = ApplicantInfo(request.POST,request.FILES)
        if form_class.is_valid():
            ### form data collected
            name = form_class.cleaned_data.get('name')
            email = form_class.cleaned_data.get('email')
            phone = form_class.cleaned_data.get('phone')
            address = form_class.cleaned_data.get('address')
            university = form_class.cleaned_data.get('university')
            graduation_Year = form_class.cleaned_data.get('graduation_Year')
            cgpa = form_class.cleaned_data.get('Cgpa')
            experiance = form_class.cleaned_data.get('experiance')
            current_working_place = form_class.cleaned_data.get('current_working_place')
            applying_in = form_class.cleaned_data.get('applying_in')
            if applying_in=='1':
                interst_in ="Android"
            elif applying_in=='2':
                interst_in="Backend"
            else:
                interst_in="None"
            expected_salary = form_class.cleaned_data.get('expected_salary')
            field_Buzz_Ref = form_class.cleaned_data.get('field_Buzz_Ref')
            github_url = form_class.cleaned_data.get('github_url')
            resume = request.FILES['resume']
            resume_size = resume.size
            
            ### data validation check
            message1 = ""
            message1 = dataRestictions_handle(name,email,phone,address,university,graduation_Year,cgpa,experiance,current_working_place,interst_in,expected_salary,field_Buzz_Ref,github_url)
            message.append(message1)
            if message==['']:
                if not str(resume).endswith('.pdf') or resume_size>4000000:
                    message.append("File format (shoud be pdf) or size (should be 4MB) may Occure Error")
                else:
                    try:
                        ### database check, exits info or not
                        try:
                            exit_mail =userDetails.objects.get(email=email)
                        except :
                            exit_mail = userDetails.objects.filter(email=email)
                        print(exit_mail)
                        if not exit_mail:
                            obj = userDetails()
                            tsync_id, tsync_pdf_id  = tsyncID_genarator(email)
                            created_at = time_calculation()
                            updated_at = time_calculation()+2
                            obj.main_tysinc_id = tsync_id
                            obj.email = email
                            obj.pdf_tysnic_id = tsync_pdf_id
                            obj.created_at = created_at
                            obj.save()
                        else:
                            tsync_id = exit_mail.main_tysinc_id
                            email = exit_mail.email
                            tsync_pdf_id = exit_mail.pdf_tysnic_id
                            created_at = exit_mail.created_at
                            updated_at = time_calculation()                        
                        ### data post into url
                        response = postData(str(token),str(tsync_id),str(name),str(email),str(phone),str(address),str(university),str(graduation_Year),str(cgpa),str(experiance),str(current_working_place),str(interst_in),str(expected_salary),str(field_Buzz_Ref),str(github_url),str(tsync_pdf_id),str(created_at),str(updated_at))
                        ### cv save in local storage
                        fs = FileSystemStorage()
                        fs.save(resume.name,resume)
                        ### file put into url
                        file_token_id= response["cv_file"]["id"]
                        file_res= putResume(file_token_id,resume.name,token)
                        ### response add into global list
                        list_of_response.append(json.dumps(response))
                        list_of_response.append(json.dumps(file_res))
                        return redirect('result')
                    except Exception as e:
                        list_of_response.append("Error!!!!!")
                        print(e)
    # message="Data saved successfully"
    context = {'form':form_class,"messages":message}
    return render(request,'home.html',context)


def result(request):
    context ={"response":list_of_response}
    return render(request,'result.html',context)


def logout(request):
    deleteCookies(request)
    return redirect('/')

