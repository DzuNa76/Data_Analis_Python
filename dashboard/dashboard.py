import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn plots
sns.set(style='dark')

# Load data
merged_customers = pd.read_csv('merged_customers.csv')
merged_order_items = pd.read_csv('merged_order_items.csv')

# Page title
st.title('E-Commerce Dashboard')

# Sidebar
st.sidebar.title('Navigation')
option = st.sidebar.selectbox('Select Analysis', ['Customer Distribution', 'Sales by Product Category'])

if option == 'Customer Distribution':
    st.header('Customer Distribution by City and State')
    
    # Distribution by city
    city_distribution = merged_customers['geolocation_city'].value_counts().reset_index()
    city_distribution.columns = ['city', 'customer_count']

    # Distribution by state
    state_distribution = merged_customers['geolocation_state'].value_counts().reset_index()
    state_distribution.columns = ['state', 'customer_count']

    # Display city distribution
    st.subheader('Top 10 Cities by Customer Count')
    st.dataframe(city_distribution.head(10))

    # Plot city distribution
    plt.figure(figsize=(10, 6))
    sns.barplot(x='customer_count', y='city', data=city_distribution.head(10))
    plt.title('Top 10 Cities by Customer Count')
    plt.xlabel('Customer Count')
    plt.ylabel('City')
    st.pyplot(plt)

    # Display state distribution
    st.subheader('Customer Distribution by State')
    st.dataframe(state_distribution)

    # Plot state distribution
    plt.figure(figsize=(10, 6))
    sns.barplot(x='customer_count', y='state', data=state_distribution)
    plt.title('Customer Distribution by State')
    plt.xlabel('Customer Count')
    plt.ylabel('State')
    st.pyplot(plt)

elif option == 'Sales by Product Category':
    st.header('Sales by Product Category')
    
    # Filter only delivered orders
    delivered_orders = merged_order_items[merged_order_items['order_status'] == 'delivered']

    # Sales count by product category
    category_sales = delivered_orders['product_category_name_english'].value_counts().reset_index()
    category_sales.columns = ['product_category', 'sales_count']

    # Display top 10 best-selling product categories
    st.subheader('Top 10 Best-Selling Product Categories')
    st.dataframe(category_sales.head(10))

    # Plot top 10 best-selling product categories
    plt.figure(figsize=(10, 6))
    sns.barplot(x='sales_count', y='product_category', data=category_sales.head(10))
    plt.title('Top 10 Best-Selling Product Categories')
    plt.xlabel('Sales Count')
    plt.ylabel('Product Category')
    st.pyplot(plt)

    # Display top 10 least-selling product categories
    st.subheader('Top 10 Least-Selling Product Categories')
    st.dataframe(category_sales.tail(10))

    # Plot top 10 least-selling product categories
    plt.figure(figsize=(10, 6))
    sns.barplot(x='sales_count', y='product_category', data=category_sales.tail(10))
    plt.title('Top 10 Least-Selling Product Categories')
    plt.xlabel('Sales Count')
    plt.ylabel('Product Category')
    st.pyplot(plt)
