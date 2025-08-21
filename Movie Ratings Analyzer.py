import pandas as pd

# Sample movie ratings dataset
data = {
    'Movie': ['Inception', 'Inception', 'Avatar', 'Avatar', 'Titanic', 'Titanic', 'Avengers', 'Avengers', 'Avengers'],
    'User': ['U1', 'U2', 'U1', 'U3', 'U2', 'U4', 'U1', 'U2', 'U3'],
    'Rating': [5, 4, 4, 5, 5, 4, 5, 4, 5]
}

df = pd.DataFrame(data)

# Average rating per movie
avg_rating = df.groupby('Movie')['Rating'].mean().sort_values(ascending=False)

# Number of ratings per movie
rating_count = df.groupby('Movie')['Rating'].count()

# Highest rated movie
highest_rated = avg_rating.idxmax()

# Movies sorted by popularity (number of ratings)
most_popular = rating_count.sort_values(ascending=False)

print("🎬 Movie Ratings Data")
print(df)

print("\n⭐ Average Rating per Movie:")
print(avg_rating)

print("\n👥 Number of Ratings per Movie:")
print(rating_count)

print("\n🏆 Highest Rated Movie:", highest_rated)

print("\n🔥 Movies by Popularity (Number of Ratings):")
print(most_popular)

# Save results
df.to_csv("movie_ratings.csv", index=False)
