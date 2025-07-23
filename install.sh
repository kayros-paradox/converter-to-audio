#!/bin/bash
pip3 install --upgrade moviepy
pip3 install --upgrade questionary
pip3 install --upgrade PyAudio
pip3 install --upgrade mutagen
pip3 install --upgrade pyinstaller
pyinstaller --onefile videotomp3.py
pyinstaller --onefile videotowav.py
pyinstaller --onefile videotoogg.py
mv dist/videoto* .
rm -rf build dist *.spec
