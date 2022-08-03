import streamlit

streamlit.title('My Parents New Healty Diner..')
streamlit.header('** Breakfast Menu **')
streamlit.text ('=> 🍞 Dosa/Idily-Chutney-Sambar')
streamlit.text ('=> 🍞 Puri Masala')
streamlit.text ('=> 🍞 Chapathi-Veg. kurma')
streamlit.text ('=> Tea/Coffee/Cold coffee')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
