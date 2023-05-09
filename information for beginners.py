import streamlit as st
import pandas as pd
from PIL import Image
# from PyPDF2 import PdfFileReader
import matplotlib.pyplot as plt
import plotly.express as px
import os

st.set_page_config(page_title="BattleGround_Final", page_icon=":guardsman:", layout="wide")
st.title(':scroll: 배틀그라운드: 초보자 꿀 정보 :scroll:')
st.header('WWCD 초보자 꿀 정보 오신 것을 환영합니다! :sparkles:')
st.markdown(' ')
st.markdown(' ')

# 마크다운 문법 지원
# 컬러코드: blue, green, orange, red, violet
st.markdown(' **PUBG 글로벌 시리즈의 그 첫 번째 대회, PGS 1**이 동남아시아의 중심, 말레이시아, 쿠알라룸푸르에서 개최되었습니다!')
st.markdown(" PGS 1은 4월 27일부터 5월 7일까지의 일정으로 진행되며, 그룹 스테이지, 승자/패자 브래킷 그리고 그랜드 파이널까지의 여정으로 구성되어 있는데요,")
st.markdown(' PGS 1은 총 24개의 탑 티어 글로벌 팀들이 Battle Arena Malaysia 경기장에 모여 총상금 $500,000을 놓고 격돌하게 됩니다!')
st.markdown(' 경기에서 진행될 맵은 에란겔과 미라마, 두 개의 맵입니다.')
st.markdown(" 4월 27일부터 29일까지의 총 18번의 경기에서 얻어온 70만 개가 넘는 다양한 로그 데이터를 분석하여 신규 유저분들에게 도움이 되고자, PGS 1에서 얻은 바탕으로 초보자위한 꿀 정보를 만들어 보았습니다.")
st.markdown(' ')
st.markdown(' ')
df_move_distance_mean = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_move_distance_mean.csv")
df_survive_mean = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_survive_mean.csv")
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.markdown(' ')
st.subheader(':mag: 선수들의 평균 생존 시간은?')
st.write('4월 27일부터 4월 29일까지 24개팀의 전체 선수들의 평균 생존 시간입니다.')
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
fig = px.bar(df_move_distance_mean.sort_values(by="평균거리", ascending=False), x="name", y = ["주행거리", "도보거리", "수영거리"], )
fig.update_layout(width=1000, height=500)
st.plotly_chart(fig)
