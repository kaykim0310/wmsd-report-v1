import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from io import BytesIO

# 표의 기본 구조(예시)
columns = [
    "부", "팀", "작업명", "단위작업명", "일일 해당작업 시간", "중량(kg)",
    "1호", "2호", "3호", "4호", "5호", "6호", "7호", "8호", "9호", "10호", "11호"
]
data = pd.DataFrame(columns=columns, data=[[""]*len(columns) for _ in range(5)])  # 5행 예시

# 표 입력/수정
st.subheader("근골격계 부담작업 체크리스트")
gb = GridOptionsBuilder.from_dataframe(data)
gb.configure_default_column(editable=True, resizable=True)
grid_options = gb.build()
grid_response = AgGrid(
    data,
    gridOptions=grid_options,
    update_mode='MODEL_CHANGED',
    fit_columns_on_grid_load=True,
    height=300,
    allow_unsafe_jscode=True,
    theme='alpine'
)
edited_df = grid_response['data']

# 엑셀로 저장
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='체크리스트')
    return output.getvalue()

st.download_button(
    label="엑셀로 저장",
    data=to_excel(edited_df),
    file_name="근골격계_부담작업_체크리스트.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
