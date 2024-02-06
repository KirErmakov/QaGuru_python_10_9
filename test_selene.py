from selene import browser, by, be
from selene.support.shared.jquery_style import s



def test_github():
    browser.open("https://github.com")

    s(".search-input").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.text("Issue for HW qa.guru")).should(be.visible)
