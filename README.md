# isaiah-foster.github.io

Personal website for Isaiah Foster, hosted on GitHub Pages at
<https://isaiah-foster.github.io/>.

It's a plain static site with no framework, bundler, or build step.

| File | Purpose |
| --- | --- |
| `index.html` | Home page: about, skills, projects, experience |
| `resume.html` | Resume page that embeds `resume.pdf` |
| `resume.pdf` | Current resume |
| `style.css` | All styles |
| `main.js` | Mobile menu, typing effect, fade-in on scroll |
| `favicon.svg` | Site icon |
| `tools/` | QR code generator for the site URL (not served content) |

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
