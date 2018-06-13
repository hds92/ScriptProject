
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
import smtplib

from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText


win = tk.Tk()  

       
win.title("Python GUI")  # GUI 프로그램 제목


# api를 이용해 대기오염 정보를 받아옵니다.
def click_me(): 
    scr.delete('1.0', tk.END)
    url="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=X%2BYNKenOMmJGBUE4gnUK489qAi4%2FeRpzojpVqrWPf7eCXgJTRA4AYFYijIsEXzXw24GRK0MT98bCcU%2BHHIqWNw%3D%3D&numOfRows=100&pageSize=100&pageNo=1&startPage=1&sidoName="+str(number_chosen.get())+"&searchCondition=DAILY&_returnType=json"
    req = requests.get(url)
    result=req.json() # 정보를 json 포맷으로 파싱합니다.
    Index=[]
	# GUI 창에서 입력한 도시이름과 같은 json list를 추출합니다.
    for i in range(len(result['list'])):
        if result['list'][i]['cityName'] == number_chosen2.get():
            Index.append(i)
    # scroll text창에 정보를 insert 합니다.
    scr.insert(tk.INSERT,"일산화탄소 : "+"\t")
    scr.insert(tk.INSERT,result['list'][Index[0]]['coValue']+"\n")
    scr.insert(tk.INSERT,"오존 : "+"\t")
    scr.insert(tk.INSERT,result['list'][Index[0]]['o3Value']+"\n")
    scr.insert(tk.INSERT,"이산화질소 : "+"\t")
    scr.insert(tk.INSERT,result['list'][Index[0]]['no2Value']+"\n")
    scr.insert(tk.INSERT,"미세먼지 : "+"\t")
    scr.insert(tk.INSERT,result['list'][Index[0]]['pm10Value']+"\n")
   
# 대기오염 정보를 scroll text창에 insert 합니다.
def click_me2(): 
    scr.delete('1.0', tk.END)
    scr.insert(tk.INSERT,"일산화탄소"+"\n")
    scr.insert(tk.INSERT,"일산화탄소는 무색, 무취의 기체로서 산소가 부족한 상태로 연료가 연소할 때 불완전연소로 발생한다.사람의 폐로 들어가면 혈액 중의 헤모글로빈과 결합하여 산소보급을 가로막아 심한 경우 사망에까지 이르게 한다. 일산화탄소는 연탄의 연소가스나 자동차의 배기가스 중에 많이 포함되어 있으며, 큰 산불이 일어날 때도 주위에 산소가 부족하여 많은 양의 일산화탄소가 발생되기도 하고 담배를 피울 때 담배연기 속에 함유되어 배출되기도 한다."+"\n\n")
    scr.insert(tk.INSERT,"오존"+"\n") 
    scr.insert(tk.INSERT,"특유한 냄새 때문에 ‘냄새를 맡다’를 뜻하는 그리스어 ozein을 따서 명명되었다.인체에 독성이 있어 장시간 흡입하면 호흡기관을 해치므로 주의해야 한다.지상에서 20~25km 고도에 20km 두께로 비교적 농도가 높은 오존이 분포하는데, 이것을 오존층이라고 한다. 이 오존층에서 태양의 자외선을 흡수하기 때문에 지구의 생물은 자외선에 의한 피해를 막을 수 있다."+"\n\n") 
    scr.insert(tk.INSERT,"이산화질소"+"\n") 
    scr.insert(tk.INSERT,"자극성 냄새가 나는 갈색의 유해한 기체로서 과산화질소라고도 한다.연료의 고온 연소 등으로 발생하며, 대기 오염 물질이 된다.장기간 흡입하면 눈과 목에 자극, 가슴의 긴장, 두통, 구역질, 점차적인 무력함이 일어날 수 있다."+"\n\n")
    scr.insert(tk.INSERT,"미세먼지"+"\n") 
    scr.insert(tk.INSERT,"미세먼지는 우리 눈에 보이지 않는 아주 작은 물질로 대기 중에 오랫동안 떠다니거나 흩날려 내려오는 직경 10 μm 이하의 입자상 물질이다.미세먼지에 포함된 중금속, 유기탄화수소, 질산염, 황산염 등은 크기가 매우 작아 호흡기의 깊숙한 곳까지 도달이 가능하며 혈액을 통해 전신으로 순환하면서 우리 신체에 영향을 줄 수 있다."+"\n") 

    
