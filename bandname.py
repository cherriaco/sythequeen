import streamlit as st

st.title('남몰래 꿈꿔온 밴드 이름 만들기')

# 삶의 가치 선택
value = st.selectbox('내가 중요하게 여기는 삶의 가치를 선택해주세요:', ['낭만', '성장', '평등', '진실', '성실', '사랑', '정직', '자유', '건강', '연대'])

# 상의 색 선택
shirt_color = st.selectbox('내가 입고 있는 상의 색을 선택해주세요:', ['블랙', '화이트', '핑크', '옐로우', '그린', '민트', '카키', '네이비', '블루', '그레이', '베이지', '퍼플'])

# 먹고 싶은 음식 선택
food = st.selectbox('내가 먹고 싶은 음식을 선택해주세요:', ['포케', '샐러드', '마라탕', '반미', '꿔바로우', '초밥', '순두부찌개', '보쌈', '김치찜'])

# 포지션 선택
position = st.selectbox('당신의 밴드 포지션을 선택해주세요:', ['보컬', '베이스', '일렉', '드럼', '키보드'])

# 상의 색에 따른 이미지 설명
color_descriptions = {
    '블랙': '멋진',
    '화이트': '깨끗한',
    '핑크': '귀여운',
    '옐로우': '밝은',
    '그린': '상쾌한',
    '민트': '신선한',
    '카키': '스타일리시한',
    '네이비': '차분한',
    '블루': '시원한',
    '그레이': '중립적인',
    '베이지': '부드러운',
    '퍼플': '우아한'
}

# 인디밴드 이름 생성
if st.button('인디밴드 이름 생성'):
    band_name = f"{value} {shirt_color} {food}"
    chrr = color_descriptions[shirt_color]
    st.write(f"이제 당신은 '{band_name}'에 소울을 바칩니다.")
    st.write(f"당신은 {food}에 영혼을 바치고 {chrr} {shirt_color}의 소울을 챙긴 {value} {position} 이군요.")
