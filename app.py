import streamlit as st
import pandas as pd
from io import BytesIO

st.title("사업장 개요")

# 입력값 받기
col1, col2 = st.columns([1, 2])
사업장명 = col2.text_input("사업장명", key="사업장명")
소재지 = col2.text_input("소재지", key="소재지")
업종 = col2.text_input("업종", key="업종")

col3, col4 = st.columns(2)
예비조사 = col3.date_input("예비조사일", key="예비조사")
본조사 = col4.date_input("본조사일", key="본조사")

col5, col6 = st.columns(2)
수행기관 = col5.text_input("수행기관", key="수행기관")
성명 = col6.text_input("성명", key="성명")

# 표 형태로 출력
st.markdown("""
<table border="1" style="width:60%; text-align:center;">
  <tr><th colspan="3" style="font-size:20px;">사업장 개요</th></tr>
  <tr><td>사업장명</td><td colspan="2">{}</td></tr>
  <tr><td>소재지</td><td colspan="2">{}</td></tr>
  <tr><td>업종</td><td colspan="2">{}</td></tr>
  <tr>
    <td rowspan="2">조사일</td>
    <td>예비조사</td><td>{}</td>
  </tr>
  <tr>
    <td>본조사</td><td>{}</td>
  </tr>
  <tr>
    <td rowspan="2">수행자</td>
    <td>수행기관</td><td>{}</td>
  </tr>
  <tr>
    <td>성명</td><td>{}</td>
  </tr>
</table>
""".format(사업장명, 소재지, 업종, 예비조사, 본조사, 수행기관, 성명), unsafe_allow_html=True)

# 엑셀로 저장
data = {
    "항목": ["사업장명", "소재지", "업종", "예비조사일", "본조사일", "수행기관", "성명"],
    "값": [사업장명, 소재지, 업종, str(예비조사), str(본조사), 수행기관, 성명]
}
df = pd.DataFrame(data)

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='사업장 개요')
    return output.getvalue()

st.download_button(
    label="엑셀로 저장",
    data=to_excel(df),
    file_name="사업장_개요.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)