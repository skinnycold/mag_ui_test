from pages.base_page import BasePage
from pages.locators import customer_login_locators as loc
import allure

class CustomerLoginPage(BasePage):
    current_page = "/customer/account/login"
    @allure.step("Заполняем форму данными")
    def fill_the_form(self, email='', password=''):
       email_field = self.find(loc.email_field_loc)
       password_field = self.find(loc.password_field_loc)
       email_field.send_keys(email)
       password_field.send_keys(password)

    @allure.step('Нажимаем кнопку регистрации')
    def click_on_button(self):
        sign_in_button = self.find(loc.sign_in_button_loc)
        sign_in_button.click()

    @allure.step("Проверяем успешность авторизации")
    def check_successful_authorization(self, email):
        contact_information = self.find(loc.contact_information_loc)
        assert email in contact_information.text, f"{email} IS NOT IN {contact_information.text}"

    @allure.step("Проверяем неуспешную авторизацию")
    def check_unsuccessful_authorization(self, error_text):
        error_alert_message = self.find(loc.error_alert_message_loc)
        assert error_alert_message.text == error_text, f"{error_text} DOESN'T MATCH WITH {error_alert_message.text}"

    def check_required_fields_validation(self):
        error_alert_message = self.find(loc.error_alert_message_loc)
        assert error_alert_message.text == 'A login and a password are required.'

