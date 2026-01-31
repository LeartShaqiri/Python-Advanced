import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling books from 2009 to 2022.")

st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User Rating", 0.0, 5.0, 0.0, 0.1)
    new_reviews = st.number_input("Reviews", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=0, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Reviews': new_reviews,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_genre,
    }
    
    books_df = pd.concat([pd.DataFrame([new_data]), books_df], ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
    st.sidebar.success("New book added successfully!")

st.sidebar.header("Filter Options")
selected_author = st.sidebar.selectbox("Select Author", ['All'] + list(books_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year", ['All'] + list(books_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ['All'] + list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum User Rating", 0.0, 5.0, 0.0, 0.1)
max_price = st.sidebar.slider("Maximum Price", 0, int(books_df['Price'].max()), int(books_df['Price'].max()))

filtered_books_df = books_df.copy()

# Apply filters
if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selected_author]
if selected_year != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Year'] == selected_year]
if selected_genre != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Genre'] == selected_genre]

# Apply rating and price filters
filtered_books_df = filtered_books_df[filtered_books_df['User Rating'] >= min_rating]
filtered_books_df = filtered_books_df[filtered_books_df['Price'] <= max_price]

# Display filtered results
st.subheader("Filtered Books")
st.write(f"Found {len(filtered_books_df)} books matching your criteria")
st.dataframe(filtered_books_df)

# Visualizations
st.subheader("Visualizations")

# Distribution of ratings
if len(filtered_books_df) > 0:
    fig1 = px.histogram(filtered_books_df, x='User Rating', title='Distribution of User Ratings')
    st.plotly_chart(fig1)
    
    # Price vs Rating scatter plot
    fig2 = px.scatter(filtered_books_df, x='Price', y='User Rating', color='Genre',
                     hover_data=['Name', 'Author'], title='Price vs User Rating')
    st.plotly_chart(fig2)
else:
    st.write("No books match the selected filters. Try adjusting your criteria.")









    # Assuming col1 and col2 are already defined as columns
with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df["Author"].value_counts().head(10)
    st.bar_chart(top_authors)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)

st.subheader("Genre Distribution")
fig = px.pie(books_df, names="Genre", title="Most Liked Genre (2009-2022)", 
             color="Genre", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs Non-Fiction Books Over the Years")
size = books_df.groupby(["Year", "Genre"]).size().reset_index(name="Counts")
fig = px.bar(size, x="Year", y="Counts", color="Genre", 
             title="Number of Fiction vs Non-Fiction Books from 2009-2022",
             color_discrete_sequence=px.colors.sequential.Plasma,
             barmode="group")
st.plotly_chart(fig)

st.subheader("Top 15 Authors by Counts of the Books Published (2009-2022)")
top_authors = books_df["Author"].value_counts().head(15).reset_index()
top_authors.columns = ["Author", "Count"]
fig = px.bar(top_authors, x="Count", y="Author", orientation="h", 
             title="Top 15 Authors by Counts of the Books Published", 
             color="Count", color_continuous_scale=px.colors.sequential.Plasma,
             labels={"Count": 'Counts of Books Published', 'Author': 'Author'})
st.plotly_chart(fig)

st.subheader("Filter Data by Genre")
genre_filter = st.selectbox("Select Genre", books_df["Genre"].unique())
filter_df = books_df[books_df["Genre"] == genre_filter]
st.write(f"Showing {len(filter_df)} books in the {genre_filter} genre:")
st.dataframe(filter_df)