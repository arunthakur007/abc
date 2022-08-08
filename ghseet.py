import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(credentials)
sheet = client.open('trial')
get_sheet = sheet.worksheet('test')
# insertRow = ["Zayn","Malik",12,20]
mylist = [['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=40692&campus=1','John Smith',' Dir Fin Info Mgmt','FINANCIAL INFORMATION MANAGEMENT', '405-744-6475',' john.smith@okstate.edu',' OSU Stillwater'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=92161&campus=1','John Smith ','Hd Coach Wrestling',' ATHLETIC BUSINESS OFFICE',' 405-744-4541',' john.w.smith@okstate.edu ','OSU Stillwater'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=1003498&campus=12','Jayson Smith',' Student',' ',' ',' jayson.smith10@neo.edu','Northeastern Oklahoma A & M, Miami'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=65414&campus=1','Jon Smythe',' Ast Prof', 'SCHOOL OF TEACHING,LEARNING AND EDUCATIONAL SCIENCES',' 405-744-7125',' jon.smythe@okstate.edu ','OSU Stillwater'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=875925&campus=7','Jordan Smith', 'PATIENT SERV REP II','Internal Medicine', '918-582-7711 ','jordan.smith15@okstate.edu', 'OSU Center for Health Sciences'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=203683&campus=1','Jordan Smith',' Web Des','ATHLETIC BUSINESS OFFICE',' 405-334-6792',' jordan.smith@okstate.edu' ,'OSU Stillwater'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=784314&campus=12','Ashton Smith','Student',' ',' ','ashton.smith12@neo.edu',' Northeastern Oklahoma A & M Miami'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=682928&campus=1','Joe Smith',' Tmp Wkr', 'ATHLETIC BUSINESS OFFICE', '405-744-4541', 'joseph.w.smith@okstate.edu', 'OSU Stillwater'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=1003626&campus=1','Jermonte Smith', 'Student',' ',' ', 'jermosm@okstate.edu ','OSU Stillwater'],
          ['https://directory.okstate.edu/index.php/module/Default/action/ViewPerson?dirkey=978553&campus=11','Jonathan Smith', 'Vice President',' ', '405-744-1887', 'jonathan.r.smith@okstate.edu', 'Langston University, Langston']]

count = 1
for data in mylist:
    print(data)
    get_sheet.insert_row(data,count)
    count += 1
