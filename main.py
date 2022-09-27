from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


class PythonGuviProject:
    def __init__(self):
        self.username = 'Admin'
        self.password = 'admin123'
        self.firstName = 'Shubham'
        self.middleName = 'B'
        self.lastName = 'Savantre'
        self.newPassword = 'Admin@123'
        self.newUsername = 'Shubham.Savantre'
        self.driver = webdriver.Chrome(executable_path="D:\\Personal\\Guvi project 2\\chromedriver.exe")
        self.driver.maximize_window()

    def log_in_as_admin(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        time.sleep(2)

        my_username = self.driver.find_element(By.XPATH,
                                               '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div['
                                               '1]/div/div[2]/input')
        my_username.send_keys(self.username)

        my_password = self.driver.find_element(By.XPATH,
                                               '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div['
                                               '2]/div/div[2]/input')
        my_password.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()
        time.sleep(5)

    def pim_create_user(self):
        select_pim = self.driver.find_element(By.XPATH,
                                              "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']["
                                              "normalize-space()='PIM']")
        select_pim.click()
        time.sleep(1)

        add_employee_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
        add_employee_button.click()
        time.sleep(1)

        employee_first_name = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        employee_first_name.send_keys(self.firstName)
        employee_middle_name = self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
        employee_middle_name.send_keys(self.middleName)
        employee_last_name = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        employee_last_name.send_keys(self.lastName)

        create_login_button = self.driver.find_element(By.XPATH,
                                                       "//span[@class='oxd-switch-input oxd-switch-input--active "
                                                       "--label-right']")
        create_login_button.click()

        insert_username = self.driver.find_element(By.XPATH,
                                                   "//body/div[@id='app']/div[@class='oxd-layout']/div["
                                                   "@class='oxd-layout-container']/div["
                                                   "@class='oxd-layout-context']/div["
                                                   "@class='orangehrm-background-container']/div["
                                                   "@class='orangehrm-card-container']/form[@class='oxd-form']/div["
                                                   "@class='orangehrm-employee-container']/div["
                                                   "@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div["
                                                   "1]/div[1]/div[1]/div[2]/input[1]")
        insert_username.send_keys(self.newUsername)

        insert_password = self.driver.find_element(By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters "
                                                             "user-password-cell']//div[@class='oxd-input-group "
                                                             "oxd-input-field-bottom-space']//div//input["
                                                             "@type='password']")
        insert_password.send_keys(self.newPassword)

        insert_confirm_password = self.driver.find_element(By.XPATH, "//div[@class='oxd-grid-item "
                                                                     "oxd-grid-item--gutters']//div["
                                                                     "@class='oxd-input-group "
                                                                     "oxd-input-field-bottom-space']//div//input["
                                                                     "@type='password']")
        insert_confirm_password.send_keys(self.newPassword)

        add_employee = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        add_employee.click()
        time.sleep(5)

    """The below function has minor corrections. Hence Bypassing the 4th and 5th point in the project document and 
    implementing it in the above code i.e. in pim_create_user function. """

    def admin_user_create(self):
        admin_tab = self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > "
                                                              "div:nth-child(1) > aside:nth-child(1) > nav:nth-child("
                                                              "1) > div:nth-child(2) > ul:nth-child(2) > "
                                                              "li:nth-child(1) > a:nth-child(1) > span:nth-child(2)")
        admin_tab.click()

        add_admin_user = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
        add_admin_user.click()

        user_role_drop = self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div["
                                                            "1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                                            "1]/div[1]/div[2]")
        user_role_drop.click()
        select_role = self.driver.find_element(By.XPATH, "//*[text()='ESS']")
        select_role.click()

        status_role_drop = self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div["
                                                              "1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div["
                                                              "1]/div[1]/div[2]")
        status_role_drop.click()
        select_status = self.driver.find_element(By.XPATH, "//*[text()='Enabled']")
        select_status.click()

        employee_name = self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
        employee_name.send_keys('Shubham')
        select_employee = self.driver.find_element(By.XPATH, "//div[@class='oxd-autocomplete-dropdown "
                                                             "--position-bottom']//*[text()='Shubham B Savantre']")
        select_employee.click()

        employee_username = self.driver.find_element(By.CSS_SELECTOR, "div[class='oxd-form-row'] div["
                                                                      "class='oxd-grid-2 orangehrm-full-width-grid'] "
                                                                      "div[class='oxd-grid-item "
                                                                      "oxd-grid-item--gutters'] div["
                                                                      "class='oxd-input-group "
                                                                      "oxd-input-field-bottom-space'] div input["
                                                                      "class='oxd-input oxd-input--active']")
        employee_username.send_keys(self.newUsername)

        employee_password = self.driver.find_element(By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters "
                                                               "user-password-cell']//div[@class='oxd-input-group "
                                                               "oxd-input-field-bottom-space']//div//input["
                                                               "@type='password']")
        employee_password.send_keys(self.newPassword)

        employee_confirm_password = self.driver.find_element(By.XPATH, "//div[@class='oxd-grid-item "
                                                                       "oxd-grid-item--gutters']//div["
                                                                       "@class='oxd-input-group "
                                                                       "oxd-input-field-bottom-space']//div//input["
                                                                       "@type='password']")
        employee_confirm_password.send_keys(self.newPassword)

        time.sleep(5)

        save_credentials = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        save_credentials.click()

    def admin_user_search(self):
        admin_tab = self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > "
                                                              "div:nth-child(1) > aside:nth-child(1) > nav:nth-child("
                                                              "1) > div:nth-child(2) > ul:nth-child(2) > "
                                                              "li:nth-child(1) > a:nth-child(1) > span:nth-child(2)")
        admin_tab.click()

        username_search = self.driver.find_element(By.XPATH, "//div[@class='oxd-input-group "
                                                             "oxd-input-field-bottom-space']//div//input["
                                                             "@class='oxd-input oxd-input--active']")
        username_search.send_keys(self.newUsername)

        search_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
        search_button.click()
        time.sleep(5)

    def admin_verify_user(self):
        try:
            if self.driver.find_element(By.XPATH, "//div[@class='orangehrm-container']//div["
                                                  "@class='oxd-table-body']//div[contains(.,'Shubham.Savantre')]"):
                print('User verified')

        except NoSuchElementException:
            print("User not found")

    def log_out(self):

        profile_button = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        profile_button.click()
        log_out_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        log_out_button.click()
        time.sleep(5)

    def relogin_as_user(self):

        my_username = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div["
                                                         "2]/form/div[1]/div/div[2]/input")
        my_username.send_keys(self.newUsername)

        my_password = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div["
                                                         "2]/form/div[2]/div/div[2]/input")
        my_password.send_keys(self.newPassword)

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        login_button.click()


guvi = PythonGuviProject()
guvi.log_in_as_admin()
guvi.pim_create_user()
#guvi.admin_user_create()
guvi.admin_user_search()
guvi.admin_verify_user()
guvi.log_out()
guvi.relogin_as_user()
