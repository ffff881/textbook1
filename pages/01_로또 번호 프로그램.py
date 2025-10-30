import streamlit as st
import random

# Streamlit 앱 설정
st.title('🍀 로또 6/45 번호 생성기')
st.markdown('1부터 45까지의 숫자 중 6개의 숫자를 무작위로 선택합니다.')

# --- 입력 섹션 ---
st.header('몇 게임을 생성할까요?')
# 게임 수를 1부터 10까지 입력받는 슬라이더
game_count = st.slider(
    '게임 수',
    min_value=1,
    max_value=10,
    value=1,  # 기본값
    step=1
)

st.subheader(f'총 **{game_count}** 게임을 생성합니다.')

# --- 버튼 및 결과 섹션 ---
# '생성' 버튼
if st.button('로또 번호 생성'):
    st.markdown('---')
    st.header('🎁 생성된 로또 번호')
    
    # 입력된 게임 수만큼 로또 번호 조합 생성
    for i in range(1, game_count + 1):
        # 1부터 45까지의 숫자 중 중복 없이 6개 선택
        lotto_numbers = random.sample(range(1, 46), 6)
        # 오름차순으로 정렬
        lotto_numbers.sort()
        
        # 결과를 보기 좋게 출력
        st.success(f'**게임 {i}:** {lotto_numbers}')
        
    st.balloons() # 번호 생성 완료 시 애니메이션 효과
