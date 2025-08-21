
import pandas as pd

# Sample library data
data = {
    'Book_ID': [1, 2, 3, 4, 5, 6, 7],
    'Title': [
        'Python Basics', 'Data Science 101', 'AI Revolution',
        'Deep Learning', 'Machine Learning', 'Pandas Guide', 'Statistics Made Easy'
    ],
    'Author': ['James', 'Alice', 'Robert', 'Clara', 'David', 'Ella', 'Frank'],
    'Genre': ['Programming', 'Data Science', 'AI', 'AI', 'Data Science', 'Programming', 'Statistics'],
    'Borrowed_By': ['John', 'Alice', 'Bob', 'Clara', 'David', 'John', 'Alice'],
    'Days_Borrowed': [10, 5, 7, 12, 3, 15, 6]
}

df = pd.DataFrame(data)

# Most borrowed by each user
borrow_count = df['Borrowed_By'].value_counts()

# Average days borrowed by genre
avg_days = df.groupby('Genre')['Days_Borrowed'].mean()

# Most borrowed genre
most_borrowed_genre = df['Genre'].mode()[0]

# Longest borrowed book
longest_borrowed_book = df.loc[df['Days_Borrowed'].idxmax()]

print("📚 Library Borrowing System")
print(df)

print("\n👥 Borrow Count per User:")
print(borrow_count)

print("\n⏳ Average Borrowing Days per Genre:")
print(avg_days)

print(f"\n🏆 Most Borrowed Genre: {most_borrowed_genre}")

print("\n📖 Book Borrowed for the Longest Time:")
print(longest_borrowed_book)

# Save to JSON
df.to_json("library_records.json", orient="records", indent=4)
