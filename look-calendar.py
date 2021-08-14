from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import json

with open("locations_dict.json") as json_file:
    locations_dict = json.load(json_file)

# for location, url in locations_dict.items():
#     print(url)

url = 'https://vadmvappointments.as.me/schedule.php?calendarID=5776710'

driver = Safari()

driver.get(url)

driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

form = driver.find_element(By.ID, 'appointment-form')
step_container = form.find_element(By.ID, 'step-pick-appointment')
appt_pane = step_container.find_element_by_class_name('pick-appointment-pane')
choose_date = appt_pane.find_element_by_class_name('choose-date')

calendar = driver.find_element_by_xpath("//table[@class='calendar']")
print(calendar)
# cal_rows = calendar.find_elements_by_xpath("//tbody/tr[@class='calendar-date-row']")


try:
    pass
except selenium.common.exceptions.NoSuchElementException:
    pass

driver.quit()
# dmv_page = requests.get(url)
#
# soup = BeautifulSoup(dmv_page.text, "html.parser")
# body = soup.body
#
# print(body.text)
# content = body.find("div", {"class": "content"})
# form = content.find("form", {"id": "appointment-form"})
# print(form.text)
# pick_appt_container = form.find("div", {"id", "step-pick-appointment"})
# print(pick_appt_container.text)
