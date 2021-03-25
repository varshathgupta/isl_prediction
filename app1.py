import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# loading 1st data set
file1="dataset/All_Matches.csv"
allmatches_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")

# loading 2nd data set
file1="dataset/Match_Info.csv"
matchinfo_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")

# loading 3rd data set
file1="dataset/Season_Teams.csv"
seasonteams_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")


# loading 4th data set
file1="dataset/Teams_Profile.csv"
tmprof_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")

# loading 5th data set
file1="dataset/Player_Bio.csv"
playerbio_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")


#st.sidebar.header('User Input Feaature')
def about():
    
    st.image("logo.png")
    st.title("Hello All ! ")
    st.write(
        """
                     
        This  app built for my final year project in my Bachelours Degree.

        From the app the user may get intrest in ISL and start loving on that event.

        The app is build by **Muthu Siva Balaji** of Final Year in Bsc(CS)
        
        This app performs a stats about ISL matches from 2014 to 2017.

        Libraries used in this application is 

        * **Streamlit**
        * **Pandas** 
        * **Matplotlib**
        * **Seaborn** 
        * **Numpy**
        * **base64**  

        """
    )

def dataset():

    st.title("Loading match info dataset")

    nav_dataset = ["Data of seasons, team names, date & time, goal information ",
    "Data of stadium, attendance, referee and match ID",
    " Data of playoff playing information",
    "Data of foundation date, full names, nick names, home stadium, capacity and team codes.",
    "Data of playing team names, dob, height and playing position information"
    ]


    choice_dataset = st.sidebar.radio("Select Your needy",nav_dataset)


    def fun1():
        st.markdown("""

        * This dataset provides a match wise detail of ISL Seasons from 2014 to 2017 in India, including seasons, team names, date & time, goal information and match round.
        """)
        st.write(allmatches_df.head())

    def fun2():
        st.markdown("""
        * This dataset provides a match wise detail of ISL Seasons from 2014 to 2017 in India, including stadium, attendance, referee and match ID
        """)
           
        st.write(matchinfo_df.head())


    def fun3():
        st.markdown("""
        * This dataset provides a **season & team wise detail of ISL Seasons from 2014 to 2017 in India**, including seasons, team names, team code and playoff playing information.
        """)
        st.write(seasonteams_df.head())


    def fun4():
        st.markdown("""
        * This dataset provides a **team wise detail of ISL Seasons from 2014 to 2017** in India, including foundation date, full names, nick names, home stadium, capacity and team codes.
        """)
        st.write(tmprof_df.head())


    def fun5():
        st.markdown("""
        * This dataset provides a **season wise detail of ISL Players from 2014 to 2017 in India**, including seasons, playing team names, dob, height and playing position information.
        """)
        st.write(playerbio_df.head())





    if choice_dataset == "Data of seasons, team names, date & time, goal information":
        fun1()
           


def eda():
    st.title("Data Processing")

    nav_eda = ["match count","stadium count","seasonwise matches","Attendance distribution"]
    choice_eda = st.sidebar.radio("Select Your needy",nav_eda)




nav = ["About","ISL Data Set","EDA"]

choice = st.sidebar.radio("Select Your needy",nav)

if choice == "About":
    about()

if choice  == "ISL Data Set":
    dataset()

if choice == "EDA":
    eda()