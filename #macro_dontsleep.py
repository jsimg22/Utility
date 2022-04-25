#macro_test

import pyautogui 

pyautogui.PAUSE = 1 #모든 동작에 SLEEP 적용
#size= pyautogui.size() #active 된 창 크기

#pyautogui.moveTo(100,100) #지정한 위치로 마우스 이동
#pyautogui.moveTo(1000,1000, duration=0.5) # 0.5초 동안 이동
#print(pyautogui.position())

#pyautogui.sleep(3) # dealy
#print(pyautogui.position())

#pyautogui.click(64,17 ,duration=1, clicks=2) #좌표를 클릭 duration=1s동안 이동하면서 클릭 clicks=클릭횟수
#pyautogui.mauseDown() #마우스 누르고 있기
#pyautogui.mauseUp() #마우스 떼기
#pyautogui.rightClick(1000,500) #우클릭
#pyautogui.middleClick() #휠 클릭
#pyautogui.drag(-500,-200 ,duration=1) #현재 마우스 위치 기준으로 이동
#pyautogui.dragTo(700,400 ,duration=1) #현재 위치에서 절대 좌표 타겟으로 
#pyautogui.scroll(300) #입력한 만큼 스크롤 양수는 위 방향

#pixel = pyautogui.pixel(28,18) #좌표의 RGB 가져오기
#print(pixel)
#print(pyautogui.pixelMatchesColor(28,18,(60,60,60))) # 색이 동일한지 확인 (좌표 , (RGB값))

#pyautogui.mouseInfo() 

#CTRL+C 강제 종료

minite = 1 # 몇분

pyautogui.moveTo(1000,500)
for i in range (minite) :
    pyautogui.move(500,0,duration=5)
    pyautogui.moveTo(1000,500)
    pyautogui.move(-500,0,duration=5)
    
