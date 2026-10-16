💰 Personal Expense Tracker with CSV

📌 Project Overview

The Personal Expense Tracker is a Python-based command-line application that helps users record, manage, and analyze their daily expenses. It uses CSV (Comma-Separated Values) file storage to save expense records permanently, allowing users to access their data whenever they run the application again.

This project demonstrates Python programming fundamentals, file handling, structured data storage, and input validation.

🎯 Objectives

- Record daily expenses with date, category, amount, and description.
- View all recorded expenses.
- Filter expenses by category.
- Calculate category-wise spending summaries.
- Store expense data persistently in a CSV file.
- Practice Python file I/O operations and exception handling.

✨ Features

- Add Expense: Record a new expense with its date, category, amount, and description.
- View Expenses: Display all saved expense records.
- Filter Expenses: Find expenses belonging to a specific category.
- Category Summary: Calculate total spending for each category and overall spending.
- CSV Storage: Save and retrieve data using Python's built-in "csv" module.
- Input Validation: Handle invalid dates, empty categories, and incorrect or non-positive amounts.

🛠️ Technologies Used

- Python 3
- CSV Module
- File Handling
- Lists and Dictionaries
- Functions and Loops
- Exception Handling

📂 Project Structure

PersonalExpenseTracker/
│
├── expense_tracker.py
├── README.md
├── .gitignore
└── expenses.csv  (created automatically)

⚙️ Requirements

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.
- Basic knowledge of running Python programs.

No external Python packages are required.

🚀 Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/Nanmugil/personal-expense-tracker.git

Step 2: Navigate to the Project Folder

cd personal-expense-tracker

Step 3: Run the Application

python expense_tracker.py

If your system uses the Python launcher on Windows, you can run:

py expense_tracker.py

🖥️ How to Use

After running the application, a menu appears:

===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Filter Expenses by Category
4. Category Summary
5. Exit

Select an option by entering its corresponding number.

Example Expense

Date: 2026-10-16
Category: Food
Amount: 150.00
Description: Lunch

Example CSV Data

Date,Category,Amount,Description
2026-10-16,Food,150.00,Lunch
2026-10-16,Travel,60.00,Bus ticket

The application creates "expenses.csv" automatically when it runs. Expense records are appended to the file and remain available between program sessions.

📊 Category Summary Example

--- Category Summary ---
Food            Rs. 150.00
Travel          Rs. 60.00
------------------------------
Total Spending  Rs. 210.00

📚 Concepts Learned

- Python functions and modular programming
- Conditional statements and loops
- Lists and dictionaries
- CSV reading and writing
- File modes and persistent storage
- Input validation and exception handling
- Basic expense analysis and aggregation

🔮 Future Enhancements

- Monthly and yearly expense reports
- Search by date range
- Edit and delete expense records
- Budget limits and spending alerts
- Graphical charts for expense analysis
- A graphical user interface using Tkinter
- Export reports for monthly spending

👩‍💻 Author

Nanmugil

GitHub: https://github.com/Nanmugil

📄 License

This project is available for educational and personal learning purposes.

---

If you find this project useful, feel free to explore the code and improve it.
