import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🎨 앱 기본 설정
st.set_page_config(layout="wide")
st.title("📈 이차함수 표준형 $y=a(x-p)^2+q$ 학습 앱")
st.markdown("---")

# ⚙️ 사이드바에서 a, p, q 값 입력받기
st.sidebar.header("함수 계수 설정")
a = st.sidebar.slider("a 값 (그래프 모양)", -2.0, 2.0, 1.0, 0.1) # a는 0이 아니어야 함
if a == 0:
    st.sidebar.warning("a는 0이 될 수 없습니다. (a=0.1로 자동 설정)")
    a = 0.1

# x 값 범위
x = np.linspace(-10, 10, 400)

def plot_quadratic(a, p, q, title, base_func=None):
    """이차함수 그래프를 그리고 Streamlit에 표시하는 함수"""
    y = a * (x - p)**2 + q
    
    fig, ax = plt.subplots()
    
    # 💡 기본 함수 그래프 (비교용)
    if base_func is not None:
        y_base = base_func(x)
        ax.plot(x, y_base, 'r--', label='기본형 $y=ax^2$', alpha=0.6)
    
    # 📊 현재 함수 그래프
    ax.plot(x, y, 'b', label=f'$y={a}(x-{p})^2+{q}$')
    
    # 📌 꼭짓점 표시
    ax.plot(p, q, 'go', label=f'꼭짓점 ({p}, {q})')
    
    # 그래프 꾸미기
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlim(-5, 5) # 적절한 범위로 조정
    ax.set_ylim(-5, 5)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)


# 1️⃣ $x$축 평행이동 학습: $y=a(x-p)^2$
st.header("1. $x$축 평행이동 학습: $y=a(x-p)^2$")
col1, col2 = st.columns(2)

with col1:
    p1 = st.slider("p 값", -3.0, 3.0, 0.0, 0.1, key="p_move_x")
    q1 = 0
    st.latex(f"y={a}(x-{p1})^2")
    plot_quadratic(a, p1, q1, "$x$축 평행이동 ($q=0$)", base_func=lambda x_val: a * x_val**2)

with col2:
    st.markdown(f"""
    **개념 확인:**
    - $y={a}x^2$의 그래프를 **$x$축 방향으로 $p={p1}$만큼** 평행이동합니다.
    - 꼭짓점은 $(0, 0)$에서 **$({p1}, 0)$**으로 이동합니다.
    """)
st.markdown("---")

# 2️⃣ $y$축 평행이동 학습: $y=ax^2+q$
st.header("2. $y$축 평행이동 학습: $y=ax^2+q$")
col3, col4 = st.columns(2)

with col3:
    p2 = 0
    q2 = st.slider("q 값", -3.0, 3.0, 0.0, 0.1, key="q_move_y")
    st.latex(f"y={a}x^2+{q2}")
    plot_quadratic(a, p2, q2, "$y$축 평행이동 ($p=0$)", base_func=lambda x_val: a * x_val**2)

with col4:
    st.markdown(f"""
    **개념 확인:**
    - $y={a}x^2$의 그래프를 **$y$축 방향으로 $q={q2}$만큼** 평행이동합니다.
    - 꼭짓점은 $(0, 0)$에서 **$(0, {q2})$**으로 이동합니다.
    """)
st.markdown("---")

# 3️⃣ 표준형 통합 학습: $y=a(x-p)^2+q$
st.header("3. 표준형 통합 학습: $y=a(x-p)^2+q$")
col5, col6 = st.columns(2)

with col5:
    p3 = st.slider("p 값", -3.0, 3.0, 1.0, 0.1, key="p_full")
    q3 = st.slider("q 값", -3.0, 3.0, 1.0, 0.1, key="q_full")
    
    # LaTeX 수식 표시
    if q3 >= 0:
        st.latex(f"y={a}(x-{p3})^2+{q3}")
    else:
        st.latex(f"y={a}(x-{p3})^2{q3}") # q가 음수일 때 +를 붙이지 않음

    plot_quadratic(a, p3, q3, "표준형 $y=a(x-p)^2+q$")

with col6:
    st.markdown(f"""
    **종합 개념:**
    - 이차함수 $y=a(x-p)^2+q$의 그래프는 $y=ax^2$의 그래프를
    - **$x$축 방향으로 $p={p3}$만큼**,
    - **$y$축 방향으로 $q={q3}$만큼** 평행이동한 것입니다.
    - **꼭짓점의 좌표**는 **$({p3}, {q3})$**입니다.
    - **축의 방정식**은 $x={p3}$입니다.
    """)
st.markdown("---")


# 4️⃣ 개념 이해 퀴즈
st.header("4. 개념 이해 퀴즈 🤔")

quiz_q = "이차함수 $y=-2(x+3)^2-4$의 그래프의 **꼭짓점 좌표**는?"
quiz_options = ["(3, -4)", "(-3, -4)", "(3, 4)", "(-3, 4)"]
correct_answer = "(-3, -4)"

st.markdown(f"**문제:** {quiz_q}")
quiz_select = st.radio("정답을 선택하세요:", quiz_options)

if st.button("정답 확인"):
    if quiz_select == correct_answer:
        st.success("🎉 정답입니다! $y=a(x-p)^2+q$에서 $p=-3, q=-4$이므로 꼭짓점은 $(-3, -4)$입니다.")
    else:
        st.error("❌ 오답입니다. $y=a(x-p)^2+q$ 꼴에서 $x+3$은 $x-(-3)$으로 생각해야 합니다.")
