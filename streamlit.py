import streamlit as st
import pandas as pd
import sqlite3

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('Invt.db')
    query = "SELECT image, price, description, name FROM Inventory"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def main():
    st.title('View Catalog')

    # Fetch data from the database
    images_data = fetch_data()

    if not images_data.empty:

        # Shopping basket icon in the top right corner
        st.sidebar.image('shopB.png', width=50)

        # Search bar for filtering products
        search_term = st.sidebar.text_input("Search by Product Name", "")

        # Filter images based on search term
        filtered_images = images_data[images_data['name'].str.contains(search_term, case=False)]

        # Display filtered images with "Add to Cart" button
        for index, row in filtered_images.iterrows():
            col1, col2 = st.columns([2, 1])  # Split the row into 3:1 ratio for image and button

            # Display the image
            if col1.image(row['image'], width=200, caption=row['name'], use_column_width=False):
                col1.write(f"Price: £{row['price']}")
                col1.write(row['description'])

                # Add to Cart button
                if col2.button(f"Add to Cart {row['name']}"):
                    # Implement the logic to add the item to the cart here
                    st.sidebar.write(f"Added {row['name']} to Cart!")

    else:
        st.write('No images found in the database.')


main()

