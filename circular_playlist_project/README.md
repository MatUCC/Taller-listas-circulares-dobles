# Circular Music Player

A small desktop playlist simulator built with Python, Tkinter, object-oriented programming, and a manually implemented doubly circular linked list.

## Requirements

- Python 3.10 or newer recommended
- Tkinter (usually included with the standard Python installation)
- No third-party packages are required

## Run the application

1. Extract the ZIP file.
2. Open a terminal in the `circular_playlist_project` folder.
3. Run:

   ```bash
   python app.py
   ```

## Features

- Add tracks with a title, artist, and duration in `mm:ss` format.
- Move to the next or previous track. Both directions wrap around the playlist.
- Delete the current track.
- Double-click a row to select that track as the current track.
- Highlight the current track in the playlist view.
- Handle empty playlists and playlists containing only one track.

## Project files

- `node.py`: Defines a node with track data and `next` / `prev` pointers.
- `circular_list.py`: Implements `DoublyCircularLinkedList` and its pointer operations.
- `app.py`: Creates the Tkinter interface and connects it to the data structure.

## Data structure notes

The playlist is managed through node pointers. No native Python list or `deque` is used to store or simulate the circular linked list. When the first node is inserted, its `next` and `prev` pointers refer to itself. For multiple nodes, the tail points to the head and the head points back to the tail.

This project demonstrates playlist navigation and current-track selection. It does not decode or play audio files.
