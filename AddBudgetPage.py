from appium.webdriver.common.mobileby import MobileBy
from BasePage import BasePage

class AddBudgetPage(BasePage):
    type = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText')
    value = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.EditText')
    save = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.Button[2]')
    cancel = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.Button[1]')

    def set_type(self, type_text):
        type = self.driver.find_element(*AddBudgetPage.type)
        type.send_keys(type_text)

    def set_value(self, value_text):
        value = self.driver.find_element(*AddBudgetPage.value)
        value.send_keys(value_text)

    def save_click(self):
        save = self.driver.find_element(*AddBudgetPage.save)
        save.click()

    def cancel_click(self):
        cancel = self.driver.find_element(*AddBudgetPage.cancel)
        cancel.click()