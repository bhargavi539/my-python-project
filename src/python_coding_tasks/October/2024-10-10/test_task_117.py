import pytest
import requests

def test_selenium(launch_chrome,close_chrome):
    launch_chrome
    print("executing the test cases...")
    close_chrome