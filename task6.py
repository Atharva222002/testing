from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "F:\Program\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.thesparksfoundationsingapore.org")
time.sleep(10)
# TEST- 1] Checking If The Spark Foundation Name Exist in Title of website or not
print("# TEST- 1] Checking If The Spark Foundation Name Exist in Title of website or not :\n")
try:
    if("The Sparks Foundation" in driver.title):
        print("Title of website is correct.\n")
    else:
        print("Title of website is incorrect.\n\n")
    print("-"*10+"*"*3+"-"*10+"\n")
except:
    pass

# TEST- 2] Checking existence of Logo
print("# TEST- 2] Checking existence of Logo :\n")
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/img')
    print("Logo exists on the Home Page.\n")
    print("-" * 10 + "*" * 3 + "-" * 10+"\n")
except NoSuchElementException:
    print("Logo does not exist.")

# TEST- 3] Checking existence of Contact Us page
print("# TEST- 3] Checking existence of Contact Us page :\n")
try:
    driver.find_element_by_link_text("Contact Us").click()
    print("Contact Us page is displayed successfully.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10+"\n")
except NoSuchElementException:
    print("Contact Page does not exist")

# TEST- 4] Checking address is correct or not
print("# TEST- 4] Checking address is correct or not :\n")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(2)
    address=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/p")
    if("119613" in address.text):
        print("PIN is correct.\n")
        driver.back()
        print("-" * 10 + "*" * 3 + "-" * 10+"\n")
except NoSuchElementException:
    print("Pin does not exist or is incorrect.")

# TEST- 5] Checking Why Join Us page
print("# TEST- 5] Checking Why Join Us page :\n")
try:
    driver.find_element_by_link_text("Join Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Why Join Us").click()
    time.sleep(2)
    driver.back()
    print("Why Join Us page exists.\n")
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Why Join Us page does not exist.")


# TEST- 6] Checking Contact Number is correct or not
print("# TEST- 6] Checking Contact Number is correct or not :\n")
try:
    driver.find_element_by_link_text("Contact Us").click()
    driver.implicitly_wait(5)
    contact=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]")
    if("+65-8402-8590" in contact.text):
        print("Contact number is correct.\n")
        driver.back()
        print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Contact Number does not exist or is incorrect.")

# TEST- 7] Checking if Executive Team page exist or not
print("# TEST- 7] Checking if Executive Team page exist or not :\n")
try:
    driver.find_element_by_link_text("About Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Executive Team").click()
    time.sleep(2)
    print("Execitive Team Members page is displayed.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Executive Team info is not displayed.")

# TEST- 8] Checking if AI in Education page exist or not
print("# TEST- 8] Checking if AI in Education page exist or not\n")
try:
    driver.find_element_by_link_text("LINKS").click()
    time.sleep(2)
    driver.find_element_by_link_text("AI in Education").click()
    time.sleep(2)
    print("AI in Education page is displayed.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("AI in Education is not displayed.")

# TEST- 9] Checking if AI in Education page exist or not
print("# TEST- 9] Checking if AI in Education page exist or not\n")
try:
    driver.find_element_by_link_text("Programs").click()
    time.sleep(2)
    driver.find_element_by_link_text("Student Scholarship Program").click()
    time.sleep(2)
    print("Student Scholarship Program page is displayed.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Student Scholarship Program is not displayed.")

# TEST- 10] Checking if Event Volunteer page exist or not
print("# TEST- 10] Checking if Event Volunteer page exist or not :\n")
try:
    driver.find_element_by_link_text("Join Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Events Volunteer").click()
    time.sleep(2)
    print("Events Volunteers page exist.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Events Volunteers page does not exist")

# TEST- 11] Checking if Join Us form works
print("# TEST- 11] Checking if Join Us form works :\n")
try:
    driver.find_element_by_link_text("Join Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Events Volunteer").click()
    time.sleep(2)
    driver.find_element_by_name("Name").send_keys("atharva")
    time.sleep(2)
    driver.find_element_by_name("Email").send_keys("atharva")
    time.sleep(2)
    driver.find_element_by_xpath("/ html / body / div[2] / div / div[2] / div[2] / div / form / select / option[2]").click()
    time.sleep(3)
    print("Join US form accepts input.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Join US form does not accept input.")

# TEST- 12] Checking if instagram icon works
print("# TEST- 12] Checking if instagram icon works :\n")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(2)
    driver.find_element_by_class_name("fa-instagram").click()
    time.sleep(20)
    print("Instagram icon work well.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Instagram icon don't work.")

# TEST- 13] Checking if The Sparks Foundation (Global) website works
print("# TEST- 13] Checking if The Sparks Foundation (Global) website works :\n")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("The Sparks Foundation (Global)").click()
    time.sleep(20)
    print("The Sparks Foundation (Global) website is visited.\n")
    driver.back()
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("The Sparks Foundation (Global) website is not visited.")

# TEST- 14] Checking The Sparks Foundation Internships on Internshala
print("# TEST- 14] Checking The Sparks Foundation Internships on Internshala :\n")
try:
    driver.find_element_by_link_text("Internships at Internshala").click()
    time.sleep(20)
    print("Internships at Internshala page is visited.\n")
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Internships at Internshala is not visited.")

# TEST- 15] Applying for Advisor role
print("# TEST- 15] Applying for Advisor role :\n")
try:
    driver.find_element_by_link_text("Join Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Events Volunteer").click()
    time.sleep(2)
    driver.find_element_by_name("Name").send_keys("atharva")
    time.sleep(2)
    driver.find_element_by_name("Email").send_keys("atharva")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select/option[6]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/ html / body / div[2] / div / div[2] / div[2] / div / form / input[3]").click()
    time.sleep(4)
    print("Successfully applied for Advisor role.\n")
    print("-" * 10 + "*" * 3 + "-" * 10 + "\n")
except NoSuchElementException:
    print("Cannot apply for Advisor role.")

driver.quit()