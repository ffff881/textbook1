import streamlit as st
import random
import pandas as pd

# 최근 로또 당첨 번호 (검색 결과 기반, 1195회 기준)
RECENT_WINNING_NUMBERS = {
    '회차': 1195,
    '당첨번호': [3, 15, 27, 33, 34, 36]
}

def generate_lotto_numbers():
    """1부터 45 사이에서 중복 없이 6개의 숫자를 생성합니다."""
    return sorted(random.sample(range(1, 46), 6))

def compare_numbers(generated_numbers, winning_numbers):
    """생성된 번호와 당첨 번호를 비교하여 일치하는 개수를 반환합니다."""
    return len(set(generated_numbers) & set(winning_numbers))

def main():
    st.set_page_config(page_title="로또 번호 추천 및 비교 앱 🍀", layout="centered")
    st.title("🍀 로또 번호 추천 및 비교 앱")
    st.markdown("1부터 45까지의 숫자 중 6개의 로또 번호를 추천해 드립니다.")
    st.markdown("---")

    # 1. 생성할 세트 수 선택 (st.number_input으로 변경)
    st.subheader("1️⃣ 생성할 세트 수 선택")
    
    # 사용자가 1부터 20까지의 숫자를 직접 입력할 수 있도록 변경
    num_sets = st.number_input(
        "몇 세트의 번호를 추천받으시겠어요? (1부터 20까지 입력)", 
        min_value=1, 
        max_value=20, 
        value=5, 
        step=1
    )
    
    # 정수형으로 사용
    num_sets = int(num_sets)

    # 2. 번호 생성 버튼
    if st.button("🔢 번호 생성 및 비교", type="primary"):
        st.subheader("2️⃣ 추천 로또 번호")
        
        results = []
        comparison_data = []

        # 입력된 세트 수만큼 반복
        for i in range(1, num_sets + 1):
            numbers = generate_lotto_numbers()
            results.append(f"**세트 {i}:** **{', '.join(map(str, numbers))}**")
            
            # 3. 당첨 번호 비교
            match_count = compare_numbers(numbers, RECENT_WINNING_NUMBERS['당첨번호'])
            
            comparison_data.append({
                '세트': i,
                '추천 번호': ' '.join(map(str, numbers)),
                f"{RECENT_WINNING_NUMBERS['회차']}회 당첨 번호": ' '.join(map(str, RECENT_WINNING_NUMBERS['당첨번호'])),
                '일치 개수': match_count,
                '비고': f"{match_count}개 일치"
            })

        # 추천 번호 출력
        for result in results:
            st.markdown(f"- {result}")
        
        st.markdown("---")
        
        # 4. 비교 결과 출력
        st.subheader(f"3️⃣ {RECENT_WINNING_NUMBERS['회차']}회 당첨 번호와 비교")
        st.info(f"👉 **{RECENT_WINNING_NUMBERS['회차']}회 당첨 번호:** {', '.join(map(str, RECENT_WINNING_NUMBERS['당첨번호']))}")

        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df.set_index('세트'))

        st.balloons()

if __name__ == "__main__":
    main()
