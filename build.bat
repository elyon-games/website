@echo off
setlocal enabledelayedexpansion
set "current_dir=%~dp0"
set "public_path=%current_dir%build/web"
set "src_path=%current_dir%main.py"

if exist main.spec del main.spec
if exist dist\main.exe del dist\main.exe
if exist build rmdir /S /Q build

set "pyinstaller_path=%appdata%\Python\Python312\Scripts\pyinstaller.exe"

npm run build && "%pyinstaller_path%" --add-data "%public_path%:public" --onefile "%src_path%"

echo PyInstaller build completed.
