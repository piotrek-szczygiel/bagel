import logging
import os
import subprocess
import sys
import time
from typing import Dict

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

output_dir = ""
cmd_template = ["pipenv", "run", "pyside2-uic", "-d", "-o"]
timestamps: Dict[str, float] = {}


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.ui"]

    def process(self, event) -> None:
        now = time.monotonic()

        ui_path = event.src_path

        if ui_path in timestamps:
            if now < timestamps[ui_path] + 1.0:
                return

        timestamps[ui_path] = now

        name = os.path.splitext(os.path.basename(ui_path))[0]
        py_path = os.path.join(output_dir, name + ".py")

        cmd = cmd_template + [py_path, ui_path]
        subprocess.run(cmd)

        logging.info(ui_path + " -> " + py_path)

    def on_modified(self, event) -> None:
        self.process(event)

    def on_created(self, event) -> None:
        self.process(event)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "usage: {} intput_dir output_dir".format(sys.argv[0]),
            file=sys.stderr,
        )
        sys.exit(1)

    input_dir = os.path.normpath(sys.argv[1])
    output_dir = os.path.normpath(sys.argv[2])

    if not os.path.isdir(input_dir):
        print(
            "input directory {} does not exists".format(input_dir),
            file=sys.stderr,
        )
        sys.exit(1)

    if not os.path.isdir(output_dir):
        print(
            "output directory {} does not exists".format(output_dir),
            file=sys.stderr,
        )
        sys.exit(1)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    observer = Observer()
    observer.schedule(MyHandler(), path=input_dir)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
