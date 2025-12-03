# Monitors a directory for changes (creation, modification, deletion) using the 'watchdog' library.

import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- 1. Define the Watcher Class ---
class Watcher(FileSystemEventHandler):
    """
    A custom handler for filesystem events.
    This class overrides the methods for handling file system events.
    """
    def __init__(self, watch_path: str):
        """Initializes the watcher with the path to monitor."""
        super().__init__()
        self.watch_path = Path(watch_path)

    def on_modified(self, event):
        """Called when a file or directory is modified."""
        # Only process file events, not directory modifications
        if not event.is_directory:
            print(f"✅ Modified: {event.src_path}")

    def on_created(self, event):
        """Called when a file or directory is created."""
        # Only process file events, not directory creation
        if not event.is_directory:
            print(f"➕ Created: {event.src_path}")

    def on_deleted(self, event):
        """Called when a file or directory is deleted."""
        # Only process file events, not directory deletion
        if not event.is_directory:
            print(f"❌ Deleted: {event.src_path}")

# --- 2. Define the Watcher Setup Function ---
def start_watcher(path: str) -> None:
    """
    Sets up the observer, schedules the handler, and starts the monitoring loop.
    :param path: The directory path to monitor.
    """
    event_handler = Watcher(path)
    observer = Observer()
    
    # Schedule the handler to watch the path, including subdirectories (recursive=True)
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    print(f"👀 Watching {path} ... Press Ctrl+C to stop.")

    # Keep the main thread alive until interrupted
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer gracefully on interruption
        observer.stop()
        print("\nWatcher stopped.")

    # Wait until the thread finishes (optional, but good practice)
    observer.join()

# --- 3. Example Usage ---
if __name__ == "__main__":
    # Note: For this example to work, you must create a directory named 'demo_folder'
    # and then perform file operations (create/modify/delete) inside it.
    start_watcher("demo_folder")