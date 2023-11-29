import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        destination_dir = "C:/Users/infos/Desktop"
        copy_file(file_path, destination_dir)

def copy_file(src_path, destination_dir):
    file_name = os.path.basename(src_path)
    destination_path = os.path.join(destination_dir, file_name)
    shutil.copy2(src_path, destination_path)
    print(f"File '{file_name}' copied to {destination_dir}")

def main():
    source_directory = "C:/Users/infos/Downloads"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_directory, recursive=True)
    observer.start()
    try:
        print(f"Watching for changes in {source_directory}...")
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
