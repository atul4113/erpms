from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,"index.html")

@csrf_exempt
def js_register(request):
    if request.method == "POST":
        uname = request.POST.get("js_name")
        email = request.POST.get("js_email")
        mobile = request.POST.get("js_mobile")
        password = request.POST.get("js_password")
        education = request.POST.get("js_education")
        skills = request.POST.get("js_skills")
        location = request.POST.get("js_location")
        resume = request.POST.get("js_resume")
        profile = request.POST.get("js_profile")
        from .models import JS
        data =JS(name_js=uname,email=email,mobile=mobile,password=password,education=education,skills=skills,location=location,resume=resume,profile=profile)
        data.save()
        return render(request,"jobseeker/register.html",{"msg": "You are now Registered"})
    else:
        return render(request,"jobseeker/register.html",{"msg": ""})

@csrf_exempt
def js_login(request):
    return render(request,"jobseeker/login.html")

@csrf_exempt
def js_dashboard(request):
    if request.method == "GET":
        return render(request,"jobseeker/dashboard.html",{"msg":"Uff!!! Something Went Wrong, Please Try Again"})
    else:
        request.method == "POST"
        from .models import JS
        email = request.POST.get("js_email")
        password = request.POST.get("js_password")
        login = JS.objects.filter(email=email, password=password)
        return render(request, "jobseeker/dashboard.html", {"login": login})

@csrf_exempt
def js_profile_edit(request):
    if request.method =="GET":
        from .models import JS
        email = request.GET.get("js_email")
        edit = JS.objects.filter(email=email)
        return render(request,"jobseeker/edit-profile.html",{"edit":edit})
    else:
        request.method == "POST"
        uname = request.POST.get("js_name")
        email = request.POST.get("js_email")
        mobile = request.POST.get("js_mobile")
        password = request.POST.get("js_password")
        education = request.POST.get("js_education")
        skills = request.POST.get("js_skills")
        location = request.POST.get("js_location")
        resume = request.POST.get("js_resume")
        profile = request.POST.get("js_profile")
        from .models import JS
        data = JS(name_js=uname, email=email, mobile=mobile, password=password, education=education, skills=skills,
                  location=location, resume=resume, profile=profile)
        data.save()
        return render(request, "jobseeker/edit-profile.html", {"msg": "Data Updated"})

@csrf_exempt
def js_view_jobs(request):
    from .models import Jobs
    res = Jobs.objects.all()
    return render(request, "jobseeker/view-jobs.html", {"jobs": res})

@csrf_exempt
def js_online_exam_registration(request):
    if request.method == "GET":
        from .models import JS
        email = request.GET.get("js_email")
        show = JS.objects.filter(email=email)
        return render(request, "jobseeker/online-exam-registration.html",{"res":show})
    else:
        request.method == "POST"
        from .models import Exams
        uname = request.POST.get("js_name")
        email = request.POST.get("js_email")
        mobile = request.POST.get("js_mobile")
        exams = request.POST.get("exams")
        exams = Exams(e_name=uname,e_email=email,e_mobile=mobile,e_exams=exams)
        exams.save()
        return render(request,"jobseeker/online-exam-registration.html",{"msg":"You are registered successfully"})


@csrf_exempt
def comp_registration(request):
    if request.method == "POST":
        from .models import Company
        c_name = request.POST.get("comp_name")
        c_email = request.POST.get("comp_email")
        c_contact = request.POST.get("comp_contact")
        c_pw = request.POST.get("comp_password")
        c_add = request.POST.get("comp_address")
        res = Company(c_name=c_name,c_email=c_email,c_contact=c_contact,c_pw=c_pw,c_address=c_add)
        res.save()
        return render(request,"company/registration.html",{"msg":"Successfully Registered"})
    else:
        return render(request,"company/registration.html")

@csrf_exempt
def comp_login(request):
    return render(request,"company/login.html")

@csrf_exempt
def comp_dashboard(request):
    if request.method == "GET":
        return render(request,"company/dashboard.html")
    else:
        request.method == "POST"
        from .models import Company
        c_email = request.POST.get("comp_email")
        c_pw = request.POST.get("comp_password")
        login = Company.objects.filter(c_email=c_email,c_pw=c_pw)
        return render(request,"company/dashboard.html",{"login":login})

@csrf_exempt
def comp_profile_edit(request):
    if request.method == "GET":
        from .models import Company
        c_email = request.GET.get("comp_email")
        edit = Company.objects.filter(c_email=c_email)
        return render(request, "company/edit-comp-profile.html", {"edit": edit})
    else:
        request.method == "POST"
        from .models import Company
        c_name = request.POST.get("comp_name")
        c_email = request.POST.get("comp_email")
        c_contact = request.POST.get("comp_contact")
        c_pw = request.POST.get("comp_password")
        c_add = request.POST.get("comp_address")
        res = Company(c_name=c_name, c_email=c_email, c_contact=c_contact, c_pw=c_pw, c_address=c_add)
        res.save()
        return render(request, "company/dashboard.html", {"msg": "Successfully Updated"})

@csrf_exempt
def post_jobs(request):
    if request.method == "GET":
        return render(request,"company/post-jobs.html")
    else:
        request.method == "POST"
        from .models import Jobs
        title = request.POST.get("job_title")
        type = request.POST.get("job_type")
        detail = request.POST.get("job_detail")
        tags = request.POST.get("tags")
        job_post = Jobs(job_title=title,job_type=type,job_detail=detail,job_tags=tags)
        job_post.save()
        return render(request,"company/post-jobs.html",{"jobs":"Job posted"})

@csrf_exempt
def view_jobs(request):
    from .models import Jobs
    res = Jobs.objects.all()
    return render(request,"company/view-jobs.html",{"jobs":res})

@csrf_exempt
def login(request):
    if request.method == "POST":
        from .models import Admin
        usr = request.POST.get("usr")
        pw = request.POST.get("pw")
        login = Admin.objects.filter(ausr=usr,apw=pw)
        return render(request,"dashboard.html",{"login":login})
    else:
        return render(request,"login.html")

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        request.method == "POST"
        usr = request.POST.get("usr")
        pw = request.POST.get("pw")
        from .models import Admin
        ad = Admin(ausr=usr,apw=pw)
        ad.save()
    return render(request,"register.html",{"msg":"Congratulation!! You are register as admin User"})

@csrf_exempt
def dashboard(request):
    from .models import Admin,Company,JS,Jobs,Exams
    comp = Company.objects.all()
    js = JS.objects.all()
    jobs = Jobs.objects.all()
    exam = Exams.objects.all()
    usr = request.POST.get("usr")
    pw = request.POST.get("pw")
    login = Admin.objects.filter(ausr=usr, apw=pw)
    return render(request,"dashboard.html",{"comp":comp,"js":js,"jobs":jobs,"login": login,"exam":exam})

@csrf_exempt
def delete(request):
    return render(request,"delete.html")

@csrf_exempt
def view_all_company(request):
    return render(request,"view-all-company.html")

@csrf_exempt
def view_all_jobseeker(request):
    return render(request,"view-all-jobseeker.html")

@csrf_exempt
def view_all_jobs(request):
    return render(request,"view-all-jobs.html")
