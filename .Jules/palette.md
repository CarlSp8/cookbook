## 2025-02-28 - FastRTC Implicit Submission Discovery
**Learning:** The explicit instructional `info` text ("Press Enter to submit and continue") is critical for WebRTC API keys, as users otherwise miss that submission is bound specifically to Enter without an explicit submit button, preventing the UI from unhiding the core interaction components.
**Action:** Always add explicit info text on single-input auth flows where `api_key.submit()` hides/unhides layout without an associated button.
