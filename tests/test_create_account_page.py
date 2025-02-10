

def test_successful_registration(account_page):
    account_page.open_page()
    account_page.fill_the_form('Aqlbert', 'Fqedotov', '12milo@mail.com', '1qwer@@qQ24')
    account_page.click_on_button()
    account_page.check_successful_registration('Aqlbert', 'Fqedotov', '12milo@mail.com')

def test_registration_the_same_email(account_page):
    account_page.open_page()
    account_page.fill_the_form('Aqlbert', 'Fqedotov', '7712551t12es1tffewwfqf@mail.com', '1qwer@@qQ24')
    account_page.click_on_button()
    account_page.check_registration_already_email("There is already an account with this email address")

def test_required_fields(account_page):
    account_page.open_page()
    account_page.fill_the_form()
    account_page.click_on_button()
    account_page.check_required_fields_validation()