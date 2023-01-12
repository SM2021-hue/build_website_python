import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image




# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":smile:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ----load assets---------
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_llbjwp92qL.json")
img_contact_form = Image.open("images/img_1.png")
img_lottie_animation = Image.open("images/img_2.png")





# -----HEADER-----
with st.container():
    st.subheader("Hi! I am Suneeta :wave:")
    st.title("An Aspiring MLE")
    st.write("I am trying to find ways to use python, Machine Learning and Bioinformatics to make the world a better place to live.")
    st.write("[Learn More About My Work >](https://github.com/SM2021-hue)")

# ----What I do --------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("###")
        st.write(
            '''
            - I code in Python, SQL, R and Linux
            - I am a life long learner
            - I like to enhance my ML and DL knowledge on a daily basis
            '''
        )
        # st.write("[YouTube Channel >](https://youtube.com/")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Let's host our apps with Streamlit App")
        st.write(
                """
                It's easy to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
                """
            )


