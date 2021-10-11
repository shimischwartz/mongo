import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MongoObjects:

    def __init__(self):
        self.chrome_options = Options()
        self.edge_options = Options()
        self.driver1 = webdriver.Chrome(options=self.chrome_options)
        self.driver2 = webdriver.Chrome(options=self.chrome_options)
        self.objects = dict()
        self.open_page()
        self.open_mongo_page()
        self.set_elements()

    def open_page(self):
        self.driver1.get("http://localhost:3000/")

    def open_mongo_page(self):
        self.driver2.get("http://localhost:8080/db/my-db/users")

    def get_browser(self):
        return "chrome"

    def set_elements(self):
        self.objects["edit_profile"] = self.driver1.find_element_by_xpath('//*[@id="container"]/button').click()
        self.objects["name"] = self.driver1.find_element_by_xpath('//*[@id="input-name"]')
        self.objects["mail"] = self.driver1.find_element_by_xpath('//*[@id="input-email"]')
        self.objects["interests"] = self.driver1.find_element_by_xpath('//*[@id="input-interests"]')
        self.objects["update_profile"] = self.driver1.find_element_by_xpath('//*[@id="container-edit"]/button')
        self.objects["mongo_name"] = self.driver2.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[4]/table/tbody/tr/td[5]')
        self.objects["mongo_mail"] = self.driver2.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[4]/table/tbody/tr/td[3]')
        self.objects["mongo_interests"] = self.driver2.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[4]/table/tbody/tr/td[4]')

    def change_name(self, name):
        time.sleep(2)
        self.objects["name"].clear()
        self.objects["name"].send_keys(name)
        time.sleep(2)

    def change_mail(self, mail):
        time.sleep(2)
        self.objects["mail"].clear()
        self.objects["mail"].send_keys(mail)
        time.sleep(2)

    def update(self):
        self.objects["update_profile"].click()
        time.sleep(2)

    def change_interests(self, interests):
        time.sleep(2)
        self.objects["interests"].clear()
        self.objects["interests"].send_keys(interests)
        time.sleep(2)

    def close_drivers(self):
        self.driver1.close()
        self.driver2.close()

    def get_name_from_mongo(self):
        return self.objects["mongo_name"].text

    def get_mail_from_mongo(self):
        return self.objects["mongo_mail"].text

    def get_interests_from_mongo(self):
        return self.objects["mongo_interests"].text
