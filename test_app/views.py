import csv
import json
import os
import random
import sqlite3
import string

from faker import Faker
from django.shortcuts import render
from django.http import HttpResponse, FileResponse

# Create your views here.
def hello(request):
    return HttpResponse('hello')

def requirements(request):
    with open("requirements.txt", 'r') as file:
        data = '<br>'.join(file.readlines())
    return FileResponse(data)

def get_customers(request):
    query = 'select distinct FirstName from customers'
    records = execute_query(query)
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return HttpResponse(result)

def execute_query(query, *args):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, args)
    records = cur.fetchall()
    return records

def get_city_and_state(request):
    state = request.GET.get('State', '?') # штат или город обьязателен
    city = request.GET.get('City', '?')
    query = f'select FirstName, LastName, State, City from customers where State = "{state}" or City = "{city}"'
    records = execute_query(query)
    result = '<br>'.join([
        str(record)
        for record in records
    ])
    return HttpResponse(result)

def fake_user(request):
    fake = Faker()
    fake_users = '<br>'.join([
        str(fake.email() + ' - ' + fake.name())
        for _ in range(100)
    ])
    return HttpResponse(fake_users)

def turnover(request):
    query = 'select round(sum(UnitPrice*Quantity), 2) from invoice_items'
    records = execute_query(query)
    return HttpResponse(list("Оборот компании - ") + records)

def students(request):
    with open('hw2.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        total = total2 = count = 0

        for row in csv_reader:
            total += float(row[' \"Height(Inches)\"'])
            total2 += float(row[' \"Weight(Pounds)\"'])
            count += 1

        if count:
            aver1 = total / count
            aver2 = total2 / count
            ### 1дюйм = 2,54см   и  1фунт = 0,453592кг

            #########  переводим в см и кг, как и указано в задании
            average1 = round(aver1 * 2.54, 2)
            average2 = round(aver2 * 0.453592, 2)
            foo = average1, average2
            result = 'Средний рост и вес соответственно составляют - ' + str(foo)
            return HttpResponse(result)

def gen_password(request):
    length = int(request.GET.get('length', 12)) # default length = 12
    digit = int(request.GET.get('digit', 0))
    chars = string.ascii_letters
    if length < 8 or length > 24:
        return HttpResponse('Bad parameters', 400)
    elif digit == 1:
        chars += string.digits
    passw = ''.join([
        random.choice(chars)
        for _ in range(int(length))
    ])
    return HttpResponse(passw)

############# необязаельное задание
def orders(request):
    city = request.GET.get('BillingCity', '')
    country = request.GET.get('BillingCountry', '')
    query = f'select * from invoices where BillingCity = "{city}" or BillingCountry = "{country}"'
    records = execute_query(query)
    result = '<br>'.join([
        str(record)
        for record in records
    ]) # не сделано еще, не возращает .json
    return HttpResponse(result)
