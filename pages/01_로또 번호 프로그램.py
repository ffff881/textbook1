import streamlit as st
import random

# Streamlit 앱 설정
st.title('🍀 로또 6/45 번호 생성기')
st.markdown('1부터 45까지의 숫자 중 6개의 숫자를 무작위로 선택합니다.')

# --- 입력 섹션 (슬라이더 대신 숫자 입력 필드 사용) ---
st.header('몇 게임을 생성할까요?')
# 게임 수를 1부터 10까지 직접 입력받는 숫자 입력 필드
game_count = st.number_input(
    '생성할 로또 게임 수를 입력하세요 (1부터 10까지)',
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
        # st.columns를 사용하여 번호들을 시각적으로 돋보이게 표시
        cols = st.columns(6)
        for j, number in enumerate(lotto_numbers):
            # CSS를 사용하여 로또 공 모양으로 스타일링 (Streamlit에서 HTML/CSS를 직접 사용하는 방법)
            # st.markdown를 사용하여 HTML 렌더링
            cols[j].markdown(
                f"""
                <div style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    background-color: #f7d794; /* 공 색상 */
                    color: black;
                    font-weight: bold;
                    border: 2px solid #e7ba66;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
                ">
                    {number}
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # 게임 번호 표시
        st.caption(f'**게임 {i}**')
        st.write(' ') # 간격 띄우기
        
    st.balloons() # 번호 생성 완료 시 애니메이션 효과
