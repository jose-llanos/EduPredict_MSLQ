#!/usr/bin/env python3
"""
Servidor simple para documentación HTML y ReDoc
Se ejecuta en puerto 8001 para no interferir con la API en 8000
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8001
DOCS_DIR = Path(__file__).parent / "docs"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler con CORS y manejo de MIME types"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DOCS_DIR), **kwargs)
    
    def end_headers(self):
        """Agregar headers CORS"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Manejar CORS preflight"""
        self.send_response(200)
        self.end_headers()
    
    def guess_type(self, path):
        """Tipos MIME mejorados"""
        if path.endswith('.json'):
            return 'application/json'
        return super().guess_type(path)
    
    def log_message(self, format, *args):
        """Log más limpio"""
        if '200' in format:
            print(f"✅ {args[0]}")
        elif '404' in format:
            print(f"❌ 404: {args[0]}")


def main():
    """Ejecutar servidor"""
    Handler = MyHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"""
╔════════════════════════════════════════════════════════════╗
║          📚 Servidor de Documentación ReDoc                ║
╚════════════════════════════════════════════════════════════╝

🌐 Servidor ejecutándose en: http://localhost:{PORT}

📖 Accede a:
  • HTML Completo: http://localhost:{PORT}/documentacion-completa.html
  • ReDoc Index:   http://localhost:{PORT}/index.html
  • OpenAPI JSON:  http://localhost:{PORT}/../openapi.json

📁 Sirviendo desde: {DOCS_DIR}

Presiona CTRL+C para detener el servidor
════════════════════════════════════════════════════════════
            """)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Servidor detenido")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Error: Puerto {PORT} en uso")
            print(f"Usa: lsof -ti:{PORT} | xargs kill -9")
        else:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
