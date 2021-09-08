from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import contextlib
import time


@contextlib.contextmanager
def chrome_connect(path, url, headless):
    # Set up a database connection
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(path, options=options)
    driver.get(url)
    try:
        yield driver
    except Exception as e:
        print(e)
    finally:
        # Close the connection
        driver.quit()


class DataSourceMgr:

    def __init__(self, path="./chromedriver_win32/chromedriver.exe",
                 url="https://www.viennaairport.com/passagiere/ankunft__abflug/abfluege",
                 headless=True) -> None:
        self.path = path
        self.url = url
        self.headless = headless
        self.datas = []
        self.date = ""

    def getDatasFromTable(self):
        with chrome_connect(self.path, self.url, self.headless) as driver:
            # first popup accept cookies.
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()

            # wait till get table body
            table_body = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.CLASS_NAME, "fd-detail-rows")))
            # expand table body
            driver.execute_script("$.flugdaten.getAll();")

            # get all rows from table
            rows = table_body.find_elements_by_class_name('detail-table__row')
            for row in rows:
                if row.get_attribute('class') == 'detail-table__row newdate':
                    self.date = row.text
                else:
                    cells = row.find_elements_by_class_name(
                        'detail-table__cell')
                    if len(cells) != 8:
                        continue
                    item = [self.date]
                    for cell in cells:
                        item.append(cell.text)
                    self.datas.append(item)


A = DataSourceMgr(headless=True)

A.getDatasFromTable()
print(len(A.datas))
