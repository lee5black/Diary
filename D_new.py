'''
새로운 일기장 생성 후 쓰기 모듈

1. 입력받은 이름으로 일기장 생성
2. 일기 내용을 입력 받는다
3. 저장한다

'''

import os

filelist = os.listdir('.')

txtfile = []

for listname in filelist:
    if ".txt" in listname :
        list =""
        list += listname
        print (list)
        txtfile += [list]

print (txtfile)
print (txtfile[0])




