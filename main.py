from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



main_list=list()

driver = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
First_name = "Jhon"
last_name = "Smith"
driver.get("https://directory.okstate.edu/")
time.sleep(2)
google_input=driver.find_element(By.NAME,'search-first-name')
google_input.send_keys(First_name)

google_input1=driver.find_element(By.NAME,'search-last-name')
google_input1.send_keys(last_name)
google_input1.send_keys(Keys.ENTER)


#
# driver.get (f'https://directory.okstate.edu/index.php/module/Default/action/PersonSearch?campus=&first_name={First_name}&last_name={last_name}')

table=driver.find_element(By.ID,"content")
print(table.text)
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    # print(row.text)
    # Get the columns (all the column 2)
    col = row.find_elements(By.TAG_NAME, "td")
    if len(col) > 0:
        # print(col[0].find_element(By.TAG_NAME, 'a').get_attribute('href'))
        href = col[0].find_element(By.TAG_NAME,'a').get_attribute('href')
        name = col[0].text
        title = col[1].text
        dept = col[2].text
        phone = col[3].text
        email = col[4].text
        campus = col[5].text
        main_list.append([href,name,title,dept,phone,email,campus])
        # [store,col[]]
        # print(store,"===")
#
# print(main_list)
        # get_sheet.insert_row(store)











# row={"ram","mishra"}
# index=2
# sheet.insert_row(row,index)

#
# First_name = "Jhon"#input('Enter the first name\n')
# last_name = "Smith"#input('Enter the last name\n')
#
# driver = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
#
# driver.get("https://directory.okstate.edu/")
# time.sleep(2)
# google_input=driver.find_element(By.NAME,'search-first-name')
# google_input.send_keys(First_name)
#
# google_input1=driver.find_element(By.NAME,'search-last-name')
# google_input1.send_keys(last_name)
# google_input1.send_keys(Keys.ENTER)
#
#
# #
# # driver.get (f'https://directory.okstate.edu/index.php/module/Default/action/PersonSearch?campus=&first_name={First_name}&last_name={last_name}')
#
# table=driver.find_element(By.ID,"content")
# # print(table.text,"+++++++++++++++++++++++++++++++++++++++++++++")
# rows = table.find_elements(By.TAG_NAME, "tr")
# for row in rows:
#     print(row.text)
#     # Get the columns (all the column 2)
#     col = row.find_elements(By.TAG_NAME, "td")
#     if len(col) > 0:
#         print(col[0].find_element(By.TAG_NAME,'a').get_attribute('href'))
















# with open('people.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["sr no.", "name", "title", "department", "phone", "email", "campus"])
#     writer.writerow([1, "John Smith", "	Dir Fin Info Mgmt", "FINANCIAL INFORMATION MANAGEMENT", 405 - 744 - 6475,
#                      "john.smith@okstate.edu", "OSU Stillwater"])

