import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=(lambda x: x[1]))[1:6]

    recommeded_movies=[]

    for i in movie_list:
        recommeded_movies.append(movies.iloc[i[0]].title)
    return recommeded_movies


movies_list=pickle.load(open('movies.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))


movies=pd.DataFrame(movies_list)
movies_l=movies.title

st.title('Movies Recommender System')
selected_movies_name= st.selectbox('Enter the movies',movies_l)

if st.button('Recommmed'):
    recommendations=recommend(selected_movies_name)

    for i in recommendations:
        st.write(i)
print(movies_list.shape)