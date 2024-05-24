class loginPage():
    email = 'Email'
    psw = 'Password'
    login_btn = '//input[@class="button-1 login-button"]'
    err_msg = '//div[@class="validation-summary-errors"]'

class loginData():
    url = 'https://demowebshop.tricentis.com/'
    url_regist = 'https://demowebshop.tricentis.com/register'
    url_login = 'https://demowebshop.tricentis.com/login'
    title = 'Demo Web Shop'
    email_valid = 'sel@test.com'
    psw_valid = '123456'
    email_invalid = 'tested@test.com'
    psw_invalid = "098765"
    msg_error_login = 'Login was unsuccessful.'