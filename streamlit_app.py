import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Customer Analytics Dashboard")
df = pd.read_csv("customers (4).csv")

st.sidebar.header("Filter Data")
departments = st.sidebar.multiselect(
    "Pilih Departments",
    df["Department"].dropna().unique()
)

genders = st.sidebar.multiselect(
    "Pilih Gender",
    df["Gender"].dropna().unique()
)

st.sidebar.header("Filter Rentang Umur")
min_usia, max_usia = int(df["Age"].min()), int(df["Age"].max())
usia_range = st.sidebar.slider(
    "Usia",
    min_value=min_usia,
    max_value=max_usia,
    value=(min_usia, max_usia)
)

df_filtered = df[
    (df["Department"].isin(departments)) &
    (df["Gender"].isin(genders)) &
    (df["Age"].between(usia_range[0], usia_range[1]))
]

st.subheader("Data Tabel")

st.dataframe(df_filtered)

st.subheader("Visualisasi Statistik")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribusi Gender")
    pie_gender = px.pie(
        df_filtered,
        names="Gender",
        color="Gender",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(pie_gender)

with col2:
    st.subheader("Gaji Rata-rata per Department")

    salary_dept = (
        df_filtered
        .groupby("Department")["AnnualSalary"]
        .mean()
        .reset_index()
    )

    bar_salary = px.bar(
        salary_dept,
        x="Department",
        y="AnnualSalary",
        color="Department",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(bar_salary)

    
st.subheader("Rata-rata Gaji Berdasarkan Usia")

salary_age = (
    df_filtered
    .groupby("Age")["AnnualSalary"]
    .mean()
    .reset_index()
    .sort_values("Age")
)

line_age = px.line(
    salary_age,
    x="Age",
    y="AnnualSalary",
    markers=True
)

st.plotly_chart(line_age)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("customers (4).csv")

# Bersihkan nama kolom
df.columns = df.columns.str.strip()

st.subheader("Jumlah Customers per City")

# Hitung jumlah per city
city_count = df["City"].value_counts()

# Optional: ambil Top 10 city agar tidak terlalu panjang
top_city = city_count.head(10)

fig, ax = plt.subplots()
top_city.plot(kind="bar", ax=ax)
ax.set_xlabel("City")
ax.set_ylabel("Jumlah Customers")
ax.set_title("Top 10 City dengan Customers Terbanyak")

st.pyplot(fig)
