#!/bin/bash
# Install packages.
pip3 install --upgrade moviepy
pip3 install --upgrade questionary
pip3 install --upgrade PyAudio
pip3 install --upgrade mutagen
pip3 install --upgrade pyinstaller
# Create bin files.
pyinstaller --onefile videotomp3.py
pyinstaller --onefile videotowav.py
pyinstaller --onefile videotoogg.py
# Move bin files.
mv dist/videoto* .
# Delete build files.
rm -rf build dist *.spec
