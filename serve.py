import os, http.server, socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 3333
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.js': 'application/javascript', '.css': 'text/css'})

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'Serving on http://localhost:{PORT}')
    httpd.serve_forever()
