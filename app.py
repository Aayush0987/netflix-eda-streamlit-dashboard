import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Netflix EDA Dashboard",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Netflix Movies & TV Shows Dashboard")
st.markdown("Exploratory Data Analysis Dashboard built using Streamlit")

@st.cache_data
def load_data():
    return pd.read_csv("netflix_titles.csv")

df = load_data()

total_titles = df.shape[0]
total_movies = df[df['type'] == 'Movie'].shape[0]
total_tv_shows = df[df['type'] == 'TV Show'].shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("🎬 Total Titles", total_titles)
col2.metric("🎥 Movies", total_movies)
col3.metric("📺 TV Shows", total_tv_shows)

# Preprocess date_added for filtering
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Sidebar
st.sidebar.header("🔍 Filters")

# Content type filter
type_filter = st.sidebar.multiselect(
    "Select Content Type",
    options=df['type'].unique(),
    default=df['type'].unique()
)

# Year filter
year_filter = st.sidebar.multiselect(
    "Select Year Added",
    options=sorted(df['year_added'].dropna().unique()),
    default=sorted(df['year_added'].dropna().unique())
)

# Country filter
country_filter = st.sidebar.multiselect(
    "Select Country",
    options=sorted(df['country'].dropna().unique()),
    default=sorted(df['country'].dropna().unique())
)

# Apply filters
filtered_df = df[
    (df['type'].isin(type_filter)) &
    (df['year_added'].isin(year_filter)) &
    (df['country'].isin(country_filter))
]

import plotly.express as px

# KPI calculations (filtered)
total_titles = filtered_df.shape[0]
total_movies = filtered_df[filtered_df['type'] == 'Movie'].shape[0]
total_tv_shows = filtered_df[filtered_df['type'] == 'TV Show'].shape[0]

st.subheader("📊 Content Type Distribution")

# Prepare data for Plotly
type_counts = (
    filtered_df['type']
    .value_counts()
    .reset_index()
)
type_counts.columns = ['type', 'count']

# Plotly bar chart
fig = px.bar(
    type_counts,
    x='type',
    y='count',
    text='count',
    color='type',
    color_discrete_map={
        'Movie': '#E50914',   # Netflix red
        'TV Show': '#221F1F'  # Netflix dark
    },
    title="Distribution of Movies vs TV Shows"
)

# Styling
fig.update_traces(
    textposition='outside',
    textfont_size=14
)

fig.update_layout(
    xaxis_title="Content Type",
    yaxis_title="Number of Titles",
    title_font_size=18,
    showlegend=False,
    template='plotly_white'
)

# Render in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 Content Added Over the Years")

# Group data by year_added
yearly_counts = (
    filtered_df
    .groupby('year_added')
    .size()
    .reset_index(name='count')
    .sort_values('year_added')
)

fig_year = px.line(
    yearly_counts,
    x='year_added',
    y='count',
    markers=True,
    title="Number of Titles Added Over the Years"
)

fig_year.update_traces(
    line=dict(color='#E50914', width=3),
    marker=dict(size=8)
)

fig_year.update_layout(
    xaxis_title="Year Added",
    yaxis_title="Number of Titles",
    title_font_size=18,
    template='plotly_white'
)

st.plotly_chart(fig_year, use_container_width=True)

st.subheader("📊 Movies vs TV Shows Over the Years")

# Group by year and type
year_type_counts = (
    filtered_df
    .groupby(['year_added', 'type'])
    .size()
    .reset_index(name='count')
    .sort_values('year_added')
)

fig_type_year = px.line(
    year_type_counts,
    x='year_added',
    y='count',
    color='type',
    markers=True,
    color_discrete_map={
        'Movie': '#E50914',   # Netflix red
        'TV Show': '#221F1F'  # Netflix dark
    },
    title="Movies vs TV Shows Added Over the Years"
)

fig_type_year.update_traces(
    line=dict(width=3),
    marker=dict(size=7)
)

fig_type_year.update_layout(
    xaxis_title="Year Added",
    yaxis_title="Number of Titles",
    title_font_size=18,
    template='plotly_white'
)

st.plotly_chart(fig_type_year, use_container_width=True)

st.subheader("🎭 Top 10 Genres on Netflix")

