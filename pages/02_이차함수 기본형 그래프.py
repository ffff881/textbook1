import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 제목 설정
st.title('이차함수의 그래프 기본형($y=ax^2$) 분석하기 📈')
st.markdown("""
이 앱을 통해 이차함수의 기본형 $y=ax^2$에서 **계수 $a$의 값**이 그래프 모양에 미치는 영향을 탐구해 보세요.
""")

st.sidebar.header('조절 패널')

# a 값 조절을 위한 슬라이더
# a는 0이 아니어야 하므로, -5.0부터 5.0까지의 범위에서 0 근처는 건너뛰도록 설정
# st.slider는 실수형을 지원하며, step을 0.1로 설정
a = st.sidebar.slider(
    '계수 a 값 선택',
    min_value=-5.0,
    max_value=5.0,
    value=1.0,
    step=0.1
)

# a가 0일 경우, 이차함수가 아니므로 재선택을 유도
if a == 0.0:
    st.error("⚠️ 계수 $a$는 0이 될 수 없습니다. $a$ 값이 0이면 이차함수가 아닌 $y=0$ (x축)이 됩니다.")
    st.sidebar.write("현재 $y=0$ (x축) 그래프가 표시됩니다.")
    a = 0.000001 # 0을 피해 아주 작은 값으로 설정하여 에러 방지 (그래프는 거의 x축으로 보임)

# x 값 범위 설정 (그래프를 그릴 범위)
x = np.linspace(-5, 5, 400)
# 이차함수 y = ax^2 계산
y = a * x**2

# 그래프 생성
fig, ax = plt.subplots()
ax.plot(x, y, label=f'$y = {a:.1f}x^2$', color='blue')

# y = x^2 (a=1) 그래프를 기준선으로 표시
x_ref = np.linspace(-5, 5, 400)
y_ref = 1 * x_ref**2
ax.plot(x_ref, y_ref, '--', color='gray', label='$y=x^2$ (기준)')

# 그래프 설정
ax.set_title(f'$y = {a:.1f}x^2$ 그래프')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True, linestyle='--', alpha=0.6)
ax.axhline(0, color='black', linewidth=0.5) # x축
ax.axvline(0, color='black', linewidth=0.5) # y축
ax.legend()
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 10) # y축 범위를 고정하여 비교 용이하게 함

# 스트림릿에 그래프 표시
st.pyplot(fig)

---

## 🔎 관찰 및 학습 내용

### 1. **볼록한 방향** (부호 관찰)

* **$a > 0$ (양수)일 때:** 그래프는 **아래로 볼록**합니다. (최솟값 존재)
* **$a < 0$ (음수)일 때:** 그래프는 **위로 볼록**합니다. (최댓값 존재)

> **👉 슬라이더를 움직여 $a$의 부호를 바꿔가며 그래프가 뒤집히는 것을 확인해 보세요.**

### 2. **그래프의 폭** (절댓값 관찰)

* **$|a|$ (a의 절댓값)이 클수록:** 그래프의 폭은 **좁아집니다**. ($y$축에 가까워집니다.)
    * 예: $|a|=3$인 $y=3x^2$ 또는 $y=-3x^2$은 $|a|=1$인 $y=x^2$보다 폭이 좁습니다.
* **$|a|$ (a의 절댓값)이 작을수록:** 그래프의 폭은 **넓어집니다**. ($x$축에 가까워집니다.)
    * 예: $|a|=0.5$인 $y=0.5x^2$은 $|a|=1$인 $y=x^2$보다 폭이 넓습니다.

> **👉 슬라이더를 움직여 $a$의 절댓값을 변화시키며 그래프의 폭이 넓어지거나 좁아지는 것을 확인해 보세요.**

---

이 앱을 실행하려면, 위 코드를 `app.py` 파일로 저장하고 터미널에서 다음 명령어를 실행하면 됩니다:

```bash
streamlit run app.py
