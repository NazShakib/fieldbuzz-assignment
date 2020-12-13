from django import forms


class ApplicantInfo(forms.Form):
    name = forms.CharField(max_length=256,widget=forms.TextInput(attrs={"class": "form-control","name":"fullname",'placeholder':'Full Name'}))
    email=forms.EmailField(max_length=256,widget=forms.TextInput(attrs={"class": "form-control","name":"email",'placeholder':'Email'}))
    phone = forms.CharField(max_length=14,widget=forms.TextInput(attrs={"class": "form-control","name":"phone",'placeholder':'Phone Number'}))
    address = forms.CharField(max_length=512,widget=forms.TextInput(attrs={"class": "form-control","name":"address",'placeholder':'Adress'}))
    university = forms.CharField(max_length=256,widget=forms.TextInput(attrs={"class": "form-control","name":"university",'placeholder':'University Name'}))
    graduation_Year = forms.IntegerField(max_value=2020,min_value=2015,widget=forms.TextInput(attrs={"class": "form-control","name":"graduation",'placeholder':'Graduation Year'}))
    Cgpa = forms.DecimalField(max_value=4,min_value=2,widget=forms.TextInput(attrs={"class": "form-control","name":"cgpa",'placeholder':'CGPA'}))
    experiance = forms.IntegerField(max_value=100,min_value=0,widget=forms.TextInput(attrs={"class": "form-control","name":"experiance",'placeholder':'Experiance'}))
    current_working_place = forms.CharField(max_length=256,widget=forms.TextInput(attrs={"class": "form-control","name":"current_work",'placeholder':'Current Working Place'}))
    applying_in = forms.ChoiceField(choices= ((0,'Select an Item'),(1, 'Android'),(2, 'Backend')),widget=forms.Select(attrs={"class": "custom-select my-1 mr-sm-2","name":"applying"}))
    expected_salary = forms.IntegerField(max_value=60000,min_value=15000,widget=forms.TextInput(attrs={"class": "form-control","name":"expected_salary",'placeholder':'Expected Salary'}))
    field_Buzz_Ref = forms.CharField(max_length=256,widget=forms.TextInput(attrs={"class": "form-control","name":"field_ref",'placeholder':'Field Buzz Reference'}))
    github_url = forms.CharField(max_length=512,widget=forms.TextInput(attrs={"class": "form-control","name":"github_link",'placeholder':'Github Link'}))
    resume = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control","name":"resume",'accept':'application/pdf'}))



    