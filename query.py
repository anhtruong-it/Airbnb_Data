import sqlite3
import pandas as pd
import numpy as mp
import matplotlib.pyplot as plt


class Query:
    def __init__(self):
        self.connect = sqlite3.connect('dataCSV.db')
        self.cursor = self.connect.cursor()

    def listingSuburb(self):
        self.cursor.execute("SELECT host_since FROM suburb, listingDetails "
                            "WHERE suburb.neighbourhood == listingDetails.neighbourhood AND host_since BETWEEN '2017-01-01' AND '2018-01-01' ORDER BY host_since DESC")
        result = pd.DataFrame(self.cursor.fetchall())
        result.columns = [x[0] for x in self.cursor.description]
        return result

    def recordKeyword(self, keywords):
        self.cursor.execute("SELECT reviewer_name, comments FROM reviewDetails WHERE comments LIKE '%my dog%'")
        result = pd.DataFrame(self.cursor.fetchall())
        result.columns = [x[0] for x in self.cursor.description]
        return result

    def getPrice(self):
        self.cursor.execute("SELECT price, weekly_price, monthly_price, security_deposit, cleaning_fee, extra_people"
                            " FROM listingDetails WHERE host_since BETWEEN '2017-01-01' AND '2017-02-01' ORDER BY host_since ASC ")
        result = pd.DataFrame(self.cursor.fetchall())
        #result.columns = [x[0] for x in self.cursor.description]
        return result

    def getPriceAnhTime(self):
        result = self.getPrice().values.tolist()
        #print(result)
        result2 = []
        for i in result:
            data = []
            for j in i:
                temp = str(j)
                result = temp.strip('$')
                result1 = result.replace(",","")
                print(result1)
                if result1 == 'None':
                    result1 = 0

                data.append(float(result1))
            result2.append((data))

        return result2

    def getTitle(self):
        title = ['price', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'extra_people']
        return title

    def plotPrice(self):
        self.cursor.execute("SELECT host_since"
                            " FROM listingDetails WHERE host_since BETWEEN '2017-01-01' AND '2017-01-02' ORDER BY host_since ASC ")
        result = pd.DataFrame(self.cursor.fetchall())
        time = result.values.tolist()
        times =[]

        for i in time:
            for j in i:
                times.append(j)
        print(times)

        values = self.getPriceAnhTime()
        price = []
        weekly_price = []
        monthly_price = []
        security_deposit = []
        cleaning_fee = []
        extra_people = []

        for i in values:
            price.append(i[0])
            weekly_price.append(i[1])
            monthly_price.append(i[2])
            security_deposit.append(i[3])
            cleaning_fee.append(i[4])
            extra_people.append(i[5])

        re = [price,weekly_price, monthly_price, security_deposit, cleaning_fee, extra_people]
        fig = plt.figure()
        plt.plot(times, re[0], 'b--', label='Normal Price')
        plt.plot(times, re[1], 'k-', label='weekly price')
        plt.plot(times, re[2], 'r--', label='monthly Price')
        plt.plot(times, re[3], 'y.-', label='security Price')
        plt.plot(times, re[4], 'g-', label='cleaning Price')
        plt.plot(times, re[5], 'g-.', label='extra Price')
        fig.legend(fontsize='x-small')
        plt.title('distribution of prices of properties')
        plt.show()


        #return  re



#a = Query()
#print(a.listingSuburb())
#print(a.recordKeyword(4))
#print(a.getPrice())
#print(a.getPriceAnhTime())
#print(a.plotPrice())


