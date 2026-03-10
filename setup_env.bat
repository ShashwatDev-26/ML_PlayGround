@echo off
SETLOCAL EnableDelayedExpansion

:: Define the name of the virtual environment folder
SET VENV_NAME="ML_playGround"

echo [1/3] Checking for Python...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in your PATH.
    pause
    exit /b
)

echo [2/3] Creating Virtual Environment in "!VENV_NAME!"...
IF NOT EXIST %VENV_NAME% (
    python -m venv %VENV_NAME%
    echo Virtual environment created.
) ELSE (
    echo Virtual environment already exists. Skipping creation.
)

echo [3/3] Installing dependencies from requirements.txt...
IF EXIST requirements.txt (
    call %VENV_NAME%\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    echo Installation complete!
) ELSE (
    echo Warning: requirements.txt not found. No packages installed.
)

echo.
echo Setup finished successfully. To start working, run: %VENV_NAME%\Scripts\activate
pause