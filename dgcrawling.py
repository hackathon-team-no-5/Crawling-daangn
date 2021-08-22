from selenium import webdriver
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# driver = webdriver.Chrome((executable_path= r'/Users/hyungjucha/PycharmProjects/202002/chromedriver')
driver.get('https://www.daangn.com/search/%EB%AA%85%ED%92%88')
bb2 = []
dataset = []
time.sleep(2)

for l in range(1,5):
    tag = driver.find_elements_by_xpath('//*[@id="flea-market-wrap"]/article')
    bb2 = tag
    time.sleep(2)
    
    for i in range(len(bb2)):
        dataset.append(bb2[i].text)

    if l % 10 == 0:
        c10 = driver.find_element_by_link_text('더보기')
        c10.click()
    else:
        a = str(l+1)
        c = driver.find_element_by_link_text(a)
        c.click()
    time.sleep(2)

driver.quit()


data = len(dataset)-1
while data >= 0:
    if data % 2 == 1:
        del dataset[data]
    data-=1
print(dataset[:30])
