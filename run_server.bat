@echo off
setlocal
cd /d "%~dp0"

set "PATH=C:\Ruby33-x64\bin;%PATH%"

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
)

echo.
echo Starting Jekyll preview...
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --livereload

echo.
pause
