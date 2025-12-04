
# 🐍 Python Mini-Projects Collection

A diverse collection of small, practical Python scripts showcasing real-world use cases for various libraries like `watchdog`, `scipy`, `sounddevice`, `Pillow (PIL)`, `PyPDF2`, `pdf2docx`, `cachetools`, and more.

---

## 🌟 Project Status & Metadata

| Badge              | Status | Description                                         |
| :----------------- | :----- | :-------------------------------------------------- |
| **Stars**          |        | Show your support!                                  |
| **Forks**          |        | Fork the repository to contribute or adapt.         |
| **License**        |        | Indicates the open-source license.                  |
| **Contribution**   |        | Encourages community involvement.                   |
| **Python Version** |        | Requires a modern Python environment.               |
| **Code Quality**   |        | *Placeholder, adapt to a real metric if available.* |

---

## 📚 Table of Contents

1. **Project Overview**
2. **Installation & Setup**
3. **Project Scripts**

   * File Watcher
   * TTL Cache Utility
   * PDF File Protection
   * Duplicate File Finder
   * Voice Recorder
   * Image to Grayscale Converter
   * PDF to DOCX Converter
   * Auto Wallpaper Changer
   * Universal File Search
   * Steganography Tool
   * EAN-13 Barcode Generator    
   * Code128 Barcode Generator    
   * Image Cartoonifier (OpenCV)    
   * Network I/O Monitor    
   * RAM Usage Checker    
   * Artistic WordCloud Generator    
   * Interactive Folium Map (Single Marker)    
   * Interactive Folium Map (Multi Marker)    
   * Desktop Notification Alert    
   * Simple Data Validator (Placeholder)
   * Auto Title Generator
   * Find Your Country In MAP
   * Beep Alarm Clock
   * Mini PDF Text Writer
   * Colorful Calendar
   * Qr Code Generates
   * Image Color Extraction
   * Text to Audio
   * AudioBook
   * Color Name INTO Hex
   * Interactive HTML Table
   * Wifi QR Code Generator
4. **Contributing**
5. **License**

---

## 💡 Project Overview

This repository is a curated set of ten plus focused Python scripts designed to perform **singular, useful automation or utility tasks**.
Each script demonstrates the use of a specific third-party library or Python’s advanced built-in features.

---

## ⚙️ Installation & Setup

Install all core dependencies:

```bash
pip install watchdog cachetools PyPDF2 pdf2docx sounddevice scipy Pillow psutil folium opencv-python python-barcode wordcloud matplotlib plyer
```

> **Note:** Auto Wallpaper Changer is Windows-only (uses `ctypes` from Python standard library).

---

# 🧩 Project Scripts

Below are detailed explanations, functionality, and use cases for every script.

---

## **1. File Watcher**

<details>
<summary>👀 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses **`watchdog`** to monitor directories for real-time events.
* The `Watcher` class handles file events like creation, deletion, modification.
* `Observer` is run on a background thread and stopped gracefully with Ctrl+C.
* Filters out directory events.

### ✔ Use Cases

* Auto-reload configs when changed
* Detect new log files
* Trigger build scripts on file save

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1760859833294.jpg" width="50%" height="50%">

</details>

---

## **2. TTL Cache Utility**

<details>
<summary>⏱️ Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Implements **TTL caching** using `cachetools.TTLCache`.
* Cache auto-expires keys based on TTL.
* Simulates an expensive calculation when cache misses occur.

### ✔ Use Cases

* Cache API calls
* Cache config lookups
* Store short-lived tokens


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1760859772234.jpg" width="50%" height="50%">

</details>

---

## **3. PDF File Protection using Password**

<details>
<summary>🔒 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses **PyPDF2** to read & write PDF pages.
* Uses `getpass()` for hidden password input.
* `writer.encrypt()` applies password protection.

### ✔ Use Cases

* Secure confidential documents
* Bulk protect reports or invoices


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764735247249.jpg" width="50%" height="50%">

</details>

---

## **4. Duplicate File Finder (Power File Tool)**

<details>
<summary>🔎 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Reads files and computes **MD5 hash**.
* Identifies duplicates via hash collisions.
* Uses a dictionary to track seen files.

### ✔ Use Cases

* Free disk space
* Check for identical files

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764735292135.jpg" width="50%" height="50%">

</details>

---

## **5. Voice Recorder (WAV Save)**

