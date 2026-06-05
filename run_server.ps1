$rubyBin = "C:\Ruby33-x64\bin"
if (Test-Path $rubyBin) {
  $env:Path = "$rubyBin;$env:Path"
}

Write-Host ""
Write-Host "Updating Google Scholar data..."
Write-Host "Using fast mode: publication list and citation history only."
if (Get-Command py -ErrorAction SilentlyContinue) {
  & py -3 scripts\update_scholar.py --skip-links --limit 20
} else {
  & python scripts\update_scholar.py --skip-links --limit 20
}

if ($LASTEXITCODE -ne 0) {
  Write-Host ""
  Write-Host "Google Scholar update failed. Existing _data files were kept."
}

Write-Host ""
Write-Host "Starting Jekyll preview..."
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --livereload
