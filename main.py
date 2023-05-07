
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sched



username = input('Username: ')
password = input('Password: ')
sarmaye = input('Mizan sarmaye baray kharid ra be Rial vared konid: ')
start_time = input('Saati ke mikhahid ersal sefaresh aghaz shava vared konid(Format: HH:MM:SS): ')
delay = input('Fasele bein orderha ra be mili sanie vared konid(Hadeaghal 300): ')
order_quantity = input('Tedad orderha: ')
order_quantity = int(order_quantity)
delay = int(delay)/1000

driver = webdriver.Chrome(executable_path='D:\Projects\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.nahayatnegar.com/online')

# login
driver.find_element(By.NAME, 'userEmail').send_keys(username)
driver.find_element(By.NAME, 'userPassword').send_keys(password)
time.sleep(10)
try:
    driver.find_element(By.NAME, 'submit').click()
except:
    pass
time.sleep(10)

# finding target stocks
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "html/body/div[3]/div/div[1]/div/div/div[1]/div/div/form/div/div"))).click()

time.sleep(1)
try:
    driver.find_element(By.XPATH,"//*[contains(text(), 'سرخطی')]").click()
except:
    print('Dideban peyda nashod!')
    
time.sleep(10)

# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[3]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/table/tbody/tr[1]"))).click()
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/table/tbody/tr[1]')
# time.sleep(2)

# Enter to Info Tab
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[1]"))).click()

# time.sleep(1)
price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[2]/span[3]"))).text.replace(',', '')

# Enter to Buy Tab
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]"))).click()

time.sleep(1)

# fill thet order fields
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div[1]/div[2]/div/input').send_keys(price)
volume = (int(sarmaye) / int(price)) - 10
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div[3]/div[2]/div[1]/input').send_keys(int(volume))
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[3]/input').click()
buy_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[4]/div[1]/button')

def send_order():
    for i in range(order_quantity):
        buy_button.click()
        time.sleep(delay)


scheduler = sched.scheduler(time.time, time.sleep)

# define the time to run the function
run_time = time.strptime(f"{start_time}", "%H:%M:%S")

# get the current time
current_time = time.localtime()
# calculate the time until the function should run
time_diff = (run_time.tm_hour - current_time.tm_hour) * 3600 + (run_time.tm_min - current_time.tm_min) * 60 + (run_time.tm_sec - current_time.tm_sec)

# schedule the function to run at the specified time
scheduler.enter(time_diff, 1, send_order, ())

# start the scheduler
scheduler.run()

time.sleep(20)