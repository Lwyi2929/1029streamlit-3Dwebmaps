import streamlit as st

# 這裡放所有您想在首頁顯示的內容
st.title("歡迎來到我的 3D GIS 專案！")
st.write("這是一個使用 Streamlit 建立的3D互動式地圖應用程式。")


# 直接將 MP4 影片的 URL 傳給 st.video()
video_url = "埋要.mp4"

st.write(f"正在播放影片： {video_url}")

st.video(video_url)

# 直接將 照片的 URL 傳給 st.image()
st.write("下面是一張可愛小孩的照片：")
image_url = "可愛小孩.jpg"
st.image(image_url)