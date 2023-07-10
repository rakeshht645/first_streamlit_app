streamlit.title('My Parents New Healthy Diner')

streamlit.title('Breakfast Menu')
streamlit.title('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.title('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.title('🐔 Hard-Boiled Free-Range Egg')
streamlit.title('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
