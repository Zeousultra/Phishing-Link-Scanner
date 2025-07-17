# 🛡️ Phishing Link Scanner

A simple Python-based command-line tool to scan and analyze URLs for potential phishing threats using heuristic detection techniques.

---

## 📖 Description

This tool helps identify suspicious or malicious links by applying a combination of phishing heuristics such as keyword inspection, URL shortener detection, suspicious IP usage, and redirection analysis.

---

## 🚀 Features

- 🔍 Detects phishing-related keywords (e.g., `login`, `verify`, `secure`, etc.)
- 🔗 Flags known URL shorteners (e.g., `bit.ly`, `t.co`, etc.)
- 🧠 Identifies use of IP addresses in place of domain names
- 🔁 Follows and displays redirections (if any)
- 🖥️ Command-line interface for fast usage
- 🪶 Lightweight and fast

---

## ⚙️ How It Works

The tool uses the following logic to evaluate and classify URLs:

1. **Phishing Keywords**: Looks for suspicious terms like `login`, `account`, `secure`, `verify`, `update`, etc.
2. **Shortened URLs**: Detects shortened domains like `bit.ly`, `t.co`, `tinyurl.com`, etc.
3. **Suspicious Structure**: Flags URLs that use raw IP addresses instead of domain names.
4. **Redirections**: Follows redirects and reveals the final destination for transparency.

---

## 💾 Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/Zeousultra/Phishing-Link-Scanner.git
cd Phishing-Link-Scanner
pip install -r requirements.txt
```

---

## 📦 Dependencies

Ensure Python 3 is installed along with the following:

- `requests`
- `tldextract`
- `argparse`
- `colorama`

These are listed in `requirements.txt`.

---

## 🧪 Usage

```bash
python3 phishscan.py -u "http://example.com"
```

---

## 💡 Examples

```bash
python3 phishscan.py -u "http://198.51.100.23/login"
```

**Output:**
```
🔍 PHISHING LINK SCANNER
────────────────────────────
Scanning: http://198.51.100.23/login

🔎 Flags Detected:
  ❌ Uses IP address instead of domain
  ❌ Contains phishing keywords: login

🧠 Final Verdict:
 ⚠ Suspicious — Might be phishing.
```

```bash
python3 phishscan.py -u "http://bit.ly/2z3Fz9n"
```

**Output:**
```
🔍 PHISHING LINK SCANNER
────────────────────────────
Scanning: http://bit.ly/2z3Fz9n

🔎 Flags Detected:
  ❌ Uses URL shortener: bit.ly

🧠 Final Verdict:
 ✅ Likely safe.
```

---

## 📁 File Structure

```
Phishing-Link-Scanner/
├── phishscan.py
├── requirements.txt
└── README.md
```

---

## 🛡 Disclaimer

This tool is built for educational and research purposes **only**. Always scan URLs responsibly and never target systems or users without proper authorization.

---
