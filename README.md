# 🚀 Arch Init | System Automation Script
<video src="preview.mp4">
A minimalist, lightweight automation script designed to turn a fresh Arch Linux installation into a fully configured development workspace in seconds. 

> 🧪 **Status:** Actively under development! Expect frequent updates and new templates.

---

## ✨ Features

*   **System Update:** Syncs and refreshes core system repositories safely.
*   **Core Development Tools:** Automates the installation of `git` and `base-devel`.
*   **IDE Support:** Installs standard Visual Studio Code / community variants.
*   **AUR Helper:** Automatically bootstraps and compiles `yay` directly from the AUR repository.
*   **Flex Metrics:** Includes `fastfetch` because a clean setup isn't complete without showing off your fetch.

---

## 🛠️ How It Works

The project uses a Python CLI wrapper to dynamically manage modular shell scripts, keeping the footprint light and highly customizable.

```text
├── arch_init.py             # Main interactive Python CLI menu
└── src/
    └── templates-shell/
        └── base.sh          # Core system installation script
```
---
## Installation
**Clone**
```bash
git clone https://github.com/goldstac/arch-init.git
```
**Move To The Directory**
```bash
cd arch-init
```
**Run**
```bash
python main.py
```
