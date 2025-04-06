 # shredpy — A Simple Yet Effective File Shredder

`shredpy` is a Python-based command-line tool that securely shreds files by overwriting them with multiple patterns and deleting them. Lightweight, no dependencies required.
## Features
- Overwrite files with customizable number of passes
- Supports patterns: `0x00`, `0xFF`, and random data (`os.urandom`)
- Verbose output for nerdy satisfaction
- Dry-run mode for safety checks
- Cross-platform compatible (Windows/Linux/macOS)

## Installation

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

## Contributing
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
