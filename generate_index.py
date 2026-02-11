#!/usr/bin/env python3
"""
Generate index.html for the Gemini API Cookbook website
"""
import os
import json
from pathlib import Path

def scan_directory(base_path, dir_name):
    """Scan a directory for notebooks and Python files"""
    path = Path(base_path) / dir_name
    items = []
    
    if path.exists() and path.is_dir():
        for item in sorted(path.iterdir()):
            if item.is_file():
                if item.suffix == '.ipynb':
                    items.append({
                        'name': item.stem.replace('_', ' '),
                        'path': f'{dir_name}/{item.name}',
                        'type': 'notebook'
                    })
                elif item.suffix == '.py':
                    items.append({
                        'name': item.stem.replace('_', ' '),
                        'path': f'{dir_name}/{item.name}',
                        'type': 'python'
                    })
    
    return items

def generate_html(quickstarts, examples):
    """Generate the HTML content"""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gemini API Cookbook - Local Browser</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .content {
            padding: 40px;
        }
        
        .intro {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            border-left: 4px solid #667eea;
        }
        
        .intro h2 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .section {
            margin-bottom: 40px;
        }
        
        .section h2 {
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.8em;
        }
        
        .items-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .item-card {
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
        }
        
        .item-card:hover {
            border-color: #667eea;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
            transform: translateY(-5px);
        }
        
        .item-card h3 {
            color: #333;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        
        .item-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            margin-top: auto;
        }
        
        .badge-notebook {
            background: #e3f2fd;
            color: #1976d2;
        }
        
        .badge-python {
            background: #fff3e0;
            color: #f57c00;
        }
        
        .item-card a {
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        
        .search-box {
            margin-bottom: 30px;
            padding: 15px;
            background: white;
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            font-size: 1.1em;
            width: 100%;
            transition: border-color 0.3s ease;
        }
        
        .search-box:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .stats {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .stat-card {
            flex: 1;
            min-width: 150px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
        }
        
        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
        }
        
        footer {
            background: #f8f9fa;
            padding: 30px;
            text-align: center;
            color: #666;
        }
        
        footer a {
            color: #667eea;
            text-decoration: none;
        }
        
        footer a:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 768px) {
            .items-grid {
                grid-template-columns: 1fr;
            }
            
            header h1 {
                font-size: 1.8em;
            }
            
            .content {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🌟 Gemini API Cookbook</h1>
            <p>Explore tutorials, quickstarts, and practical examples for the Gemini API</p>
        </header>
        
        <div class="content">
            <div class="intro">
                <h2>Welcome to Your Local Cookbook!</h2>
                <p>This is your local instance of the Gemini API Cookbook. Browse through quickstarts to learn API features, or explore examples to see practical applications.</p>
                <p><strong>To run notebooks:</strong> Use Jupyter Notebook or JupyterLab. Click the links below to open them.</p>
            </div>
            
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{quickstart_count}</div>
                    <div class="stat-label">Quickstarts</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{example_count}</div>
                    <div class="stat-label">Examples</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{total_count}</div>
                    <div class="stat-label">Total Resources</div>
                </div>
            </div>
            
            <input type="text" id="searchBox" class="search-box" placeholder="🔍 Search for tutorials and examples...">
            
            <div class="section">
                <h2>📚 Quickstarts</h2>
                <p style="margin-bottom: 20px; color: #666;">Step-by-step guides covering introductory topics and specific API features.</p>
                <div class="items-grid" id="quickstarts">
                    {quickstart_items}
                </div>
            </div>
            
            <div class="section">
                <h2>💡 Examples</h2>
                <p style="margin-bottom: 20px; color: #666;">Practical use cases demonstrating how to combine multiple features.</p>
                <div class="items-grid" id="examples">
                    {example_items}
                </div>
            </div>
        </div>
        
        <footer>
            <p>
                <strong>Gemini API Cookbook</strong> - Local Deployment<br>
                <a href="https://ai.google.dev/gemini-api/docs" target="_blank">Official Documentation</a> | 
                <a href="https://github.com/google-gemini/cookbook" target="_blank">GitHub Repository</a> | 
                <a href="https://aistudio.google.com/app/apikey" target="_blank">Get API Key</a>
            </p>
        </footer>
    </div>
    
    <script>
        // Search functionality
        const searchBox = document.getElementById('searchBox');
        const quickstarts = document.getElementById('quickstarts');
        const examples = document.getElementById('examples');
        
        searchBox.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            
            // Search in quickstarts
            const quickstartCards = quickstarts.getElementsByClassName('item-card');
            Array.from(quickstartCards).forEach(card => {
                const text = card.textContent.toLowerCase();
                card.style.display = text.includes(searchTerm) ? 'block' : 'none';
            });
            
            // Search in examples
            const exampleCards = examples.getElementsByClassName('item-card');
            Array.from(exampleCards).forEach(card => {
                const text = card.textContent.toLowerCase();
                card.style.display = text.includes(searchTerm) ? 'block' : 'none';
            });
        });
    </script>
</body>
</html>
"""
    
    # Generate quickstart items
    quickstart_items = ""
    for item in quickstarts:
        badge_class = "badge-notebook" if item['type'] == 'notebook' else "badge-python"
        badge_text = "Notebook" if item['type'] == 'notebook' else "Python Script"
        quickstart_items += f"""
                    <div class="item-card">
                        <a href="{item['path']}">
                            <h3>{item['name']}</h3>
                            <span class="item-badge {badge_class}">{badge_text}</span>
                        </a>
                    </div>"""
    
    # Generate example items
    example_items = ""
    for item in examples:
        badge_class = "badge-notebook" if item['type'] == 'notebook' else "badge-python"
        badge_text = "Notebook" if item['type'] == 'notebook' else "Python Script"
        example_items += f"""
                    <div class="item-card">
                        <a href="{item['path']}">
                            <h3>{item['name']}</h3>
                            <span class="item-badge {badge_class}">{badge_text}</span>
                        </a>
                    </div>"""
    
    # Replace placeholders
    html = html.replace('{quickstart_count}', str(len(quickstarts)))
    html = html.replace('{example_count}', str(len(examples)))
    html = html.replace('{total_count}', str(len(quickstarts) + len(examples)))
    html = html.replace('{quickstart_items}', quickstart_items)
    html = html.replace('{example_items}', example_items)
    
    return html

def main():
    base_path = Path(__file__).parent
    
    # Scan directories
    quickstarts = scan_directory(base_path, 'quickstarts')
    examples = scan_directory(base_path, 'examples')
    
    # Generate HTML
    html_content = generate_html(quickstarts, examples)
    
    # Write to file
    output_path = base_path / 'index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated index.html with {len(quickstarts)} quickstarts and {len(examples)} examples")
    print(f"📄 Output: {output_path}")

if __name__ == "__main__":
    main()
