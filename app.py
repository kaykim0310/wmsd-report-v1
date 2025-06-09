import streamlit as st
import pandas as pd
from io import BytesIO

st.title("사업장 개요")

# 입력폼
사업장명 = st.text_input("사업장명")
소재지 = st.text_input("소재지")
업종 = st.text_input("업종")
예비조사 = st.date_input("예비조사일")
본조사 = st.date_input("본조사일")
수행기관 = st.text_input("수행기관")
성명 = st.text_input("성명")

def to_excel(사업장명, 소재지, 업종, 예비조사, 본조사, 수행기관, 성명):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        # 빈 DataFrame 생성 (실제 데이터는 직접 쓰기)
        df = pd.DataFrame([[]])
        df.to_excel(writer, index=False, header=False, startrow=0, startcol=0)
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']

        # 표 스타일
        cell_format = workbook.add_format({'border': 1, 'align': 'center', 'valign': 'vcenter'})
        header_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#f2f2f2', 'border': 1, 'font_size': 14})

        # 표 그리기
        worksheet.merge_range('A1:C1', '사업장 개요', header_format)
        worksheet.write('A2', '사업장명', cell_format)
        worksheet.merge_range('B2:C2', 사업장명, cell_format)
        worksheet.write('A3', '소재지', cell_format)
        worksheet.merge_range('B3:C3', 소재지, cell_format)
        worksheet.write('A4', '업종', cell_format)
        worksheet.merge_range('B4:C4', 업종, cell_format)

        worksheet.write('A5', '조사일', cell_format)
        worksheet.write('B5', '예비조사', cell_format)
        worksheet.write('C5', str(예비조사), cell_format)
        worksheet.write('B6', '본조사', cell_format)
        worksheet.write('C6', str(본조사), cell_format)
        worksheet.merge_range('A6:A6', '', cell_format)  # 조사일 셀 병합 유지

        worksheet.write('A7', '수행자', cell_format)
        worksheet.write('B7', '수행기관', cell_format)
        worksheet.write('C7', 수행기관, cell_format)
        worksheet.write('B8', '성명', cell_format)
        worksheet.write('C8', 성명, cell_format)
        worksheet.merge_range('A8:A8', '', cell_format)  # 수행자 셀 병합 유지

        # 셀 병합 (조사일, 수행자)
        worksheet.merge_range('A5:A6', '조사일', cell_format)
        worksheet.merge_range('A7:A8', '수행자', cell_format)

        # 열 너비 조정
        worksheet.set_column('A:A', 12)
        worksheet.set_column('B:B', 12)
        worksheet.set_column('C:C', 20)

    output.seek(0)
    return output

st.download_button(
    label="엑셀로 저장",
    data=to_excel(사업장명, 소재지, 업종, 예비조사, 본조사, 수행기관, 성명),
    file_name="사업장_개요.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
