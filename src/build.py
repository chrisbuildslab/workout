"""Builds index.html from src/app.html + src/exercises.json.
Usage: python3 src/build.py   (from the repo root)"""
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent
ex = (R/'src/exercises.json').read_text(encoding='utf-8').replace('</', '<\\/')
html = (R/'src/app.html').read_text(encoding='utf-8').replace('__EXDATA__', ex)
(R/'index.html').write_text(html, encoding='utf-8')
# Bump the offline cache version on every build so installed iPhones pick up the update
sw = R/'sw.js'; t = sw.read_text()
n = int(re.search(r"workout-v(\d+)", t).group(1)) + 1
sw.write_text(re.sub(r"workout-v\d+", f"workout-v{n}", t))
print("built index.html, sw cache =", f"workout-v{n}")
