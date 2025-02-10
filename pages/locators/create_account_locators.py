from selenium.webdriver.common.by import By

first_name_field_loc = (By.ID, 'firstname')
last_name_field_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
password_field_loc = (By.ID, 'password')
confirm_password_loc = (By.ID, 'password-confirmation')
create_account_button_loc = (By.CSS_SELECTOR, "[class='action submit primary']")



first_name_error_loc = (By.ID, 'firstname-error')
last_name_error_loc = (By.ID, 'lastname-error')
email_error_loc = (By.ID, 'email_address-error')
password_error_loc = (By.ID, 'password-error')
confirm_error_loc = (By.ID, 'password-confirmation-error')

successful_registration_alert_loc = (By.CSS_SELECTOR, "[class='page messages']")
contact_information_loc = (By.XPATH, "//div[@class='box box-information']//div[@class='box-content']")

cookie_agree_button_loc = (By.CSS_SELECTOR, "[class=' css-1n36tvh']")