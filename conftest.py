import pytest
from selenium.webdriver import Firefox
import psycopg2
from selenium.webdriver import FirefoxOptions


@pytest.fixture(scope='session')
def driver():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = Firefox(options=opts)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def connect_to_db():
    connection = psycopg2.connect(dbname='postgres', user='postgres',
                                  password='postgres', host='localhost')
    db_session = connection.cursor()
    yield db_session
    connection.close()
