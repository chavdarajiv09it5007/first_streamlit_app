import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



#read cav and show it on ui
#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)

#read csv,make it user interactive with dropdown ndex and show it on ui
#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include. [generate dropdown with index values in the list]
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
#streamlit.dataframe(my_fruit_list)

#read csv,make it user interactive with dropdown name and show it on ui
#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
#streamlit.dataframe(my_fruit_list)


#read csv,make it user interactive with dropdown name,prepopulate dropdown and show it on ui
#import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
#streamlit.dataframe(my_fruit_list)


#read csv,make it user interactive with dropdown name,prepopulate dropdown and show fruits on ui with filter applied
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)




#chapter 9: making api calls in streamlit

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

#streamlit.header("Fruityvice Fruit Advice!")
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())


#streamlit.header("Fruityvice Fruit Advice!")
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())  # writes json data to screen

# take the jsoan version and normalize it 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# writes the normalise dta to scerrn
#streamlit.dataframe(fruityvice_normalized)



#Let's removed the line of raw JSON, and separate the base URL from the fruit name (which will make it easier to use a variable there).
#streamlit.header("Fruityvice Fruit Advice!")
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# take the jsoan version and normalize it 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# writes the normalise dta to scerrn
#streamlit.dataframe(fruityvice_normalized)





# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# take the jsoan version and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# writes the normalise dta to scerrn
streamlit.dataframe(fruityvice_normalized)




#chater 12 badge2
#Let's Set Up Streamlit to Work with Snowflake
import snowflake.connector

#Let's Query Our Trial Account Metadata 
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)



#Let's Query Some Data, Instead
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)


#Let's Change the Streamlit Components to Make Things Look a Little Nicer
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_row)



#Oops! Let's Get All the Rows, Not Just One
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

