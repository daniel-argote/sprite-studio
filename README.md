Sprite Studio v1.2

A specialized tool for game developers to quickly clean up sprite assets. This project uses a lightweight Python backend to serve a high-performance, client-side HTML5 Canvas interface for removing backgrounds and smoothing edges.

Features

Color Sampling: Click anywhere on the sprite to instantly select the background color you want to remove.

Real-time Processing: Adjust tolerance and smoothing on the fly with immediate visual feedback.

Edge Smoothing: Uses alpha-falloff logic to prevent "jaggies" on processed sprites.

Pixel-Perfect Preview: Supports zooming up to 400% with pixelated rendering for precise asset inspection.

Zero Dependencies: Runs on standard Python libraries—no need to install complex machine learning frameworks.

Project Structure

app.py: A Python-based automation script that launches a local server and opens your browser.

sprite_studio.html: The core application containing the UI and the Canvas-based image processing logic.

LICENSE: MIT License information.

Getting Started

Local Development

Ensure app.py and sprite_studio.html are in the same folder.

Run the server script:

python app.py


The app will automatically open at http://localhost:8000.

Running without Python

You can also simply open sprite_studio.html directly in any modern web browser.

Deployment (GitHub Pages)

This app is 100% static and can be hosted for free:

Push this code to a GitHub repository.

Go to Settings > Pages.

Select the main branch and /root folder.

Your Sprite Studio will be live at https://<your-username>.github.io/<repo-name>/sprite_studio.html.

How to Use

Load: Drag and drop an image file (PNG, JPG) into the browser window.

Sample: Click on the background color in the preview area to target it for removal.

Refine: Use the Tolerance slider to catch similar shades and Edge Smoothing to soften the transition.

Export: Click "Export Game Sprite" to save your transparent PNG.

License

This project is licensed under the MIT License - see the LICENSE file for details.