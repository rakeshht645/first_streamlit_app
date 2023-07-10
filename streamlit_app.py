streamlit.title('My Parents New Healthy Diner')

streamlit.title('Breakfast Menu')
streamlit.title('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.title('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.title('🐔 Hard-Boiled Free-Range Egg')
streamlit.title('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my _cnx_cursor() as my_cur:
    my_cur_execute("insert into fruit_load_list values ('" + ???? + "')")
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('what fruit would you like to add?')
if streamlit.button ('Add a Fruit to the list'):
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
back_from-function = insert_row_snowflake(add_my_fruit)
streamlit.text(back_from_function)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# don't run anything past here while we troubleshoot
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
