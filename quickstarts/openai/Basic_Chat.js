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

/* Markdown (render)
# Basic Chat with Gemini using OpenAI SDK (JavaScript)

This example demonstrates how to use the **OpenAI Node.js SDK** to interact with **Gemini models** for basic text generation and chat completions.
*/

/* Markdown (render)
## Setup

### Install the OpenAI SDK

```bash
npm install openai
```

### API Key Configuration

Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Set it as an environment variable:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Or in code (not recommended for production):
```javascript
const client = new OpenAI({
    apiKey: 'your-api-key-here',
    baseURL: 'https://generativelanguage.googleapis.com/v1beta/openai/'
});
```
*/

// [CODE STARTS]
// Import OpenAI SDK
const OpenAI = (await import('openai')).default;

// Initialize client with Gemini endpoint
const client = new OpenAI({
    apiKey: process.env.GOOGLE_API_KEY || process.env.GEMINI_API_KEY,
    baseURL: 'https://generativelanguage.googleapis.com/v1beta/openai/'
});
// [CODE ENDS]

/* Markdown (render)
## List Available Models

First, let's see which Gemini models are available:
*/

// [CODE STARTS]
const models = await client.models.list();

console.log("Available Gemini models:");
for (const model of models.data) {
    if (model.id.toLowerCase().includes('gemini')) {
        console.log(`  - ${model.id}`);
    }
}
// [CODE ENDS]

/* Output Sample
Available Gemini models:
  - gemini-2.5-flash-lite
  - gemini-2.5-flash
  - gemini-2.5-pro
  - gemini-3-flash-preview
  - gemini-3-pro-preview
*/

/* Markdown (render)
## Simple Text Generation

Let's start with a simple single-turn text generation:
*/

// [CODE STARTS]
const MODEL = "gemini-2.5-flash"; // Fast, efficient model

const response = await client.chat.completions.create({
    model: MODEL,
    messages: [
        { role: "user", content: "Write a haiku about artificial intelligence." }
    ]
});

console.log(response.choices[0].message.content);
// [CODE ENDS]

/* Output Sample
Silicon neurons fire,
Learning patterns, swift and bright,
Future's dawn takes flight.
*/

/* Markdown (render)
## Multi-turn Conversation

Build a conversation with multiple messages:
*/

// [CODE STARTS]
const messages = [
    { role: "user", content: "What is the capital of France?" },
    { role: "assistant", content: "The capital of France is Paris." },
    { role: "user", content: "What is its population?" }
];

const multiTurnResponse = await client.chat.completions.create({
    model: MODEL,
    messages: messages
});

console.log(multiTurnResponse.choices[0].message.content);
// [CODE ENDS]

/* Output Sample
The population of Paris proper is approximately 2.1 million people. However, the wider Paris metropolitan area (Île-de-France region) has a population of around 12 million people, making it one of the largest metropolitan areas in Europe.
*/

/* Markdown (render)
## System Instructions

Use a system message to set the behavior:
*/

// [CODE STARTS]
const systemResponse = await client.chat.completions.create({
    model: MODEL,
    messages: [
        { role: "system", content: "You are a helpful assistant that speaks like a pirate." },
        { role: "user", content: "Tell me about the weather." }
    ]
});

console.log(systemResponse.choices[0].message.content);
// [CODE ENDS]

/* Output Sample
Ahoy there, matey! The weather, ye say? Well, I can't be seein' the skies from me cabin here, but I can tell ye how to find out!

Just tell me yer location, and I'll be consultin' me charts (well, the internet) to give ye the forecast, savvy? Otherwise, ye best be lookin' out yer own porthole or askin' a local landlubber!
*/

/* Markdown (render)
## Temperature and Generation Parameters

Control the randomness and creativity of responses:
*/

// [CODE STARTS]
// Creative response (high temperature)
const creativeResponse = await client.chat.completions.create({
    model: MODEL,
    messages: [{ role: "user", content: "Write a creative story opening." }],
    temperature: 1.5,
    max_tokens: 100
});

console.log("Creative (temperature=1.5):");
console.log(creativeResponse.choices[0].message.content);
console.log();

// Focused response (low temperature)
const focusedResponse = await client.chat.completions.create({
    model: MODEL,
    messages: [{ role: "user", content: "Write a creative story opening." }],
    temperature: 0.2,
    max_tokens: 100
});

