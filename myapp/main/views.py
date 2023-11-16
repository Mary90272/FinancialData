import json
from django.shortcuts import render
from main.models import Data
from django.http import JsonResponse
from django.core import serializers
import csv
from django.views.decorators.csrf import csrf_exempt
# import requests doent need anymore
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Create your views here.


def index(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    job_filter = request.GET.get('job_filter')
    batch_filter = request.GET.get('batch_filter')
    reference_filter = request.GET.get('reference_filter')
    transfer_date_filter = request.GET.get('transfer_date_filter')
    sort_by = request.GET.get('sort_by')

    date_range_filter = {"Due_Date__range": [startDate, endDate]}
    dynamic_filter = {}
    if job_filter:
        dynamic_filter['Job__exact'] = 'Job'
    if batch_filter:
        dynamic_filter['Batch__exact'] = 'Batch'
    if reference_filter:
        dynamic_filter['Ref__exact'] = 'Ref'
    if transfer_date_filter:
        dynamic_filter['Chk_Date__exact'] = 'Chk_Date'

    if sort_by == 'Job':
        order_by_field = 'Job'
    elif sort_by == 'Due__Date':
        order_by_field = '"Due__Date"'
    elif sort_by == 'Amt':
        order_by_field = 'Amt'

    order_by_field = sort_by if sort_by else 'Job'

    # Query the Data model based on the 'job' parameter
    all_data = Data.objects.all()
    all_data = all_data.filter(
        **date_range_filter).order_by(order_by_field)
    # Serialize the QuerySet to a JSON-serializable format
    data_list = list(all_data.values())

    # create_csv(filtered_data)
    return JsonResponse(data_list, safe=False)

    # Return the serialized data as a JSON response


@csrf_exempt
def receiveData(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            create_csv(data)
            upload_csv('data.csv')

            # Return a JSON response
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def create_csv(data_list):

    # Create csv file from data_list
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Sequence', 'Acct', 'Acct_Per', 'Desc', 'Dept_Desc', 'Dept', 'Invoice_Nbr',
                      'Batch_Close_Date', 'Tran_Date', 'Vend_Cust_Nbr', 'Comment', 'Acct_Desc', 'JV', 'Due_Date', 'Job', 'Ref', 'Chk_Date', 'Batch', 'Amt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_list:
            print("Writing data to csv file")
            writer.writerow(data)


def upload_csv(filename):

    # Parse CSV file
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        csv_data = list(csv_reader)
    # Use Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'onemore.json', scope)  # Replace with your Google API key file onemore.json
    client = gspread.authorize(creds)
    # Open Google Sheets and get the first sheet
    # create new sheet
    # Replace 'test' with your Google Sheet name
    sheet = client.open('test').sheet1
    # create rows in sheet

    # Write the CSV data to Google Sheets
    sheet.update('A1', csv_data)
