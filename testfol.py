import os
import pathlib

for obj in os.scandir():
    fname=pathlib.Path(obj)
    print(fname)
    form=fname.suffix.lower()
    print(form)
    print()
