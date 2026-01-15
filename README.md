# 🎬 Netflix EDA & Interactive Streamlit Dashboard

An end-to-end **Exploratory Data Analysis (EDA)** and **interactive dashboard** built using the **Netflix Movies and TV Shows dataset** from Kaggle.  
This project combines data cleaning, analysis, and visualization with a modern **Streamlit + Plotly** dashboard.

---

## 📌 Project Overview

This project aims to analyze Netflix’s content catalog to uncover insights related to:
- Content type distribution (Movies vs TV Shows)
- Growth of content over time
- Genre popularity
- Country-wise content contribution
- Audience targeting through ratings
- Duration patterns for movies and TV shows

The insights are presented through an **interactive dashboard** that allows dynamic filtering and exploration.

---

## ✨ Key Features

### 🔍 Interactive Filters
- Content Type (Movie / TV Show)
- Year Added
- Country

### 📊 Dashboard Visualizations
- KPI Cards (Total Titles, Movies, TV Shows)
- Movies vs TV Shows distribution
- Content added over the years
- Movies vs TV Shows trend comparison
- Top 10 genres
- Top 10 content-producing countries
- Ratings distribution
- Movie duration distribution
- TV show seasons distribution

All visualizations are **interactive** using Plotly.

---

## 🗂️ Project Structure
SESSION 3/
│
├── app.py                # Streamlit dashboard application
├── netflix_titles.csv    # Netflix dataset
├── EDA.ipynb             # Complete Exploratory Data Analysis notebook
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

---

🧠 Key Insights
	•	Netflix’s catalog is dominated by movies, though TV shows have grown rapidly since 2016.
	•	United States and India are the largest content contributors.
	•	Netflix focuses strongly on mature and teen audiences (TV-MA, TV-14).
	•	Most movies are between 80–120 minutes long.
	•	Most TV shows have 1–2 seasons, indicating a preference for shorter series.

⸻

🛠️ Technologies Used
	•	Python
	•	Pandas
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	Plotly
	•	Streamlit

⸻

📚 Dataset Source
	•	Kaggle – Netflix Movies and TV Shows Dataset

⸻

👤 Author

Aayush Kumar
B.Tech – Computer & Communication Engineering
Manipal University Jaipur

⸻

📈 Future Enhancements
	•	Deploy the dashboard on Streamlit Cloud
	•	Add recommendation system
	•	Improve country and genre level drill-downs
	•	Convert into a full BI dashboard
