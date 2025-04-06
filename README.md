 # shredpy — A Simple Yet Effective File Shredder

`shredpy` is a Python-based command-line tool that securely shreds files by overwriting them with multiple patterns and deleting them. Lightweight, no dependencies required.

## ⚠️ WARNING ⚠️
This tool ***will*** permanently destroy files. Use at your own risk.

## 🎛️ Features
- Overwrite files with customizable number of passes
- Supports patterns: `0x00`, `0xFF`, and random data (`os.urandom`)
- Verbose output for nerdy satisfaction
- Dry-run mode for safety checks
- Cross-platform compatible (Windows/Linux/macOS)

## ❓ Purpose
Deleting files does not actually erase the file. The operating system just marks the space as "available", the data is still there until new data overwrites it.
With basic recovery tools (many of them free), someone could easily bring back those "deleted" files if they haven't been overwritten yet. This is a big risk for sensitive data—bank info, passwords, personal documents, etc. A shredder ensures no one can snoop through your old files.

## 📥 Installation

Clone it to your machine:
```bash
git clone https://github.com/HazmatPants/shredpy.git
```

Install it:
```bash
cd shredpy
pip install .
```

Then use it with:
```bash
shredpy --help
```

### ⚙️ Options
```
-h, --help            show this help message and exit
-p, --passes PASSES   Number of times to pass the file through the shredder
-f, --files FILES [FILES ...]
                      File(s) to shred
-nd, --nodelete       Do not delete the file(s), only overwrite
-nc, --noconfirm      Do not ask for confirmation
-d, --dryrun          Only show what would be shredded
-v, --verbose         Enable verbose output
-P, --pattern PATTERN Use a specific pattern
```

### Example usage
```bash
shredpy -v -nc -p 100 -f file1.txt file2.mp4 file3.wav
```
This shreds the 3 files in verbose mode, with no confirmation, and 100 passes.

## 🤝 Contributing
If you'd like to contribute or modify `shredpy`, clone the repository and install it locally in editable mode:
```bash
git clone https://github.com/HazmatPants/shredpy.git
cd shredpy
pip install -e .
```
This will install `shredpy` in editable mode, so any changes you make to the code will be immediately reflected.

### Running Tests
If you have tests set up (e.g., using `pytest`), you can run them with:
```bash
pytest
```

## ⚖️ License
`shredpy` is licensed under the GPL-2.0 license, check the [LICENSE](https://github.com/HazmatPants/shredpy/blob/main/LICENSE).
