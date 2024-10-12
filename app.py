import streamlit as st
import requests

# Function to display the item creation screen
def create_item_screen():
    st.title("Create Item")
    name = st.text_input("Item Name")
    price = st.number_input("Price", min_value=0.0)
    description = st.text_area("Description")
    in_stock = st.checkbox("In Stock", value=True)

    if st.button("Create Item"):
        # Add API call here
        response = requests.post("http://127.0.0.1:8000/items/", json={
            "name": name,
            "price": price,
            "description": description,
            "in_stock": in_stock
        })
        if response.status_code == 201:
            st.success("Item created successfully!")
        else:
            st.error("Error creating item.")

# Function to display the item management screen
def manage_items_screen():
    st.title("Manage Items")
    response = requests.get("http://127.0.0.1:8000/items/")
    items = response.json()
    
    for item in items:
        st.write(f"**{item['name']}** - {item['price']} - {item['description']} - In Stock: {item['in_stock']}")
        if st.button(f"Delete {item['name']}"):
            # Add API call for deletion here
            delete_response = requests.delete(f"http://127.0.0.1:8000/items/{item['id']}")
            if delete_response.status_code == 204:
                st.success("Item deleted successfully!")
            else:
                st.error("Error deleting item.")

# Function to display the authentication screen
def auth_screen():
    st.title("User Authentication")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        # Add API call for login here
        st.success("Logged in successfully!")
    elif st.button("Create Account"):
        # Add API call for account creation here
        st.success("Account created successfully!")

# Main app
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Create Item", "Manage Items", "Authentication"])

if options == "Create Item":
    create_item_screen()
elif options == "Manage Items":
    manage_items_screen()
else:
    auth_screen()
