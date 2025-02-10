#!/bin/bash

current_dir="$(dirname "$0")/"
public_path="${current_dir}build/web"
src_path="${current_dir}main.py"

if [ -f main.spec ]; then
    rm main.spec
fi

if [ -f dist/main.exe ]; then
    rm dist/main.exe
fi

if [ -d build ]; then
    rm -rf build
fi

pyinstaller_path="$HOME/.local/bin/pyinstaller"

npm run build && "$pyinstaller_path" --add-data "$public_path:public" --onefile "$src_path"

echo "PyInstaller build completed."