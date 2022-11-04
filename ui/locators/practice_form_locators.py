from selenium.webdriver.common.by import By


class FormLocators:
    LOCATOR_FIRST_NAME_FIELD = (By.XPATH, "//input[@id='firstName']")
    LOCATOR_LAST_NAME_FIELD = (By.XPATH, "//input[@id='lastName']")
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//input[@id='userEmail']")
    LOCATOR_GENDERS_RADIO = (By.XPATH, "//div[@class='custom-control custom-radio custom-control-inline']")
    LOCATOR_GENDER_RADIO = (By.XPATH, 'input')
    LOCATOR_NUMBER_FIELD = (By.XPATH, "//input[@id='userNumber']")
    LOCATOR_DATE_OF_BIRTH_INPUT = (By.XPATH, "//input[@id='dateOfBirthInput']")
    LOCATOR_DATE_OF_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    LOCATOR_DATE_OF_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    LOCATOR_DATE_OF_DAY = (By.XPATH, "//div[contains(concat(' ', @class), 'react-datepicker__day--')]")
    LOCATOR_SUBJECTS_INPUT = (By.XPATH, "//input[@id='subjectsInput']")
    LOCATOR_HOBBIES_CHECKBOX = (By.XPATH, "//div[@class='custom-control custom-checkbox custom-control-inline']")
    LOCATOR_FILE_UPLOAD = (By.XPATH, "//input[@id='uploadPicture']")
    LOCATOR_ADDRESS_FIELD = (By.XPATH, "//textarea[@id='currentAddress']")
    LOCATOR_STATE_SELECT = (By.XPATH, "//input[@id='react-select-3-input']")
    LOCATOR_CITY_SELECT = (By.XPATH, "//input[@id='react-select-4-input']")
    LOCATOR_BUTTON_SUBMIT = (By.XPATH, "//button[@id='submit']")
    LOCATOR_TABLE_RESULT = (By.XPATH, "//tbody")
    LOCATOR_TABLE_ROW = (By.XPATH, "tr")
    LOCATOR_TABLE_COLUMN = (By.XPATH, "td")