<details>
<summary>🎤 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `sounddevice` to record audio.
* Saves WAV using `scipy.io.wavfile`.
* CD-quality (44100 Hz) recording.

### ✔ Use Cases

* Quick audio memos
* Audio dataset creation

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764435940098.jpg" width="50%" height="50%">

</details>

---

## **6. Convert Image to Grayscale**

<details>
<summary>🖼️ Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses **Pillow (PIL)**.
* `.convert("L")` performs grayscale conversion.
* Saves processed image.

### ✔ Use Cases

* Photography workflows
* Preprocessing for ML models

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764735322911.jpg" width="50%" height="50%">

</details>

---

## **7. Convert PDF to DOCX**

<details>
<summary>📄 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `pdf2docx.Converter`.
* Converts PDFs to editable Word (.docx).
* Attempts layout preservation.

### ✔ Use Cases

* Edit locked PDF files
* Extract structured text

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764735336629.jpg" width="50%" height="50%">

</details>

---

## **8. Auto Wallpaper Changer (Windows)**

<details>
<summary>💻 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Windows-only script.
* Uses `ctypes` to call `SystemParametersInfoW`.
* Randomly selects wallpaper from provided folder.

### ✔ Use Cases

* Automated wallpaper rotation
* Personalized desktop themes

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764735370118.jpg" width="50%" height="50%">

</details>

---

## **9. Universal File Search Tool**

<details>
<summary>🗂️ Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `os.walk()` to recursively scan directories.
* Stops on first match for efficiency.

### ✔ Use Cases

* Locate files across drives
* Build simple indexing utilities

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764735391205.jpg" width="50%" height="50%">

</details>

---

## **10. Hidden Message in Image (Steganography)**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Demonstrates **Least Significant Bit (LSB)** extraction.
* Reads pixel data using PIL.
* Extracts hidden message bits from pixel channel LSBs.

### ✔ Use Cases

* Intro to steganography
* Digital watermarking basics

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/FB_IMG_1764735353161.jpg" width="50%" height="50%">

</details>

---


## **11. EAN-13 Barcode Generator**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses **python-barcode** to create an EAN-13 standard barcode.
* Outputs the barcode image in both PNG and SVG formats.
* Demonstrates image generation from a numerical string.

### ✔ Use Cases

* Inventory management
* Product labeling and tracking
* Generating test assets

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/m.jpg" width="50%" height="50%">

</details>

---

## **12. Code128 Barcode Generator**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses **python-barcode** to create a high-density Code128 barcode..
* Code128 supports all 128 ASCII characters (numbers, uppercase, lowercase, special characters).
* Saves the output as a high-quality PNG image.

### ✔ Use Cases

* Supply chain and logistics tracking

* Asset tagging (internal use)

* Library systems

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/n.jpg" width="50%" height="50%">

</details>

---

## **13. Image Cartoonifier (OpenCV)**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses OpenCV **(cv2)** for image manipulation.
* Applies a bilateral filter to smooth colors while preserving edges.
* Uses adaptive thresholding on the grayscale version to find sharp, black outlines.
* Combines the smoothed color with the sharp edges using **cv2.bitwise_and**.

### ✔ Use Cases

* Fun photo editing effects
* Preprocessing for stylized art generation
* Basic computer vision demonstration

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/o.jpg" width="50%" height="50%">

</details>

---

## **14. Network I/O Monitor**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses **psutil** to capture network statistics.
* Measures the difference in bytes received **(bytes_recv)** and sent **(bytes_sent)** over a 1-second interval.
* Calculates and displays current ` Download and Upload speed ` in real-time.

### ✔ Use Cases

* Simple bandwidth usage tool
* Monitoring background data transfer
* System diagnostics

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/p.jpg" width="50%" height="50%">

</details>

---

## **15. RAM Usage Checker**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `psutil` to access system virtual memory statistics.
* Converts raw byte counts into human-readable **Gigabytes (GB)**.
* Reports Total, Available, Used **RAM**, and the overall usage percentage.

### ✔ Use Cases

* Resource monitoring for application testing
* Quick system status check
* Understanding memory consumption

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/q.jpg" width="50%" height="50%">

</details>

---

## **16. Artistic WordCloud Generator**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `wordcloud` and `matplotlib` for visualization.
* Generates word frequency visualization with custom styling.
* Configuration includes black background, `plasma colormap`, and a **cyan contour** for artistic effect.

