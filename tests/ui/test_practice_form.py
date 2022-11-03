import os

from ui.page_objects.practice_form import Form


def test(browser):
    form_page = Form(browser, 'automation-practice-form')
    form_page.go_to_site()
    form_page.delete_footer()
    form_page.enter_first_name('sergo')
    form_page.enter_last_name('code')
    form_page.enter_email('s.ivanoff071@gmail.com')
    form_page.choose_gender('Male')
    form_page.enter_number('91234567890')
    form_page.enter_date_of_birth('1', 'January', '1900')
    form_page.enter_subjects('English')
    form_page.choose_hobbies(['1', '3'])
    form_page.upload_file(f'{os.getcwd()}/image.jpeg')
    form_page.enter_address('749 Tatum Street Hamline - Midway Ramsey County Миннесота 55104 Соединённые Штаты Америки')
    form_page.select_state('NCR')
    form_page.select_city('Noida')
    form_page.send_form()

