# Workout

A small, private strength-training web app for iPhone (UI in French).

## Features
- Up to a few training programs, each split into workout days with sets / reps / rest targets
- Illustrated library of 146 common exercises, grouped by muscle, plus custom exercises (optional photo)
- Workout logging (kg × reps), pre-filled from your previous session, with a "last time" reminder
- Rest timer with a beep (±15 s adjustments)
- History calendar
- Light / dark / automatic theme

## Privacy
- Static site, no backend, no account: all data stays on your device (`localStorage`).
- Export / import a JSON backup from Settings.
- Works offline once installed (Safari → Share → Add to Home Screen).

## Project structure
```
index.html             Built app (generated, do not edit by hand)
sw.js                  Service worker (offline cache)
manifest.webmanifest   PWA manifest
icon-*.png             App icons
sp/                    Exercise sprites (start | end positions)
src/app.html           App source: vanilla JS + CSS in a single file
src/build.py           Injects exercises.json into app.html → index.html, bumps the cache version
src/curate.py          Builds exercises.json + sprites from free-exercise-db (French names and cues)
src/exercises.json     Curated exercise data
CLAUDE.md              Design decisions and data model
```

## Development
- Edit `src/app.html`, then run `python3 src/build.py` to regenerate `index.html`.
- Exercise list: edit `src/curate.py`, then `python3 src/curate.py path/to/free-exercise-db`.
- Test locally with `python3 -m http.server` and open it in a browser (iPhone viewport).
- Design decisions are recorded in `CLAUDE.md`.

## Hosting
GitHub Pages: Settings → Pages → Deploy from a branch → `main` / `(root)`.

## Credits
Exercise images and data: [free-exercise-db](https://github.com/yuhonas/free-exercise-db) (public domain / Unlicense).
