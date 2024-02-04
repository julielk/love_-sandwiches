
# python code goes here
import gspread
from google.oauth2.service_account import credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# check if API id working
#sales = SHEET.worksheet('sales')
#data = sales.get_all_values()

#print(data)

def get_sales_data():
  """
    Get  sales figures to input from the user
  """
print("please enter sales data from the last market")

print("Data should be six numbers separated by a comma")

print("Example: 10,20,30,40,50,60\n")

data_str = input("Enter your data here")

print(f"The data provided is {data_str}")



sales_data_str.split(",")
validate_data(sales)

#print(sale_data)

def validate_data():
  """
  Inside the try ,convert all strings values
  into integer raise valueError if the string
  cannot be converted  into int or if there aren't exactly 6 values
  """
   # print(values)

   try:
      if len(values) != 6:
        raise ValueError(
         f'Exactly 6 values required you provided (len(values))'

        )
  
except: ValueError as e:

       print(f'Invalid data:(e) please try again')

get_sales_data()