# Server lokal LinguaLens:
#  1. menyajikan file website (index.html, audio, dll.)
#  2. meneruskan gambar dari browser ke Roboflow (menghindari blokir CORS)
# Jalankan:  python server.py    lalu buka http://localhost:8000
# Tidak perlu install library tambahan.

import json
import urllib.request
import urllib.error
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

# ===== ISI DUA BARIS INI =====
WORKFLOW_URL = " "
API_KEY = " "
# =============================

PORT = 8000


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/detect":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        try:
            image_b64 = json.loads(self.rfile.read(length))["image"]
        except Exception:
            self.send_error(400, "Body harus berisi field 'image'")
            return

        payload = json.dumps({
            "api_key": API_KEY,
            "inputs": {"image": {"type": "base64", "value": image_b64}},
        }).encode()

        req = urllib.request.Request(
            WORKFLOW_URL,
            data=payload,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + API_KEY,
                "User-Agent": "LinguaLens/1.0",
            },
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                status, data = r.status, r.read()
        except urllib.error.HTTPError as e:
            status, data = e.code, e.read()
        except Exception as e:
            status, data = 502, json.dumps({"error": str(e)}).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    if "PASTE" in WORKFLOW_URL or "PASTE" in API_KEY:
        print("Isi WORKFLOW_URL dan API_KEY di server.py dulu.")
    else:
        print(f"Server jalan di http://localhost:{PORT}  (Ctrl+C untuk berhenti)")
        ThreadingHTTPServer(("", PORT), Handler).serve_forever()