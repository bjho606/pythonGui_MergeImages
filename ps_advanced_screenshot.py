# 사용자의 키보드 입력을 통해 원하는 스크린을 캡처할 수 있는 프로그램
import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save(r"C:\JB\Coding\Python\Practice\inflearn_lecture\resources\image{}.png".format(curr_time))   # ex) image_20200601_102030.png

keyboard.add_hotkey("F9", screenshot)               # 사용자가 'F9' 키를 누르면 스크린샷 저장
# keyboard.add_hotkey("ctrl+shift+s", screenshot)   # 이렇게 복합적인 키도 가능

keyboard.wait("esc")                                # 사용자가 'esc'를 누를 때까지 프로그램 수행