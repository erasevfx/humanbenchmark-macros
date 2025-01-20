# HumanBenchmark Macros

Automated macros designed to achieve the 100th percentile on every test at [humanbenchmark.com](https://humanbenchmark.com).

![Preview Image](https://github.com/user-attachments/assets/adf4eec9-f955-4cff-b8a5-84ca0203d866)

---

## Requirements

### Necessary Python Packages
To use these scripts, you need to install the following packages:
- `pynput`
- `mss`
- `selenium`
- `pyautogui`
- `numpy`
- `pillow`
- `opencv-python`

Install them using pip:

```bash
pip install pynput mss selenium pyautogui numpy pillow opencv-python

### ChromeDriver Setup
1. **Download ChromeDriver**: Get a version compatible with your Chrome browser from [ChromeDriver Downloads](https://developer.chrome.com/docs/chromedriver/downloads).
2. **Place ChromeDriver**: Ensure the `chromedriver` executable is in a directory included in your system's PATH or in the same folder as your scripts.
3. **Enable Remote Debugging**: Run the following command in your terminal (close all open Chrome instances first):
   ```bash
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
4. Open [humanbenchmark.com](https://humanbenchmark.com) in the browser launched with remote debugging enabled.

---

## Usage

1. Launch Chrome with remote debugging (as explained above).
2. Navigate to [humanbenchmark.com](https://humanbenchmark.com).
3. Run the desired script to automate a specific test.

---

## Monitor Resolution Adjustments

You may need to update certain pixel values in the scripts to match your monitor resolution. These values are used to accurately locate and interact with on-screen elements.

---

## Credits

This repository includes a slightly optimized version of the aim trainer script by [bahadiraraz](https://github.com/bahadiraraz/humanbenchmark).
