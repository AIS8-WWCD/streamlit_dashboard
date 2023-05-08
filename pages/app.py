import streamlit as st
import pandas as pd
from PIL import Image
from PyPDF2 import PdfFileReader
import matplotlib.pyplot as plt
import plotly.express as px
import os

st.set_page_config(page_title="BattleGround_Final", page_icon=":guardsman:", layout="wide")
st.title(':scroll: 배틀그라운드: 초보자 가이드 :scroll:')
st.header('WWCD 초보자 가이드에 오신 것을 환영합니다! :sparkles:')
st.markdown(' ')
st.markdown(' ')

# 마크다운 문법 지원
# 컬러코드: blue, green, orange, red, violet
st.markdown(' **PUBG 글로벌 시리즈의 그 첫 번째 대회, PGS 1**이 동남아시아의 중심, 말레이시아, 쿠알라룸푸르에서 개최되었습니다!')
st.markdown(" PGS 1은 4월 27일부터 5월 7일까지의 일정으로 진행되며, 그룹 스테이지, 승자/패자 브래킷 그리고 그랜드 파이널까지의 여정으로 구성되어 있는데요,")
st.markdown(' PGS 1은 총 24개의 탑 티어 글로벌 팀들이 Battle Arena Malaysia 경기장에 모여 총상금 $500,000을 놓고 격돌하게 됩니다!')
st.markdown(' 경기에서 진행될 맵은 에란겔과 미라마, 두 개의 맵입니다.')
st.markdown(" 4월 27일부터 29일까지의 총 18번의 경기에서 얻어온 70만 개가 넘는 다양한 로그 데이터를 분석하여 신규 유저분들에게 도움이 되고자, PGS 1에서 얻은 바탕으로 초보자 가이드를 만들어 보았습니다.")
st.markdown(' 초보자 가이드로 쓰일 만한 내용들을 많이 추가해야할 듯하다! ! ! ! 아 건님거랑 합치면 되겠다')
st.markdown(' ')
st.markdown(' ')
# Subheader 적용
st.subheader(':mag: 선수들이 가장 많이 사용했던 이것은?')

# 데이터 불러오기
df_use_gun = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_use_gun.csv")
df_handgun_weapon = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_handgun_weapon.csv")
df_throwable_weapon = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_throwable_weapon.csv")
df_parts_value = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_parts_value.csv")
df_upper = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_upper.csv")
df_Muzzle = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_Muzzle.csv")
df_Stock = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_Stock.csv")
df_Lower = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_Lower.csv")
df_Magazine = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_Magazine.csv")

df_move_distance_mean = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_move_distance_mean.csv")
df_survive_mean = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/pages/df_survive_mean.csv")


# 선택 박스
pick = st.selectbox(
    ' 공식 경기에서 선수들이 가장 많이 사용했던 **이것**은? 원하시는 선택지를 골라주세요! 추가로 이에 관련된 무기 정보들 더 넣기',
    ("선택해주세요", '총기류', '보조무기', "투척무기", "총구", "탄창",  '손잡이', "파츠", "조준선", "스톡"),  index=0)