### ✔ Use Cases

* Text data visualization
* Presentation graphics
* Social media analytics summaries

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/r.jpg" width="50%" height="50%">

</details>

---

## **17. Interactive Folium Map (Single Marker)**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `folium` to create an interactive Leaflet map embedded in an **HTML** file.
* Centers the map at a specified latitude/longitude (e.g., New Delhi).
* Adds a single `Marker` with a popup label that appears on click.

### ✔ Use Cases

* Geolocation visualization
* Simple location sharing
* Embedded web map utility

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/s.jpg" width="50%" height="50%">

</details>

---

## **18. Interactive Folium Map (Multi Marker)**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Expands on the basic map by iterating over a dictionary of cities and coordinates.
* Adds **multiple distinct markers** to the world map.
* Useful for visualizing geographical datasets or comparison points globally.

### ✔ Use Cases

* Global logistics visualization
* Tracking company offices worldwide
* Educational geography tools

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/u.jpg" width="50%" height="50%">

</details>

---


## **19. Desktop Notification Alert**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `plyer`, a cross-platform library, to display native OS desktop notifications.
* Implements a simple infinite loop to send recurring alerts (e.g., every 10 seconds).
* Useful for productivity timers or background job status updates.

### ✔ Use Cases

* Pomodoro timer implementation
* Long-running script completion alerts
* System warnings

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/t.jpg" width="50%" height="50%">

</details>

---

## **20. Altair (CO2 Emissions By Country)**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `altire` and `pandas` for visualization.
* Generates worrld grph to represent carbon emssion.

### ✔ Use Cases

* altire and pandas implementation
* Visualization.

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/v.jpg" width="50%" height="50%">

</details>

---

## **21. Wifi QR Code Generator**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses QR Code for your WIFI.

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/l.jpg" width="50%" height="50%">

</details>

---

## **22. Interactive HTML Table in Browser**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/k.jpg" width="50%" height="50%">

</details>

---

## **23. Tunrn Any Color Name Into HEX**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/j.jpg" width="50%" height="50%">

</details>

---

## **24. AudioBook Creater using gTTS**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `gTTS` .
* Convert Your Text File into audio book.

### ✔ Use Cases

* Using this code you can make your own audiobook app

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/i.jpg" width="50%" height="50%">

</details>

---


## **25. Speak Text As Audio**

<details>
<summary>🤫 Click to view code explanation and usage</summary>

### ✔ Code Explanation

* Uses `pyttsx3` .

### ✔ Use Cases

* what ever you input in text it speaksup.

### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/h.jpg" width="50%" height="50%">

</details>

---


## **26. Color Extraction From Image**

<details>
<summary>🤫 Click to view code explanation and usage</summary>


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/g.jpg" width="50%" height="50%">

</details>

---


## **27. QR Code Generator**

<details>
<summary>🤫 Click to view code explanation and usage</summary>


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/f.jpg" width="50%" height="50%">

</details>

---

## **28. Colorful Calander**

<details>
<summary>🤫 Click to view code explanation and usage</summary>


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/e.jpg" width="50%" height="50%">

</details>

---

## **29. Mini PDF Text Writer**

<details>
<summary>🤫 Click to view code explanation and usage</summary>


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/d.jpg" width="50%" height="50%">

</details>

---

## **30. Beep Alarm**

<details>
<summary>🤫 Click to view code explanation and usage</summary>


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/c.jpg" width="50%" height="50%">

</details>

---


## **31. Find Your Country On MAP**

<details>
<summary>🤫 Click to view code explanation and usage</summary>


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/b.jpg" width="50%" height="50%">

</details>

---
## **32. AI Auto Title Generator**

<details>
<summary>🤫 Click to view code explanation and usage</summary>


### ✔ Code

<img src="https://github.com/alok-kumar8765/python_mini_project/blob/main/Assert/a.jpg" width="50%" height="50%">

</details>

---


## 🤝 Contributing

Contributions are welcome!
Follow the steps:

1. Fork the project
2. Create a branch
3. Commit changes
4. Push your branch
5. Open a Pull Request

---

## ⚖️ License

Distributed under the **MIT License**.
See `LICENSE` for details.

---
<details>
<summary>🤫 Click to view code explanation and usage</summary>

## Gallery of Images
<!-- Auto-generated -->
{% include README_IMAGES.md %}

</details>

---