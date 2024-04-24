import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sortDownloads import main as sort_downloads_main  

class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Change detected in {event.src_path}")
        sort_downloads_main()

def start_monitoring(path):
    event_handler = DownloadHandler()
    print(event_handler)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    downloads_path = r"C:\Users\sabar\Downloads" 
    start_monitoring(downloads_path)
