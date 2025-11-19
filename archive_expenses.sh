#!/bin/bash

ARCHIVE_DIR="archives"
LOG_FILE="archive_log.txt"

# Create archive directory if not exists
mkdir -p "$ARCHIVE_DIR"

# Function to log messages
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Main logic
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <YYYY-MM-DD> [search]"
    echo "  Without 'search': Archives expenses_YYYY-MM-DD.txt"
    echo "  With 'search': Prints archived file content"
    exit 1
fi

DATE="$1"
ACTION="${2:-archive}"

FILE="expenses_$DATE.txt"
ARCHIVED_FILE="$ARCHIVE_DIR/$FILE"

if [ "$ACTION" = "search" ]; then
    if [ -f "$ARCHIVED_FILE" ]; then
        echo "Content of archived file: $ARCHIVED_FILE"
        cat "$ARCHIVED_FILE"
    else
        echo "Archived file not found: $ARCHIVED_FILE"
        exit 1
    fi
else
    if [ ! -f "$FILE" ]; then
        echo "Expense file not found: $FILE"
        exit 1
    fi

    mv "$FILE" "$ARCHIVE_DIR/"
    log "Archived $FILE"
    echo "Archived $FILE to $ARCHIVE_DIR/"
fi