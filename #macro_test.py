#macro_test

import pyautogui 

size= pyautogui.size() #active 된 창 크기

#pyautogui.moveTo(100,100) #지정한 위치로 마우스 이동
#pyautogui.moveTo(1000,1000, duration=0.5) # 0.5초 동안 이동
#print(pyautogui.position())

pyautogui.sleep(3) # dealy
print(pyautogui.position())

pyautogui.click(64,17 ,duration=1, clicks=2) #좌표를 클릭 duration=1s동안 이동하면서 클릭 clicks=클릭횟수
#pyautogui.mauseDown() #마우스 누르고 있기
#pyautogui.mauseUp() #마우스 떼기
pyautogui.rightClick(1000,500)
