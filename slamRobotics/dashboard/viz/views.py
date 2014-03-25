__author__ = 'shruti jain'

import json
import datetime
from django.shortcuts import render
from django.db import connection
from django.shortcuts import render_to_response
from datetime import date, timedelta

def default(o):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.isoformat()

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def getH2Sconc(request):

    pipe_id = str(request.GET.get('pid'))
    entry_date = str(request.GET.get('edate'))

    cursor = connection.cursor()

    query_readings = cursor.execute("Select * from readings_h2s where entry_date = '2/18/2014' and pipe_id = '"+ '1'+"'")
    result_readings = dictfetchall(cursor)

    query_dates = cursor.execute("Select distinct entry_date from readings_h2s")
    result_dates = json.dumps(dictfetchall(cursor), default=default)

    query_pipes = cursor.execute("Select distinct pipe_id from readings_h2s")
    result_pipes = json.dumps(dictfetchall(cursor), default=default)

    result = {
        'entry_date' : result_dates,
        'pipe_id' : result_pipes,
        'reading' : result_readings
    }


    return render_to_response('home.html',result)