console.log("Focused (temperature=0.2):");
console.log(focusedResponse.choices[0].message.content);
// [CODE ENDS]

/* Output Sample
Creative (temperature=1.5):
The rain tasted like copper and regret. Elara licked her lips, the metallic tang mixing with the salt of her tears as she stared at the crimson puddle spreading beneath the overturned fruit cart. It wasn't her blood. Not yet. But the city's shadows were deepening, and she knew, with a bone-deep certainty

Focused (temperature=0.2):
The rain hammered against the corrugated iron roof, a relentless percussion that mirrored the frantic beat of Elara's heart. She pressed her back against the cold, damp brick wall of the alley, her breath misting in the frigid air. The city
*/

/* Markdown (render)
## Streaming Responses

Get responses as they're generated in real-time:
*/

// [CODE STARTS]
console.log("Streaming response:");
console.log("-".repeat(50));

const stream = await client.chat.completions.create({
    model: MODEL,
    messages: [{ role: "user", content: "Count from 1 to 5 with descriptions." }],
    stream: true
});

for await (const chunk of stream) {
    if (chunk.choices[0]?.delta?.content) {
        process.stdout.write(chunk.choices[0].delta.content);
    }
}

console.log("\n" + "-".repeat(50));
// [CODE ENDS]

/* Output Sample
Streaming response:
--------------------------------------------------
1. **One:** The singular, the beginning, the foundation upon which all else is built. It represents unity and individuality.
2. **Two:** The pair, duality, balance. It signifies partnership, comparison, and the beginning of plurality.
3. **Three:** The triad, stability, and completion. Often seen as a magical or powerful number, representing harmony.
4. **Four:** The square, solidity, order. It symbolizes structure, earthiness, and the four directions.
5. **Five:** The pentad, change, and humanity. It represents the five senses, dynamism, and adventure.
--------------------------------------------------
*/

/* Markdown (render)
## Response Metadata

Access token usage and other metadata:
*/

// [CODE STARTS]
const metadataResponse = await client.chat.completions.create({
    model: MODEL,
    messages: [{ role: "user", content: "Explain quantum computing in one sentence." }]
});

console.log("Response:", metadataResponse.choices[0].message.content);
console.log();
console.log("Metadata:");
console.log(`  Model: ${metadataResponse.model}`);
console.log(`  Finish reason: ${metadataResponse.choices[0].finish_reason}`);
if (metadataResponse.usage) {
    console.log(`  Prompt tokens: ${metadataResponse.usage.prompt_tokens}`);
    console.log(`  Completion tokens: ${metadataResponse.usage.completion_tokens}`);
    console.log(`  Total tokens: ${metadataResponse.usage.total_tokens}`);
}
// [CODE ENDS]

/* Output Sample
Response: Quantum computing harnesses the principles of quantum mechanics, like superposition and entanglement, to perform calculations in fundamentally different ways than classical computers, potentially solving problems that are currently intractable.

Metadata:
  Model: gemini-2.5-flash
  Finish reason: stop
  Prompt tokens: 12
  Completion tokens: 38
  Total tokens: 50
*/

/* Markdown (render)
## Error Handling

Handle API errors gracefully:
*/

// [CODE STARTS]
try {
    const errorResponse = await client.chat.completions.create({
        model: "invalid-model-name",
        messages: [{ role: "user", content: "Hello" }]
    });
} catch (error) {
    console.log("Error caught:");
    console.log(`  Status: ${error.status}`);
    console.log(`  Message: ${error.message}`);
}
// [CODE ENDS]

/* Output Sample
Error caught:
  Status: 404
  Message: Model not found: invalid-model-name
*/

/* Markdown (render)
## Next Steps

Explore more advanced features:

- [Full OpenAI Compatibility Guide](../Get_started_OpenAI_Compatibility.ipynb) - Complete guide with advanced features
- [OpenAI SDK README](./README.md) - Overview of all available guides
- [Quick Reference](./Quick_Reference.md) - Cheat sheet with common patterns

For more information:
- [OpenAI SDK Compatibility Docs](https://ai.google.dev/gemini-api/docs/openai)
- [Full Getting Started Guide](../Get_started_OpenAI_Compatibility.ipynb)
- [OpenAI Node.js SDK](https://github.com/openai/openai-node)
*/
