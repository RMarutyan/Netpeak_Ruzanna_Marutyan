from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color
import time

Chrome_path=r'C:\Users\Asus\Desktop\Ruzanna\Automation\Drivers\chromedriver.exe'

#Elements
career_element   =  (By.XPATH,"//li[@class='main-link']//a[text()='Карьера']")
want_work        =  (By.XPATH,"//div[@class='text-center agree-btn']//a[text()='Я хочу работать в Netpeak']")
submit           = (By.ID, "submit")
warning_mes      = (By.XPATH, "//p[@class='warning-fields help-block']")
page_career      = (By.XPATH, "//h2[@class='expandOpen']")

# Create chrome driver
driver = webdriver.Chrome(Chrome_path)
# maximize the browser window
driver.maximize_window()
# navigate to the Netpeak page (task-1)
driver.get("https://netpeak.ua")
# find the "Карьера" element
work_link=driver.find_element(*career_element)
#Navigate to "Работа в Netpeak" tab by clicking "Карьера" button (task-2)
work_link.click()
time.sleep(3)
action = ActionChains(driver)
main = driver.window_handles[0]
career = driver.window_handles[1]
#switch to newly opened "career.netpeak.group" tab
driver.switch_to.window(career)
#Open the page for the questionnaire by clicking "Я хочу работать в Netpeak" button (task-3)
want_work_link = driver.find_element(*want_work)
action.move_to_element(want_work_link)
want_work_link.click()
#Upload file
upload_button = driver.find_element_by_xpath("//input[@type='file']")
upload_button.send_keys(r'C:\Users\Asus\Desktop\Ruzanna\Automation\Homeworks_QA_Automation\CV.png')
time.sleep(5)
#compare actual and expected messages (task-4)
actual_msg = driver.find_element(By.XPATH, "//div[@id='up_file_name']/label").text
exp_msg = 'Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).'
assert exp_msg == actual_msg
#enter values in the Name, Lastname, email, Phone fields (task-5)
driver.find_element_by_id("inputName").send_keys('Ruzanna'+Keys.TAB+'Marutyan'+Keys.TAB+'mail@mail.ru'+Keys.TAB*2+'010123456')
time.sleep(5)
#select an option from Year DDL
year_list = Select(driver.find_element_by_xpath("//select[@name='by']"))
year_list.select_by_index('12')
#select an option from Month DDL
month_list = Select(driver.find_element_by_xpath("//select[@name='bm']"))
month_list.select_by_index('1')
#select an option from Day DDL
day_list = Select(driver.find_element_by_xpath("//select[@name='bd']"))
day_list.select_by_index('15')
#Click Submit button (task-6)
submit_button =driver.find_element(*submit)
action.move_to_element(submit_button)
time.sleep(3)
#check validation message for required fields and get the color of message (task-7)
submit_button.click()
#scroll to the element
driver.execute_script("window.scrollTo(0, 2000)")
warn_message = driver.find_element(*warning_mes)
action.move_to_element(warn_message)
warn_mes_str = driver.find_element(*warning_mes).text
rgb = warn_message.value_of_css_property("color")
color = Color.from_string(rgb).hex
assert color == '#ff0000'
#click Курсы tab
course=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.LINK_TEXT,'Курсы'))
)
course.click()
time.sleep(3)
page_text=driver.find_element(*page_career).text
exp__page_msg='строй свою карьеру вместе с нами'
#check that desired page is opened by locating one element from the current page
assert exp__page_msg==page_text
driver.quit()
print("Test is finished")
