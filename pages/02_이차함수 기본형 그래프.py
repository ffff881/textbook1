import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os # 파일 경로 확인을 위해 os 모듈 추가

# 1. 페이지 설정
# ----------------------------------------------------------------------
st.set_page_config(layout="wide") # 넓은 레이아웃 사용
st.title('이차함수의 그래프 기본형($y=ax^2$) 분석하기 📈')
st.markdown("""
**계수 $a$의 변화**가 그래프의 **볼록 방향**과 **폭**에 어떤 영향을 미치는지 확인하고, 퀴즈를 풀어 학습 내용을 점검해 보세요!
""")

# 2. 사이드바 (사용자 입력)
# ----------------------------------------------------------------------
st.sidebar.header('계수 A 값 조절')

# a 값 조절 슬라이더 설정
a = st.sidebar.slider(
    'a 값 선택',
    min_value=-100.0,
    max_value=100.0,
    value=1.0,
    step=0.1,
    help='a는 0이 아니어야 합니다. 폭의 변화를 잘 관찰하려면 -5.0 ~ 5.0 사이의 작은 값을 추천합니다.'
)

# a가 0일 경우 예외 처리
if a == 0.0:
    st.sidebar.error("🚨 **a는 0이 될 수 없습니다!** (a=0이면 직선 y=0이 됩니다.)")
    a = 0.0001

# 3. 그래프 생성 및 출력
# ----------------------------------------------------------------------
# x 값 범위 정의
x = np.linspace(-2, 2, 400)
# y = ax^2 계산
y = a * x**2

# y축 표시 범위를 a 값에 따라 동적으로 설정
y_limit = max(10, min(100, abs(a) * 4))

col_graph, col_info = st.columns([2, 1])

with col_graph:
    fig, ax = plt.subplots(figsize=(7, 5))

    # 현재 a 값의 그래프
    ax.plot(x, y, label=f'$y = {a:.1f}x^2$', color='blue', linewidth=2)

    # 기준선 y = x^2 (a=1) 그래프
    ax.plot(x, 1 * x**2, '--', color='gray', alpha=0.6, label='$y=x^2$ (기준)')

    # 그래프 스타일 설정
    ax.set_title(f'$y = {a:.1f}x^2$ 그래프')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-y_limit, y_limit)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, linestyle=':', alpha=0.5)
    ax.legend(loc='upper right', frameon=True)

    st.pyplot(fig)

with col_info:
    st.header("📊 관찰 요약")
    
    st.subheader("1. 볼록 방향 (a의 부호)")
    if a > 0:
        st.success(f"**a = {a:.1f}** (> 0) 이므로 **아래로 볼록**")
    else:
        st.error(f"**a = {a:.1f}** (< 0) 이므로 **위로 볼록**")

    st.subheader("2. 그래프의 폭 (a의 절댓값)")
    st.info(f"**|a| = {abs(a):.1f}** 입니다.")
    st.markdown("""
    * $\\mathbf{|a|}$ **클수록** ($\mathbf{|a|}$ > 1): 폭이 **좁아집니다** ($\mathbf{y}$축에 가까워짐).
    * $\\mathbf{|a|}$ **작을수록** ($\mathbf{0 < |a|}$ < 1): 폭이 **넓어집니다** ($\mathbf{x}$축에 가까워짐).
    """)

st.markdown("---")

# 4. 퀴즈 섹션 (학습 확인)
# ----------------------------------------------------------------------
st.header("📝 퀴즈: $a$ 값에 따른 그래프 특징 확인")

# 퀴즈 결과 저장을 위한 session state 초기화
if 'q1_correct' not in st.session_state:
    st.session_state.q1_correct = False
if 'q2_correct' not in st.session_state:
    st.session_state.q2_correct = False

with st.expander("퀴즈 풀기"):
    
    # --- 문제 1 ---
    st.subheader("문제 1. 볼록 방향 (선택형)")
    st.markdown("이차함수 $y = -0.5x^2$ 의 그래프는 어느 방향으로 볼록한가요?")
    
    q1_answer = st.radio(
        "선택하세요:",
        ('아래로 볼록', '위로 볼록', '좌우로 볼록'),
        key='q1'
    )
    
    if st.button('정답 확인 1', key='btn_q1'):
        if q1_answer == '위로 볼록':
            st.success("✅ 정답입니다! $a = -0.5$ (음수)이므로 위로 볼록합니다.")
            st.session_state.q1_correct = True
        else:
            st.error("❌ 오답입니다. $a$ 값이 음수이면 그래프는 위로 볼록합니다. a 값의 부호를 다시 확인하세요.")
            st.session_state.q1_correct = False

    st.markdown("---")

    # --- 문제 2 ---
    st.subheader("문제 2. 그래프 폭 (주관식/개념 확인)")
    st.markdown("두 이차함수 $y = 3x^2$ 와 $y = 0.5x^2$ 중, 그래프의 폭이 **더 좁은** 것은 무엇인가요? (정답을 수식으로 입력하세요)")
    
    q2_answer = st.text_input(
        "정답 (예: y=ax^2):",
        key='q2'
    )
    
    if st.button('정답 확인 2', key='btn_q2'):
        processed_answer = q2_answer.replace(" ", "").lower()
        correct_answers = ['y=3x^2', '3x^2']
        
        if processed_answer in correct_answers:
            st.success("✅ 정답입니다! $|3| > |0.5|$ 이므로, $|a|$ 값이 더 큰 $y = 3x^2$ 의 폭이 더 좁습니다.")
            st.session_state.q2_correct = True
        else:
            st.error("❌ 오답입니다. 폭은 $a$의 **절댓값 $|a|$**에 의해 결정됩니다. 절댓값이 클수록 폭이 좁아집니다. $y=3x^2$를 입력하세요.")
            st.session_state.q2_correct = False
            
# 5. 모든 퀴즈 정답 시 이미지 표시
# ----------------------------------------------------------------------
if st.session_state.q1_correct and st.session_state.q2_correct:
    st.sidebar.success("👏 모든 퀴즈 정답! 축하합니다!")
    st.markdown("## 🎉 축하합니다! 모든 퀴즈를 맞히셨습니다!")
    
    # 'images/1.png' 파일이 존재하는지 확인하고 표시
    image_path = 'images/1.png'
    if os.path.exists(image_path):
        st.image(image_path, caption='완벽하게 이해했어요!')
    else:
        st.warning(f"이미지 파일 ({image_path})을 찾을 수 없습니다. 'app.py' 파일과 같은 위치에 'images' 폴더를 만들고, 그 안에 '1.png' 파일을 넣어주세요.")