# 두번째 콤보박스창(군/구)를 업데이트하는 함수입니다. 만약 첫번째 콤보박스창에서 서울을 선택했으면 두번째 콤보박스 창에서 서울의 구들을 보여줍니다. 
def TextBoxUpdate():
    if number_chosen.get() == "서울":
        number_chosen2['values'] = string_서울
    elif number_chosen.get() == "부산" :
        number_chosen2['values'] = string_부산
    elif number_chosen.get() == "대구" :
        number_chosen2['values'] = string_대구
    elif number_chosen.get() == "인천" :
        number_chosen2['values'] = string_인천
    elif number_chosen.get() == "광주" :
        number_chosen2['values'] = string_광주
    elif number_chosen.get() == "대전" :
        number_chosen2['values'] = string_대전
    elif number_chosen.get() == "울산" :
        number_chosen2['values'] = string_울산
    elif number_chosen.get() == "경기" :
        number_chosen2['values'] = string_경기
    elif number_chosen.get() == "강원" :
        number_chosen2['values'] = string_강원
    elif number_chosen.get() == "충북" :
        number_chosen2['values'] = string_충북
    elif number_chosen.get() == "충남" :
        number_chosen2['values'] = string_충남
    elif number_chosen.get() == "전북" :
        number_chosen2['values'] = string_전북
    elif number_chosen.get() == "전남" :
        number_chosen2['values'] = string_전남
    elif number_chosen.get() == "경북" :
        number_chosen2['values'] = string_경북
    elif number_chosen.get() == "경남" :
        number_chosen2['values'] = string_경남
    elif number_chosen.get() == "제주" :
        number_chosen2['values'] = string_제주
    elif number_chosen.get() == "세종" :
        number_chosen2['values'] = string_세종

# 지메일 전송하는 함수합니다.        
def gmail():
    usermail = gmail_id.get() # 텍스트 박스에서 아이디를 가져옵니다.
    receivermail=gmail_receiver.get() # 텍스트 박스에서 받는이 계정을 가져옵니다.        
    pass_word=gmail_password.get() # 텍스트 박스에서 비밀번호를 가져옵니다.
   
	# 대기오염 정보를 파싱, 추출합니다.
    url="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=X%2BYNKenOMmJGBUE4gnUK489qAi4%2FeRpzojpVqrWPf7eCXgJTRA4AYFYijIsEXzXw24GRK0MT98bCcU%2BHHIqWNw%3D%3D&numOfRows=100&pageSize=100&pageNo=1&startPage=1&sidoName="+str(number_chosen.get())+"&searchCondition=DAILY&_returnType=json"
    req = requests.get(url)
    result=req.json()
    Index=[]
    for i in range(len(result['list'])):
        if result['list'][i]['cityName'] == number_chosen2.get():
            Index.append(i)

    # 대기오염정보를 이어 붙입니다.
    main_message = number_chosen.get() + "\t" + number_chosen2.get() + "\n\n" + "일산화탄소 : " + "\t" + \
                   result['list'][Index[0]]['coValue'] + "\n" "오존 : " + "\t" + result['list'][Index[0]][
                       'o3Value'] + "\n" + "이산화질소 : " + "\t" + result['list'][Index[0]][
                       'no2Value'] + "\n" + "미세먼지 : " + "\t" + result['list'][Index[0]]['pm10Value'] + "\n"

    msg=MIMEMultipart('alternative')
    msg['From'] = usermail 
    msg['To'] = receivermail 
    msg['Subject'] = 'Sending email with environment information' # 제목 
    msg.attach(MIMEText(main_message, 'plain', 'utf-8')) # 메일 내용


    
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(usermail, pass_word  ) #로그인
    server.sendmail(usermail,receivermail, msg.as_string() ) # 전송
    server.quit()
    
    

