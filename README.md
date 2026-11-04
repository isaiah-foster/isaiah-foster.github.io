# isaiah-foster.github.io

Personal website for Isaiah Foster, hosted on GitHub Pages at
<https://isaiah-foster.github.io/>.

It's a plain static site with no framework, bundler, build step, or JavaScript.
It follows the system light/dark setting.

| File | Purpose |
| --- | --- |
| `index.html` | Home page: intro, experience, projects, skills, education |
| `resume.html` | Resume page that embeds `resume.pdf` |
| `resume.pdf` | Current resume |
| `style.css` | All styles |
| `palouse.svg` | Hills illustration on the home page (generated) |
| `favicon.svg` | Site icon |
| `tools/` | Generators for the QR code and the hills illustration (not served content) |

## Run locally

```sh
python3 -m http.server
```

Then open <http://localhost:8000>.

## Update the resume

Replace `resume.pdf` and commit. The resume page and download button pick it up automatically.

## Regenerate the QR code

```sh
pip install "qrcode[pil]"
python3 tools/qrcode_maker.py
```

## Regenerate the hills illustration

```sh
python3 tools/palouse_art.py
```

Colors and the random seed are at the top of the script. Light and dark colors
live inside the SVG, so keep its fill colors in sync with `--bg` in `style.css`.
