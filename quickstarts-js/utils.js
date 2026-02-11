/*
 * Copyright 2025 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Shared utilities for Gemini API quickstart scripts
 */

/**
 * Initialize the Google GenAI client
 * @param {string} version - SDK version (default: "1.4.0")
 * @returns {Promise<Object>} Initialized GoogleGenAI client
 */
async function initializeGeminiClient(version = "1.4.0") {
  const module = await import(`https://esm.sh/@google/genai@${version}`);
  const GoogleGenAI = module.GoogleGenAI;
  return new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
}

/**
 * Convert a blob to base64 string
 * @param {Blob} blob - The blob to convert
 * @returns {Promise<string>} Base64 encoded string (without data URL prefix)
 */
function blobToBase64(blob) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onerror = reject;
    reader.onloadend = () => resolve(reader.result.split(',')[1]);
    reader.readAsDataURL(blob);
  });
}

export { initializeGeminiClient, blobToBase64 };
