import streamlit as st
import pandas as pd

# -----------------------------
# App title
# -----------------------------
st.title("Lesson 19 - Simple Streamlit Data App")

# -----------------------------
# Initial data (session state)
# -----------------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Name", "Age", "Score"]
    )

# -----------------------------
# SIDEBAR - Add Data
# -----------------------------
st.sidebar.header("➕ Add New Data")

name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
score = st.sidebar.number_input("Score", min_value=0, max_value=100, step=1)

if st.sidebar.button("Add"):
    if name != "":
        new_row = {
            "Name": name,
            "Age": age,
            "Score": score
        }
        st.session_state.data = pd.concat(
            [st.session_state.data, pd.DataFrame([new_row])],
            ignore_index=True
        )
        st.sidebar.success("Data added!")
    else:
        st.sidebar.error("Name cannot be empty")

# -----------------------------
# SIDEBAR - Filter Data
# -----------------------------
st.sidebar.header("🔍 Filter Data")

min_age = st.sidebar.slider(
    "Minimum Age",
    min_value=0,
    max_value=120,
    value=0
)

# Apply filter
filtered_data = st.session_state.data[
    st.session_state.data["Age"] >= min_age
]

# -----------------------------
# Show Data
# -----------------------------
st.subheader("📋 Data Table")
st.dataframe(filtered_data)

# -----------------------------
# Data Visualization
# -----------------------------
st.subheader("📊 Score Visualization")

if not filtered_data.empty:
    st.bar_chart(
        filtered_data.set_index("Name")["Score"]
    )
else:
    st.info("No data to display. Add some data first.")
