from selenium import webdriver
import time
browser = webdriver.Chrome() #괄호안에는 경로명 지금은 같은폴더에 있으므로 생략

#1.네이버로 이동
browser.get("http://naver.com")

#2.로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3.id, pw입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#4.로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)


#5.아이디 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#6.html정보 출력
print(browser.page_source)

#7.브라우저 종료
# browser.close() #현재 탭만 종료
browser.quit() #전체 종료

