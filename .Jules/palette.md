## 2025-02-19 - Graceful API Key Handling
**Learning:** Users often launch example apps without setting environment variables first. Crashing with a traceback is a poor experience.
**Action:** Always include an optional UI input for API keys (hidden if env var is set) and validate the key at runtime or connection time, showing a helpful message if missing.
