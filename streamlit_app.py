import streamlit as st  
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# Load data
data = pd.read_csv(r'C:\Users\shamli\Downloads\chatgpt_reviews.csv')

# Sidebar
st.sidebar.title("AI Echo Sentiment Analysis")
st.sidebar.write("Filter and visualize data insights.")

# Sentiment distribution
st.title("Sentiment Distribution")
rating_counts = data['rating'].value_counts().sort_index()
st.bar_chart(rating_counts)

# Word Cloud
st.title("Word Cloud")

# Data cleaning function
def some_cleaning_function(text):
    # Removing any non-alphabetic characters and making everything lowercase
    return ' '.join(re.findall(r'\b[a-zA-Z]+\b', text.lower()))

# Apply cleaning function to reviews
data['cleaned_review'] = data['review'].apply(some_cleaning_function)

# Print the cleaned data for debugging
print(data.head())

# Filter positive and negative reviews based on rating (assuming 5 is positive and 1 is negative)
positive_reviews = data[data['rating'] >= 4]  # You can adjust this threshold
negative_reviews = data[data['rating'] <= 2]  # You can adjust this threshold

# Generate Word Cloud for positive reviews
positive_wordcloud = WordCloud(background_color='white').generate(' '.join(positive_reviews['cleaned_review']))

# Generate Word Cloud for negative reviews
negative_wordcloud = WordCloud(background_color='white').generate(' '.join(negative_reviews['cleaned_review']))

# Display the positive reviews Word Cloud
st.subheader("Positive Reviews Word Cloud")
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

# Display the negative reviews Word Cloud
st.subheader("Negative Reviews Word Cloud")
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)

# Optional: Plot a simple graph (Example)
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])
st.pyplot(fig)
