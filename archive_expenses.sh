#!/bin/bash

#ARCHIVE SCRIPT FOR PERSONAL EXPENSE TRACKER
ARCHIVE_DIR="archives"
LOG_FILE="archive_log.txt"

# -------------------------------------------------------
# Step 1: Make sure the archives folder exists
# -------------------------------------------------------
if [ ! -d "$ARCHIVE_DIR" ]; then
    echo "Creating archives directory..."
    mkdir "$ARCHIVE_DIR"
fi

# -------------------------------------------------------
# Step 2: Menu system for the shell script
# -------------------------------------------------------
echo "======================================"
echo "      EXPENSE ARCHIVE MANAGEMENT"
echo "======================================"
echo ""
echo "1. Move an expense file into archives"
echo "2. Search archived expenses by date"
echo "3. Exit"
echo ""

read -p "Choose an option (1-3): " choice


# -------------------------------------------------------
#1: Move file to archives
# -------------------------------------------------------
if [ "$choice" = "1" ]; then
    echo ""
    read -p "Enter the date of the expense file (YYYY-MM-DD): " date

    filename="expenses_${date}.txt"
    destination="$ARCHIVE_DIR/$filename"

    if [ -f "$filename" ]; then
        mv "$filename" "$destination"
        echo "File moved to archives: $destination"

        # Log the operation with timestamp
        timestamp=$(date +"%Y-%m-%d %H:%M:%S")
        echo "[$timestamp] Archived file: $filename" >> "$LOG_FILE"

        echo "Operation logged in archive_log.txt"
    else
        echo "No expense file found for that date!"
    fi

    exit 0
fi


# -------------------------------------------------------
# 2: Search archives by date
# -------------------------------------------------------
if [ "$choice" = "2" ]; then
    echo ""
    read -p "Enter the date to search (YYYY-MM-DD): " search_date
    search_file="$ARCHIVE_DIR/expenses_${search_date}.txt"

    if [ -f "$search_file" ]; then
        echo ""
        echo "======================================"
        echo "   EXPENSE FILE FOUND FOR $search_date"
        echo "======================================"
        echo ""
        cat "$search_file"
    else
        echo "No archived file found for that date."
    fi

    exit 0
fi


# -------------------------------------------------------
#3: Exit
# -------------------------------------------------------
if [ "$choice" = "3" ]; then
    echo "Exiting archive script."
    exit 0
fi


# -------------------------------------------------------
# If user enters anything else
# -------------------------------------------------------
echo "Invalid option. Please run the script again."
exit 1
