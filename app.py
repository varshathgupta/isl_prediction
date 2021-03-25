import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #111;
}
</style>
    """, unsafe_allow_html=True)

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
    st.markdown("""
    <style>
    body {
        color: #fff;
        background-color: #111;
    }
    </style>
        """, unsafe_allow_html=True)
    
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

    nav_dataset = ["Data of seasons, team names, date & time, goal information",
    "Data of stadium, attendance,referee and match ID",
    "Data of playoff playing information",
    "Data of foundation date,full names, nick names,home stadium,capacity and team codes",
    "Data of playing team names,dob,height and playing position information"
    ]


    choice_dataset = st.sidebar.radio("Select Your needy",nav_dataset)


    def fun1():
        st.markdown("""

        * This dataset provides a match wise detail of ISL Seasons from 2014 to 2017 in India, including **seasons, team names, date & time, goal information and match round**.
        """)
      
        st.write(allmatches_df.head(15))

    def fun2():
        st.markdown("""
        * This dataset provides a match wise detail of ISL Seasons from 2014 to 2017 in India, including **stadium, attendance, referee and match ID**.
        """)
           
        st.write(matchinfo_df.head(15))


    def fun3():
        st.markdown("""
        * This dataset provides a season & team wise detail of ISL Seasons from 2014 to 2017 in India,including **seasons, team names, team code and playoff playing information**.
        """)
        st.write(seasonteams_df.head(15))


    def fun4():
        st.markdown("""
        * This dataset provides a **team wise detail of ISL Seasons from 2014 to 2017** in India, including foundation date, full names, nick names, home stadium, capacity and team codes.
        """)
        st.write(tmprof_df.head(15))


    def fun5():
        st.markdown("""
        * This dataset provides a season wise detail of ISL Players from 2014 to 2017 in India, including **seasons, playing team names, dob, height and playing position information**.
        """)
        st.write(playerbio_df.head(15))


    if choice_dataset == "Data of seasons, team names, date & time, goal information":
        fun1()

    if choice_dataset == "Data of stadium, attendance,referee and match ID":
        fun2()
    
    if choice_dataset == "Data of playoff playing information":
        fun3()

    if choice_dataset == "Data of foundation date,full names, nick names,home stadium,capacity and team codes":
        fun4()
    
    if choice_dataset == "Data of playing team names,dob,height and playing position information":
        fun5()



    
    
           


def eda():
    

    nav_eda = ["match count","stadium count","Seasonwise matches","Attendance distribution"]
    choice_eda = st.sidebar.radio("Select Your needy",nav_eda)

    def fun1():
        st.markdown("""
        ## Data Preprocessing
        * Number of matches played by each team
        """)
        
        total_matches = allmatches_df['Team1_Code'].value_counts() + allmatches_df['Team2_Code'].value_counts() 
        st.write(total_matches)
        plt.plot(total_matches)
        plt.ylabel('Match counts')
        plt.xlabel('Team Names')
        st.pyplot()

    def fun2():
        m_df=pd.merge(left = matchinfo_df, right = allmatches_df, on = 'MatchID', how ='outer')
        match_df = m_df.set_index('MatchID')
        st.markdown("""
        * **Number matches held in each stadium in India  from 2014 to 2017**
        """)
        st.write(match_df['Stadium'].value_counts())

        st.markdown("""
        **How the Matches Distributed across all the seasons?**
        """)

        sns.set(color_codes=True)                                               
        sns.set_palette(sns.color_palette("muted"))
        sns.distplot([tuple(match_df.Season)],bins=4)

        plt.xlabel('ISL seasons', color='blue')
        plt.title('ISL Match Distribution across the Years',color='red',fontsize=20)
        st.pyplot()

    def fun3():
        # matches seasonwise
        st.markdown("""
        **How the no.of Matches played season wise**
        """)
        m_df=pd.merge(left = matchinfo_df, right = allmatches_df, on = 'MatchID', how ='outer')
        match_df = m_df.set_index('MatchID')
        match_df.reset_index(inplace=True)
        seasonMatches =match_df.groupby(['Season'])['MatchID'].count().reset_index()
        seasonMatches.columns=['Seasons','TotalMatchesPlayed']
        st.write(seasonMatches)

        seasonMatches.plot(x='Seasons', y='TotalMatchesPlayed', kind='bar')
        plt.xlabel('ISL season year',fontsize=15)
        plt.ylabel('No of ISL matches ',fontsize=15)
        plt.title('No of matches played per year',fontsize=20)
        st.pyplot()
    
    def fun4():
        # Attendance distribution
        st.markdown("""
        **Attendance Distribution**
        """)
        m_df=pd.merge(left = matchinfo_df, right = allmatches_df, on = 'MatchID', how ='outer')
        match_df = m_df.set_index('MatchID')
        sns.set(color_codes=True)                                               
        sns.set_palette(sns.color_palette("muted"))
        sns.distplot([tuple(match_df.Attendance)],bins=10)

        plt.xlabel('Attendance in 1000', color='blue')
        plt.title('ISL Attendance Distribution',color='red',fontsize=20)
        st.pyplot()

    if choice_eda == "match count":
        fun1()

    if choice_eda == "stadium count":
        fun2()
    
    if choice_eda == "Seasonwise matches":
        fun3()
    if choice_eda == "Attendance distribution":
        fun4()
    





nav = ["About","ISL Data Set","EDA"]

choice = st.sidebar.radio("Select Your needy",nav)

if choice == "About":
    about()

if choice  == "ISL Data Set":
    dataset()

if choice == "EDA":
    eda()