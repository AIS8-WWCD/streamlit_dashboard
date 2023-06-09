import streamlit as st
import pandas as pd
from PIL import Image
# from PyPDF2 import PdfFileReader
import matplotlib.pyplot as plt
import plotly.express as px
import os


# Subheader 적용
st.subheader(':mag: 선수들이 가장 많이 사용했던 이것은?')

# 데이터 불러오기
df_use_gun = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_use_gun.csv")
df_handgun_weapon = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_handgun_weapon.csv")
df_parts_value = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_parts_value.csv")
df_upper = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_upper.csv")
df_Muzzle = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_Muzzle.csv")
df_Stock = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_Stock.csv")
df_Lower = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_Lower.csv")
df_Magazine = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_Magazine.csv")

df_move_distance_mean = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_move_distance_mean.csv")
df_survive_mean = pd.read_csv("https://raw.githubusercontent.com/AIS8-WWCD/streamlit_dashboard/main/pages/df_survive_mean.csv")

translation_dict = {
    'Item_Weapon_Sawnoff_C': '소드오프',
    'Item_Weapon_NagantM1895_C': '리볼버',
    'Item_Weapon_M9_C': 'p92',
    'Item_Weapon_M1911_C': 'p1911',
    'Item_Weapon_G18_C': 'p18c'
}

df_handgun_weapon['index'] = df_handgun_weapon['index'].map(translation_dict)

translation_dict = {
    'Upper': '상단 부착물',
    'Magazine': '탄창 부착물',
    'Muzzle': '총구 부착물',
    'Lower': '하부 부착물',
    'Stock': '개머리판 부착물'
}

df_parts_value['index'] = df_parts_value['index'].map(translation_dict)

translation_dict = {
    'Item_Attach_Weapon_Upper_DotSight_01_C':'레드 도트 사이트',
    'Item_Attach_Weapon_Upper_Scope3x_C':'3배율 스코프',
    'Item_Attach_Weapon_Upper_ACOG_01_C':'4배율 (ACOG) 스코프',
    'Item_Attach_Weapon_Upper_Scope6x_C':'6배율 스코프',
    'Item_Attach_Weapon_Upper_Aimpoint_C':'2배율 스코프'
}

df_upper['index'] = df_upper['index'].map(translation_dict)

translation_dict = {
    'Item_Attach_Weapon_Muzzle_FlashHider_Large_C':'AR용 소염기(DMR 공용)',
    'Item_Attach_Weapon_Muzzle_Compensator_Large_C':'AR용 보정기(DMR 공용)',
    'Item_Attach_Weapon_Muzzle_Compensator_SniperRifle_C':'SR용 보정기(DMR 공용)',
    'Item_Attach_Weapon_Muzzle_Suppressor_Large_C':'AR용 소음기(DMR 공용)',
    'Item_Attach_Weapon_Muzzle_FlashHider_SniperRifle_C':'SR용 소염기(DMR 공용)'
}

df_Muzzle['index'] = df_Muzzle['index'].map(translation_dict)

translation_dict = {
    'Item_Attach_Weapon_Stock_AR_Composite_C': '전술 개머리판',
    'Item_Attach_Weapon_Stock_SniperRifle_CheekPad_C': '칙패드',
    'Item_Attach_Weapon_Stock_SniperRifle_BulletLoops_C': '탄띠',
    'Item_Attach_Weapon_Stock_UZI_C': '접이식 개머리판'
}

df_Stock['index'] = df_Stock['index'].map(translation_dict)

translation_dict = {
    'Item_Attach_Weapon_Lower_Foregrip_C': '수직손잡이',
    'Item_Attach_Weapon_Lower_HalfGrip_C': '하프 그립',
    'Item_Attach_Weapon_Lower_ThumbGrip_C': '엄지 그립',
    'Item_Attach_Weapon_Lower_LightweightForeGrip_C': '라이트 그립',
    'Item_Attach_Weapon_Lower_AngledForeGrip_C': '앵글 손잡이'
}

df_Lower['index'] = df_Lower['index'].map(translation_dict)

translation_dict = {
    'Item_Attach_Weapon_Magazine_Extended_Large_C': '대용량 탄창',
    'Item_Attach_Weapon_Magazine_QuickDraw_Large_C': '퀵드로우 대용량 탄창',
    'Item_Attach_Weapon_Magazine_ExtendedQuickDraw_Large_C': '대용량 퀵드로우 탄창',
    'Item_Attach_Weapon_Magazine_Extended_SniperRifle_C': '저격소총용 대용량 탄창',
    'Item_Attach_Weapon_Magazine_Extended_Medium_C': 'SMG 대용량 탄창'
}

