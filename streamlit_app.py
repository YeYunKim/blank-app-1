import streamlit as st

st.set_page_config(
    page_title="서울 데이트 코스 추천",
    page_icon="❤️",
)

st.title("❤️ 서울 감성 데이트 코스")

st.write("""
북촌 한옥마을, 경복궁, 덕수궁 돌담길을 중심으로  
감성 데이트 코스를 추천하는 웹 애플리케이션입니다.
""")

st.image("https://images.unsplash.com/photo-1517154421773-0529f29ea451")

st.header("추천 장소")

st.markdown("""
- 🏯 경복궁
- 🌸 북촌 한옥마을
- 🍂 덕수궁 돌담길
""")

st.success("왼쪽 사이드바에서 다른 페이지를 눌러보세요!")