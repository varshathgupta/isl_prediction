import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


import warnings
warnings.filterwarnings('ignore')

from subprocess import check_output
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('ISL Football  Explorer')

st.markdown("""
This app performs a stats about ISL matches from 2014 to 2017|
* Libraries used in this application is 
 **Streamlit, Pandas , Matplotlib , Seaborn , Numpy, base64**  

""")



# loading 1st dataset

st.markdown("""
**Loading match info dataset**
* This dataset provides a match wise detail of ISL Seasons from 2014 to 2017 in India, including seasons, team names, date & time, goal information and match round.
""")

file1="dataset/All_Matches.csv"
allmatches_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")
st.write(allmatches_df.head())

#loading 2nd dataset
st.markdown("""
* This dataset provides a match wise detail of ISL Seasons from 2014 to 2017 in India, including stadium, attendance, referee and match ID
""")

file1="dataset/Match_Info.csv"
matchinfo_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")
st.write(matchinfo_df.head())

# loading 3rd dataset

st.markdown("""
* This dataset provides a **season & team wise detail of ISL Seasons from 2014 to 2017 in India**, including seasons, team names, team code and playoff playing information.
""")
file1="dataset/Season_Teams.csv"
seasonteams_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")
st.write(seasonteams_df.head())

# loading 4th dataset

st.markdown("""
* This dataset provides a **team wise detail of ISL Seasons from 2014 to 2017** in India, including foundation date, full names, nick names, home stadium, capacity and team codes.
""")

file1="dataset/Teams_Profile.csv"
tmprof_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")
st.write(tmprof_df.head())

# loading 5th dataset

st.markdown("""
* This dataset provides a **season wise detail of ISL Players from 2014 to 2017 in India**, including seasons, playing team names, dob, height and playing position information.
""")

file1="dataset/Player_Bio.csv"
playerbio_df = pd.read_csv(file1,encoding='ISO-8859-1',sep="|")
st.write(playerbio_df.head())

# findinding missing data 

st.markdown("""
**Missing data identification**
* This is done to identify the data sets, on which Pandas profiling must be done.
""")

def missing_data(data):
    total = data.isnull().sum().sort_values(ascending = False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
st.write(missing_data(allmatches_df))


# Data preprocessing 

# match count
st.markdown("""
## Data Preprocessing
* Number of matches played by each team
""")
st.write(allmatches_df['Team1_Code'].value_counts())

# stadium count
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

# matches seasonwise
st.markdown("""
**How the no.of Matches played season wise**
""")
match_df.reset_index(inplace=True)
seasonMatches =match_df.groupby(['Season'])['MatchID'].count().reset_index()
seasonMatches.columns=['Seasons','TotalMatchesPlayed']
st.write(seasonMatches)

seasonMatches.plot(x='Seasons', y='TotalMatchesPlayed', kind='bar')
plt.xlabel('ISL season year',fontsize=15)
plt.ylabel('No of ISL matches ',fontsize=15)
plt.title('No of matches played per year',fontsize=20)
st.pyplot()

# Attendance distribution
st.markdown("""
**Attendance Distribution**
""")
sns.set(color_codes=True)                                               
sns.set_palette(sns.color_palette("muted"))
sns.distplot([tuple(match_df.Attendance)],bins=10)

plt.xlabel('Attendance in 1000', color='blue')
plt.title('ISL Attendance Distribution',color='red',fontsize=20)
st.pyplot()
