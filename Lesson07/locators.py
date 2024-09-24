from selenium.webdriver.common.by import By

class Locators:
    TOP_NAVIGATION_LOGO = (By.XPATH, '//div[contains(@class,"navbar-brand")]/img')
    TOP_NAVIGATION_USER_ICON = (By.XPATH, '//li[contains(@class,"nav-item nav-profile")]/a/span/img')
    COURSE_LIST = (By.XPATH, '//ul[contains(@class,"sidebar-menu")]/li/a')
    LANGUAGE_SWITCHER = (By.XPATH, '//ul[contains(@class,"language-switcher")]/li/a')
    SEARCH_BOX = (By.XPATH, '//input[contains(@class,"form-control ng-pristine ng-valid ng-touched")]')
    LOGIN_FORM = (By.XPATH, '//form[contains(@class,"auth-signin")]')
    REGISTER_FORM = (By.XPATH, '//form[contains(@class,"auth-register")]')
    FORGOT_PASSWORD_FORM = (By.XPATH, '//form[contains(@class,"password-reset")]')
    MENU_ITEM_EXPLORE = (By.XPATH, '//a[contains(@href,"/explore")]')
    NOTIFICATION_SETTINGS = (By.XPATH, '//a[contains(@href,"/settings/notifications")]')