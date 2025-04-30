from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
import time
import winsound

def login_to_website(driver):
    time.sleep(1)
    Login_link = "https://ais.usvisa-info.com/en-" + driver.country_code + "/niv/users/sign_in"
    driver.get(Login_link)
    time.sleep(1)

    Password = driver.password
    Email_Address = driver.email_address

    email_address_box = driver.find_element(By.ID, 'user_email')
    pass_box = driver.find_element(By.ID, 'user_password')

    email_address_box.send_keys(Email_Address)
    pass_box.send_keys(Password)

    time.sleep(2)
    I_Have_Understood_button = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    ActionChains(driver).click(I_Have_Understood_button).perform()
    time.sleep(5)

    login_button = driver.find_element(By.NAME, 'commit')
    login_button.click()
    time.sleep(1)

def logout_to_website(driver):
    time.sleep(1)
    Logout_link = "https://ais.usvisa-info.com/en-" + driver.country_code + "/niv/users/sign_out"
    driver.get(Logout_link)
    time.sleep(1)

def group_applicants(driver, choose1, choose2, choose3):
    All_applicants = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    if len(All_applicants) >= 1 and choose1 == '1':
        ActionChains(driver).click(All_applicants[0]).perform()
    if len(All_applicants) >= 2 and choose2 == '1':
        ActionChains(driver).click(All_applicants[1]).perform()
    if len(All_applicants) >= 3 and choose3 == '1':
        ActionChains(driver).click(All_applicants[2]).perform()

    continue_button = driver.find_element(By.NAME, 'commit')
    continue_button.click()

def found_appointment(driver):
    Calendar_button = driver.find_element(By.ID, "appointments_consulate_appointment_date")
    Calendar_button.click()
    current_year = 2025
    Date_selected = False

    while True:
        current_year_element = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
        current_year = int(current_year_element.get_attribute('innerHTML'))

        current_month_element_left = driver.find_elements(By.CLASS_NAME, "ui-datepicker-month")[0]
        current_month_left = current_month_element_left.get_attribute('innerHTML')

        time.sleep(1)
        if current_year == int(driver.Year_up_to) and current_month_left == driver.Month_up_to:
            break

        Date_Available_List = driver.find_elements(By.CSS_SELECTOR, "a[class='ui-state-default']")
        if not Date_Available_List:
            Right_button_calendar = driver.find_element(By.CSS_SELECTOR, "span[class='ui-icon ui-icon-circle-triangle-e']")
            Right_button_calendar.click()
        else:
            Date_Available = driver.find_element(By.CSS_SELECTOR, "a[class='ui-state-default']")
            Date_Available.click()
            Date_selected = True
            winsound.Beep(440, 500)
            break

    if Date_selected:
        winsound.Beep(440, 500)
        Consulate_Location_Button = driver.find_element(By.ID, "appointments_consulate_address")
        Consulate_Location_Button.click()
        winsound.Beep(440, 500)
        Appointment_Time_Button = driver.find_element(By.ID, "appointments_consulate_appointment_time")
        Appointment_Time_Button.click()

        input("✅ Appointment found! Press Enter to exit or restart the bot manually.")
        return False
    else:
        return True

def create_driver():
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    time.sleep(1)
    driver = Chrome(options=options)
    return driver

def run_bot(driver):
    pause_between_commands = 1
    Try_Again = True
    log_off_log_in_time = 2
    start_time = time.time()
    Appointment_Not_Early_Enough = True
    while Appointment_Not_Early_Enough:
        while Try_Again:
            elapsed_time = (time.time()) - start_time
            if elapsed_time // 3600 == log_off_log_in_time:
                log_off_log_in_time += 2
                logout_to_website(driver)
                time.sleep(1)
                login_to_website(driver)
                time.sleep(1)
            try:
                driver.window_handles
                continue_button = driver.find_element(By.LINK_TEXT, "Continue")
                continue_button.click()
                time.sleep(pause_between_commands)
                Schedule_Appointment_button = driver.find_element(By.LINK_TEXT, "Reschedule Appointment")
                Schedule_Appointment_button.click()
                time.sleep(pause_between_commands)
                Schedule_Appointment_button = driver.find_elements(By.LINK_TEXT, "Reschedule Appointment")[1]
                Schedule_Appointment_button.click()

                group_applicants(driver, driver.choose1, driver.choose2, driver.choose3)

                select = Select(driver.find_element(By.ID, "appointments_consulate_appointment_facility_id"))
                select.select_by_value(driver.city_code)

                time.sleep(2)
                element = driver.find_element(By.ID, "consulate_date_time")
                attributeValue = element.value_of_css_property("display")
                if ('none' in attributeValue) or (attributeValue is None):
                    Try_Again = True
                    cancel_button = driver.find_element(By.CSS_SELECTOR, "a[class='button secondary']")
                    cancel_button.click()
                    time.sleep(30)
                else:
                    Try_Again = False
                    break
            except:
                print("Driver doesn't have active window.")
                return

        Appointment_Not_Early_Enough = found_appointment(driver)
        if Appointment_Not_Early_Enough:
            Try_Again = True
            cancel_button = driver.find_element(By.CSS_SELECTOR, "a[class='button secondary']")
            cancel_button.click()
            time.sleep(30)
    return

if __name__ == "__main__":
    driver = create_driver()
    driver.minimize_window()

    Embassy_Country_Code = {
        "1": "ae",
        "2": "am",
        "3": "tr",
        "4": "ca",
    }

    Canada_City_Code = {
        "1": '89',
        "2": '90',
        "3": '91',
        "4": '92',
        "5": '93',
        "6": '94',
        "7": '95',
    }

    UAE_City_Code = {
        "1": '49',
        "2": '50',
    }

    Selected_country_code = input("UAE = 1\nArmenia = 2\nTurkey = 3\nCanada = 4\nType the number for your country and press Enter:\n")

    if Selected_country_code == '1':
        Selected_city_code = input("Abu Dhabi = 1\nDubai = 2\nType the number for your city and press Enter:\n")
        Selected_city_code = UAE_City_Code[Selected_city_code]

    if Selected_country_code == '4':
        Selected_city_code = input("Calgary = 1\nHalifax = 2\nMontreal = 3\nOttawa = 4\nQuebec City = 5\nToronto = 6\nVancouver = 7\nType the number for your city and press Enter:\n")
        Selected_city_code = Canada_City_Code[Selected_city_code]

    email_address = input("Enter your login email address and press Enter:\n")
    password = input("Enter your login password and press Enter:\n")

    choose1 = input("Select applicant 1? (yes = 1, no = 0): ").strip()
    choose2 = input("Select applicant 2? (yes = 1, no = 0): ").strip()
    choose3 = input("Select applicant 3? (yes = 1, no = 0): ").strip()

    driver.Year_up_to = input("Enter the year up to which you want the algorithm to search for appointments and press Enter: (e.g. 2024)\n")
    driver.Month_up_to = input("Enter the Month up to which you want the algorithm to search for appointments and press Enter: (e.g. March)\n")

    driver.password = password
    driver.email_address = email_address
    driver.country_code = Embassy_Country_Code[Selected_country_code]
    driver.city_code = Selected_city_code
    driver.choose1 = choose1
    driver.choose2 = choose2
    driver.choose3 = choose3

    driver.maximize_window()

    login_to_website(driver)
    run_bot(driver)