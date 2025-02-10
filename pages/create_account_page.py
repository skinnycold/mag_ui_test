from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class CreateAccountPage(BasePage):
    current_page = "/customer/account/create/"

    def fill_the_form(self, name='', last_name='', email='', password=''):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable(loc.cookie_agree_button_loc))
        cookie_agree_button = self.find_all(loc.cookie_agree_button_loc)
        if cookie_agree_button:
            cookie_agree_button[0].click()
        first_name_field = self.find(loc.first_name_field_loc)
        last_name_field = self.find(loc.last_name_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password = self.find(loc.confirm_password_loc)

        first_name_field.send_keys(name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password.send_keys(password)

    def click_on_button(self):
        create_account_button = self.find(loc.create_account_button_loc)
        create_account_button.click()

    def check_required_fields_validation(self):
        first_name_error = self.find(loc.first_name_error_loc)
        last_name_error = self.find(loc.last_name_error_loc)
        email_error = self.find(loc.email_error_loc)
        password_error = self.find(loc.password_error_loc)
        confirm_error = self.find(loc.confirm_error_loc)
        error_text_message = 'This is a required field.'
        assert first_name_error.text == error_text_message, f"{first_name_error.text} IS NOT {error_text_message}"
        assert last_name_error.text == error_text_message, f"{last_name_error.text} IS NOT {error_text_message}"
        assert email_error.text == error_text_message, f"{email_error.text} IS NOT {error_text_message}"
        assert password_error.text == error_text_message, f"{password_error.text} IS NOT {error_text_message}"
        assert confirm_error.text == error_text_message, f"{confirm_error.text} IS NOT {error_text_message}"
        logging.info(f"ALL THE REQUIRED FIELDS IS EMPTY - OK IN THIS CASE")


    def check_successful_registration(self, name, last_name, email):
        successful_registration_alert = self.find(loc.successful_registration_alert_loc)
        contact_information = self.find(loc.contact_information_loc)
        assert successful_registration_alert.text == 'Thank you for registering with Main Website Store.'
        logging.info(f"SUCCESSFUL REGISTRATION ALERT IS OK")
        assert contact_information.text == f'{name} {last_name}\n{email}', (
            f'{name} {last_name}\n{email} is not {contact_information.text}'
        )
        logging.info(f"ALL INFORMATION IS CORRECT")

    def check_registration_already_email(self, error_text):
        error_message_email = self.find(loc.error_message_email_loc)
        assert error_text in error_message_email.text
        logging.info(f"ERROR TEXT IS OK")