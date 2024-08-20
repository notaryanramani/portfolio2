import streamlit as st

st.set_page_config(page_title='Aryan Ramani')

img, info = st.columns([0.3, 0.7], vertical_alignment='bottom')

with info:
    st.title('Aryan Ramani')
    icons, text = st.columns([0.05, 0.95])
    with icons:

        st.markdown('''
                    📍  
                    🎓   
                    📞   
                    ✉︎   
                    ''')
    with text:
        st.markdown('''
                    Dublin, Ireland  
                    MSc Artificial Intelligence   
                    +xx-xxxx-xxxx   
                    aryanramani67@gmail.com
                    ''')

    st.markdown('''[LinkedIn](https://www.linkedin.com/in/aryan-ramani-a516b5212/) | [Github](https://github.com/notaryanramani)''')
with img:
    st.image('src/img.png')

st.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)
st.header('Summary', divider='gray')

st.write('''Machine Learning Engineer with 3 months of Industry Experience and 1+ year of hands-on experience with project development.  
         
I like to train neural networks on fairly large datasets from scratch.
''')

st.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)
st.header('Experience', divider='gray')
pos, company = st.columns([0.7, 0.3])
with pos:
    st.markdown('<div style = "font-size: 28px;"><b>Machine Learning Engineer Intern</b></div>Feb 2024 - Apr 2024', unsafe_allow_html=True)

with company:
    st.markdown('<div style = "text-align: right; font-size: 28px;"><b>Factacy.Ai</b></div><div style = "text-align: right;">Gurugram, India</div>', unsafe_allow_html=True)

st.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)
st.header('Projects', divider='gray')

col1, col2, col3 = st.columns(3, vertical_alignment='center')
with col1:
    project1 = col1.container(border=True, height=260)
    project1.image('src/wavenet.jpg')
    project1.write('<a href="https://github.com/notaryanramani/wave-gpt">WaveGPT </a><br> A GPT enchanced with WaveNet', unsafe_allow_html=True)
    project1.write('<a href="https://medium.com/@aryanramani67/wavegpt-wavenet-gpt-86260561964f">Blog</a>', unsafe_allow_html=True)

    project2 = col1.container(border=True, height=250)
    project2.image('src/mr.png')
    project2.write('<a href="https://github.com/notaryanramani/wave-gpt">Mindvault </a> <br> A Transformer with memory using FAISS Vector Database', unsafe_allow_html=True)

with col2:
    project1 = col2.container(border=True, height=260)
    project1.image('src/sd.jpg')
    project1.write('<a href="https://github.com/notaryanramani/stable-diffusion">StaBERT Diffusion </a>  <br>Stable Diffusion with BERT Embeddings', unsafe_allow_html=True)

    project2 = col2.container(border=True, height=250)
    project2.image('src/ddpm.png')
    project2.write('<a href="https://github.com/notaryanramani/min-ddpm">Mini DDPM </a> <br>A minimal Denoising Diffusion Probablistic Model with Classifier Free Guidance', unsafe_allow_html=True)

with col3:
    project1 = col3.container(border=True, height=260)
    project1.image('src/gemini.jpg')
    project1.write('<a href="https://github.com/notaryanramani/llm-chat-app">LLM ChatApp </a> <br> A simple chat app with Google Gemini and Langchain', unsafe_allow_html=True)

    project2 = col3.container(border=True, height=250)
    project2.image('src/rec.png')
    project2.write('<a href="https://github.com/notaryanramani/recommendation-system">Recommendation App </a> <br> Movies & Book Recommendations WebApp along with API', unsafe_allow_html=True)



st.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)
st.header('Education', divider='gray')

uni, time = st.columns([0.7, 0.3], vertical_alignment='center')
with uni:
    st.markdown('<div style = "font-size: 24px;"><b>MSc Artificial Intelligence</b></div>National College of Ireland', unsafe_allow_html=True)
    

with time:
    st.markdown('<div style = "text-align: right"><b>Dublin, Ireland</b></div><div style = "text-align: right;">Sep 2024 - Ongoing</div>', unsafe_allow_html=True)
st.write('')
uni, time = st.columns([0.7, 0.3], vertical_alignment='center')
with uni:
    st.markdown('<div style = "font-size: 24px;"><b>Bachelors of Computer Applications</b></div>Vivekananda Institute of Professional Studies', unsafe_allow_html=True)
    

with time:
    st.markdown('<div style = "text-align: right"><b>Delhi, India</b></div><div style = "text-align: right;">Dec 2020 - Aug 2023</div>', unsafe_allow_html=True)


