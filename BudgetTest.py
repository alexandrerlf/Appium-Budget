import unittest
from appium import webdriver
from MainPage import MainPage
from BudgetsPage import BudgetsPage
from AddBudgetPage import AddBudgetPage
from data import Budget

class TestCaseBudget(unittest.TestCase):

    def setUp(self):
        # "configurar teste"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformName'] = 'io'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '0427118446'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_budget_empty_budget(self):
        #Tap em Budgets
        mainpage = MainPage(self.driver)
        mainpage.budgets_menu_click()
        self.driver.implicitly_wait(5)
        #Tap em Add
        budgetspage = BudgetsPage(self.driver)
        budgetspage.add_click()
        self.driver.implicitly_wait(5)
        #Entrar com os valores
        addbudgets = AddBudgetPage(self.driver)
        addbudgets.set_type(Budget.type)
        addbudgets.set_value(Budget.value)
        addbudgets.cancel_click()
        #Comparar com o experado
        self.assertEqual(Budget.empty_budget, budgetspage.get_empty_budget())

    def test_bugdet_created(self):
        #Tap em Budgets
        mainpage = MainPage(self.driver)
        mainpage.budgets_menu_click()
        self.driver.implicitly_wait(5)
        #Tap em Add
        budgetspage = BudgetsPage(self.driver)
        budgetspage.add_click()
        self.driver.implicitly_wait(5)
        #Entrar com os valores
        addbudgets = AddBudgetPage(self.driver)
        addbudgets.set_type(Budget.type)
        addbudgets.set_value(Budget.value)
        addbudgets.save_click()
        #Comparar com o experado
        self.assertEqual(Budget.type, budgetspage.get_created_budget())

    def test_budget_value_empty(self):
        #Tap em Budgets
        mainpage = MainPage(self.driver)
        mainpage.budgets_menu_click()
        self.driver.implicitly_wait(5)
        #Tap em Add
        budgetspage = BudgetsPage(self.driver)
        budgetspage.add_click()
        self.driver.implicitly_wait(5)
        #Entrar com os valores
        addbudgets = AddBudgetPage(self.driver)
        addbudgets.set_type(Budget.type)
        addbudgets.set_value(Budget.value_empty)
        addbudgets.save_click()
        #Comparar com o experado
        self.assertEqual(Budget.empty_text_value, budgetspage.get_popUp_empty())

    def  test_budget_type_empty(self):
        #Tap em Budgets
        mainpage = MainPage(self.driver)
        mainpage.budgets_menu_click()
        self.driver.implicitly_wait(5)
        #Tap em Add
        budgetspage = BudgetsPage(self.driver)
        budgetspage.add_click()
        self.driver.implicitly_wait(5)
        #Entrar com os valores
        addbudgets = AddBudgetPage(self.driver)
        addbudgets.set_type(Budget.type_empty)
        addbudgets.set_value(Budget.value)
        addbudgets.save_click()
        #Comparar com o experado
        self.assertEqual(Budget.empty_text_type, budgetspage.get_popUp_empty())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()