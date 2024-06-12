# Personal Library Management System

## Project Description
This project is a Personal Library Management System built using Python. It allows users to manage their personal book collection with functionalities to add new books, remove books, search for books, and store information about each book. The project is implemented in two versions: one without a GUI and one with a GUI using Tkinter.

## Features
- Add a book to the library
- Remove a book from the library
- Search for books by title or author
- Display the entire library collection
- Save and load library data to/from a text or CSV file

## Project Structure
The project consists of two main files:
1. **library_system.py**: The core library management system without a GUI.
2. **library_system_gui.py**: The library management system with a graphical user interface implemented using Tkinter.

## Class Definitions

### Book
Represents a book with the following attributes:
- Title
- Author
- Genre
- Publication Year

### Library
Represents the personal library with methods to:
- Add a book
- Remove a book
- Search for a book by title or author
- Display the entire library

## Data Structure
The library uses appropriate data structures such as lists and dictionaries to manage the collection of books.

## File Handling
Methods are implemented in the Library class to save the library data to a file (e.g., "library.txt" or "library.csv") and to load the data during program startup to ensure persistence across different program executions.

## Exception Handling
Exception handling is implemented to manage potential errors gracefully, such as cases where a book is not found, a file is not found, or input validation errors occur.

## User Interaction

### Command-Line Interface
A user-friendly command-line interface is provided, allowing users to:
- Add a book
- Remove a book
- Search for a book
- Display the entire library

### Graphical User Interface (Tkinter)
An additional version with a graphical user interface is implemented using Tkinter, providing an interactive and intuitive way to manage the personal library.
