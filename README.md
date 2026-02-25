# Alpha Amnesia v2.0

A versatile tool for quickly removing backgrounds and cleaning up images. This project provides a high-performance, client-side HTML5 Canvas interface for removing backgrounds and smoothing edges directly in the browser.

## Features

- **Color Sampling:** Click anywhere on the image to instantly select the background color you want to remove.
- **Real-time Processing:** Adjust tolerance and smoothing on the fly with immediate visual feedback.
- **Edge Smoothing:** Uses alpha-falloff logic to prevent "jaggies" on processed images.
- **Pixel-Perfect Quality:** Zero loss in image fidelity. The tool preserves the original pixel data for non-transparent areas.
- **Zero Dependencies:** Runs entirely in the browser—no backend required.

## Live Demo

Access the tool directly via GitHub Pages:  
**[Launch Alpha Amnesia](https://daniel-argote.github.io/alpha-amnesia/)**

## Project Structure

- `index.html`: The core application containing the UI and the Canvas-based image processing logic.
- `LICENSE`: MIT License information.

## How to Use

1. **Load:** Drag and drop an image file (PNG, JPG) into the browser window.
2. **Sample:** Click on the background color in the preview area to target it for removal.
3. **Refine:** Use the Tolerance slider to catch similar shades and Edge Smoothing to soften the transition.
4. **Export:** Click "Export PNG" to save your transparent image.

## Deployment (GitHub Pages)

This app is 100% static and is designed to be hosted for free on GitHub Pages:

1. Push this code to a GitHub repository.
2. Go to **Settings > Pages**.
3. Select the `main` branch and `/ (root)` folder.
4. Your Alpha Amnesia will be live at `https://daniel-argote.github.io/alpha-amnesia/`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Built with the assistance of Google Gemini.