"""mkdocs serve

This module wraps the vanilla `mkdocs serve` with an additional call
to :module:`_watch.py` which keeps an eye on changes to templates.

"""

import os
import threading
import importlib
import subprocess

# Expose watch.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

watch = importlib.import_module("_watch")
thread = threading.Thread(target=watch.run)
thread.daemon = True
thread.start()

# Block
subprocess.call(["mkdocs", "serve", "-a", "0.0.0.0:8000"])
