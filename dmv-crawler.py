from selenium import webdriver
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.select import Select

driver = Safari()

print("open DMV scheduling website")
driver.get("https://www.dmv.virginia.gov/onlineservices/appointments.aspx")

print("set up wait")
wait = WebDriverWait(driver, 10)

print("maximze window")
driver.maximize_window()

print("find form element")
form = driver.find_element(By.ID, 'apptForm')

print("click form element")
form.click()

print("find Driver's License Skills Test button")
license_button = driver.find_element(By.ID, 'driverSkillsTest')

print("find driverSkillsTestSelect div")
skill_test_div = driver.find_element_by_class_name('driverSkillsTestSelect')

print("find location dropdown menu element")
locations_elem = skill_test_div.find_element(By.ID, 'apptLocation')

print("create location dropdown menu Select object")
locations_menu = Select(locations_elem)

# iterate over locations
locations_list = locations_menu.options  # list of option elements in dropdown menu
num_locations = len(locations_list)  # number of locations in dropdown menu
handle_1 = driver.current_window_handle  # window handle for first tab
locations_dict = {}
for i in range(1, num_locations):
    elem = locations_list[i]
    location_name = elem.text

    print("select a location")
    locations_menu.select_by_index(i)

    print("scroll to end of page")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    print("find Make an Appointment button")
    appt_button = driver.find_element(By.ID, 'apptLink')

    print("click to open appointment page")
    appt_button.click()

    wait.until(EC.number_of_windows_to_be(2))  # wait for new tab to open

    print("switch to appointment page tab")
    for window_handle in driver.window_handles:
        if window_handle != handle_1:
            driver.switch_to.window(window_handle)
            print("scroll to end of page")
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            break

    locations_dict[location_name] = driver.current_url

    driver.close()  # close this tab
    driver.switch_to.window(handle_1)  # switch back to first tab

print(locations_dict)
driver.quit()
