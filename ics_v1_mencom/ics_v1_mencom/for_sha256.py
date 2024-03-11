import pandas as pd
import os
import shutil
import pymysql

# Read CSV with hash_id and restaurant_id
db_host = 'localhost'
db_user = 'root'
db_password = 'actowiz'
db_name = 'ics_master_db_v1_mancom'

db_data_table = "asset_table"
product_table = "product_table"
pricing_table = "pricing_table"

con = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
sql = f"select sha256 from {db_data_table} where status ='Done'"

df = pd.read_sql(sql=sql, con=con)
# dir_list_22 = os.listdir(r"D:\Work\Actowiz\pages\ics\assets\ACT-B6-009")
dir_list = os.listdir(r"D:/Work/Actowiz/pages/ics/assets/ACT-B7-002/")
# dir_list = os.listdir('E:\\Didi_Food_Page\\CLOSEDRES\\')
# dir_list = os.listdir('E:\\Didi_Food_Page\\refresh\\')


df1 = pd.DataFrame()
df1['sha256'] = dir_list

values_not_in_df = df1[~df1['sha256'].isin(df['sha256'])]

# Display the result
print(values_not_in_df)
# df = pd.read_csv('data.csv')

# Set path for current and new folders
current_folder = r"D:/Work/Actowiz/pages/ics/assets/ACT-B7-002/"
new_folder = r"D:/Work/Actowiz/pages/ics/assets/ACT-B7-002_new/"
mn = 1
mn1 = 1
# Create new folder if it doesn't exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Loop through CSV rows
for index, row in values_not_in_df.iterrows():


    sha256 = row['sha256']
    # restaurant_id = row['res_id']

    # Construct current and new file paths
    current_path = os.path.join(current_folder, sha256)
    new_path = os.path.join(new_folder, sha256)

    # Move HTML file to new folder and rename
    try:
        shutil.move(current_path, new_path)
        print('Good',mn1)
        mn1+=1
    except:
        print('Exeption',mn)
        mn+=1
        pass

    print("HTML files renamed and moved")

# import pandas as pd
# import os
# import shutil
# import pymysql
#
# # Read CSV with hash_id and restaurant_id
# db_host = 'localhost'
# db_user = 'root'
# db_password = 'actowiz'
# db_name = 'ics_master_db_v1_testequity'
#
#
# # db_data_table = f"didi_data_23022023"
# db_data_table = f"asset_table"
#
# con = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
# sql = f"select sha256 from {db_data_table} where status ='Done'"
# curser = con.cursor()
#
# df = pd.read_sql(sql=sql, con=con)
# # dir_list_22 = os.listdir(r"D:\Work\Actowiz\pages\ics\assets\ACT-B6-009")
# dir_list = os.listdir(r"D:\Work\Actowiz\pages\ics\assets\ACT-B7-006")
#
#
# df1 = pd.DataFrame()
# df1['sha256'] = dir_list
#
# values_not_in_df = df[~df['sha256'].isin(df1['sha256'])]
#
# # Display the result
# print(values_not_in_df)
#
# current_folder = r"D:/Work/Actowiz/pages/ics/assets/ACT-B6-009/"
# new_folder = r"U:/Ankit B/ACT-B6-009_NEW/"
# mn = 1
# mn1 = 1
# # Create new folder if it doesn't exist
# if not os.path.exists(new_folder):
#     os.makedirs(new_folder)
# true_count = 1
# false_count = 1
# # Loop through CSV rows
# list1 = []
# for index, row in values_not_in_df.iterrows():
#
#     # Get hash_id and restaurant_id
#     sha256 = row['sha256']
#     filename = current_folder+sha256
#     if os.path.exists(filename):
#         print(True)
#         print('Trupe',true_count)
#         true_count += 1
#     else:
#         print(False)
#         print('false',false_count)
#         list1.append(sha256)
# tuple_data = tuple(list1)
# pdate = f'update {db_data_table} set status="Pending" where sha256 in {tuple_data}'
# curser.execute(pdate)
#
# con.commit()
# # self.logger.info(f'{db.asset_table} Inserted...')
# # con.commit()
# false_count += 1
# print('True',true_count)
# print('False',false_count)

    # restaurant_id = row['res_id']

    # Construct current and new file paths
    # current_path = os.path.join(current_folder, sha256)
    # new_path = os.path.join(new_folder, sha256)
    #
    # # Move HTML file to new folder and rename
    # try:
    #     shutil.move(current_path, new_path)
    #     print('Good',mn1)
    #     mn1+=1
    # except:
    #     print('Exeption',mn)
    #     mn+=1
    #     pass

# print("HTML files renamed and moved")