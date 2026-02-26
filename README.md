# Alpha Amnesia v2.0

A versatile, client-side image utility for sprite and asset preparation. This tool provides a high-performance HTML5 Canvas interface for background removal, sprite sheet manipulation, and game navigation mask creation, all directly in the browser.

## Features

- **Color Sampling:** Click anywhere on the image to instantly select the background color you want to remove.
- **Real-time Processing:** Adjust tolerance and smoothing on the fly with immediate visual feedback.
- **Edge Smoothing:** Uses alpha-falloff logic to prevent "jaggies" on processed images.
- **Sprite Sheet Tools:** Crop, Trim transparent pixels, and Pad canvas to Power-of-2 dimensions.
- **Navigation Painter Module:** A complete toolset for creating navigation masks for game engines.
    - **Multiple Brush Types:** Define Walkable, Obstacle, and Spawn Point areas with distinct colors.
    - **Raster & Vector Tools:** Use a free-form Pen, a Flood Fill, or draw precise Rectangle and Oval shapes.
    - **Object Manipulation:** Select, Move, Resize, and Delete vector shapes to fine-tune your mask.
    - **Layered History:** A robust undo/redo system that tracks both pixel-based drawings and vector shape manipulations.
    - **Dual Export:** Save the navigation mask as a clean PNG with a transparent background, separate from the main sprite.
- **Zero Dependencies:** Runs entirely in the browser—no backend required.

## Live Demo

Access the tool directly via GitHub Pages:  
**[Launch Alpha Amnesia v2.0](https://daniel-argote.github.io/alpha-amnesia/)**

## Project Structure

- `index.html`: The core application containing the UI and the Canvas-based image processing logic.
- `LICENSE`: MIT License information.
- `README.md`: This file.

## How to Use

1. **Load:** Drag and drop an image file (PNG, JPG) into the browser window.
2. **Sample:** Click on the background color in the preview area to target it for removal.
3. **Refine:** Use the Tolerance slider to catch similar shades and Edge Smoothing to soften the transition.
4. **Manipulate:** Use the Crop, Trim, or Pad tools to adjust the canvas and sprite dimensions.
5. **Create Nav Mask:** Enable the "Nav Painter" to draw walkable areas, obstacles, and spawn points for game engine use.
6. **Export:** Click "Export PNG" to save your transparent image, or "Export Nav Mask" to save the collision map.

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