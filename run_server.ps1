$rubyBin = "C:\Ruby33-x64\bin"
if (Test-Path $rubyBin) {
  $env:Path = "$rubyBin;$env:Path"
}

bundle exec jekyll serve --host 127.0.0.1 --port 4000 --livereload
