import csv
import datetime as dt
import sqlite3 as sql
import pandas as pd

calendar = pd.read_csv('calendar_dec18.csv')
listingDetails = pd.read_csv('listings_dec18.csv')
listingSummary = pd.read_csv('listings_summary_dec18.csv')
suburb = pd.read_csv('neighbourhoods_dec18.csv')
reviewSummary = pd.read_csv('reviews_summary_dec18.csv')
reviewDetails = pd.read_csv('reviews_dec18.csv')

conn = sql.connect('dataCSV.db')
calendar.to_sql('calendar', conn)
listingDetails.to_sql('listingDetails', conn)
listingSummary.to_sql('listingSummary', conn)
suburb.to_sql('suburb', conn)
reviewSummary.to_sql('reviewSummary', conn)
reviewDetails.to_sql('reviewDetails', conn)
