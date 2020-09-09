#to convert excel file into json with pandas
# for print column wise

import pandas

excel_data_df = pandas.read_excel('C:\\Users\\asifk\\Desktop\\movies.xlsx', sheet_name='Sheet')

json_str = excel_data_df.to_json()

print( json_str)