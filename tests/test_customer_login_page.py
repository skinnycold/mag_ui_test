def test_successful_authorization(login_page):
    login_page.open_page()
    login_page.fill_the_form('payamek485@minduls.com', 'Qwerty12@')
    login_page.click_on_button()
    login_page.check_successful_authorization('payamek485@minduls.com')

def test_unsuccessful_authorization(login_page):
    login_page.open_page()
    login_page.fill_the_form('qweqwe@mail.com', 'Qwerty1@A')
    login_page.click_on_button()
    login_page.check_unsuccessful_authorization(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )

def test_required_fields(login_page):
    login_page.open_page()
    login_page.click_on_button()
    login_page.check_required_fields_validation()