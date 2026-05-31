import streamlit as st

st.set_page_config(page_title="Math Box Diagram", page_icon="📦", layout="centered")

st.sidebar.title("메뉴")
page = st.sidebar.selectbox(
    "페이지 선택",
    ["홈", "상자그림 만들기"]
)

if page == "홈":
    st.title("🎈 중학교 3학년 수학 앱")
    st.write(
        "이 앱은 중학교 3학년 학생을 위해 상자그림(Box Diagram)을 연습할 수 있는 기본 페이지 틀을 제공합니다."
    )
    st.markdown(
        "- 왼쪽에서 '상자그림 만들기'를 선택해 보세요.\n"
        "- 문제 유형과 숫자 값을 입력하면 상자그림을 그리는 연습을 도와줍니다."
    )

elif page == "상자그림 만들기":
    st.title("📦 상자그림 만들기")
    st.write(
        "중3 수학에서 사용하는 상자그림을 쉽게 만들고 시각적으로 확인할 수 있도록 도와줍니다."
    )

    st.header("1. 문제 유형 선택")
    problem_type = st.selectbox(
        "어떤 유형의 상자그림을 만들까요?",
        [
            "덧셈/뺄셈",
            "곱셈/나눗셈",
            "비례식",
            "문장제",
        ],
    )

    st.header("2. 값 입력")
    left_value = st.number_input("왼쪽 상자 값", min_value=0, max_value=100, value=20)
    right_value = st.number_input("오른쪽 상자 값", min_value=0, max_value=100, value=40)
    total_value = st.number_input("전체 값", min_value=0, max_value=200, value=60)

    st.header("3. 상자그림 미리보기")
    st.write("입력한 값을 바탕으로 상자그림의 기본 구조를 확인할 수 있습니다.")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("왼쪽 상자")
        st.write(f"값: {left_value}")
    with col2:
        st.subheader("오른쪽 상자")
        st.write(f"값: {right_value}")

    st.markdown("---")
    st.write("### 풀이 힌트")
    st.write(
        "여기에는 입력한 값과 유형에 따라 상자그림을 어떻게 해석할지 간단한 힌트를 표시합니다."
    )
    st.write(f"- 선택한 유형: {problem_type}")
    st.write(f"- 왼쪽 상자 값: {left_value}")
    st.write(f"- 오른쪽 상자 값: {right_value}")
    st.write(f"- 전체 값: {total_value}")

    st.info(
        "※ 지금은 기본 틀입니다. 문제 문장 입력과 실제 그래픽 상자그림은 이후에 추가할 수 있습니다."
    )
