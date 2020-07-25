
import streamlit as st 



def main():
    

  #try: 
      
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">DataScience Made Easy </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    from PIL import Image
    
    #image_loan=Image.open("C:/Users/pratik.anjay/Documents/ML practice/ml4.jpg")
    logo=Image.open("C:/Users/prati/OneDrive/Documents/ML PRACTICE/Images/p11.jpg")
    st.sidebar.image(logo,use_column_width=True)
    st.sidebar.subheader("  ")
    
    st.subheader("What You Want to Learn") 
    choose_model=st.selectbox(label='Pick from Bellow : ',options=[' ','Python for Data Science','NLP','EDA & Data Visualization','Machine Learning Model Deployment','Streamlit'])
    if (choose_model=='Python for Data Science'):
            logo=Image.open("C:/Users/prati/OneDrive/Documents/ML PRACTICE/Images/p8.jpg")
            logo1=Image.open("C:/Users/prati/OneDrive/Documents/ML PRACTICE/Images/p9.jpg")
            
            
            st.write("Data Analysis with Python Part 1 :"" ""https://www.youtube.com/watch?v=DYMAb9uZEuQ&t=57s")
            st.write("Data Analysis with Python Part 2 :"" ""https://www.youtube.com/watch?v=-WwAtXYrV3E&t=33s")
            st.write("Reference Materials :" "https://realpython.com/python-beginner-tips/")
            st.image(logo,use_column_width=True)
            st.sidebar.image(logo1,use_column_width=True)
            
    if (choose_model=='NLP'):
            st.write("Natural Language Processing in Python with TextBlob :"" ""https://www.youtube.com/watch?v=xqnWr0MaX2g&t=1s&pbjreload=101")
            st.write("Sentiment Analysis :"" ""https://www.youtube.com/watch?v=M118JlgFncM&t=14s")
            logo=Image.open("C:/Users/prati/OneDrive/Documents/ML PRACTICE/Images/p7.png")
            st.write("Reference Materials :" "https://elitedatascience.com/python-nlp-libraries")
            st.write("Use Case")
            st.image(logo,use_column_width=True)
            
    if (choose_model=='EDA & Data Visualization'):
              logo=Image.open("C:/Users/prati/OneDrive/Documents/ML PRACTICE/Images/p4.jpg")
              st.write("EDA & Data Visualization :"" ""https://www.youtube.com/watch?v=hyGDbUE5qO4&t=258s")
              st.image(logo,use_column_width=True)
              
    if (choose_model=='Machine Learning Model Deployment'):
            st.write("ML model deployment in Heroku :"" ""https://www.youtube.com/watch?v=bar9E3hqUN8&t=99s")
            st.write("Automated Machine Learning (AutoMl)using Steamlit :"" ""https://www.youtube.com/watch?v=AdzuYSx_pAc&list=PL6RHLk1rGA_flZkELeMNv9Um4hTBKjOxM&index=1")
            logo=Image.open("C:/Users/prati/OneDrive/Documents/ML PRACTICE/Images/p12.png")
            st.write(" ")
            st.image(logo,use_column_width=True)
            
    if (choose_model=='Streamlit'):
            st.write("Ml Streamlit Application :"" ""https://www.youtube.com/watch?v=YA1xJVj9S1Y&list=PL6RHLk1rGA_flZkELeMNv9Um4hTBKjOxM&index=2")
            st.write("Reference Materials :" "https://docs.streamlit.io/en/stable/")
            logo=Image.open("C:/Users/prati/OneDrive/Documents/ML PRACTICE/Images/p6.png")
            st.write(" ")
            st.image(logo,use_column_width=True)
            
                    
if __name__=='__main__':
    main()
