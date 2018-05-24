from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question
from .forms import AnsForm

def match(get_ans,tag_data):

    marks = 0

    for i in get_ans:
        for j in tag_data:
            if i.upper() == j.upper():
                marks+=1
    return marks

def question_list(request):

    ques_list = Question.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(ques_list, 10)

    try:
        ques = paginator.page(page)
    except PageNotAnInteger:
        ques = paginator.page(1)
    except EmptyPage:
        ques = paginator.page(paginator.num_pages)

    template_name  = "checker/question_list.html"
    context = {

                "ques_list":ques

            }
    return render(request,template_name,context)

def question_ans(request,id=None):

    form = AnsForm(request.POST or None)
    ques = Question.objects.get(id=id)
    question_values = 0
    user_values = 0

    if form.is_valid():

        get_ans = form.cleaned_data["ans_section"]

        if "." in get_ans:
            get_ans=get_ans.replace("."," ")
        if "," in get_ans:
            get_ans=get_ans.replace(","," ")
        if "-" in get_ans:
            get_ans=get_ans.replace("-"," ")
        if "?" in get_ans:
            get_ans=get_ans.replace("?"," ")
        if "_" in get_ans:
            get_ans=get_ans.replace("_"," ")
        if ":" in get_ans:
            get_ans=get_ans.replace(":"," ")
        if "!" in get_ans:
            get_ans=get_ans.replace("!"," ")
        if '"' in get_ans:
            get_ans=get_ans.replace('"'," ")
        if "'" in get_ans:
            get_ans=get_ans.replace("'"," ")
        if "(" in get_ans:
            get_ans=get_ans.replace("("," ")
        if ")" in get_ans:
            get_ans=get_ans.replace(")"," ")
        if ";" in get_ans:
            get_ans=get_ans.replace(";"," ")
        if "[" in get_ans:
            get_ans=get_ans.replace("["," ")
        if "]" in get_ans:
            get_ans=get_ans.replace("]"," ")
        if "[" in get_ans:
            get_ans=get_ans.replace("["," ")
        if "{" in get_ans:
            get_ans=get_ans.replace("}"," ")
        if "/" in get_ans:
            get_ans=get_ans.replace("/"," ")


        get_ans = get_ans.split()
        tag_data_set = ques.tag_data.split(",")
        get_ans_final=[x.strip(' ') for x in get_ans]
        tag_data_set_final=[x.strip(' ') for x in tag_data_set]
        user_values = match(get_ans_final,tag_data_set_final)
        question_values = len(tag_data_set_final)

        if user_values >= question_values:
            user_values=question_values
        else:
            user_values = user_values

        user_values = "%.2f" % ((user_values/question_values)*100)


    template_name = "checker/question_ans.html"
    context = {
                "ques":ques,
                "form":form,
                "user_values":user_values,
        }
    return render(request,template_name,context)
