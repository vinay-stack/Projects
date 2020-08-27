import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 2hrs

#youtube link
Link:https://youtu.be/Q9Exr2cGLZY
#number of views
views =600

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
