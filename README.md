# Mac Keyboard Test

A Python script to test all keys on a Mac keyboard and verify they're working correctly. Perfect for testing keyboard functionality, especially on short/laptop keyboards without numpads.

## Features

- Tests all main keyboard keys (letters, numbers, symbols, function keys, modifiers)
- Separates main keyboard keys from numpad keys (expected to be missing on short keyboards)
- Real-time detection feedback as you press keys
- Comprehensive summary report showing:
  - Which keys were detected
  - Which main keyboard keys are missing (if any)
  - Numpad status (optional for short keyboards)
  - Coverage percentages

## Prerequisites

- macOS (tested on macOS 13+)
- Python 3.7 or higher
- Terminal or IDE with Accessibility permissions

## Setup

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/pablomotta/keyboard-test.git
   cd keyboard-test
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Grant Accessibility permissions:**
   - Open **System Settings** → **Privacy & Security** → **Accessibility**
   - Add **Terminal** (or your IDE like Cursor/VS Code) to the allowed apps
   - Restart Terminal/IDE after granting permissions

## Usage

1. **Activate the virtual environment** (if not already active):
   ```bash
   source venv/bin/activate
   ```

2. **Run the script:**
   ```bash
   python keyboard.py
   ```

3. **Test your keyboard:**
   - Press each key on your keyboard at least once
   - The script will display "Detected: [key]" as you press keys
   - Press **ESC** when you're done testing all keys

4. **Review the summary:**
   - The script will show:
     - ✅ Main keyboard status (all keys detected or missing keys)
     - 🔢 Numpad status (expected to be empty on short keyboards)
     - 📊 Overall coverage statistics

## Understanding the Output

### Main Keyboard Status
- **✅ All keys detected**: Your main keyboard is working perfectly
- **❌ Missing keys**: Some keys aren't being detected (check Accessibility permissions or hardware issues)

### Numpad Status
- **ℹ️ No numpad detected**: This is **NORMAL** for short/laptop keyboards without a numpad
- **✅ All numpad keys detected**: You have a full-size keyboard with numpad

### Final Verdict
- **🎉 SUCCESS**: All main keyboard keys are working
- **⚠️ WARNING**: Some main keyboard keys are missing (investigate further)

## Troubleshooting

### "Import 'pynput' could not be resolved"
- Make sure you've activated the virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### "This process is not trusted! Input event monitoring will not be possible"
- Grant Accessibility permissions in System Settings
- Add Terminal/IDE to Accessibility allowed apps
- Restart Terminal/IDE after granting permissions

### No keys are detected
- Check Accessibility permissions are granted
- Make sure Terminal/IDE is in the allowed apps list
- Try restarting Terminal/IDE

### Some keys not detected
- Make sure you're pressing each key individually
- Check if the key physically works (try in a text editor)
- Some keys may require special key combinations (e.g., Fn + F1-F12)

## Project Structure

```
keyboard-test/
├── keyboard.py      # Main test script
├── requirements.txt # Python dependencies
├── README.md        # This file
└── venv/            # Virtual environment (gitignored)
```

## License

This project is open source and available for personal use.

