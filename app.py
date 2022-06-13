# Import all the packages
import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

# Load The Datasets
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df = preprocessor.preprocess(df,region_df)

# Set the Title
st.set_page_config(layout="centered", page_icon="🤾‍♂️", page_title="Olympic Sport Analysis Dashboard")
st.title("🤾‍♂️Olympic Sport Analysis Dashboard")
st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Description','Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

# Olympics Analysis
st.sidebar.title("Olympics Analysis")
if user_menu == 'Description':
    with st.expander("What is this app about?"):
        st.markdown("""
                    ######  The Olympic Games is a well-known sporting platform which is recognized all over the world, has been distinguished from the late 19th century. Its origin however can be traced back to the Greek empire, at around 3,000 years ago, which consisted only of sprint race, and was held in Greece’s city Olympia only accessible to freeborn Greek people (Young & Abraham, 2020). It has grown since then and now has become a hub for all the athletes worldwide to demonstrate their abilities in more than 28 individual sporting contests. Currently, it is held every 2 years in different countries, with names Summer Olympics and Winter Olympics, both having their own set of games (Young & Abraham, 2020). It has become a place which reflects the power of the individual contestants and has become a source of pride for the countries they represent.
                    ### Motivation and Research Question
                    ###### Olympics has a rich history, spanning from 1896 till 2018, and has been a part of history. So, it is an interesting topic to see how the historical events have affected the specifics of Olympics and how it has been changing till date. Hence, this report attempts to build around the following questions, with some connection to historical happenings where suitable:
                    - 1. What effect does the host country have in the medals won at the Olympics?
                    - 2. Is the age of winning Olympics changing?
                    - 3. How many countries were participated in this event?
                    - 4. Overall Medal Tally
                    """)
    with st.expander("Literature View: "):
        st.markdown("""
                        The advantage of host country in any sporting activity is well known, as the participants will have familiarity of the field, and also there is a great support from the home crowd. Host countries are expected to win 3 times the medals that they were winning while playing as away (Clarke, 2000). Being a host nation and also having a communist background is also going to have a positive effect in the number of medals won (Bian, 2005).
                        It is found that a country’s socio-economic variables, such as GDP affects the country’s performance in the Olympics by a great factor. Country’s population and its GDP is seen to have a correlation with the number of medals won in Olympics (Bian, 2005).
                        Age factor is also one of the important ones when it comes to sports and even among the athletes of the same age, relative age effect (RAE) comes into factor which determines who triumphs (Fletcher & Sarkar, 2012). RAE states that an athlete can have more advantage as compared to another who is younger by almost a year with respect to maturity, experience and early specialization (Neill, Cotton, Cuadros & Connor, 2016).
                        Olympics has been part of the history, and has affected, and also has been affected by the history. 
                        Olympic Games has made major social and political impacts throughout the history like including women in sports, has taken a stand against racial matters, promoted civil rights, has unified countries and even has been a tool to demonstrate power by different countries (O’Connell). Similarly, the politics of the countries such as racial separation, terrorism, World Wars and the Cold War have also affected Olympics at different times in the history (Dwyer & McMaster, 2018).
                    """)
    with st.expander("Approach: "):
        st.markdown("""
                    To answer the questions, three datasets were used namely, “120 years of Olympic history: athletes and results[1]”, “Gapminder GDP per capita, constant PPP dollars- v25[2]” and “Gapminder Total Population v6[3]”. 
                    The Olympics dataset had the names of participants, their demographics, which sport they participated in and on which Olympic games. Gapminder’s GDP per capita dataset consisted of GDP of countries from 1960 forecasted till 2040, and their Population dataset had populations of all the countries of the world from 1800 till 2019 and forecasted from there onwards till 2100. 
                    A custom dataset was also created that maps the cities mentioned in the Olympics dataset to country names.
                    Visualizations were created in Tableau and Python. Initial data cleaning was done on Excel, and visualization specific data manipulation were carried out as needed on Python.
                    """)

    with st.expander("Conclusion: "):
        st.markdown("""
                        It is clear that the host countries have always a better chance of winning medals in the Olympics; 
                        they can win at least 10–20 percent more medals. 
                        Looking at the economic effect, even though country’s population and per capita GDP affected the number of medals won in the past, the total GDP of the country is more significant to determine the winnings in the recent years. 
                        With the age factor, the age range of players winning medals has decreased over the years, and an optimal age for each sport can be identified in the recent years. 
                        Thus, there is a high chance for an athlete from a host country with high GDP, whose age range falls in the optimum age range for the sport to win a medal in the Olympics.
                        """)
        st.markdown(
            """
            <style>
            [data-testid='stSidebar"][aria=expanded="true"] > div:first-child{
                width: 350px
            }
            [data-testid='stSidebar"][aria=expanded="false"] > div:first-child{
                width: 350px
                margin-left: -350px
            }
            </style>

            """,
            unsafe_allow_html=True,
        )
        st.video('https://youtu.be/rW_fwcmyIfk')



