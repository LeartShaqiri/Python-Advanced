import streamlit as st
import pandas as pd

# -----------------------
# Page config (IMPORTANT)
# -----------------------
st.set_page_config(
    page_title="Lesson 19 | Streamlit App",
    page_icon="📊",
    layout="wide"
)

# -----------------------
# Title
# -----------------------
st.title(" Store Dara with Streamlit ")
st.caption("Data input, filtering, and visualization using Streamlit")

# -----------------------
# Session state
# -----------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Name", "Age", "Score"]
    )

# -----------------------
# Sidebar (clean)
# -----------------------
with st.sidebar:
    st.header("➕ Add Data")

    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120, 18)
    score = st.number_input("Score", 0, 100, 50)

    add_btn = st.button("Add Data")

    st.divider()

    st.header("🔍 Filter")
    min_age = st.slider("Minimum Age", 0, 120, 0)

# -----------------------
# Add data logic
# -----------------------
if add_btn:
    if name:
        new_row = pd.DataFrame(
            [[name, age, score]],
            columns=["Name", "Age", "Score"]
        )
        st.session_state.data = pd.concat(
            [st.session_state.data, new_row],
            ignore_index=True
        )
        st.success("Data added successfully ✅")
    else:
        st.error("Name cannot be empty")

# -----------------------
# Filter data
# -----------------------
filtered_data = st.session_state.data[
    st.session_state.data["Age"] >= min_age
]

# -----------------------
# Main layout
# -----------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📋 Data Table")
    st.dataframe(filtered_data, use_container_width=True)

with col2:
    st.subheader("📈 Stats")

    st.metric("Total Entries", len(filtered_data))

    if not filtered_data.empty:
        st.metric("Average Score", round(filtered_data["Score"].mean(), 1))
    else:
        st.metric("Average Score", "—")

# -----------------------
# Chart Section
# -----------------------
st.subheader("📊 Score Visualization")

if not filtered_data.empty:
    st.bar_chart(
        filtered_data.set_index("Name")["Score"],
        use_container_width=True
    )
else:
    st.info("Add some data to see the chart")

# -----------------------
# Footer
# -----------------------
st.divider()
st.caption("Lesson 19 • Streamlit • Python Advanced")
