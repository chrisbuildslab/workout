# Workout — project notes for Claude

Personal strength-training web app for one user (Christophe), used on an iPhone at the gym.
Read this before changing anything; it records the decisions made so far and why.

## Conventions
- **Talk to the owner in French.** The app UI is in French.
- **Code comments, commit messages, README and these notes are in English.**
- Keep it a dependency-free static site: no framework, no bundler, no backend.

## Architecture
- Hosted as a static site on GitHub Pages (root of `main`). No server, no database, no login:
  minimal attack surface was an explicit requirement.
- Single page app: `src/app.html` (vanilla JS + CSS in one file) is the template.
  `python3 src/build.py` injects `src/exercises.json` into it and writes `index.html`.
  **Never edit `index.html` by hand** — edit `src/app.html` and rebuild.
- `build.py` also bumps the cache name in `sw.js` so installed copies update.
- PWA: `manifest.webmanifest`, icons, `sw.js`. The page is network-first (3 s timeout, then the
  cached copy, so it works offline); other files are cache-first. Stale-while-revalidate for the page
  meant iOS kept showing the old version, which is why this changed.
- Updates: `build.py` bakes the same number into the page as `APP_VER`. The app compares it with
  the server's `sw.js` on launch / return to foreground and shows a "Nouvelle version" banner;
  Settings → "Mettre à jour l'app" unregisters the SW, clears caches and reloads (data untouched).
- Reinstalling the home-screen icon wipes its storage on iOS: never suggest that as an update method.
  Installed via Safari → Share → Add to Home Screen.

## Data
- All user data lives on the device (localStorage key `muscu.v1` — the app's original name; kept so existing data isn't lost). Nothing is sent anywhere.
- Settings → Export / Import a JSON backup (`{app:"workout", version:1, programs, activeId, settings, custom, logs}`).
  Import also accepts `app:"muscu"` (backups made before the rename). Keep this format backward compatible; bump `version` and migrate on import if it changes.
- The same code also runs as a claude.ai artifact, where it syncs to the artifact's private
  per-user db (`data/users/<id>/…`: docs `state`, `current`, `ex_<id>`, `log_<id>`).
  On GitHub Pages `window.claude` is absent, so it silently falls back to local-only.
- Model:
  - program `{id, name, created, days:[{id, name, items:[{id, exId, sets, reps:"8-10", rest:90}]}]}`
  - one active program (`activeId`); every other program is "archived"
  - workout/log `{id, programId, programName, dayId, dayName, start, end, items:[{exId, target:{sets,reps,rest}, sets:[{w,r,done}]}]}`
  - in-progress workout is `current` (survives reloads); finishing moves it to `logs` (only checked sets count)
  - custom exercises `{id:"c_…", n, m, e, c, photo?(small JPEG data URL)}`

## Exercises
- 146 common exercises curated from free-exercise-db (public domain / Unlicense),
  French names and one-line French cues in `src/curate.py` (`FR` dict).
- Each has a sprite `sp/<id>.jpg` (start | end positions); the detail sheet alternates the
  two halves to suggest the movement. Run `python3 src/curate.py <path-to-free-exercise-db>`
  to regenerate after editing `FR`.

## Features chosen by the owner (and ones deliberately left out)
- In: several workout days per program; sets/reps/rest targets; workout log (kg × reps)
  pre-filled from last time; rest timer with beep (±15 s); "last time" reminder;
  custom exercises with optional photo; dark mode (auto/light/dark); history calendar;
  drag & drop (grip handle) to reorder sessions and exercises in the program editor, including
  moving an exercise to another session (replaced the up/down arrows);
  Settings → default sets / reps / rest for newly added exercises (`settings.defSets/defReps/defRest`).
- Out for now (owner didn't pick them): search box, muscle/equipment filters, favourites,
  duplicate program, per-exercise notes in programs, progression charts, 1RM estimate.
  The library is just grouped by muscle with jump chips.

## Testing
- Serve the folder (`python3 -m http.server`) and test on an emulated iPhone with Playwright
  (create program → add exercises → start workout → check set → finish → history → reload).
