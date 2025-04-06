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

### Options
```
-h, --help            show this help message and exit
-p, --passes PASSES   Number of times to pass the file through the shredder
-f, --files FILES [FILES ...]
                      File(s) to shred
-nd, --nodelete       Do not delete the file(s), only overwrite
-nc, --noconfirm      Do not ask for confirmation
-d, --dryrun          Only show what would be shredded
-v, --verbose         Enable verbose output
```

### Example usage
```bash
shredpy -v -nc -p 100 -f file1.txt file2.mp4 file3.wav
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
