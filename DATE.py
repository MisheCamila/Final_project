from datetime import date
from datetime import datetime
today= date.today()
str_d1='2017/08/01'
str_d2=today.strftime("%Y/%m/%d")
d1=datetime.strptime(str_d1,"%Y/%m/%d")
d2=datetime.strptime(str_d2,"%Y/%m/%d")
delta=d2-d1

delta_date=delta.days/365.25
