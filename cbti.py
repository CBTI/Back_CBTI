#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyrebase4


# In[2]:


from pyrebase import pyrebase


# In[3]:


pip install pyrebase4


# In[4]:


import pyrebase


# In[5]:


config = {
  "apiKey": "AIzaSyAVwr-sPn0QJs1COqzf-UWPu3cf2oVbkNQ",
  "authDomain": "psychological-server.firebaseapp.com",
  "databaseURL": "https://psychological-server-default-rtdb.firebaseio.com/",
  "projectId": "psychological-server",
  "storageBucket": "psychological-server.appspot.com",
  "messagingSenderId": "161316158562",
  "appId": "1:161316158562:web:339d81f51b6e268470a53b"
}


# In[6]:


firebase = pyrebase.initialize_app(config)


# In[7]:


firebase


# In[8]:


pip install firebase_admin


# In[3]:


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# In[17]:


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


# In[18]:


firebase = pyrebase.initialize_app(config)
fb_db = firebase.database()
user_info = {
    "USER_ID" : "아이디" "중복불가",
    "USER_PW" : "패스워드",
    "USER_NM" : "유저명" " 및 " "닉네임",
    "USER_TP" : "유저타입"  "  " "A = AUTHOR" " " "D = DEVELPOER",
    "REG_DT" : "가입일자"
}

ref = db.reference()


# In[13]:


ref = db.reference('회원정보')
ref.update({"USER_ID" : "아이디" "중복불가",
    "USER_PW" : "패스워드",
    "USER_NM" : "유저명" " 및 " "닉네임",
    "USER_TP" : "유저타입"  "  " "A = AUTHOR" " " "D = DEVELPOER",
    "REG_DT" : "가입일자"})


# In[16]:


ref = db.reference('심리테스트')
ref.update({
    "TEST_NO" : "중복불가",
    "TEST_DESC" : "테스트 설명",
    "TEST_AUTHOR" : "작가명",
    "RELEASE_DATE" : "출시일"
})


# In[17]:


import uuid
print(uuid.uuid4())


# In[21]:


ref = db.reference('심리테스트 결과')
ref.update({
    "UUID" : "f5d09742bd8449e6bb61ab4c16e92c76",
    "RES_CD" : "결과" "  " "ex) ISTJ - 0 INTJ - 1 이런식으로 코드 매겨서 저장",
    "START_TM" : "시작시간" "  " "시작버튼 누를때 체크", 
    "END_TM" : "종료시간" "  "  "종료버튼 누를때 체크",
    "TEST_YN" : "완료여부"  "  "  "최초 시작버튼 누를땐 N, 결과버튼 누를시 Y ",
    "TEST_NO" : "테스트 번호"
})


# In[12]:


ref = db.reference("회원정보")
ref.push({
    'id' : 'user1', 
    'password' : 'pw11'
})


# In[14]:


# push 하면 고유id와 함께 데이터 삽입
# ref = db.reference("회원정보")
# ref.push({
#     'id' : 'user2', 
#     'password' : 'pw22'
# })
# ref.push({
#     'id' : 'user3', 
#     'password' : 'pw33'
# })


# In[22]:


users = db.reference("회원정보")


# In[ ]:




