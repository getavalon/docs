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


def run():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = os.path.join(os.path.dirname(__file__), "pages")

    event_handler = TemplateHandler()
    observer = polling.PollingObserver()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Watching %s.." % path)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

    print("Good bye")


if __name__ == "__main__":
    run()
