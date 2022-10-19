import time
import datetime
import sys
import os
import platform
from datetime import datetime
from datetime import date
import getpass

VERSION = '1.0.0'


def time_taken(func):

    def inner_fun(*args, **kwargs):        
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Total time for -->{func.__name__} is {end - start} seconds")
    
    return inner_fun


def fib_of_n_numbers(num):
    pass
    

@time_taken
def sleeping(name = "", waittime = 2):    
    print(f"\n\n{'-'*10}Decorator Worker {'-'*10}")
    if name == "" or name == None:
        name = os.getlogin()
    # print(os.path.expanduser('~'))        
    print(f"Hello {name}!!!")
    print(f"sleeping for {waittime} seconds")
    time.sleep(waittime)    
    print(f"already woke up!!!!")


def os_details():
    print(f"\n\n{'-'*10}Operating System Details{'-'*10}")
    print(f"user:{getpass.getuser()}")
    print(platform.system())
    # print(platform.system())
    print(platform.release())
    print(platform.version())


def year_detail():
    print(f"\n\n{'-'*10}Year details{'-'*10}")
    day_of_year = datetime.now().timetuple().tm_yday
    print("Day of year-->",day_of_year)
    month = datetime.now().timetuple().tm_mon
    print("Month in year-->",month)
    day_of_month = datetime.now().timetuple().tm_mday
    print("Day of month-->",day_of_month)

    
def my_detail(birth_date):
    print(f"\n\n{'-'*10}Personal details{'-'*10}")
    d1 = date.fromisoformat(birth_date)
    # year, month, day = birth_date.split("-")
    # year = int(year)
    # month = int(month)
    # day = int(day)
    # d1 = date(year, month, day)
    print("Birth_date-->",d1)
    print("Today-->",date.today())
    print("Total number of Days till today-->", date.today() - d1)


def main():
    birth_date = "1991-03-01"
    os_details()
    # sleeping()
    year_detail()
    # my_detail(birth_date)
    

    
if __name__ == '__main__':
    sys.exit(main())