import json

from bot import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", '--data', dest="data")
(start_options, args) = parser.parse_args()

data = json.loads(start_options.data)

bot = Bot()
bot.driver.get(bot.base_url + '/login.php')
WebDriverWait(bot.driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#pun-main .formal>#login"))
)
form = bot.driver.find_element(By.CSS_SELECTOR, "#pun-main .formal>#login")
form.find_element(By.ID, "fld1").send_keys(data['username'])
form.find_element(By.ID, "fld2").send_keys(data['password'])
form.find_element(By.NAME, "login").click()
WebDriverWait(bot.driver, 5).until(
    EC.presence_of_element_located((By.ID, "navlogout"))
)

bot.driver.close()
bot.driver.quit()