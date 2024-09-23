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

bot.driver.get(bot.base_url + '/profile.php?section=fields&id='+data['id'])
WebDriverWait(bot.driver, 5).until( EC.presence_of_element_located((By.ID, "profile8")))
form = bot.driver.find_element(By.ID, "profile8")
for datum in data['update']:
    field = form.find_element(By.ID, datum['field_name'])
    bot.driver.execute_script("arguments[0].value = arguments[1]", field, datum['value'])
    #form.find_element(By.ID, datum['field_name']).send_keys(datum['value'])
form.find_element(By.NAME, "update").click()

bot.driver.close()
bot.driver.quit()
