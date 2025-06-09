import streamlit as st

st.markdown("<h2 style='text-align: center;'>사업장 개요</h2>", unsafe_allow_html=True)

# 입력값 받기
col1, col2 = st.columns([1, 2])
with col1:
    st.write("사업장명")
with col2:
    사업장명 = st.text_input("", key="사업장명", label_visibility="collapsed")
with col1:
    st.write("소재지")
with col2:
    소재지 = st.text_input("", key="소재지", label_visibility="collapsed")
with col1:
    st.write("업종")
with col2:
    업종 = st.text_input("", key="업종", label_visibility="collapsed")

st.write("조사일")
col3, col4 = st.columns(2)
with col3:
    예비조사 = st.date_input("예비조사", key="예비조사")
with col4:
    본조사 = st.date_input("본조사", key="본조사")

st.write("수행자")
col5, col6 = st.columns(2)
with col5:
    수행기관 = st.text_input("수행기관", key="수행기관")
with col6:
    성명 = st.text_input("성명", key="성명")

# 표 안에 입력란을 넣는 것은 Streamlit 기본 기능으로는 불가
# 하지만, 표처럼 보이게 컬럼과 구분선을 활용해 최대한 비슷하게 구현 가능

st.markdown("""
<style>
.table-style {
    border-collapse: collapse;
    width: 60%;
    margin-left: auto;
    margin-right: auto;
}
.table-style th, .table-style td {
    border: 1px solid #888;
    padding: 8px;
    text-align: center;
}
.table-style th {
    background-color: #f2f2f2;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<table class="table-style">
  <tr>
    <th colspan="3">사업장 개요</th>
  </tr>
  <tr>
    <td>사업장명</td>
    <td colspan="2">{사업장명}</td>
  </tr>
  <tr>
    <td>소재지</td>
    <td colspan="2">{소재지}</td>
  </tr>
  <tr>
    <td>업종</td>
    <td colspan="2">{업종}</td>
  </tr>
  <tr>
    <td rowspan="2">조사일</td>
    <td>예비조사</td>
    <td>{예비조사}</td>
  </tr>
  <tr>
    <td>본조사</td>
    <td>{본조사}</td>
  </tr>
  <tr>
    <td rowspan="2">수행자</td>
    <td>수행기관</td>
    <td>{수행기관}</td>
  </tr>
  <tr>
    <td>성명</td>
    <td>{성명}</td>
  </tr>
</table>
""", unsafe_allow_html=True)
