# DiffMatcher 🔍

A comprehensive file comparison tool that compares files line by line and provides detailed similarity analysis. Built around your original file comparison snippet with both GUI and command-line interfaces. **Now supports Microsoft Word documents (.docx)!**

## Features ✨

- **Line-by-line comparison** using Python's `difflib.SequenceMatcher`
- **📄 Microsoft Word document support** (.docx files) with automatic text extraction
- **Multiple file format support** - text files, code files, and Word documents
- **Graphical User Interface** with tkinter for easy file selection and visual results
- **Command-line interface** for automation and scripting
- **Detailed similarity analysis** with percentage scores
- **Visual diff highlighting** showing exactly which lines differ
- **Sample file generation** for testing and demonstration (including Word docs)
- **Progress tracking** and status updates
- **Mixed file type comparison** (e.g., compare .txt with .docx)

## Installation 🚀

1. Clone or download this repository
2. Install the optional dependency for Word document support:
   ```bash
   pip install python-docx
   ```
3. Run the applications directly

```bash
# Navigate to the project directory
cd DiffMatcher

# Option 1: Auto-detect best Python (recommended)
python launch_gui.py

# Option 2: Run GUI directly
python diff_matcher.py

# Option 3: Run with Word support (if using virtual environment)
start_gui.bat

# Run the CLI version
python cli_diff_matcher.py --help
```

### 🔧 **Troubleshooting Word Document Support**

If you get an error about `python-docx` not being installed:

**Option A: Install globally**
```bash
pip install python-docx
```

**Option B: Use the project's virtual environment**
```bash
# Windows
start_gui.bat
# or
python launch_gui.py
```

**Option C: Manual virtual environment setup**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install python-docx
python diff_matcher.py
```

## Supported File Types 📄

| File Type | Extension | Support Level | Notes |
|-----------|-----------|---------------|-------|
| Text files | `.txt` | ✅ Full | Native support |
| Python files | `.py` | ✅ Full | Native support |
| Code files | `.js`, `.css`, `.html`, etc. | ✅ Full | Native support |
| **Word documents** | **`.docx`** | **✅ Full** | **Requires python-docx** |
| All files | `*.*` | ⚠️ Best effort | Text extraction attempted |

**Note:** Word document support requires the `python-docx` library. Install with `pip install python-docx`.

## Usage 📖

### GUI Application (`diff_matcher.py`)

1. **Launch the application:**
   ```bash
   python diff_matcher.py
   ```

2. **Select files to compare:**
   - Click "Browse" buttons to select your files
   - Or use "Create Sample Files" to generate test files

3. **Compare files:**
   - Click "Compare Files" button
   - View detailed results in the results panel

4. **Features:**
   - Visual progress indication
   - Detailed line-by-line differences
   - Overall similarity percentage
   - Clear and intuitive interface

### Command Line Interface (`cli_diff_matcher.py`)

#### Basic Usage
```bash
# Compare two files
python cli_diff_matcher.py file1.txt file2.txt

# Compare with minimal output
python cli_diff_matcher.py file1.txt file2.txt --quiet

# Create and compare sample files
python cli_diff_matcher.py --sample
```

#### Command Line Options
- `file1 file2` - Two files to compare (supports .txt, .py, .docx, etc.)
- `--quiet, -q` - Suppress detailed output, show only summary
- `--sample, -s` - Create sample files and compare them
- `--version, -v` - Show version information
- `--help, -h` - Show help message

#### Exit Codes
- `0` - Files are nearly identical (≥95% similarity)
- `1` - Files have differences but are similar (≥50% similarity)
- `2` - Files are significantly different (<50% similarity)
- `3` - Error occurred during comparison

## Examples 🎯

### GUI Example
![GUI Interface showing file comparison results with detailed line differences]

### CLI Examples

**Basic comparison:**
```bash
$ python cli_diff_matcher.py sample_file_1.txt sample_file_2.txt

🔍 DiffMatcher CLI - File Comparison Tool
📄 Word document support: ✅ Enabled
==================================================
🚀 Comparing files...

📊 COMPARISON SUMMARY:
   File 1: sample_file_1.txt (Text file, 7 lines)
   File 2: sample_file_2.txt (Text file, 8 lines)
   Total lines to compare: 8

🛑 Line 2 differs:
   File 1: This is a sample file for testing.
   File 2: This is a sample file for testing purposes.
   Similarity: 91.89%

🛑 Line 5 differs:
   File 1: Others will be slightly different.
   File 2: Others will be very different.
   Similarity: 82.86%

📈 RESULTS:
   Differences found: 3
   Average similarity: 87.5%
   ⚠️ Files are quite similar with some differences

🎯 Final Result: 87.5% similarity
```

**Word document comparison:**
```bash
$ python cli_diff_matcher.py document1.docx document2.docx

