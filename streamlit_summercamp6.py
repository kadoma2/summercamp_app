import streamlit as st
from selenium import webdriver
import chromedriver_binary
import time
import random

# クリックの関数
def click(xpath):
    driver.find_element("xpath", xpath).click()

title = st.text_input('Your name', '')

if st.button("ANSWEAR!") :
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScpQzUYNDGwx0Y0a1a6VMl4Fp96zSj79VCtqXZbIt3H6uURCQ/viewform?usp=pp_url&entry.1079300137='
    result_url = (url + title)
    st.write(title + "で回答済みです")

    #url = 'https://docs.google.com/forms/d/e/1FAIpQLScpQzUYNDGwx0Y0a1a6VMl4Fp96zSj79VCtqXZbIt3H6uURCQ/viewform?usp=pp_url&entry.1079300137='+body_temp

    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.get(result_url)

    moving_login_button = '/html/body/div[2]/div/div[2]/div[3]/div[2]'
    time.sleep(1)

    time.sleep(1)
    submit_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div'
    click(submit_button)

    #print("Done!")

    driver.close
    # メモリーを食い散らかすのでちゃんと終了しましょう
    driver.quit

else :
    pass

