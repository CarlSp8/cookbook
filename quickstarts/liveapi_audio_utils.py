# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Shared utilities for Live API audio and video processing.

This module contains common code used across multiple Live API examples,
including audio configuration, video frame processing, and screen capture.
"""

import asyncio
import base64
import io

import cv2
import pyaudio
import PIL.Image
import mss

# Audio configuration constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024


def get_frame(cap):
    """
    Capture and process a single frame from a video capture device.
    
    Args:
        cap: OpenCV VideoCapture object
        
    Returns:
        dict: Frame data with mime_type and base64-encoded image data, or None if frame read fails
    """
    # Read the frame
    ret, frame = cap.read()
    # Check if the frame was read successfully
    if not ret:
        return None
    
    # Fix: Convert BGR to RGB color space
    # OpenCV captures in BGR but PIL expects RGB format
    # This prevents the blue tint in the video feed
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = PIL.Image.fromarray(frame_rgb)  # Now using RGB frame
    img.thumbnail([1024, 1024])

    image_io = io.BytesIO()
    img.save(image_io, format="jpeg")
    image_io.seek(0)

    mime_type = "image/jpeg"
    image_bytes = image_io.read()
    return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}


def get_screen():
    """
    Capture and process a screenshot of the entire screen.
    
    Returns:
        dict: Screen capture data with mime_type and base64-encoded image data
    """
    sct = mss.mss()
    monitor = sct.monitors[0]
    
    i = sct.grab(monitor)
    mime_type = "image/jpeg"
    image_bytes = mss.tools.to_png(i.rgb, i.size)
    img = PIL.Image.open(io.BytesIO(image_bytes))
    
    image_io = io.BytesIO()
    img.save(image_io, format="jpeg")
    image_io.seek(0)
    
    image_bytes = image_io.read()
    return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}


async def setup_audio_input_stream(pya, chunk_size=CHUNK_SIZE):
    """
    Setup and return an audio input stream.
    
    Args:
        pya: PyAudio instance
        chunk_size: Size of audio chunks to read (default: CHUNK_SIZE)
        
    Returns:
        Audio stream object configured for input
    """
    mic_info = pya.get_default_input_device_info()
    audio_stream = await asyncio.to_thread(
        pya.open,
        format=FORMAT,
        channels=CHANNELS,
        rate=SEND_SAMPLE_RATE,
        input=True,
        input_device_index=mic_info["index"],
        frames_per_buffer=chunk_size,
    )
    return audio_stream


async def setup_audio_output_stream(pya):
    """
    Setup and return an audio output stream.
    
    Args:
        pya: PyAudio instance
        
    Returns:
        Audio stream object configured for output
    """
    stream = await asyncio.to_thread(
        pya.open,
        format=FORMAT,
        channels=CHANNELS,
        rate=RECEIVE_SAMPLE_RATE,
        output=True,
    )
    return stream
