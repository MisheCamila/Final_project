"""
Michelle Munoz
STOCK PROBLEM UPDATES
"""
from tabulate import tabulate
#Read the file
read_file_path=r'C:\Users\User\Desktop\master\python\week10\final assigment\Lesson6_Data_Stocks.csv'
read2_file_path=r'C:\Users\User\Desktop\master\python\week10\final assigment\Lesson6_Data_Bonds.csv'
#Open file
try:
    read_file=open(read_file_path,'r')
   # f=open(read_file_path,'a')
except FileNotFoundError:
    print("The first file does not exist")
try:
    read2_file=open(read2_file_path,'r')
   # f2=open(read2_file_path,'a')
except FileNotFoundError:
    print("The second file does not exist")   
#Split headers
header=read_file.readline()
header_split=header.split(',')
id_index=header_split.index('purchase_id')
Symbol_index=header_split.index('symbol')
Shares_index=header_split.index('number_shares')
Purchase_Price_index=header_split.index('purchase_price')
Current_Price_index=header_split.index('current_cost')
Purchase_Date_index=header_split.index('purchase_date\n')
#Split headers Bond
header2=read2_file.readline()
header2_split=header2.split(',')
id_index=header2_split.index('purchase_id')
Symbol_index=header2_split.index('symbol')
Shares_index=header2_split.index('number_shares')
Purchase_Price_index=header2_split.index('purchase_price')
Current_Price_index=header2_split.index('current_cost')
Purchase_Date_index=header2_split.index('purchase_date')
Coupon_Price_index=header2_split.index('coupon')
Yield_Date_index=header2_split.index('yield_bond\n')

from datetime import date
from datetime import datetime
#Import module
import DATE
delta_date=DATE.delta_date

#Create Superclass stocks       
class Stock:
    def __init__(self,Name,Shares,Purchase_Price,Current_Value,Purchase_Date,purchase_id):
        self.Name=Name
        self.Shares=float(Shares)
        self.Purchase_Price=float(Purchase_Price)
        self.Current_Value=float(Current_Value)
        self.Purchase_Date=Purchase_Date
        self.purchase_id =purchase_id 
  
    def pric(self):
        return (self.Current_Value-self.Purchase_Price)*self.Shares
    

    def yearly(self):
        return round((((self.Current_Value-self.Purchase_Price)/self.Purchase_Price)*100)/delta_date,3)



class Bond(Stock):
    def __init__(self,Name,Shares,Purchase_Price,Current_Value,Purchase_Date,purchase_id,Coupon,Yield):
        super().__init__(Name,Shares,Purchase_Price,Current_Value,Purchase_Date,purchase_id)
        self.Coupon=Coupon
        self.Yield=Yield

class Investor:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.stocks = []
        self.bonds = []

    def add_stock(self,Name,Shares,Purchase_Price,Current_Value,Purchase_Date,purchase_id):
        stock = Stock(Name,Shares,Purchase_Price,Current_Value,Purchase_Date,purchase_id)
        self.stocks.append(stock)

    def add_bond(self, symbol, number_shares, purchase_price, current_cost, purchase_date, purchase_id, Coupon,Yield ):
        bond = Bond(symbol, number_shares, purchase_price, current_cost, purchase_date, purchase_id,Coupon,Yield)
        self.bonds.append(bond)

    def get_stock_table(self):
        headers = ["Symbol", "Quantity", "Earnings/Loss", "Yearly Earning/Loss"]
        data = [[stock.Name, stock.Shares, stock.pric(), stock.yearly()] for stock in self.stocks]
        return tabulate(data, headers=headers, tablefmt="grid")

    def get_bond_table(self):
        headers = ["Symbol", "Quantity", "Earnings/Loss", "Yearly Earning/Loss"]
        data = [[bond.Name, bond.Shares, bond.pric(), bond.yearly()] for bond in self.bonds]
        return tabulate(data, headers=headers, tablefmt="grid")

# Instantiate the investor
james_lawrence = Investor(name="James Lawrence", address="4345 Incline Village", phone="614-6085289")

#Create instances Stocks 
for line in read_file:
    line_split=line.strip().split(',')
    james_lawrence.add_stock(line_split[Symbol_index],line_split[Shares_index],line_split[Purchase_Price_index],line_split[Current_Price_index],line_split[Purchase_Date_index], int(id_index))  # Add purchase_id

#Create instances Bonds
for line in read2_file:
    line2_split=line.strip().split(',')
    james_lawrence.add_bond(line2_split[Symbol_index],line2_split[Shares_index],line2_split[Purchase_Price_index],line2_split[Current_Price_index],line2_split[Purchase_Date_index],int(id_index),line2_split[Coupon_Price_index],line2_split[Yield_Date_index])  # Add purchase_id
try:
    with open('report1.txt', 'w') as output_file:
        # Write stock information to the report file
        output_file.write("Stock Information:\n")
        output_file.write(james_lawrence.get_stock_table())

        # Write bond information to the report file
        output_file.write("\nBond Information:\n")
        output_file.write(james_lawrence.get_bond_table())

except IOError:
    print("Error: Unable to write to the output file.")
except Exception as e:
    print("Error:", str(e))

