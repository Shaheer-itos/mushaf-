import streamlit as st

import requests

st.title("Mushaf Web APP")

allSurahsData= requests.get("https://api.alquran.cloud/v1/surah").json()["data"]

surahs=[]

for i in allSurahsData:
    surahs.append(f"{i["number"]} | {i["name"]} | Ayahs : {i["numberOfAyahs"]}")

selectedSurah= st.selectbox("Choose The Surah ",surahs)

surahNumber= selectedSurah.split(" | ")[0]

allAyahsData= requests.get(f"https://api.alquran.cloud/v1/surah/{surahNumber}/ar.sudaisshuraymnaeemsultan").json()["data"]

allAyahs=allAyahsData["ayahs"]

surahsAudio=allAyahsData["audio"]

if surahsAudio:
    st.audio(surahsAudio)

for a in allAyahs:

    st.write(a["numberInSurah"])

    st.write(a["text"])


    








