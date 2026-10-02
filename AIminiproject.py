#Rule-Based Movie Recommendation System
# PCC304COM - AI Laboratory Mini Project (Part C)

# ---------------------------
# 1. Knowledge Base (Facts)
# ---------------------------
movies = [
    {"title": "Hera Pheri", "genre": "comedy", "mood": "happy"},
    {"title": "Golmaal", "genre": "comedy", "mood": "relaxed"},
    {"title": "Andaz Apna Apna", "genre": "comedy", "mood": "happy"},
    {"title": "3 Idiots", "genre": "comedy", "mood": "relaxed"},
    {"title": "Hangover", "genre": "comedy", "mood": "excited"},

    {"title": "John Wick", "genre": "action", "mood": "excited"},
    {"title": "Mad Max: Fury Road", "genre": "action", "mood": "excited"},
    {"title": "War", "genre": "action", "mood": "happy"},
    {"title": "Extraction", "genre": "action", "mood": "relaxed"},
    {"title": "Baaghi", "genre": "action", "mood": "happy"},

    {"title": "Conjuring", "genre": "horror", "mood": "excited"},
    {"title": "Tumbbad", "genre": "horror", "mood": "relaxed"},
    {"title": "Stree", "genre": "horror", "mood": "happy"},
    {"title": "Bhoot", "genre": "horror", "mood": "excited"},
    {"title": "Pari", "genre": "horror", "mood": "relaxed"},
]

# ---------------------------
# 2. Inference Function (Rules)
# ---------------------------
def get_recommendations(genre, mood):
    genre = genre.strip().lower()
    mood = mood.strip().lower()

    # Rule 1: exact match on both genre and mood
    exact_matches = [m["title"] for m in movies
                      if m["genre"] == genre and m["mood"] == mood]

    if exact_matches:
        return exact_matches, "exact match (genre + mood)"

    # Rule 2 (fallback): match on genre only
    genre_matches = [m["title"] for m in movies if m["genre"] == genre]

    if genre_matches:
        return genre_matches, "fallback match (genre only)"

    # Rule 3 (fallback): no genre found at all
    return [], "no match"

# ---------------------------
# 3. User Interaction Loop
# ---------------------------
def main():
    print("=" * 50)
    print(" Welcome to the Rule-Based Movie Recommender ")
    print("=" * 50)
    print("Available genres: Comedy, Action, Horror")
    print("Available moods : Happy, Relaxed, Excited\n")

    while True:
        genre = input("Enter your preferred genre: ")
        mood = input("Enter your current mood: ")

        results, rule_used = get_recommendations(genre, mood)

        print(f"\n[Rule applied: {rule_used}]")
        if results:
            print("Here are some picks for you:")
            for i, title in enumerate(results, start=1):
                print(f" {i}. {title}")
        else:
            print("Sorry, no recommendations found for that genre.")

        again = input("\nTry another search? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the recommender. Enjoy your movie!")
            break
        print()

if __name__ == "__main__":
    main()

