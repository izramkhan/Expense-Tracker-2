# Expense Tracker

A comprehensive command-line expense tracking application built with Python that helps users manage their finances efficiently with full CRUD functionality and data persistence.

## Features

### Core Functionality
- **Add Expenses** – Create new expense entries with title, amount, category, and notes
- **Update Expenses** – Modify existing expense details using unique expense IDs
- **Delete Expenses** – Remove individual expenses (moved to deleted expenses archive)
- **Delete All Expenses** – Complete reset with confirmation prompt
- **Filter by Category** – View expenses filtered by specific categories
- **View All Expenses** – Display all current expenses with calculated totals
- **View Deleted Expenses** – Access archived deleted expenses with totals

### Data Management
- **Automatic Data Persistence** – All data automatically saved to JSON files
- **Dual Storage System** – Separate files for active and deleted expenses
- **Unique ID Generation** – Each expense assigned a 4-digit random ID
- **Data Validation** – Input validation with length and type constraints

### User Experience
- **Interactive CLI Interface** – Animated headers and visual feedback
- **Input Validation** – Comprehensive error handling and user guidance
- **Process Control** – Ability to stop operations mid-process (using '0')
- **Formatted Display** – Clean, aligned tabular output for expense viewing

---

## How to Clone

### Prerequisites
- Git installed on your system
- Python 3.7 or higher

### Step-by-Step Cloning Instructions

#### 1. **Clone the Repository**
Open your terminal/command prompt and run:
```bash
git clone https://github.com/izramkhan/Expense-Tracker-2.git
