import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. 페이지 설정
# ----------------------------------------------------------------------
st.title('이차함수의 그래프 기본형($y=ax^2$) 분석하기 📈')
st.markdown("""
**계수 $a$의 변화**가 그래프의 **볼록 방향**과 **폭**에 어떤 영향을 미치는지 확인해 보세요.
""")

# 2. 사이드바 (사용자 입력)
# ----------------------------------------------------------------------
st.sidebar.header('계수 A 값 조절')

# a 값 조절 슬라이더 설정 (a는 0이 아니어야 함)
a = st.sidebar.slider(
    'a 값 선택',
    min_value=-5.0,
    max_value=5.0,
    value=1.0,
    step=0.1,
    help='a=0일 경우 이차함수가 아니므로 그래프가 x축에 가깝게 표시됩니다.'
)

# a가 0에 아주 가까울 경우 경고 메시지 표시 및 처리를 위한 조정
if abs(a) < 0.05 and a != 0.0:
    st.sidebar.warning(f"⚠️ **a={a:.1f}** 일 때, 폭이 매우 넓어져 x축에 가깝게 보입니다.")

if a == 0.0:
    st.sidebar.error("🚨 **a는 0이 될 수 없습니다!** (a=0이면 직선 y=0이 됩니다.)")
    a = 0.0001  # 그래프 계산을 위한 아주 작은 값으로 임시 대체

# 3. 그래프 생성 및 출력
# ----------------------------------------------------------------------
# x 값 범위 정의
x = np.linspace(-5, 5, 400)
# y = ax^2 계산
y = a * x**2

# Matplotlib을 이용한 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))

# 현재 a 값의 그래프
ax.plot(x, y, label=f'$y = {a:.1f}x^2$', color='blue', linewidth=2)

# 기준선 y = x^2 (a=1) 그래프
ax.plot(x, 1 * x**2, '--', color='gray', alpha=0.6, label='$y=x^2$ (기준)')

# 그래프 스타일 설정
ax.set_title(f'$y = {a:.1f}x^2$ 그래프')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 10)  # y축 고정
ax.axhline(0, color='black', linewidth=0.8) # x축
ax.axvline(0, color='black', linewidth=0.8) # y축
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='upper center', frameon=False)

# 스트림릿에 그래프 표시
st.pyplot(fig)

# 4. 관찰 결과 요약
# ----------------------------------------------------------------------
st.header("🔑 관찰 결과: 계수 $a$의 역할")

st.subheader("1. 볼록한 방향 (a의 부호)")
if a > 0:
    st.success(f"현재 $\\mathbf{{a = {a:.1f}}}>0$ 이므로 그래프는 **아래로 볼록**합니다. (최솟값: 0)")
else:
    st.error(f"현재 $\\mathbf{{a = {a:.1f}}}<0$ 이므로 그래프는 **위로 볼록**합니다. (최댓값: 0)")

st.subheader("2. 그래프의 폭 (a의 절댓값)")
st.info(f"현재 $\\mathbf{{|a| = {abs(a):.1f}}}$ 입니다.")
st.markdown(f"""
* **$|a|$ 값이 클수록** (예: $|a|=5.0$): 그래프의 폭은 **좁아집니다** ($\mathbf{y}$축에 가까워짐).
* **$|a|$ 값이 작을수록** (예: $|a|=0.1$): 그래프의 폭은 **넓어집니다** ($\mathbf{x}$축에 가까워짐).
""")
