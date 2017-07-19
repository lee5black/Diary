'''
Diary - ver 1.0
 2017 - 07 - 07 시작
 개인용 일기장 프로그램

 1. 일기장 쓰기와 읽기 기능 구현

 D_pro 는 각 모듈을 실행
'''

#import D_new   # 일기장 신규 작성
#import D_read  # 일기장 조회

while True:
    print ("="*50)
    print ("""
    개인 일기장 프로그램 ver.1

    1.일기 쓰기
    2.일기 보기
    3.종료
    """)
    print ("="*50)
    us = int(input("메뉴를 선택하세요: ")) # us = (user select)

    if us==1 :
        title = input("일기장 이름: ")
        if(title):
            filename = title + '.txt'
            f = open(filename,"w")
            content = input("today : ")
            f.write(content)
        else:
            break

    elif us==2 :

        import os

        filelist = os.listdir('.')
        txtfile = []

        for listname in filelist:
            if ".txt" in listname :
                list =""
                list += listname
                txtfile += [list]

        print ("현재 작성되어 있는 일기: \n ")
        print (txtfile)

        title =input("열람하실 일기장 제목: ")
        filename = title + '.txt'

        f = open(filename,"r")
        data = f.read()
        print ("*"*50)
        print ("today : " +data)
        print ("*"*50)
        f.close()

    else:
        break





