# Import the required libraries
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the web scraping function
def google_search(query):
    # Define the Google search URL
    url = f"https://www.google.com/search?q={query}"

    # Send a GET request to Google
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all anchor links
    anchor_links = soup.find_all("a", href=True)

    # Extract the first three links
    top_links = []
    for link in anchor_links[:3]:
        href = link.get("href")  # Use .get() to avoid NoneType error
        if href:
            top_links.append(href)

    return top_links

# Create a title for the web app
st.title("Web Scraping App")

# Create an input box for the user to enter the search query
query = st.text_input("Enter your search query:")

# Create a button for the user to run the web scraping code
if st.button("Run"):
    # Call the web scraping function with the query
    search_links = google_search(query)

    # Create a pandas DataFrame from the list of links
    df = pd.DataFrame(search_links, columns=["Links"])

    # Display the DataFrame on the web app
    st.dataframe(df)

    # Create a download button for the user to download the excel file
    st.download_button("Download Excel File", df.to_excel(index=False), file_name="links.xlsx")
