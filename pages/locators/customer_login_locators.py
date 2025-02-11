from selenium.webdriver.common.by import By

email_field_loc = (By.ID, 'email')
password_field_loc = (By.ID, 'pass')
sign_in_button_loc = (By.ID, 'send2')
forgot_password_link_loc = (By.LINK_TEXT, 'Forgot Your Password?')
email_field_error_loc = (By.ID, 'email-error')
password_field_error_loc = (By.ID, 'pass-error')
contact_information_loc = (By.XPATH, "//div[@class='box box-information']//div[@class='box-content']")
error_alert_message_loc = (By.XPATH, "//div[@role='alert']/div//div")