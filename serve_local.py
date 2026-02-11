#!/usr/bin/env python3
"""
Local web server for Gemini API Cookbook
Serves the cookbook content with proper MIME types for Jupyter notebooks
"""
import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path
import subprocess

PORT = 8000

class CookbookHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler for serving cookbook content"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)
    
    def end_headers(self):
        """Add custom headers"""
        # Enable CORS for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        # Set proper MIME type for Jupyter notebooks
        if self.path.endswith('.ipynb'):
            self.send_header('Content-Type', 'application/x-ipynb+json')
        
        super().end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        # Redirect root to index.html
        if self.path == '/':
            self.path = '/index.html'
        
        return super().do_GET()
    
    def log_message(self, format, *args):
        """Custom log format"""
        sys.stdout.write(f"[Server] {args[0]} - {args[1]}\n")

def generate_index():
    """Generate the index.html file"""
    print("🔨 Generating index.html...")
    try:
        result = subprocess.run(
            [sys.executable, 'generate_index.py'],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating index: {e.stderr}")
        return False
    return True

def main():
    """Start the web server"""
    print("=" * 60)
    print("🌟 Gemini API Cookbook - Local Web Server")
    print("=" * 60)
    print()
    
    # Check if index.html exists, generate if not
    index_path = Path(__file__).parent / 'index.html'
    if not index_path.exists():
        print("📄 index.html not found. Generating...")
        if not generate_index():
            print("❌ Failed to generate index.html")
            return
    else:
        # Optionally regenerate to ensure it's up to date
        print("📄 Regenerating index.html to ensure it's up to date...")
        generate_index()
    
    print()
    print(f"🚀 Starting server on http://localhost:{PORT}")
    print()
    print("📚 Available endpoints:")
    print(f"   • Main page:      http://localhost:{PORT}")
    print(f"   • Quickstarts:    http://localhost:{PORT}/quickstarts/")
    print(f"   • Examples:       http://localhost:{PORT}/examples/")
    print()
    print("💡 Tips:")
    print("   • Click on any notebook to download it")
    print("   • Use 'jupyter notebook' to run notebooks interactively")
    print("   • Press Ctrl+C to stop the server")
    print()
    print("=" * 60)
    print()
    
    # Change to the script directory
    os.chdir(Path(__file__).parent)
    
    # Create server
    with socketserver.TCPServer(("", PORT), CookbookHTTPRequestHandler) as httpd:
        try:
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
            
            # Start serving
            print(f"✅ Server is running. Access it at http://localhost:{PORT}")
            print("🌐 Browser should open automatically...")
            print()
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped by user")
            print("👋 Thank you for using Gemini API Cookbook!")
            sys.exit(0)

if __name__ == "__main__":
    main()
