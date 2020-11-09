from appium.webdriver.common.mobileby import MobileBy
from BasePage import BasePage

class BudgetsPage(BasePage):

    add = (MobileBy.ACCESSIBILITY_ID, 'Add')
    created_budget = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.TextView')
    popupEmpty = (MobileBy.ID, 'protect.budgetwatch:id/snackbar_text')
    budgetEmpty = (MobileBy.ID, 'protect.budgetwatch:id/helpText')


    def add_click(self):
        add = self.driver.find_element(*BudgetsPage.add)
        add.click()

    def get_created_budget(self):
        created_budget = self.driver.find_element(*BudgetsPage.created_budget)
        return created_budget.text

    def get_popUp_empty(self):
        popupEmpty = self.driver.find_element(*BudgetsPage.popupEmpty)
        return popupEmpty.text

    def get_empty_budget(self):
        budgetEmpty = self.driver.find_element(*BudgetsPage.budgetEmpty)
        return budgetEmpty.text
