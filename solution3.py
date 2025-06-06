### **Exercise 3: Implementing a Simple Recommendation System**

# Exercise 3: Implementing a Simple Recommendation System
# Objective: Build a basic collaborative filtering recommendation system using the MovieLens dataset.
#
# Steps:
# Load the MovieLens 100K dataset (u.data file) using Pandas.
# Preprocess the dataset by filtering out users who have rated fewer than 10 movies.
# Compute the average rating per movie and sort movies based on popularity.
# Recommend the top 5 most popular movies for new users.
# Expected Output: A ranked list of the top 5 movies based on user ratings.
import pandas as pd

url = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"
column_names = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_csv(url, sep="\t", names=column_names, usecols=["user_id", "movie_id", "rating"])

url_movies = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
movies = pd.read_csv(url_movies, sep="|", encoding="latin-1", names=["movie_id", "title"], usecols=[0, 1])

movies_dataset = ratings.merge(movies, on="movie_id")
movies_dataset = movies_dataset.groupby("user_id").filter(lambda x: len(x) > 10)
ratings_movies = movies_dataset.groupby("title")["rating"].mean()
top5 = ratings_movies.sort_values(ascending=False).head(5)
print(top5)