@echo off
chcp 65001 >nul
echo ====================================================================
echo HUGO AUTOMATED DEPLOYMENT TOOL - 1-CLICK GIT PUSH
echo ====================================================================

echo [1/3] Staging all changed files...
git add .

echo [2/3] Committing changes...
git commit -m "Update Hugo site content"

echo [3/3] Pushing to GitHub repository (origin main)...
git push origin main

if %errorlevel% neq 0 (
    echo.
    echo ====================================================================
    echo [ERROR] Push failed! Please check your network or Git settings.
    echo ====================================================================
    pause
    exit /b %errorlevel%
)

echo.
echo ====================================================================
echo [SUCCESS] Hugo site update successfully pushed to GitHub Pages!
echo ====================================================================
pause
