# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:32:43 2024

@author: Admin
"""

# 1. Data Cleaning
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df)
print(df.info())
df.dropna(inplace = True)
df = df.reset_index(drop=True)
print(df)
print(df.info())
# Sample dataset (replace this with your actual dataset)
movie_dataset = df
  

#This is to filter the Dataframe to show only rows with maximum rating and print the title and rating of the highest rating movie.


import pandas as pd

#  my DataFrame is named df herein referred to as movie_data:
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

print("Highest-rated movie:")
print(highest_rated_movie[['Title', 'Rating']])

# My DataFrame/movie_dataset is named df
# This code first filters the DataFrame to include only rows where the 'Year' column is between 2015 and 2017 (inclusive), and then it calculates the mean (average) of the 'Revenue (Millions)' column in the filtered DataFrame. The result is printed formatted as currency with two decimal places.



# 2. Calculating average revenue
average_revenue = df['Revenue (Millions)'].mean()

print("Average Revenue of All Movies: ${:,.2f}".format(average_revenue))



# 3. Calculating average revenue for 2015 - 2017 movies

print(f"The average revenue of all movies in the dataset is {average_revenue:.2f} million dollars.")
# 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Filtering data 
filtered_df = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]

average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

print(f"The average revenue of movies from 2015 to 2017 is {average_revenue_2015_to_2017:.2f} million dollars.")




# 4.Number of movies released in 2016
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df)
print(df.info())


# Assuming DataFrame = df otherwise load your DataFrame using pd.read_csv() or other methods
movies_2016 = df[df['Year'] == 2016]

num_movies_2016 = len(movies_2016)

print(f"The number of movies released in the year 2016 is: {num_movies_2016}")




# 5. Number of movies directed by Christopher Nolan
import pandas as pd

# Assuming DataFrame = df otherwise load your DataFrame using pd.read_csv() or other methods

nolan_movies = df[df['Director'] == 'Christopher Nolan']

num_nolan_movies = len(nolan_movies)

print(f"The number of movies directed by Christopher Nolan is: {num_nolan_movies}")


# 6.Number of movies with at least 8.0 rating

import pandas as pd

# Assuming DataFrame = df otherwise load your DataFrame using pd.read_csv() or other methods

# Filter for movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

number_of_high_rated_movies = len(high_rated_movies)

print(f"The number of movies in the dataset with a rating of at least 8.0 is {number_of_high_rated_movies}.")





# 7.Median for Christopher Nolan movies

import pandas as pd

# Assuming DataFrame = df otherwise load your DataFrame using pd.read_csv() or other methods

# Filter for Christopher Nolan movies
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median
median_rating_nolan_movies = nolan_movies['Rating'].median()

print(f"The median rating of movies directed by Christopher Nolan is {median_rating_nolan_movies}.")


# 8. Finding the year with highest average rating

import pandas as pd

# Assuming DataFrame = df otherwise load your DataFrame using pd.read_csv() or other methods

average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}.")



# 9.Calculating the percentage increase in number of movies made between 2006 and 2016

import pandas as pd

# Assuming DataFrame = df otherwise load your DataFrame using pd.read_csv() or other methods

# Filter
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

# Count the number of movies per year
count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

# Therefore percentage increase is:
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100

print(f"The percentage increase in the number of movies made between 2006 and 2016 is {percentage_increase:.2f}%.")




# 10.Finding most common actor

import pandas as pd

# Assuming DataFrame = df otherwise load your DataFrame using pd.read_csv() or other methods

# Split the multiple actors in the "Actors" column and create a new DataFrame
actors_df = df['Actors'].str.split(', ', expand=True)

# Reshape the DataFrame to have one column for each actor
actors_list = actors_df.values.flatten()

# Create a Series to count the occurrences of each actor
actors_count = pd.Series(actors_list).value_counts()

# Hence to get most common actor
most_common_actor = actors_count.idxmax()

print(f"The most common actor in all the movies is: {most_common_actor}")




# 11.Number of unique genres in the dataset

import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

# Create a new DataFrame by splitting multiple genres in the "Genre" column.
genres_df = df['Genre'].str.split(', ', expand=True)

# Reshape the DataFrame to have one column for each genre
genres_list = genres_df.values.flatten()

# Number of unique genres
unique_genres_count = len(set(genres_list))

print(f"The number of unique genres in the dataset is: {unique_genres_count}")



# 12. Data Correlation

import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

numerical_features = df[['Rank', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]

correlation_matrix = numerical_features.corr()

print("Correlation Matrix:")
print(correlation_matrix)

insights = [
    "1. There is a positive correlation between 'Rating' and 'Metascore', indicating that movies with higher Metascores tend to have higher ratings.",
    "2. 'Votes' and 'Revenue (Millions)' show a positive correlation, suggesting that more popular movies, as indicated by votes, tend to generate higher revenue.",
    "3. 'Rank' and 'Rating' have a negative correlation, meaning that movies with lower ranks (higher ranks are better) tend to have higher ratings.",
    "4. 'Year' does not show a strong correlation with other numerical features, indicating that the release year alone may not significantly impact other variables.",
    "5. 'Runtime (Minutes)' doesn't show a strong correlation with 'Rating', suggesting that the length of a movie may not be a decisive factor for its rating."
]

# Therefore, insights:
print("\nInsights:")
for insight in insights:
    print(insight)



