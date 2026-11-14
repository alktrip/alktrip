# Asset sources

Every image in `assets/` is original and generated from the HTML/SVG files in this folder.
Technology icons come from [Devicon](https://github.com/devicons/devicon) (MIT), rendered as single-color masks;
the logos remain trademarks of their owners and are used only to identify the technologies.
The Edita screenshot is taken from the public repository `alktrip/edita`.

Render (requires Python Playwright + Chrome, Inter and DejaVu Sans Mono fonts):

```bash
python3 stack.py                       # builds stack.html (edit the devicon path D at the top of the script)
python3 render.py "$PWD/hero.html"  banner.png 1600 420 1
python3 render.py "$PWD/stack.html" technology-stack.png 1100 900 1.6
python3 render.py "$PWD/hex.html"   hexagonal-architecture.png 1100 700 1.6
python3 render.py "$PWD/edita.html" edita-architecture.png 1100 860 1.6
```
