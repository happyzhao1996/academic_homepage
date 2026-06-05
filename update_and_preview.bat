@echo off
setlocal
cd /d "%~dp0"

set "SITE_URL=http://127.0.0.1:4000/"
set "RUBY_BIN=C:\Ruby33-x64\bin"
if exist "%RUBY_BIN%\ruby.exe" set "PATH=%RUBY_BIN%;%PATH%"

echo.
echo Updating Google Scholar data...
echo Using fast mode: publication list and citation history only.
where py >nul 2>nul
if %ERRORLEVEL%==0 (
  py -3 scripts\update_scholar.py --skip-links --limit 20
) else (
  python scripts\update_scholar.py --skip-links --limit 20
)

if ERRORLEVEL 1 (
  echo.
  echo Google Scholar update failed. Existing _data files were kept.
  choice /C YN /M "Start local Jekyll preview anyway"
  if ERRORLEVEL 2 exit /b 1
)

echo.
echo Starting Jekyll preview at %SITE_URL%
start "" powershell -NoProfile -WindowStyle Hidden -Command "Start-Sleep -Seconds 5; Start-Process '%SITE_URL%'"
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --livereload

echo.
pause
