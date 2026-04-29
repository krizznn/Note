from datetime import datetime
from typing import List

class Note:
    """
    Represents a basic note in the notebook organizer.
    Contains core note data: title, text, tags, and creation date.
    """

    def __init__(self, title: str, text: str, tags: List[str] = None):
        """
        Initialize a new note.

        Args:
            title (str): Note title
            text (str): Note content
            tags (List[str], optional): List of tags for categorization. Defaults to empty list.
        """
        self.title = title
        self.text = text
        self.tags = tags or []
        self.date = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """
        Convert note object to dictionary for JSON serialization.

        Returns:
            dict: Dictionary with note data (title, text, tags, date)
        """
        return {
            'title': self.title,
            'text': self.text,
            'tags': self.tags,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Note':
        """
        Create a Note instance from a dictionary (e.g., JSON data).

        Args:
            data (dict): Dictionary containing note fields

        Returns:
            Note: New Note object with data from the dictionary
        """
        note = cls(data['title'], data['text'], data['tags'])
        note.date = data['date']
        return note

    def __str__(self) -> str:
        """
        Get string representation of the note for display.

        Returns:
            str: Formatted string with all note information
        """
        return (f"Title: {self.title}\n"
                f"Text: {self.text}\n"
                f"Tags: {', '.join(self.tags)}\n"
                f"Date: {self.date}\n")
