""" Utility functions for YouTube Downloader CLI app. """

import os
import re
from typing import Optional


def seconds_from_timestamp(timestamp: str) -> int:
    """
    Convert a timestamp in HH:MM:SS or MM:SS format to total seconds.

    Args:
        timestamp (str): A timestamp string(e.g., "01:30" or "01:03:32).

    Returns:
        int: Total seconds as integer.
    """
    parts = timestamp.strip().split(":")
    parts = [int(p) for p in parts]

    if len(parts) == 3:
        hours, minutes, seconds = parts
    elif len(parts) == 2:
        hours = 0
        minutes, seconds = parts
    elif len(parts) == 1:
        hours = 0
        minutes = 0
        seconds = parts[0]
    else:
        raise ValueError(f"Invalid timestamp format: {timestamp}")
    
    return hours * 3600 + minutes * 60 + seconds

def ensure_dir(path: str) -> None:
    """
    Ensure that the given directory exists; create it if it doesn't.

    Args:
        path (str): Path to the directory.
    """
    os.makedirs(path, exist_ok=True)

def sanitize_filename(filename: str) -> str:
    """
    Remove illegal characters from a filename.

    Args:
        filename (str): Input filename.

    Returns:
        str: Sanitized filename safe for saving on most OSes.
    """
    return re.sub(r'[\\/:"*?<>|]+', "_", filename)

def is_valid_url(url: str) -> bool:
    """
    Check if the given string is a valid YouTube URL

    Args:
        url (str): URL string.

    Returns:
        bool: True if valid, False otherwise.
    """
    return "youtube.com/watch?" in url or "youtu.be/" in url