# Medal Tally
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in" + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " Overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance is " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    with st.expander("More info about Overall Analysis:"):
        st.markdown("""
                    Overall Analysis of the olympic medal System to show you the how many
                    Edition was organised in the past 120 years. It will show you the which 
                    country had hosted the event and played all around the world. 
                    """)
    st.title("Top Statistics")
    top_stat = st.checkbox('Load Data', key=int)
    if top_stat:

        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        col1,col2,col3 = st.columns(3)
        with col1:
            st.header("Editions")
            st.subheader(editions)
        with col2:
            st.header("Hosts")
            st.subheader(cities)
        with col3:
            st.header("Sports")
            st.subheader(sports)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Events")
            st.subheader(events)
        with col2:
            st.header("Nations")
            st.subheader(nations)
        with col3:
            st.header("Athletes")
            st.subheader(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title(" 1. Participating Nations over the years")
    participation = st.checkbox('Load Graph')
    if participation:
        st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title(" 2. Events over the years")
    with st.expander("Notes: "):
        st.markdown("""Every year olympic organisation  had added more games in the events.
                The first modern Olympic Games in 1896 had a total of 43 events for male-only competitors and teams; 
                this climbed above 150 events in 1972, and has generally fluctuated between 150 and 180 events since this time. 
                For women's and mixed events the number has steadily grown with each tournament, but the number of events did not surpass 100 until 200. 
                The Paris Games in 1900 had 93 events for male competitors, however the number of female and mixed events did not exceed this figure until 1996.
                Throughout Olympic history, there have been a number of events that are exclusively for women, such as rhythmic gymnastics and synchronized swimming, 
                 although there are many more male-only events, such as the pommel horse and rings, and there is a larger number of male weight classes in weightlifting and combat events. 
                There are also several mixed events, such as tennis and badminton (with set numbers of male and female competitors) whereas male and female athletes compete on equal terms in equestrian and sailing events
                (although sailing has become increasingly segregated in recent years). 
                In the 2020 Olympics in Tokyo, a number of mixed shooting events, table tennis doubles, and swimming and sprinting relays were introduced in an attempt to improve participation among female athletes.
                """)
    ecvents_over = st.checkbox('Load Graph', key=int)
    if ecvents_over:
        st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name")
    st.title(" 3. Athletes over the years")
    Athlete = st.checkbox('Load Graph', key=str)
    if Athlete:
        st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),annot=True)
    every_sport = st.checkbox('Load Heatmap')
    if every_sport:
        st.pyplot(fig)

    st.title(" 4. Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)
    with st.expander("Notes: "):
        st.markdown(""" 
                        This statistic shows the athletes with the number of Summer Olympic victories since 
                        the start of the Olympic Games from 1896 to 2021. Michael Phelps, the legendary American swimmer, 
                        won 23 gold medals across his participation in the games.
                        """)

# Country wise analysis
if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select a Country',country_list)


    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.header(" 1. " + selected_country + " Medal Tally over the years")
    over_the_year = st.checkbox('Load Graph')
    if over_the_year:
        st.plotly_chart(fig)

    st.header(" 2. " + selected_country + " excels in the following sport")
    pt = helper.country_event_heatmap(df,selected_country)
    fig,ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(pt, annot=True)
    excel_sport = st.checkbox('Load Graph', key=str)
    if excel_sport:
     st.pyplot(fig)

    st.header("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

# Athlete wise Analysis
if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()


    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000,height=600)
    st.title(" 1. Distribution of Age")
    Dist_age = st.checkbox('Load Graph')
    if Dist_age :
        st.plotly_chart(fig)


    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title(" 2. Distribution of Age wrt Sports(Gold Medalist)")
    wrt_sport= st.checkbox('Load Graph', key=int)
    if wrt_sport:
        st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title(" 3. Height vs Weight")
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(temp_df['Weight'],temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=60)
    st.pyplot(fig)

    st.title(" 4. Men Vs Women Participation Over The Years")
    with st.expander("Notes: "):
        st.markdown("""
                    The share of male athletes at the Summer Olympics has always been greater than the share of female athletes. 
                    The first modern Olympic Games in Athens in 1896 was exclusively for male competitors, and although some female events were introduced in Paris in 1900, the share of events was just 2.2 percent. 
                    Over the next century, the ratio of female to male events has gradually narrowed, and at a faster rate in recent decades, reaching almost 49 percent in Tokyo 2020. 
                    The Tokyo Games in particular saw the introduction of several mixed events, in an attempt to increase this participation further; these included mixed shooting events and both sprinting and swimming mixed relays.
                    
                    In the history of the Summer Olympics, the share of events for women athletes has grown gradually; from no events at all in 1896, to a 51.3 percent share in 2020. Growth was gradual and slow, crossing the 25 percent mark in 1984, and exceeding 50 percent in 2020. 
                    It is important to note, however, that a number of these events are mixed, for both male and female competitors, and the total number of single-gender events remains slightly higher for men. The majority of sports have mirrored events for male and female competitors, 
                    and there had been an increased number of mixed events in recent years, with a particularly high number of mixed events added in Tokyo 2020.
                    """)
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male","Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    men_vs_women = st.checkbox('Load Graph', key=str)
    if men_vs_women:
        st.plotly_chart(fig)



