from selene.support.shared import browser
from selene import by, be, have
import time


def test_bambleby_change_gender():
    browser.open("https://app.neapro.site")
    browser.element("input[type='text']").type("marina.r999@yandex.ru")
    browser.element("input[type='password']").type("01071964mama")
    browser.element("//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
    browser.element(".scrollmenu").hover()
    browser.element("//*[@id='__layout']/div/div[1]/div/div[1]/div[2]/a/div").click()
    browser.element(".name").should(have.text("Луговская Марина"))
    browser.element(by.id("vs1__combobox")).click()
    browser.element(by.id("vs1__option-2")).click()
    browser.element(".scrollmenu").hover()
    browser.element(".logout_name").click()





time.sleep(5)
