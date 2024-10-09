import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_sub1():
    assert 5 - 2 == 3


@pytest.mark.smoke
def test_sub2():
    assert 15 - 12 == 3


@pytest.mark.regression
def test_sub3():
    assert 10 - 2 == 8


@pytest.mark.skip(reason="Not relevant, skip it")
def test_sub4():
    assert 5 - 2 == 2


@pytest.mark.smoke
def test_sub5():
    assert 35 - 25 == 3



@pytest.mark.smoke
def test_sub6():
    assert 15 - 15 == 0


@pytest.mark.smoke
def test_sub7():
    assert 25 - 12 == 3
