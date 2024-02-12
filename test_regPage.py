from framework_demowebpage_register.POM.register_Page import RegisterPage

class TestRegisterPage:

    def test_register(self,_driver):

        rp = RegisterPage(_driver)
        rp.enter_firstName()
        rp.enter_lastName()
        rp.enter_email()
        rp.enter_password()
        rp.enter_confirmpassword()
        rp.click_Submit()