from pathlib import Path

import qrcode

qrcode.make("https://isaiah-foster.github.io/").save(Path(__file__).parent / "isaiah-foster_qr.png")
