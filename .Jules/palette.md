## 2025-04-10 - Implicit Submission UX
**Learning:** Gradio textboxes with `.submit()` event listeners require explicit instructions because there's no visual "submit" button by default, leading to user confusion about how to proceed. External links in web apps also risk navigating users away from their app state without `target="_blank"`.
**Action:** Always add an explicit instruction via the `info` parameter when binding `.submit()` to inputs without an accompanying submit button. Ensure external links use `target="_blank"` and `rel="noopener noreferrer"`.
