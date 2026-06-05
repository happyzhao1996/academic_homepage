# Academic Homepage Template

This is a lightweight bilingual Jekyll template for an academic personal homepage. It includes placeholder content for profile details, publications, education, experience, honors, service, conferences, research, patents, and notes.

## Local Preview

```powershell
bundle install
bundle exec jekyll serve --livereload
```

Then open <http://127.0.0.1:4000/>.

On Windows, `run_server.ps1` and `run_server.bat` can start the local Jekyll preview after Ruby and Bundler are installed.

## Editing Content

- Profile, links, education, experience, research, honors, service, conferences, and patents: `_data/profile.yml`
- Navigation labels and anchors: `_data/navigation.yml`
- Publication records: `_data/publications.yml`
- Selected publication records: `_data/selected_publications.yml`
- Citation chart data: `_data/citation_history.yml`
- Notes and posts: `_posts/`

The default language is English at `/`; Chinese pages live under `/zh/`.

## Updating Scholar Data

Jekyll reads static YAML files in `_data/`. The bundled script uses Albert Einstein's public Google Scholar profile as a safe example and limits publication fetching to 20 records by default:

```powershell
python scripts/update_scholar.py
```

To use your own Scholar profile:

```powershell
python scripts/update_scholar.py --user-id <scholar_user_id> --limit 20
```

You can also set `SCHOLAR_USER_ID` and run the script without `--user-id`. If Google blocks the request, the script exits without overwriting the existing YAML files.

## License

This template is released under the Apache License 2.0. See `LICENSE`.
