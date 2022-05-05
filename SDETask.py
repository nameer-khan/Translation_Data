# -*- coding: utf-8 -*-
"""
Created on Thu May  5 03:01:07 2022

@author: namee
"""
import streamlit as st
import pandas as pd 
import numpy as np
import googletrans
from googletrans import Translator
import warnings
import os
import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import pandas as pd 
import sys
sys.tracebacklimit = 0

warnings.simplefilter("ignore", UserWarning)

list_of_language=['Punjab','Marathi','Telugu','Hindi']
list_code_language=['pa','mr','te','hi']







def uploadcsv():
    st.subheader("Take-home Assignment - SDE \n Wadhwani AI")
    df = st.file_uploader("Upload CSV",type=["csv"])
    if df is not None:
        file_details = {"filename":df.name, "filetype":df.type,
                            "filesize":df.size}
        #st.write(file_details)
        df = pd.read_csv(df)
        st.dataframe(df)
    return df



class FileDownloader(object):
	
	def __init__(self, data,filename='myfile',file_ext='csv'):
		super(FileDownloader, self).__init__()
		self.data = data
		self.filename = filename
		self.file_ext = file_ext

	def download(self):
		b64 = base64.b64encode(self.data.encode()).decode()
		new_filename = "{}_.{}".format(self.filename,self.file_ext)
		st.markdown("#### Download File ###")
		href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!</a>'
		st.markdown(href,unsafe_allow_html=True)


def translation_work(df,lang,i):
    translator = Translator()
    translations = {}
    if(i==1):
        for column in df.columns:
            if(df[column].dtypes!='int64' ):
                unique_elements = df[column].unique()
                for element in unique_elements:
                    translations[element] = translator.translate(element,dest=lang).text
    
    df.replace(translations,inplace=True)
    return df

def choose_language(list_of_language,list_code_language):
    option = st.selectbox('Which Language you want to convert to?',list_of_language)
    'You selected: ', option
    j=0
    for i in list_of_language:
        if(i==option):
            return list_code_language[j]
        j+=1
    return 'en'
    
def display(df,lang):
    #st.write(df)
    name=os.getlogin()
    name_of_file="SDE_"+lang
    path="C:/Users/"
    path=os.path.join(path,name,"Downloads",name_of_file)
    ##df.to_csv(path)
    return name_of_file

    
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

i=0
try:
    df=uploadcsv()
    i=1
    
except:
    st.error("Upload CSV")
    st.stop() 
try:
    lang=choose_language(list_of_language, list_code_language)
    df=translation_work(df, lang,i)
    name_of_file=display(df, lang) 
    st.dataframe(df)
    download = FileDownloader(df.to_csv(),filename=name_of_file,file_ext='csv').download()
except AttributeError:
    pass


   

