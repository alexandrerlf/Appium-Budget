from appium.webdriver.common.mobileby import MobileBy
from BasePage import BasePage

class MainPage(BasePage):

    budgets_menu = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')

    def budgets_menu_click(self):
        budgets = self.driver.find_element(*MainPage.budgets_menu)
        budgets.click()
