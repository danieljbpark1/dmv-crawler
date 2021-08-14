from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json

driver = Safari()

print("open DMV scheduling website")
driver.get("https://www.dmv.virginia.gov/onlineservices/appointments.aspx")

print("maximize window")
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
locations_list = locations_menu.options  # list of options in dropdown menu
num_locations = len(locations_list)  # number of locations in dropdown menu
handle_1 = driver.current_window_handle  # window handle for first tab
locations_dict = {}
for i in range(1, num_locations):
    elem = locations_list[i]
    location_name = elem.text
    print(location_name)

    print("select a location")
    locations_menu.select_by_index(i)

    print("scroll to end of page")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    print("find dynamically updated apptLink")
    appt_link_elem = driver.find_element(By.ID, 'apptLink')
    locations_dict[location_name] = appt_link_elem.get_attribute('href')

json = json.dumps(locations_dict)
f = open("locations_dict.json", "w")
f.write(json)
f.close()

driver.quit()