action = ttk.Button(win, text="실시간조회", command=click_me) # 실시간 조회 버튼입니다. click_me를 시행합니다.
action.grid(column=0, row=0)                                
action2 = ttk.Button(win, text="대기오염정의", command=click_me2)   # 대기오염정의 버튼입니다. click_me2를 시행합니다.
action2.grid(column=1, row=0)      

ttk.Label(win, text="지메일 계정:").grid(column=2, row=0) 

# 아이디 입력하는 텍스트 엔트리를 생성합니다.
gmail_id = tk.StringVar()
gmail_id_entered = ttk.Entry(win,width=17,textvariable=gmail_id) 
gmail_id_entered.grid(column=2, row=1)

ttk.Label(win, text="비밀번호:").grid(column=2, row=2)

# 비밀번호 입력하는 텍스트 엔트리를 생성합니다.
gmail_password = tk.StringVar()
gmail_password_entered = ttk.Entry(win,width=17,textvariable=gmail_password) 
gmail_password_entered.grid(column=2, row=3)

ttk.Label(win, text="받는이:").grid(column=3, row=0)

# 보내는이 메일 계정을 입력하는 텍스트 엔트리를 생성합니다.
gmail_receiver = tk.StringVar()
gmail_receiver_entered = ttk.Entry(win,width=17,textvariable=gmail_receiver) 
gmail_receiver_entered.grid(column=3, row=1)


action3 = ttk.Button(win, text="이메일전송", command=gmail)   
action3.grid(column=3, row=2,rowspan=2,ipady=10, ipadx=10)      


# 첫번째 콤보박스 창을 정의합니다.
ttk.Label(win, text="도시선택:").grid(column=0, row=1)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = ("서울","부산","대구","인천","광주","대전","울산","경기","강원","충북","충남","전북","전남","경북","경남","제주","세종")
number_chosen.grid(column=0, row=2)

# 두번째 콤보박스 창을 정의합니다.
ttk.Label(win, text="군/구 선택:").grid(column=1, row=1)
number2 = tk.StringVar()
number_chosen2 = ttk.Combobox(win, width=12, textvariable=number2, state='readonly',postcommand =TextBoxUpdate)
string_서울 = ('종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구')
string_부산 = ('중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구', '기장군')
string_대구 = ('중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군')
string_인천 = ('중구', '동구', '남구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군')
string_광주 = ('동구', '서구', '남구', '북구', '광산구')
string_대전 = ('동구', '중구', '서구', '유성구', '대덕구')
string_울산 = ('중구', '남구', '동구', '북구', '울주군')
string_경기 = ("수원시","성남시","의정부시","안양시","부천시","광명시","평택시","동두천시","안산시","고양시","과천시","구리시","남양주시", "오산시","시흥시","군포시","의왕시","하남시","용인시","파주시","이천시","안성시","김포시","화성시","광주시","양주시","포천시","여주시","연천군","가평군","양평군")
string_강원 = ('춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군')
string_충북 = ('청주시', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군', '음성군', '단양군')
string_충남 = ('천안시', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군')
string_전북 = ('전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군')
string_전남 = ('목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군')
string_경북 = ('포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군')
string_경남 = ('창원시', '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군')
string_제주 = ('제주시','서귀포시')
string_세종 = ('세종시')

number_chosen2.grid(column=1, row=2)


# 스크롤 텍스트장을 만급니다. 창의 크기를 지정해줍니다.    
scrol_w  = 70
scrol_h  =  20
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, sticky="W")


win.mainloop()

