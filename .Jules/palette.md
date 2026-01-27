## 2025-05-23 - Graceful API Key Handling in Gradio
**Learning:** Hard crashes on missing env vars (like API keys) are hostile UX. Users often run examples without setup.
**Action:** Always wrap the main UI in a check for the key. If missing, render a friendly `gr.Markdown` warning + `gr.Warning()` instead of letting the app crash or the registry function fail.
