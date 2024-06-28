import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

dataset = pd.read_csv("world cup new2.csv")

st.set_page_config(page_title="T20 World Cup Data Analysis",page_icon="🏟")

with st.sidebar:
    selected = option_menu(
        menu_title='Menu 📁',
        options=["Home🏠", "Projects📚", "Search🔍","Attributes📒", "About us🪪","Contacts📞"]
    )




if selected == "Home🏠":
    st.write(dataset)

star=0
if selected=="Projects📚":
    star=st.selectbox('Select Plot',['1.Bar','2.Histogram','3.Pie chart' ,'4.Line plots' ,'5.Scatter plots'])
if star=='1.Bar':
    if st.button('►Bar plot  📊'):
     st.subheader("Bar Plot ")
     fig,ax=plt.subplots()
     nation= dataset.groupby('Winner Team')['Player Of The Match'].count()
     plt.bar(nation.index, nation.values,color='Black')
     plt.xlabel('Team')
     plt.ylabel('MOST PLAYER OF THE MATCH IN THE WORLD CUP')
     plt.title('player count')
     plt.xticks(rotation=90)
     st.pyplot(fig)
    
if star=='2.Histogram':
    if st.button('  ►Hist Plot 📶'):
     st.subheader("Histogram Plot ")
     fig,ax=plt.subplots()
     top_two_nations = dataset['Winner Team'].value_counts().nlargest(10).index.tolist()
     filtered_dataset = dataset[dataset['Winner Team'].isin(top_two_nations)]
     plt.hist(filtered_dataset['Winner Team'], bins=25, color='grey')
     plt.xlabel('Winner Team')
     plt.ylabel('Number of Wins')
     plt.title(' Wins by Top Ten Nations')
     plt.xticks(rotation=90)
     plt.tight_layout()
     st.pyplot(fig)

if star=='3.Pie chart':
   if st.button('►Pie Plot🛞'):
    st.subheader("Pie Plot ")
    fig,ax=plt.subplots()
    winner_team_counts = dataset['Winner Team'].value_counts().sort_values(ascending=False).head(10)
    plt.pie(winner_team_counts, labels=winner_team_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart of Winner Teams')
    plt.axis('equal')
    st.pyplot(fig)

if star=='4.Line plots':
   if st.button('►Line plots  📈'):
    st.subheader("Line Plots ")
    fig,ax=plt.subplots()
    plt.plot(dataset['Winner Team'].head(10),dataset['Winning Team Score'].head(10),color='r')

    plt.title('winning team margin')
    plt.xlabel('Teams')
    plt.ylabel('Score of winning team')

    plt.grid()
    plt.xticks(rotation=90)
    plt.legend(['Winning Team Score'])
    st.pyplot(fig)

    fig,ax=plt.subplots()
    plt.plot(dataset['Losing Team'].head(10),dataset['Losing Team Score'].head(10),color='b')
    plt.title('Losing team margin')
    plt.xlabel('Teams')
    plt.ylabel('Score of Losing team')

    plt.grid()
    plt.xticks(rotation=90)
    plt.legend(['Losing Team Score'])
    st.pyplot(fig)

if star=='5.Scatter plots':
   if st.button('►Scatter plot 📉'):
    st.subheader("Scatter Plot ") 
    fig,ax=plt.subplots()
    dataset = dataset.rename(columns={'Group/Semi Final/Final': 'Match Stage'})
    final_matches = dataset[dataset['Match Stage'] == 'Final']
    column1 = 'Winning Team Score'
    column2 = 'Winner Team'
    plt.scatter(final_matches[column1], final_matches[column2],color='Black')
    plt.xlabel("Winning Team Score")
    plt.ylabel("Winner Team")
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.title('Final Matches')
    st.pyplot(fig)



if selected == "Search🔍":
    player_name = st.text_input("Enter the player name ")
    if player_name:
        results = dataset[dataset['Player Of The Match'] == player_name]
        # Display results if any
        if not results.empty:
            st.write(results)  # Assuming you want to display all columns

    team_name = st.text_input("Enter the team name")
    if team_name:
        results = dataset[dataset['Winner Team'] == team_name]
        if not results.empty:
            st.write(results[['Result', 'Venue']])  # Display specific columns

    match_bw = st.text_input("Enter the team names")
    if match_bw:
        between = dataset[dataset['Match Between'] == match_bw]
        if not between.empty:
            st.write(between[['Winner Team', 'Winning Team Score', 'Losing Team', 'Losing Team Score']])
        else:
            st.write("No results found for the entered team names.")  # Plural for consistency

    date=st.text_input("Enter the date of the match")
    if date:
       time=dataset[dataset['Date']==date]
       if not time.empty:
          st.write(time[['Match Between','Winner Team','Losing Team']])

if selected == "Attributes📒":
    column_names = dataset.columns
    label = "Select columns to display"
    selected_columns = st.multiselect(label,column_names)
    
    if selected_columns:
        st.write("Selected columns data:")
        st.dataframe(dataset[selected_columns])
    else:
        st.write("Please select columns to display the data.")      
    



if selected=="About us🪪":
   st.title("About us")
   st.subheader("This website provides a detailed analysis of the T20 World Cup from 2007 to 2021. It offers comprehensive records for each World Cup, represented through various plots such as bar plots, pie plots, histograms, scatter plots, and line plots. We utilized powerful Python libraries, including NumPy for numerical operations, pandas for data manipulation, matplotlib for plotting, and Streamlit for creating interactive web applications. Additionally, the site includes interactive features that allow users to filter and explore the data in more depth.")
   st.markdown("---")
   st.markdown("Location : Mumbai 📍")

if selected=="Contacts📞":
   st.subheader("Contact Details")
   st.markdown("**Name:** Anant Maurya ")
   st.markdown("**Phone No:** 9152990014")
   st.markdown("[**GitHub Profile**](https://github.com/mauryaanant005)")
   st.markdown("**Name:** Rayyan Bhati")
   st.markdown("**Phone No:** 8779811107")
   st.markdown("[**GitHub Profile**](https://github.com/RAYYAN2906)")
   st.markdown("**Name:** Anas Malkani")
   st.markdown("**Phone No:** 7039372198")
   st.markdown("[**GitHub Profile**](https://github.com/ANASMALKANI189)")
   st.markdown("**Name:** Manas Londhe")
   st.markdown("**Phone No:** 8850205475")
   st.markdown("[**GitHub Profile**](https://github.com/GamerMANAS09)")
