# shredpy — A Simple Yet Effective File Shredder

`shredpy` is a Python-based command-line tool that securely shreds files by overwriting them with multiple patterns and optionally deleting them. Lightweight, no dependencies required.
## Features
- Overwrite files with customizable number of passes
- Supports patterns: `0x00`, `0xFF`, and random data (os.urandom)
- Optional file deletion
- Verbose output for nerdy satisfaction
- Dry-run mode for safety checks
- Cross-platform compatible (Windows/Linux/macOS)

## Installation

```bash
git clone https://github.com/HazmatPants/shredpy.git
cd shredpy
python3 shredpy.py --help
```
