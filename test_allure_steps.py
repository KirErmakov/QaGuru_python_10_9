from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s
import allure


@allure.tag('GitHub')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'K1rMac')
@allure.feature("Issue in repository steps_version")
@allure.story('Find issue: Issue for HW qa.guru')
@allure.link('https://github.com', name='Testing')
def test_github_allure_steps():

    with allure.step("Открыть главную страницу"):
        browser.open("/")

    with allure.step("Bыполнить поиск репозитория"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    with allure.step("Перейти на страницу репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Перейти в раздел Issues"):
        s("#issues-tab").click()

    with allure.step("Проверить наличие Issue на странице"):
        s(by.text("Issue for HW qa.guru")).should(be.visible)