if pick == '총기류':
    st.write('선수들이 가장 많이 사용했던 **총기류**는 무엇일까요?')
    fig = px.bar(df_use_gun.set_index("index").sort_values("itemId"), orientation='h', color=df_use_gun["itemId"][::-1], color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '보조무기':
    df_handgun_weapon["index"] = df_handgun_weapon["index"].str.replace("Item_Weapon_", repl=r'', regex=True)
    df_handgun_weapon["index"] = df_handgun_weapon["index"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_handgun_weapon.set_index("index"), color=df_handgun_weapon["itemId"], color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '투척무기':
    st.write('선수들이 가장 많이 사용했던 **투척y무기**는 무엇일까요?')
    df_throwable_weapon["index"] = df_throwable_weapon["index"].str.replace("Item_Weapon_", repl=r'', regex=True)
    df_throwable_weapon["index"] = df_throwable_weapon["index"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_throwable_weapon.set_index("index"), color=df_throwable_weapon["itemId"], color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)    
elif pick == '총구':
    st.write('선수들이 가장 많이 사용했던 **총구**는 무엇일까요?')
    df_Muzzle["index"] = df_Muzzle["index"].str.replace("Item_Attach_Weapon_Muzzle_", repl=r'', regex=True)
    df_Muzzle["index"] = df_Muzzle["index"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Muzzle.set_index("index").sort_values(by="itemId"), orientation='h', color=df_Muzzle["itemId"][::-1] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '탄창':
    st.write('선수들이 가장 많이 사용했던 **탄창**은 무엇일까요?')
    df_Magazine["index"] = df_Magazine["index"].str.replace("Item_Attach_Weapon_Magazine_", repl=r'', regex=True)
    df_Magazine["index"] = df_Magazine["index"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Magazine.set_index("index").sort_values(by="itemId"), orientation='h', color=df_Magazine["itemId"][::-1] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '손잡이':
    st.write('선수들이 가장 많이 사용했던 **손잡이**는 무엇일까요?')
    df_Lower["index"] = df_Lower["index"].str.replace("Item_Attach_Weapon_Lower_", repl=r'', regex=True)
    df_Lower["index"] = df_Lower["index"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Lower.set_index("index"), color=df_Lower["itemId"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '파츠':
    st.write('선수들이 가장 많이 사용했던 **파츠**는 무엇일까요?')
    fig = px.bar(df_parts_value, x="index", y="parts", color=df_parts_value["parts"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '조준선':
    st.write('선수들이 가장 많이 사용했던 **조준선**은 무엇일까요?')
    df_upper["index"] = df_upper["index"].str.replace("Item_Attach_Weapon_Upper_", repl=r'', regex=True)
    df_upper["index"] = df_upper["index"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_upper.set_index("index"), color=df_upper["itemId"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == "스톡":
    st.write('선수들이 가장 많이 사용했던 **스톡**은 무엇일까요?')
    df_Stock["index"] = df_Stock["index"].str.replace("Item_Attach_Weapon_Stock_", repl=r'', regex=True)
    df_Stock["index"] = df_Stock["index"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Stock.set_index("index"), color=df_Stock["itemId"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
else:
     st.write(" ")

st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.subheader(':mag: 선수들의 평균 생존 시간은?')
st.write('4월 27일부터 4월 29일까지 24개팀의 전체 선수들의 평균 생존 시간입니다.')
st.caption('그래프 특성상 x축에 99명의 전체 선수의 이름이 표시되지 않았습니다.. 이 부분은 사진 첨부 말고 코드를 넣어서 직접 그래프를 짜보는 게 어떨까 ')
fig = px.bar(df_survive_mean.sort_values('timeSurvived', ascending=False), x="name", y = 'timeSurvived')
fig.update_layout(width=1000, height=500)
st.plotly_chart(fig)
# img = Image.open(r"C:\Users\wldus\OneDrive\바탕 화면\pythonworkspace\final_project\image\전체선수_평균생존시간.png")
# st.image(img, width=1000)

st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.subheader(':mag: 선수들의 평균 이동 거리는?')
st.write('4월 27일부터 4월 29일까지 24개팀의 전체 선수들의 평균 이동 거리입니다.')
st.caption('그래프 특성상 x축에 99명의 전체 선수의 이름이 표시되지 않았습니다.. 이 부분은 사진 첨부 말고 코드를 넣어서 직접 그래프를 짜보는 게 어떨까 ')
fig = px.bar(df_move_distance_mean.sort_values(by="평균거리", ascending=False), x="name", y = ["주행거리", "도보거리", "수영거리"], )
fig.update_layout(width=1000, height=500)
st.plotly_chart(fig)

