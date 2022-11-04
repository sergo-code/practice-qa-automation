import os
import pytest

from ui.page_objects.practice_form import Form
from utils.json_reader import get_data


@pytest.mark.parametrize('item', get_data('practice_form.json'))
def test(browser, item):
    item = item[1]
    form_page = Form(browser, 'automation-practice-form')
    form_page.go_to_site()
    form_page.delete_footer()
    form_page.enter_first_name(item['first_name'])
    form_page.enter_last_name(item['last_name'])
    form_page.enter_email(item['email'])
    form_page.choose_gender(item['gender'])
    form_page.enter_number(item['number'])
    form_page.enter_date_of_birth(item['date_of_birth']['day'],
                                  item['date_of_birth']['month'],
                                  item['date_of_birth']['year'])
    form_page.enter_subjects(item['subjects'])
    form_page.choose_hobbies(list(item['hobbies'].keys()))
    form_page.upload_file(os.path.join(os.getcwd(), 'config', 'file', item['file']))
    form_page.enter_address(item['address'])
    form_page.select_state(item['state'])
    form_page.select_city(item['city'])
    form_page.send_form()

    assert form_page.check_result() == form_page.set_jsom_form(item)
