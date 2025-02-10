from pages.create_account_page import CreateAccountPage

def test_successful_registration(driver,account_page):
    # account_page = CreateAccountPage(driver)
    account_page.open_page()
    account_page.fill_the_form('Albert', 'Fedotov', 'testffewwfqf@mail.com', 'qwer@@qQ24')
    account_page.click_on_button()