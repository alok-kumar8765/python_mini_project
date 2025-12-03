
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
4. **Contributing**
5. **License**

---

## 💡 Project Overview

This repository is a curated set of ten focused Python scripts designed to perform **singular, useful automation or utility tasks**.
Each script demonstrates the use of a specific third-party library or Python’s advanced built-in features.

---

## ⚙️ Installation & Setup

Install all core dependencies:

```bash
pip install watchdog cachetools PyPDF2 pdf2docx sounddevice scipy Pillow
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