🔍 DiffMatcher CLI - File Comparison Tool
📄 Word document support: ✅ Enabled
==================================================
🚀 Comparing files...

📊 COMPARISON SUMMARY:
   File 1: document1.docx (Word document, 5 lines)
   File 2: document2.docx (Word document, 6 lines)
   Total lines to compare: 6

🛑 Line 3 differs:
   File 1: This paragraph is different in document 1.
   File 2: This paragraph is different in document 2.
   Similarity: 71.43%

📈 RESULTS:
   Differences found: 2
   Average similarity: 92.3%
   ✅ Files are nearly identical!

🎯 Final Result: 92.3% similarity
```

**Mixed file types:**
```bash
$ python cli_diff_matcher.py report.txt report.docx --quiet

🔍 DiffMatcher CLI - File Comparison Tool
📄 Word document support: ✅ Enabled
==================================================
🚀 Comparing files...

📊 COMPARISON SUMMARY:
   File 1: report.txt (Text file, 50 lines)
   File 2: report.docx (Word document, 48 lines)
   Total lines to compare: 50

📈 RESULTS:
   Differences found: 8
   Average similarity: 94.2%
   ✅ Files are nearly identical!

🎯 Final Result: 94.2% similarity
```

## Word Document Features 📄

### What's Supported
- ✅ **Text extraction** from .docx files
- ✅ **Paragraph comparison** line by line
- ✅ **Mixed file type comparison** (e.g., .txt vs .docx)
- ✅ **Table content extraction** (if no paragraphs found)
- ✅ **Automatic sample generation** for both text and Word formats

### How It Works
1. **Text Extraction**: Uses `python-docx` to extract text from Word documents
2. **Paragraph Processing**: Each paragraph becomes a line for comparison
3. **Table Handling**: If no paragraphs are found, text from tables is extracted
4. **Line-by-Line Analysis**: Same algorithm as text files, applied to extracted content

### Word Document Comparison Examples

**Creating Word document samples:**
```bash
python cli_diff_matcher.py --sample
# Creates both .txt and .docx versions for testing
```

**Comparing Word documents:**
```bash
python cli_diff_matcher.py document1.docx document2.docx
```

**Comparing text with Word document:**
```bash
python cli_diff_matcher.py report.txt report.docx
```

**Word document demonstration:**
```bash
python word_demo.py
# Creates complex Word documents and shows detailed comparison
```

### Limitations
- Only `.docx` format is supported (not `.doc`)
- Images, charts, and complex formatting are ignored
- Only text content is compared
- Requires `python-docx` library installation

## Core Algorithm 🧮

The application uses Python's `difflib.SequenceMatcher` to calculate similarity ratios for each line:

```python
similarity = SequenceMatcher(None, line1, line2).ratio()
```

**Similarity interpretation:**
- **≥95%**: Files are nearly identical ✅
- **≥80%**: Files are quite similar with some differences ⚠️
- **≥50%**: Files have moderate similarity 🔶
- **<50%**: Files are significantly different ❌

## File Structure 📁

```
DiffMatcher/
├── diff_matcher.py          # GUI application (with Word support)
├── cli_diff_matcher.py      # Command-line interface (with Word support)
├── test_diff_matcher.py     # Main test suite (including Word document tests)
├── test_gui.py              # GUI functionality tests
├── test_file_dialog.py      # File dialog testing
├── word_demo.py             # Word document demonstration
├── requirements.txt         # Dependencies (python-docx)
├── README.md               # This file
├── launcher.bat            # Windows launcher script
└── sample_files/           # Generated sample files
    ├── sample_file_1.txt
    ├── sample_file_2.txt
    ├── sample_document_1.docx
    ├── sample_document_2.docx
    ├── report_v1.docx      # Demo Word documents
    └── report_v2.docx
```

## Technical Details 🔧

### GUI Application
- Built with `tkinter` (included in Python standard library)
- Responsive interface with progress indication
- Scrollable results area for large files
- File browser integration
- Status bar for real-time feedback

### CLI Application
- Argument parsing with `argparse`
- Colored output with emoji indicators
- Exit codes for automation
- Quiet mode for scripting
- Sample file generation

### Comparison Algorithm
- Reads files with UTF-8 encoding
- Handles files of different lengths
- Strips whitespace for comparison
- Calculates per-line similarity ratios
- Provides overall average similarity

## Use Cases 💡

- **Code Review**: Compare different versions of source code files
- **Configuration Management**: Check differences in config files
- **Documentation**: Compare document versions
- **Data Analysis**: Compare data files or logs
- **Quality Assurance**: Verify file integrity and changes
- **Automation**: Integrate into CI/CD pipelines with CLI

## Contributing 🤝

Feel free to contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License 📄

This project is open source. Feel free to use, modify, and distribute.

## Author ✍️

Based on the original file comparison snippet, enhanced with GUI and CLI interfaces for practical use.

---

**Happy file comparing!** 🎉
