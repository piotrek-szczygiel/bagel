import os
import subprocess
import pathlib
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "usage: {} intput_dir output_dir".format(sys.argv[0]),
            file=sys.stderr,
        )
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

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

    cmd_template = ["pipenv", "run", "pyside2-uic", "-d", "-o"]

    pathlist = pathlib.Path(input_dir).glob("**/*.ui")

    for path_obj in pathlist:
        ui_path = str(path_obj)
        name = os.path.splitext(os.path.basename(ui_path))[0]
        py_path = os.path.join(output_dir, name + ".py")

        cmd = cmd_template + [py_path, ui_path]
        subprocess.run(cmd)
