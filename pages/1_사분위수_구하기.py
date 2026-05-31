import streamlit as st

st.set_page_config(page_title="사분위수 구하기", page_icon="📊", layout="centered")

st.title("사분위수 구하기")
st.write("사분위수는 데이터를 네 개의 같은 개수 구간으로 나누는 기준 값입니다.")

st.header("1. 사분위수란?")
st.write(
    "사분위수는 전체 데이터를 크기 순서로 정렬한 뒤 네 개의 구간으로 나누는 기준 값입니다."
)
st.write(
    "- 제1사분위수(Q1): 하위 25% 지점의 값\n"
    "- 제2사분위수(Q2): 중앙값, 하위 50% 지점의 값\n"
    "- 제3사분위수(Q3): 하위 75% 지점의 값"
)
st.latex(r"""
Q2 = \text{median}(x_1, x_2, \dots, x_n)
""")
st.latex(r"""
Q1 = \text{median}(x_1, x_2, \dots, x_{\lfloor n/2 \rfloor})
""")
st.latex(r"""
Q3 = \text{median}(x_{\lceil n/2 \rceil + 1}, \dots, x_n)
""")
st.write(
    "사분위수는 데이터의 분포와 중심 위치를 파악하는 데 유용하며, 이상치와 범위를 이해하는 데 도움이 됩니다."
)

st.header("2. 직접 데이터 입력")
st.write("아래 상자에 1부터 1000까지 범위의 숫자를 직접 입력하세요. 숫자는 쉼표(,), 공백, 또는 줄바꿈으로 구분할 수 있습니다.")
text_input = st.text_area(
    "데이터 입력",
    value="10, 20, 30, 40, 50",
    placeholder="예: 10, 20, 30 또는 10 20 30 또는 10\n20\n30",
    help="입력한 데이터로 사분위수를 계산합니다."
)

numbers = []
for token in text_input.replace(",", " ").split():
    try:
        value = int(token)
        if 1 <= value <= 1000:
            numbers.append(value)
        else:
            st.warning(f"범위를 벗어난 숫자: {value} (1~1000 사이만 허용)")
    except ValueError:
        if token.strip():
            st.warning(f"올바른 숫자가 아닙니다: {token}")

if numbers:
    st.header("3. 사분위수 계산 과정")
    st.write("입력한 숫자를 오름차순으로 정렬한 뒤 사분위수를 단계별로 계산합니다.")

    정렬된 = sorted(numbers)
    st.write(f"정렬된 데이터: {정렬된}")

    n = len(정렬된)
    st.write(f"데이터 개수: {n}")

    m = 정렬된[0]
    M = 정렬된[-1]
    st.write(f"- 최솟값 m: {m}")
    st.write(f"- 최댓값 M: {M}")

    def 중앙값(자료):
        길이 = len(자료)
        중간 = 길이 // 2
        if 길이 % 2 == 1:
            return 자료[중간]
        return (자료[중간 - 1] + 자료[중간]) / 2

    if n % 2 == 1:
        st.write("데이터 개수가 홀수이므로 중앙값 Q2는 가운데 값입니다.")
        st.write(f"Q2 위치: {(n + 1) // 2}번째 값")
        st.write(f"Q2 계산: {정렬된[(n - 1) // 2]} = {정렬된[(n - 1) // 2]}")
    else:
        st.write("데이터 개수가 짝수이므로 중앙값 Q2는 가운데 두 값의 평균입니다.")
        left_index = n // 2 - 1
        right_index = n // 2
        st.write(f"Q2 계산: ({정렬된[left_index]} + {정렬된[right_index]}) / 2")
        st.write(f"Q2 값: {(정렬된[left_index] + 정렬된[right_index]) / 2}")

    q2 = 중앙값(정렬된)
    lower_half = 정렬된[: n // 2]
    upper_half = 정렬된[(n + 1) // 2 :]

    st.write(f"하위 절반 데이터: {lower_half}")
    st.write(f"상위 절반 데이터: {upper_half}")

    st.write("### Q1 계산 과정")
    if len(lower_half) % 2 == 1:
        mid = len(lower_half) // 2
        st.write(f"Q1 위치: {mid + 1}번째 값")
        st.write(f"Q1 값: {lower_half[mid]}")
    else:
        mid = len(lower_half) // 2
        st.write(f"Q1 계산: ({lower_half[mid - 1]} + {lower_half[mid]}) / 2")
        st.write(f"Q1 값: {(lower_half[mid - 1] + lower_half[mid]) / 2}")

    q1 = 중앙값(lower_half)

    st.write("### Q3 계산 과정")
    if len(upper_half) % 2 == 1:
        mid = len(upper_half) // 2
        st.write(f"Q3 위치: {mid + 1}번째 값")
        st.write(f"Q3 값: {upper_half[mid]}")
    else:
        mid = len(upper_half) // 2
        st.write(f"Q3 계산: ({upper_half[mid - 1]} + {upper_half[mid]}) / 2")
        st.write(f"Q3 값: {(upper_half[mid - 1] + upper_half[mid]) / 2}")

    q3 = 중앙값(upper_half)

    st.write("### 최종 사분위수 결과")
    st.write(f"- 제1사분위수 Q1: {q1}")
    st.write(f"- 제2사분위수 Q2 (중앙값): {q2}")
    st.write(f"- 제3사분위수 Q3: {q3}")

    st.markdown("---")
    st.write("### 계산 과정 요약")
    st.write(
        "1. 데이터를 오름차순으로 정렬합니다.\n"
        "2. 최솟값 m과 최댓값 M을 찾습니다.\n"
        "3. 전체 데이터의 중앙값을 Q2로 계산합니다.\n"
        "4. 중앙값을 기준으로 하위 절반과 상위 절반을 나눕니다.\n"
        "5. 하위 절반의 중앙값을 Q1, 상위 절반의 중앙값을 Q3로 계산합니다."
    )
else:
    st.info("숫자를 입력하면 사분위수를 계산합니다.")
