import gspread
from oauth2client.service_account import ServiceAccountCredentials

#definig the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open("DATA_SHEET").sheet1

list_of_hashes = sheet.get_all_records()
print(sheet.row_values(1))
sheet.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")
print(sheet.row_values(1))
