from .base_page import DemoQA
from ui.locators.practice_form_locators import FormLocators


class Form(DemoQA):
    def delete_footer(self):
        self.driver.execute_script("""var l = document.getElementsByTagName("footer")[0]; 
                                            l.parentNode.removeChild(l);""")
        self.driver.execute_script("""var l = document.getElementById("close-fixedban"); 
                                            l.parentNode.removeChild(l);""")

    def enter_first_name(self, first_name):
        self.find_element(FormLocators.LOCATOR_FIRST_NAME_FIELD).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_element(FormLocators.LOCATOR_LAST_NAME_FIELD).send_keys(last_name)

    def enter_email(self, email):
        self.find_element(FormLocators.LOCATOR_EMAIL_FIELD).send_keys(email)

    def choose_gender(self, gender):
        genders = self.find_elements(FormLocators.LOCATOR_GENDERS_RADIO)
        for gen in genders:
            if self.find_element(FormLocators.LOCATOR_GENDER_RADIO, gen).get_attribute('value') == gender:
                gen.click()
                break

    def enter_number(self, number):
        self.find_element(FormLocators.LOCATOR_NUMBER_FIELD).send_keys(number)

    def enter_date_of_birth(self, day, month, year):
        self.find_element(FormLocators.LOCATOR_DATE_OF_BIRTH_INPUT).click()
        self.select_element(self.find_element(FormLocators.LOCATOR_DATE_OF_YEAR), year)
        self.select_element(self.find_element(FormLocators.LOCATOR_DATE_OF_MONTH), month)

        days = self.find_elements(FormLocators.LOCATOR_DATE_OF_DAY)
        for _day in days:
            if _day.text == day:
                _day.click()
                break

    def enter_subjects(self, subjects):
        self.select_element_react(self.find_element(FormLocators.LOCATOR_SUBJECTS_INPUT), subjects)

    def choose_hobbies(self, *hobbies):
        list_hobbies = self.find_elements(FormLocators.LOCATOR_HOBBIES_CHECKBOX)
        for hobbie in list_hobbies:
            if self.find_element(FormLocators.LOCATOR_GENDER_RADIO, hobbie).get_attribute('value') in hobbies[0]:
                hobbie.click()

    def upload_file(self, file_path):
        self.find_element(FormLocators.LOCATOR_FILE_UPLOAD).send_keys(file_path)

    def enter_address(self, address):
        self.find_element(FormLocators.LOCATOR_ADDRESS_FIELD).send_keys(address)

    def select_state(self, state):
        self.select_element_react(self.find_element(FormLocators.LOCATOR_STATE_SELECT), state)

    def select_city(self, city):
        self.select_element_react(self.find_element(FormLocators.LOCATOR_CITY_SELECT), city)

    def send_form(self):
        self.find_element(FormLocators.LOCATOR_BUTTON_SUBMIT).click()

    def set_jsom_form(self, item):
        return {
            "Student Name": f"{item['first_name']} {item['last_name']}",
            "Student Email": item['email'],
            "Gender": item['gender'],
            "Mobile": item['number'],
            "Date of Birth": item['_date_of_birth'],
            "Subjects": ", ".join(item['subjects']),
            "Hobbies": ", ".join(list(item['hobbies'].values())),
            "Picture": item['file'],
            "Address": item['address'],
            "State and City": f"{item['state']} {item['city']}"
        }

    def check_result(self):
        data = dict()
        table_body = self.find_element(FormLocators.LOCATOR_TABLE_RESULT)
        for row in self.find_elements(FormLocators.LOCATOR_TABLE_ROW, table_body):
            column = self.find_elements(FormLocators.LOCATOR_TABLE_COLUMN, row)
            data[column[0].text] = column[1].text
        return data


