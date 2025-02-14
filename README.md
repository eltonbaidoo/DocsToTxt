### **\ud83d\udcdd DocsToTxt - Convert DOCX to TXT Locally**  

![Python](https://img.shields.io/badge/Made%20with-Python-blue)  
![License](https://img.shields.io/github/license/eltonbaidoo/DocsToTxt)  
![Repo Stars](https://img.shields.io/github/stars/eltonbaidoo/DocsToTxt?style=social)  

#### **\ud83d\udd39 About**  
DocsToTxt is a lightweight Python script that converts `.docx` files into plain `.txt` format **locally**, without requiring an internet connection. This ensures **privacy, speed, and reliability** when processing documents.  

---

## \ud83d\ude80 **Features**  
✅ Convert `.docx` to `.txt` **without losing content**  
✅ Works **offline** – no internet required  
✅ Simple and **lightweight** Python script  
✅ **Batch processing** (convert multiple files in a directory)  
✅ Cross-platform support: **Windows, macOS, Linux**  

---

## \ud83d\udccc **Installation**  
Make sure you have **Python 3.x** installed on your system.  

### **1️⃣ Clone the Repository**  
```sh  
git clone https://github.com/eltonbaidoo/DocsToTxt.git  
cd DocsToTxt  
```

### **2️⃣ Install Dependencies**  
This project requires the `python-docx` library for reading `.docx` files. Install it using:  
```sh  
pip install python-docx  
```

---

## \ud83d\udee0 **Usage**  
### **Convert a Single File**  
Run the script with the file path:  
```sh  
python docx_to_txt.py input.docx  
```
This will generate `input.txt` in the same directory.  

### **Convert All `.docx` Files in a Folder**  
Run:  
```sh  
python docx_to_txt.py /path/to/folder/  
```
All `.docx` files in the folder will be converted to `.txt`.  

---

## \ud83d\udee0 **How It Works**  
- Uses `python-docx` to **read** `.docx` content  
- Extracts **text** while preserving formatting  
- Saves it as a `.txt` file in the same location  

---

## \ud83d\udda5 **Example Output**  
### **Original DOCX File**  
\ud83d\udcdd _Sample.docx_  
```  
Title: Meeting Notes  
Date: 2025-02-13  

- Discussed project deadlines  
- Assigned tasks to team members  
- Next meeting: Monday  
```

### **Converted TXT File**  
\ud83d\udcdd _Sample.txt_  
```  
Meeting Notes  
Date: 2025-02-13  

- Discussed project deadlines  
- Assigned tasks to team members  
- Next meeting: Monday  
```

---

## ❓ **FAQ**  
**Q: Does this support `.doc` files?**  
A: No, Not yet (Working on it) this only works with `.docx` files. You can convert `.doc` to `.docx` using Microsoft Word or Google Docs.  

**Q: Will formatting be preserved?**  
A: Only **text content** is extracted. Formatting (bold, italic) is not retained in `.txt` files.  

**Q: Can I use this on Mac/Linux?**  
A: Yes! As long as Python is installed, it works on **Windows, macOS, and Linux**.  

---

## \ud83c\udf1f **Contributing**  
Want to improve DocsToTxt? Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-name`)  
3. Commit and push changes  
4. Submit a pull request  

---

## \ud83d\udcdd **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## \ud83d\udc64 **Author**  
Developed by **[Elton Baidoo](https://github.com/eltonbaidoo)**  
\ud83d\udc8e Contact: [LinkedIn](https://linkedin.com/in/baidooelton)  

---
