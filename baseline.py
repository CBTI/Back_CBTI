#pip install pyrebase4
#pip install firebase_admin
# 위에 먼저 실행

from pyrebase import pyrebase
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

config = {
  "apiKey": "AIzaSyAVwr-sPn0QJs1COqzf-UWPu3cf2oVbkNQ",
  "authDomain": "psychological-server.firebaseapp.com",
  "databaseURL": "https://psychological-server-default-rtdb.firebaseio.com/",
  "projectId": "psychological-server",
  "storageBucket": "psychological-server.appspot.com",
  "messagingSenderId": "161316158562",
  "appId": "1:161316158562:web:339d81f51b6e268470a53b"
}
firebase = pyrebase.initialize_app(config)

# test
db_url = "https://psychological-server-default-rtdb.firebaseio.com/"

config = {
  "apiKey": "AIzaSyAVwr-sPn0QJs1COqzf-UWPu3cf2oVbkNQ",
  "authDomain": "psychological-server.firebaseapp.com",
  "databaseURL": "https://psychological-server-default-rtdb.firebaseio.com/",
  "projectId": "psychological-server",
  "storageBucket": "psychological-server.appspot.com",
  "messagingSenderId": "161316158562",
  "appId": "1:161316158562:web:339d81f51b6e268470a53b"
}

# 인증 및 앱 초기화
cred = credentials.Certificate("CBTI_Key.json")
firebase_admin.initialize_app(cred,
                             {'databaseURL' : db_url})

'''
# 여긴 UUID 부분인데 실행 안하셔도 됩니다.
import uuid
#print(uuid.uuid4())
ref = db.reference('심리테스트 결과')
ref.update({
    "UUID" : "f5d09742bd8449e6bb61ab4c16e92c76",
    "RES_CD" : "결과" "  " "ex) ISTJ - 0 INTJ - 1 이런식으로 코드 매겨서 저장",
    "START_TM" : "시작시간" "  " "시작버튼 누를때 체크", 
    "END_TM" : "종료시간" "  "  "종료버튼 누를때 체크",
    "TEST_YN" : "완료여부"  "  "  "최초 시작버튼 누를땐 N, 결과버튼 누를시 Y ",
    "TEST_NO" : "테스트 번호"
})
'''
