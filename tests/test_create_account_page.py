from utils.generator_test_data import DataGenerator
gen = DataGenerator()
first_name = gen.first_name()
last_name = gen.last_name()
email = gen.email()
password = gen.password()


def test_successful_registration(account_page):
    account_page.open_page()
    account_page.fill_the_form(first_name, last_name, email, password)
    account_page.click_on_button()
    account_page.check_successful_registration(first_name, last_name, email)

def test_registration_the_same_email(account_page):
    account_page.open_page()
    account_page.fill_the_form(first_name, last_name, email, password)
    account_page.click_on_button()
    account_page.check_registration_already_email("There is already an account with this email address")

def test_required_fields(account_page):
    account_page.open_page()
    account_page.fill_the_form()
    account_page.click_on_button()
    account_page.check_required_fields_validation()