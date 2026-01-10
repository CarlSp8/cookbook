## 2025-01-10 - Graceful Failure in UI
**Learning:** Users can't fix configuration issues (like missing API keys) if the app crashes on startup.
**Action:** Instead of raising exceptions for missing config, return a "safe mode" UI (e.g., a Markdown warning) that explains what is missing and how to fix it. This keeps the user engaged and provides a path forward.
