from .decorator_functions import *
from allure_commons.types import Severity


@allure.tag('GitHub')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'K1rMac')
@allure.feature("Issue in repository decorator_version")
@allure.story('Find issue: Issue for HW qa.guru')
@allure.link('https://github.com', name='Testing')
def test_github_allure_decorator():
    open_main_page()
    search_for_repository(repository)
    go_to_repository(repository)
    open_issue_tab()
    should_be_issue_with_name(issue_name)
