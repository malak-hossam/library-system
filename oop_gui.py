import pandas as pd
import csv
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

class Library:
    def __init__(self):
        self.dic = {}
        self.count = 0
        self.load_from_file()

    def add(self, book):
        if book.title not in [details['title'] for _, details in self.dic.items()]:
            self.count += 1
            self.dic[self.count] = {'title': book.title, 'author': book.author, 'genre': book.genre, 'year': book.publication_year}
        else:
            messagebox.showinfo("Info", "The book is already here")

    def remove(self, title):
        for key, details in list(self.dic.items()):
            if details['title'] == title:
                del self.dic[key]
                messagebox.showinfo("Info", f"The book '{title}' has been removed")
                break
        else:
            messagebox.showinfo("Info", "The book isn't in the library")

    def search(self, item):
        found_book = {key: details for key, details in self.dic.items() if item in details['title'] or item in details['author']}
        if found_book:
            result = "Books found:\n"
            for key, details in found_book.items():
                result += f"{details['title']}: Author: {details['author']}, Genre: {details['genre']}, Year: {details['year']}\n"
            messagebox.showinfo("Search Result", result)
        else:
            messagebox.showinfo("Search Result", "No books found with that title or author.")

    def display(self):
        result = "Library:\n"
        for key, details in self.dic.items():
            result += f"{key}: {details}\n"
        messagebox.showinfo("Library", result)

    def open_file(self):
        with open("library.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['title', 'author', 'genre', 'year'])
            for key, details in self.dic.items():
                writer.writerow(list(details.values()))

    def load_from_file(self):
        if os.path.exists("library.csv"):
            data = pd.read_csv('library.csv')
            for _, row in data.iterrows():
                self.count += 1
                self.dic[self.count] = {'title': row['title'], 'author': row['author'], 'genre': row['genre'], 'year': row['year']}
        else:
            with open("library.csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['title', 'author', 'genre', 'year'])

class LibraryApp:
    def __init__(self, root):
        self.library = Library()

        root.title("Library Management System")
        root.geometry("400x300")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.title_label = tk.Label(self.frame, text="Title:")
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(self.frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.author_label = tk.Label(self.frame, text="Author:")
        self.author_label.grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(self.frame)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        self.genre_label = tk.Label(self.frame, text="Genre:")
        self.genre_label.grid(row=2, column=0, padx=5, pady=5)
        self.genre_entry = tk.Entry(self.frame)
        self.genre_entry.grid(row=2, column=1, padx=5, pady=5)

        self.year_label = tk.Label(self.frame, text="Year:")
        self.year_label.grid(row=3, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(self.frame)
        self.year_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Book", command=self.remove_book)
        self.remove_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Book", command=self.search_book)
        self.search_button.pack(pady=5)

        self.display_button = tk.Button(root, text="Display Library", command=self.display_library)
        self.display_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Library", command=self.save_library)
        self.save_button.pack(pady=5)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        year = self.year_entry.get()

        if title and author and genre and year:
            try:
                year = int(year)
                book = Book(title, author, genre, year)
                self.library.add(book)
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Error", "Year must be an integer")
        else:
            messagebox.showerror("Error", "All fields are required")

    def remove_book(self):
        title = simpledialog.askstring("Input", "Enter the title of the book to remove:")
        if title:
            self.library.remove(title)

    def search_book(self):
        item = simpledialog.askstring("Input", "Enter the title or author of the book to search for:")
        if item:
            self.library.search(item)

    def display_library(self):
        self.library.display()

    def save_library(self):
        self.library.open_file()
        messagebox.showinfo("Info", "Library saved successfully")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
