from selene import browser, by, be
from selene.support.shared.jquery_style import s
import allure


repository = "eroshenkoam/allure-example"
issue_name = "Issue for HW qa.guru"


@allure.step("Открыть главную страницу")
def open_main_page():
    browser.open("/")


@allure.step("Bыполнить поиск репозитория {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Перейти на страницу репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Перейти в раздел Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверить наличие Issue c именем {name} на странице")
def should_be_issue_with_name(name):
    s(by.text(name)).should(be.visible)
