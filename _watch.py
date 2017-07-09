"""Watch for changes amongst templates

This module is responsible for calling :module:`_build.py` whenever
a change is made in one of the templates.

"""

import os
import sys
import time
import logging
import subprocess

from watchdog import events
from watchdog.observers import polling

module = sys.modules[__name__]
module.previous_time = time.time()
module.observer = None


class TemplateHandler(events.FileSystemEventHandler):
    def on_modified(self, event):
        super(TemplateHandler, self).on_modified(event)

        # Avoid duplicate updates within a fixed time frame
        # Sometimes, an IDE may update a file multiple times
        # for a single save. It happens instantaneously, but
        # watchdog may still pick it up and trigger the event twice.
        if module.previous_time + 1 < time.time():
            path = os.path.normpath(event.src_path)
            subprocess.call([sys.executable, "_build.py", path])

        module.previous_time = time.time()


def start(standalone=True):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = os.path.join(os.path.dirname(__file__), "pages")

    event_handler = TemplateHandler()
    observer = polling.PollingObserver()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    # Keep reference for external control
    module.observer = observer

    print("_watch.py: Watching %s.." % path)

    observer.join()

    print("_watch.py: Good bye")


def stop():
    print("_watch.py: Stopping..")
    module.observer.stop()


if __name__ == "__main__":
    start()
