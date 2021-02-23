import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog      # filedialog 는 서브모듈이기 때문에 자동으로 import 해주지 않기 때문에 별도로 명시해줘야함 (ex. __all__)

root = Tk()
root.title("My GUI")
root.resizable(False, False)

# 파일추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"),("모든 파일", "*.*")),\
        initialdir=r"C:\JB\Coding\Python\Practice\inflearn_lecture\resources")   # 최초에 C:/JB/ 경로를 보여줌
                    # r"..." : 기존 '//' 나 '/' 로 바꾸지 않아도 경로를 그대로(사용자가 최초로 지정한 경로) 쓸수 있다.

    # 사용자가 선택한 파일 목록
    for file in files:
        # print(file)
        list_file.insert(END, file)

# 선택삭제
def del_file():
    # print(list_file.curselection())   # index를 반환한다
    # 리스트에 있는 목록을 삭제할 때는 앞에서부터 지우면 index가 앞으로 땡겨오면서 값이 변하기 때문에 뒤에서부터 지운다!
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:     # 사용자가 취소를 누를 때
        return
    # print(folder_selected)
    text_dest_path.delete(0, END)
    text_dest_path.insert(0, folder_selected)

# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    # 저장 경로 확인
    if len(text_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=10, text="파일추가", command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=10, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

text_dest_path = Entry(path_frame)
text_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
    # 가로 넓이 레이블
lbl_width = Label(option_frame, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)
    # 가로 넓이 콤보박스
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
    # 간격 옵션 레이블
lbl_space = Label(option_frame, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)
    # 간격 옵션 콤보박스
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
    # 파일 포맷 옵션 레이블
lbl_format = Label(option_frame, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)
    # 파일 포맷 옵션 콤보박스
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Progress Bar
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progressbar.pack(fill='x', padx=5, pady=5)

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close=Button(run_frame, padx=5, pady=5, text="닫기", width=10, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start=Button(run_frame, padx=5, pady=5, text="시작", width=10, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()