df_Magazine['index'] = df_Magazine['index'].map(translation_dict)

df_use_gun = df_use_gun.rename(columns = {"index" : "총 이름","itemId":"개수"})

df_handgun_weapon = df_handgun_weapon.rename(columns = {"index" : "보조무기 이름","itemId":"개수"})

df_parts_value = df_parts_value.rename(columns = {"index" : "총기 부착물","parts":"개수"})

df_upper = df_upper.rename(columns = {"index" : "조준경","itemId":"개수"})

df_Muzzle = df_Muzzle.rename(columns = {"index" : "총구","itemId":"개수"})

df_Stock = df_Stock.rename(columns = {"index" : "개머리판","itemId":"개수"})

df_Lower = df_Lower.rename(columns = {"index" : "손잡이","itemId":"개수"})

df_Magazine = df_Magazine.rename(columns = {"index" : "탄창","itemId":"개수"})


# 선택 박스
pick = st.selectbox(
    ' 공식 경기에서 선수들이 가장 많이 사용했던 **이것**은? 원하시는 선택지를 골라주세요!',
    ("선택해주세요", '총기류', '보조무기', "파츠","총구", "탄창",  '손잡이', "조준경", "개머리판"),  index=0)
if pick == '총기류':
    st.write('선수들이 가장 많이 사용했던 **총기류**는 무엇일까요?')
    fig = px.bar(df_use_gun.set_index("총 이름").sort_values("개수"), orientation='h', color=df_use_gun["개수"][::-1], color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '보조무기':
    df_handgun_weapon["보조무기 이름"] = df_handgun_weapon["보조무기 이름"].str.replace("Item_Weapon_", repl=r'', regex=True)
    df_handgun_weapon["보조무기 이름"] = df_handgun_weapon["보조무기 이름"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_handgun_weapon.set_index("보조무기 이름"), color=df_handgun_weapon["개수"], color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '총구':
    st.write('선수들이 가장 많이 사용했던 **총구**는 무엇일까요?')
    df_Muzzle["총구"] = df_Muzzle["총구"].str.replace("Item_Attach_Weapon_Muzzle_", repl=r'', regex=True)
    df_Muzzle["총구"] = df_Muzzle["총구"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Muzzle.set_index("총구").sort_values(by="개수"), orientation='h', color=df_Muzzle["개수"][::-1] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '탄창':
    st.write('선수들이 가장 많이 사용했던 **탄창**은 무엇일까요?')
    df_Magazine["탄창"] = df_Magazine["탄창"].str.replace("Item_Attach_Weapon_Magazine_", repl=r'', regex=True)
    df_Magazine["탄창"] = df_Magazine["탄창"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Magazine.set_index("탄창").sort_values(by="개수"), orientation='h', color=df_Magazine["개수"][::-1] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '손잡이':
    st.write('선수들이 가장 많이 사용했던 **손잡이**는 무엇일까요?')
    df_Lower["손잡이"] = df_Lower["손잡이"].str.replace("Item_Attach_Weapon_Lower_", repl=r'', regex=True)
    df_Lower["손잡이"] = df_Lower["손잡이"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Lower.set_index("손잡이"), color=df_Lower["개수"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '파츠':
    st.write('선수들이 가장 많이 사용했던 **파츠**는 무엇일까요?')
    fig = px.bar(df_parts_value, x="총기 부착물", y="개수", color=df_parts_value["개수"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == '조준경':
    st.write('선수들이 가장 많이 사용했던 **조준경**은 무엇일까요?')
    df_upper["조준경"] = df_upper["조준경"].str.replace("Item_Attach_Weapon_Upper_", repl=r'', regex=True)
    df_upper["조준경"] = df_upper["조준경"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_upper.set_index("조준경"), color=df_upper["개수"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
elif pick == "개머리판":
    st.write('선수들이 가장 많이 사용했던 **개머리판**은 무엇일까요?')
    df_Stock["개머리판"] = df_Stock["개머리판"].str.replace("Item_Attach_Weapon_Stock_", repl=r'', regex=True)
    df_Stock["개머리판"] = df_Stock["개머리판"].str.replace("_C", repl=r'', regex=True)
    fig = px.bar(df_Stock.set_index("개머리판"), color=df_Stock["개수"] , color_continuous_scale='YlOrBr')
    fig.update_layout(width=1000, height=500)
    st.plotly_chart(fig)
else:
     st.write(" ")
