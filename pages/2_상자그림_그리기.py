import streamlit as st
from decimal import Decimal, InvalidOperation
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="상자그림 그리기", page_icon="🧮", layout="centered")

st.title("상자그림 시각화")
st.write(
    "1_사분위수_구하기.py에 입력한 데이터 값을 동일하게 사용하여 상자그림을 시각화합니다."
)

text_input = st.text_area(
    "데이터 입력",
    value="10, 20, 30, 40, 50",
    placeholder="예: 10, 20, 30 또는 10 20 30 또는 10\n20\n30",
    help="쉼표, 공백, 줄바꿈으로 숫자를 구분하여 입력하세요. 1부터 1000까지 범위의 숫자를 지원합니다."
)

font_path = Path(__file__).resolve().parents[1] / "fonts" / "NotoSansKR-Medium.ttf"
font_name = None
if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    font_prop = fm.FontProperties(fname=str(font_path))
    font_name = font_prop.get_name()
    plt.rcParams["font.family"] = font_name
    plt.rcParams["axes.unicode_minus"] = False
    sns.set(font=font_name)
else:
    st.warning(f"한글 폰트 파일을 찾을 수 없습니다: {font_path}")

numbers = []
for token in text_input.replace(",", " ").split():
    try:
        value = Decimal(token)
        if Decimal("1") <= value <= Decimal("1000"):
            numbers.append(value)
        else:
            st.warning(f"범위를 벗어난 숫자: {token} (1~1000 사이만 허용)")
    except (InvalidOperation, ValueError):
        if token.strip():
            st.warning(f"올바른 숫자가 아닙니다: {token}")


def format_value(value):
    if isinstance(value, Decimal):
        if value == value.to_integral():
            return str(value.quantize(Decimal(1)))
        return format(value.normalize(), 'f')
    if isinstance(value, int):
        return str(value)
    return str(value)


def format_list(values):
    return [format_value(v) for v in values]

if numbers:
    정렬된 = sorted(numbers)
    st.subheader("입력한 데이터")
    st.write(format_list(정렬된))

    float_values = [float(v) for v in 정렬된]

    st.subheader("Matplotlib 상자그림")
    fig1, ax1 = plt.subplots(figsize=(8, 3))
    sns.boxplot(x=float_values, ax=ax1, color="#82c4ff")
    ax1.set_title("Matplotlib으로 그린 상자그림", fontsize=14)
    ax1.set_xlabel("값", fontsize=12)
    ax1.set_ylabel("")
    ax1.set_yticks([])
    st.pyplot(fig1)

    st.subheader("Seaborn 상자그림")
    fig2, ax2 = plt.subplots(figsize=(8, 3))
    sns.boxplot(x=float_values, ax=ax2, color="#ff9999")
    ax2.set_title("Seaborn으로 그린 상자그림", fontsize=14)
    ax2.set_xlabel("값", fontsize=12)
    ax2.set_ylabel("")
    ax2.set_yticks([])
    st.pyplot(fig2)

    st.subheader("Plotly 상자그림")
    fig3 = px.box(
        x=float_values,
        points="all",
        title="Plotly로 그린 상자그림",
    )
    fig3.update_layout(
        xaxis_title="값",
        yaxis_title="",
        title_font_size=16,
        template="simple_white",
        font=dict(family=font_name if font_name else "sans-serif"),
    )
    fig3.update_traces(name="데이터", boxmean=True)
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.info("숫자를 입력하면 상자그림을 세 가지 방법으로 시각화합니다.")
