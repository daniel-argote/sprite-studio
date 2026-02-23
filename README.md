# Sprite Studio v1.2

A specialized tool for game developers to quickly clean up sprite assets. This project provides a high-performance, client-side HTML5 Canvas interface for removing backgrounds and smoothing edges directly in the browser.

## Features

- **Color Sampling:** Click anywhere on the sprite to instantly select the background color you want to remove.
- **Real-time Processing:** Adjust tolerance and smoothing on the fly with immediate visual feedback.
- **Edge Smoothing:** Uses alpha-falloff logic to prevent "jaggies" on processed sprites.
- **Pixel-Perfect Quality:** Zero loss in image fidelity. The tool preserves the original pixel data for non-transparent areas.
- **Zero Dependencies:** Runs entirely in the browser—no backend required.

## Live Demo

Access the tool directly via GitHub Pages:  
**[Launch Sprite Studio](https://<your-username>.github.io/<repo-name>/sprite_studio.html)**

## Project Structure

- `sprite_studio.html`: The core application containing the UI and the Canvas-based image processing logic.
- `LICENSE`: MIT License information.

## How to Use

1. **Load:** Drag and drop an image file (PNG, JPG) into the browser window.
2. **Sample:** Click on the background color in the preview area to target it for removal.
3. **Refine:** Use the Tolerance slider to catch similar shades and Edge Smoothing to soften the transition.
4. **Export:** Click "Export Game Sprite" to save your transparent PNG.

## Deployment (GitHub Pages)

This app is 100% static and is designed to be hosted for free on GitHub Pages:

1. Push this code to a GitHub repository.
2. Go to **Settings > Pages**.
3. Select the `main` branch and `/ (root)` folder.
4. Your Sprite Studio will be live at `https://<your-username>.github.io/<repo-name>/sprite_studio.html`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.