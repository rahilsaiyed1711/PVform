import os
import pandas as pd
import re
import csv
import openpyxl
import ast
import certifi
import ssl
import requests
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime, timedelta, date
from subprocess import Popen, check_output, check_call, PIPE, call
import pathlib
import calendar


path = "D:/OneDrive - Adani/Documents"  # Laptop Path

os.chdir(path)

df11 = pd.read_csv('PVform1.csv', sep=',')


Table1= "Pvform1"
Tablename = Table1

table_id = "agel-svc-winddata-dmz-prod.winddata"+"."+ Tablename


job = client.load_table_from_dataframe(df11, table)
