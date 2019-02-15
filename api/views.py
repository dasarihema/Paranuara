from django.shortcuts import render

# Create your views here.
import requests
import json

def get_company_id(request,company_name):
    #Code to get company name and list people working in the company
    response = requests.get('https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/companies.json')
    companydata = response.json()
    l=len(companydata)
    company_id=''
    for i in range(0,l):
        if companydata[i]['company']==company_name:
            company_id=companydata[i]['index']
    return get_people_in_company(request,company_id)
    #return render(request, 'api/company.html', {
       #'company': company_id
    #})


def get_people_in_company(request,company_id):
    #Code to get list of people working in a company by company id
    response=requests.get('https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/people.json')
    peopledata=response.json()
    p=len(peopledata)
    people=[]
    for i in range(0,p):
        if peopledata[i]['company_id']==company_id:
            people.append(peopledata[i]['name'])
    #Code to get company name  company id
    response1 = requests.get('https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/companies.json')
    companydata = response1.json()
    c=len(companydata)
    company_name=''
    for i in range(0,c):
        if companydata[i]['index']==company_id:
            company_name=companydata[i]['company']
    #put together company name and people working in that company
    #return render(request, 'api/company.html', {
       #'people': people, 'company_name' : company_name,'company_id':company_id
    #})
    if people:
        dict_obj_1={'Employees':people}
        json_str_1=json.dumps(dict_obj_1)
        return render(request,'api/company.html',{'json_str_1':json_str_1})
    else:
        return render(request,'api/company.html',{'Message': 'This company does not have any employees.'})


def get_people_info(request,people1,people2):
    response=requests.get('https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/people.json')
    peopledata=response.json()
    p=len(peopledata)
    people3=peopledata[0]['name']
    p1=[]
    p2=[]
    for i in range(0,p):
        if peopledata[i]['name']==people1:
            p1.append(peopledata[i]['name'])
            p1.append(peopledata[i]['age'])
            p1.append(peopledata[i]['address'])
            p1.append(peopledata[i]['phone'])
            p1.append(peopledata[i]['friends'])
        elif peopledata[i]['name']==people2:
            p2.append(peopledata[i]['name'])
            p2.append(peopledata[i]['age'])
            p2.append(peopledata[i]['address'])
            p2.append(peopledata[i]['phone'])
            p2.append(peopledata[i]['friends'])
    #return render(request, 'api/company.html', {
       #'people1': p1, 'people2' : p2
    #})
    return get_friends_in_common_withbrowneyes_andalive(request,p1,p2)


def get_friends_in_common_withbrowneyes_andalive(request,people1,people2):
    response=requests.get('https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/people.json')
    peopledata=response.json()
    p=len(peopledata)
    len_friends_p1=len(people1[4])
    len_friends_p2=len(people2[4])
    friends_p1=[]
    friends_p2=[]
    for i in range(len_friends_p1):
        friends_p1.append(people1[4][i]['index'])
    for j in range(len_friends_p2):
        friends_p2.append(people2[4][j]['index'])
    common_friends=list(set(friends_p1)&set(friends_p2))
    common_friends_with_browneyes_andalive=[]
    for j in common_friends:
        for i in range(p):
            if peopledata[i]['index']==j:
                if peopledata[i]['eyeColor']=="brown" and peopledata[i]['has_died']== False:
                    common_friends_with_browneyes_andalive.append(peopledata[i]['name'])
    dict_obj_2={'Username1': people1[0:4], 'Username2' : people2[0:4] ,'common_friends_with_browneyes_and_arealive':common_friends_with_browneyes_andalive}
    json_str_2=json.dumps(dict_obj_2)
    return render(request, 'api/company.html', {'json_str_2':json_str_2})

    #return render(request, 'api/company.html', {
           #'people1': people1, 'people2' : people2 ,'common_friends':common_friends,'common_friends_with_browneyes_andalive':common_friends_with_browneyes_andalive
        #})


def get_favourite_fruits_and_vegetables(request,people1):
    response=requests.get('https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/people.json')
    peopledata=response.json()
    p=len(peopledata)
    food=[]
    for i in range(0,p):
        for j in range(len(peopledata[i]['favouriteFood'])):
            food.append(peopledata[i]['favouriteFood'][j])
    fruits_and_vegetables_set=set(food)
    fruits_and_vegetables={'fruits':['banana','strawberry','apple','orange'],'vegetables':['beetroot','cucumber','carrot','celery']}
    favourite_fruits_by_people1=[]
    favourite_vegetables_by_people1=[]
    for i in range(0,p):
        if peopledata[i]['name']==people1:
            age=str(peopledata[i]['age'])
            for j in range(len(peopledata[i]['favouriteFood'])):
                if peopledata[i]['favouriteFood'][j] in fruits_and_vegetables['fruits']:
                    favourite_fruits_by_people1.append(peopledata[i]['favouriteFood'][j])
                elif peopledata[i]['favouriteFood'][j] in fruits_and_vegetables['vegetables']:
                    favourite_vegetables_by_people1.append(peopledata[i]['favouriteFood'][j])
    dict_obj_3={'username': people1, 'age': age,'fruits':favourite_fruits_by_people1,'vegetables':favourite_vegetables_by_people1}
    json_str_3=json.dumps(dict_obj_3)
    return render(request, 'api/company.html', {'json_str_3':json_str_3})