# Split and explode genres
genre_df = filtered_df.copy()
genre_df['listed_in'] = genre_df['listed_in'].str.split(', ')
genre_df = genre_df.explode('listed_in')

# Count top 10 genres
top_genres = (
    genre_df['listed_in']
    .value_counts()
    .head(10)
    .reset_index()
)

top_genres.columns = ['genre', 'count']

fig_genre = px.bar(
    top_genres,
    x='count',
    y='genre',
    orientation='h',
    text='count',
    title="Top 10 Genres by Number of Titles",
    color='count',
    color_continuous_scale='Reds'
)

fig_genre.update_traces(
    textposition='outside'
)

fig_genre.update_layout(
    xaxis_title="Number of Titles",
    yaxis_title="Genre",
    title_font_size=18,
    template='plotly_white',
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(fig_genre, use_container_width=True)

st.subheader("🌍 Top 10 Content Producing Countries")

# Split and explode countries
country_df = filtered_df.copy()
country_df['country'] = country_df['country'].str.split(', ')
country_df = country_df.explode('country')

# Count top 10 countries
top_countries = (
    country_df['country']
    .value_counts()
    .head(10)
    .reset_index()
)

top_countries.columns = ['country', 'count']

fig_country = px.bar(
    top_countries,
    x='count',
    y='country',
    orientation='h',
    text='count',
    title="Top 10 Countries by Number of Titles",
    color='count',
    color_continuous_scale='Blues'
)

fig_country.update_traces(
    textposition='outside'
)

fig_country.update_layout(
    xaxis_title="Number of Titles",
    yaxis_title="Country",
    title_font_size=18,
    template='plotly_white',
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(fig_country, use_container_width=True)

st.subheader("🔞 Content Ratings Distribution")

# Count ratings
rating_counts = (
    filtered_df['rating']
    .value_counts()
    .reset_index()
)

rating_counts.columns = ['rating', 'count']

fig_rating = px.bar(
    rating_counts,
    x='rating',
    y='count',
    text='count',
    title="Distribution of Content Ratings on Netflix",
    color='count',
    color_continuous_scale='OrRd'
)

fig_rating.update_traces(
    textposition='outside'
)

fig_rating.update_layout(
    xaxis_title="Rating",
    yaxis_title="Number of Titles",
    title_font_size=18,
    template='plotly_white'
)

st.plotly_chart(fig_rating, use_container_width=True)

st.subheader("⏱️ Duration Analysis")

# Split duration into value and unit
duration_df = filtered_df.copy()
duration_df[['duration_value', 'duration_unit']] = (
    duration_df['duration']
    .str.split(' ', n=1, expand=True)
)

duration_df['duration_value'] = pd.to_numeric(
    duration_df['duration_value'], errors='coerce'
)

st.markdown("### 🎥 Movie Duration (in minutes)")

movie_df = duration_df[
    (duration_df['type'] == 'Movie') &
    (duration_df['duration_unit'].str.contains('min', case=False, na=False))
]

fig_movie = px.histogram(
    movie_df,
    x='duration_value',
    nbins=30,
    title="Distribution of Movie Duration",
    color_discrete_sequence=['#E50914']
)

fig_movie.update_layout(
    xaxis_title="Duration (minutes)",
    yaxis_title="Number of Movies",
    title_font_size=18,
    template='plotly_white'
)

st.plotly_chart(fig_movie, use_container_width=True)

st.markdown("### 📺 TV Show Duration (Number of Seasons)")

tv_df = duration_df[
    (duration_df['type'] == 'TV Show') &
    (duration_df['duration_unit'].str.contains('Season', case=False, na=False))
]

# Prepare correct dataframe for Plotly
tv_season_counts = (
    tv_df['duration_value']
    .value_counts()
    .sort_index()
    .reset_index()
)

tv_season_counts.columns = ['seasons', 'count']

fig_tv = px.bar(
    tv_season_counts,
    x='seasons',
    y='count',
    text='count',
    title="Distribution of TV Shows by Number of Seasons",
    color='count',
    color_continuous_scale='Greys'
)

fig_tv.update_layout(
    xaxis_title="Number of Seasons",
    yaxis_title="Number of TV Shows",
    title_font_size=18,
    template='plotly_white'
)

st.plotly_chart(fig_tv, use_container_width=True)
