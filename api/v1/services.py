from collections import OrderedDict

from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


def list_foods(request):
    if request.GET.get('user'):
        user = request.GET.get('user')
    sql = """ 
        select * from foods_foods 
        ORDER BY created_dt DESC
        """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return OrderedDict([
        ("items", data)
    ])
def one_food(request,pk):
    if request.GET.get('user'):
        user = request.GET.get('user')
    sql = """ 
        select * from foods_foods
        where id = %s 
         """
    with connection.cursor() as cursor:
        cursor.execute(sql, [pk])
        data = dictfetchone(cursor)
    return OrderedDict([
        ("item", data)
    ])

def list_category(request):
    sql = """ 
            select * from foods_category 
            """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return OrderedDict([
        ("items", data)
    ])
def one_category(request,pk):

    sql = """ 
        select * from foods_category
        where id = %s 
         """
    with connection.cursor() as cursor:
        cursor.execute(sql, [pk])
        data = dictfetchone(cursor)
    return OrderedDict([
        ("item", data)
    ])