"""
Name:MA YONGJIN
Date started:2024.24.03
GitHub URL (of this assignment):https://github.com/cp1404-students/a1-movies2see-Mayongjin1404/blob/main/assignment1.py
Remember to NEVER make this assignment repo public
"""
import csv

# Constants for movie status
WATCHED = 'w'
UNWATCHED = 'u'

# Sample CSV file path
FILENAME = 'movies.csv'


def load_movies(filename):
    """Load movies from a CSV file into a list of lists."""
    movies = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                movies.append(row)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    return movies


def save_movies(filename, movies):
    """Save the list of movies back to the CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(movies)


def display_movies(movies):
    """Display the list of movies."""
    for i, movie in enumerate(movies):
        status = '*' if movie[3] == UNWATCHED else ''
        print(f"{i}. {status} {movie[0]} - {movie[2]} ({movie[1]})")
    print(f"{len(movies)} movies loaded.")


def add_movie(movies):
    """Add a new movie to the list."""
    title = input("Title: ")
    category = input("Category: ")
    year = input("Year: ")
    movies.append([title, category, year, UNWATCHED])
    print(f"{title} added.")


def watch_movie(movies):
    """Mark a movie as watched."""
    display_movies(movies)
    try:
        choice = int(input("Enter the number of a movie to mark as watched: "))
        if 0 <= choice < len(movies) and movies[choice][3] == UNWATCHED:
            movies[choice][3] = WATCHED
            print(f"{movies[choice][0]} from {movies[choice][2]} watched")
        else:
            print("Invalid selection or movie already watched.")
    except ValueError:
        print("Invalid input; please enter a valid number.")


def show_menu():
    """Display the main menu and handle user choices."""
    movies = load_movies(FILENAME)
    menu = "\nMenu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit\n"
    
    while True:
        print(menu)
        choice = input(">>> ").upper()
        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        elif choice == "Q":
            save_movies(FILENAME, movies)
            print("Movies saved. Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    print("Movies2See 1.0 - Welcome")
    show_menu()

