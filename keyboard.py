from pynput import keyboard
import time

# Main keyboard keys (expected on all Mac keyboards)
main_keyboard = {
    # Function keys
    'esc','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12',
    # Top row
    '`','1','2','3','4','5','6','7','8','9','0','-','=','backspace',
    # Second row
    'tab','q','w','e','r','t','y','u','i','o','p','[',']','\\',
    # Third row
    'caps_lock','a','s','d','f','g','h','j','k','l',';',"'",'enter',
    # Fourth row
    'shift','z','x','c','v','b','n','m',',','.','/','shift_r',
    # Bottom row
    'ctrl','alt','cmd','space','cmd_r','alt_r','ctrl_r',
    # Arrow keys
    'up','down','left','right',
    # Other keys
    'delete','home','end','page_up','page_down','insert',
    # Additional Mac keys
    'fn'
}

# Numpad keys (only on full-size keyboards, not on short/laptop keyboards)
numpad_keys = {
    'num_lock','num_0','num_1','num_2','num_3','num_4','num_5',
    'num_6','num_7','num_8','num_9','num_enter','num_+','num_-',
    'num_*','num_/','num_.'
}

# All expected keys combined
expected = main_keyboard | numpad_keys

seen = set()
print("=" * 60)
print("Mac Keyboard Test - Press all keys to test")
print("=" * 60)
print("Press ESC when done testing all keys\n")
print("Note: On macOS, you may need to grant Accessibility permissions")
print("in System Settings > Privacy & Security > Accessibility\n")

def name_from_key(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            return key.char.lower()
        else:
            k = str(key).lower()
            # normalize some names
            mapping = {
                'key.shift':'shift', 'key.shift_r':'shift_r',
                'key.ctrl':'ctrl', 'key.ctrl_r':'ctrl_r',
                'key.alt':'alt', 'key.alt_r':'alt_r',
                'key.cmd':'cmd', 'key.cmd_r':'cmd_r',
                'key.space':'space', 'key.tab':'tab',
                'key.enter':'enter', 'key.backspace':'backspace',
                'key.caps_lock':'caps_lock', 'key.delete':'delete',
                'key.esc':'esc', 'key.up':'up','key.down':'down',
                'key.left':'left','key.right':'right',
                'key.home':'home', 'key.end':'end',
                'key.page_up':'page_up', 'key.page_down':'page_down',
                'key.insert':'insert',
                'key.num_lock':'num_lock', 'key.fn':'fn',
                # Numpad keys
                'key.num_0':'num_0', 'key.num_1':'num_1', 'key.num_2':'num_2',
                'key.num_3':'num_3', 'key.num_4':'num_4', 'key.num_5':'num_5',
                'key.num_6':'num_6', 'key.num_7':'num_7', 'key.num_8':'num_8',
                'key.num_9':'num_9', 'key.num_enter':'num_enter',
                'key.num_+':'num_+', 'key.num_-':'num_-',
                'key.num_*':'num_*', 'key.num_/':'num_/', 'key.num_.':'num_.'
            }
            if k in mapping: return mapping[k]
            if k.startswith('key.f'): return k.replace('key.','')
            # Handle numpad keys that might come as 'key.kp_*'
            if k.startswith('key.kp_'):
                numpad_map = {
                    'key.kp_0':'num_0', 'key.kp_1':'num_1', 'key.kp_2':'num_2',
                    'key.kp_3':'num_3', 'key.kp_4':'num_4', 'key.kp_5':'num_5',
                    'key.kp_6':'num_6', 'key.kp_7':'num_7', 'key.kp_8':'num_8',
                    'key.kp_9':'num_9', 'key.kp_enter':'num_enter',
                    'key.kp_add':'num_+', 'key.kp_subtract':'num_-',
                    'key.kp_multiply':'num_*', 'key.kp_divide':'num_/',
                    'key.kp_decimal':'num_.'
                }
                if k in numpad_map: return numpad_map[k]
            return k.replace('key.','')
    except:
        return None

def on_press(key):
    global seen
    nm = name_from_key(key)
    if nm:
        if nm == 'esc':
            return False
        if nm not in seen:
            seen.add(nm)
            print("Detected:", nm)

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Give listener a moment to start and check if it's actually running
time.sleep(0.1)
if not listener.running:
    print("\n⚠️  ERROR: Keyboard listener failed to start!")
    print("This usually means Accessibility permissions are not granted.")
    print("\nTo fix:")
    print("1. Open System Settings > Privacy & Security > Accessibility")
    print("2. Add Terminal (or your IDE) to the allowed apps")
    print("3. Restart Terminal/IDE and try again\n")
    exit(1)

try:
    while listener.running:
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    listener.stop()

# Separate missing keys by category
missing_main = sorted(main_keyboard - seen)
missing_numpad = sorted(numpad_keys - seen)
extra = sorted(seen - expected)

print("\n" + "=" * 60)
print("=== Test Summary ===")
print("=" * 60)
if len(seen) == 0:
    print("⚠️  No keys were detected!")
    print("This likely means Accessibility permissions are not granted.")
    print("Check System Settings > Privacy & Security > Accessibility")
else:
    # Main keyboard status (the important one)
    print("\n" + "─" * 60)
    print("📱 MAIN KEYBOARD STATUS")
    print("─" * 60)
    main_detected = len(seen & main_keyboard)
    main_total = len(main_keyboard)
    main_percentage = (main_detected / main_total) * 100
    
    if missing_main:
        print(f"❌ Missing main keyboard keys ({len(missing_main)}/{main_total}):")
        print("   " + ", ".join(missing_main))
        print(f"\n⚠️  Main keyboard coverage: {main_percentage:.1f}% - INCOMPLETE!")
    else:
        print(f"✅ All main keyboard keys detected! ({main_detected}/{main_total})")
        print(f"📊 Main keyboard coverage: {main_percentage:.1f}% - COMPLETE ✓")
    
    # Numpad status (expected to be missing on short keyboards)
    print("\n" + "─" * 60)
    print("🔢 NUMPAD STATUS (Optional - only on full-size keyboards)")
    print("─" * 60)
    numpad_detected = len(seen & numpad_keys)
    numpad_total = len(numpad_keys)
    
    if numpad_detected == 0:
        print(f"ℹ️  No numpad keys detected ({numpad_total} expected)")
        print("   This is NORMAL for short/laptop keyboards without numpad")
    elif missing_numpad:
        print(f"⚠️  Partial numpad detected ({numpad_detected}/{numpad_total})")
        print(f"   Missing: {', '.join(missing_numpad)}")
    else:
        print(f"✅ All numpad keys detected! ({numpad_detected}/{numpad_total})")
    
    # Overall summary
    print("\n" + "─" * 60)
    print("📊 OVERALL SUMMARY")
    print("─" * 60)
    print(f"Total keys detected: {len(seen)}")
    print(f"Main keyboard: {main_detected}/{main_total} ({main_percentage:.1f}%)")
    print(f"Numpad: {numpad_detected}/{numpad_total}")
    
    if extra:
        print(f"\n⚠️  Unexpected keys detected ({len(extra)}):")
        print("   " + ", ".join(extra))
        print("   (These may be Mac-specific or from external keyboard)")
    
    # Final verdict
    print("\n" + "─" * 60)
    if not missing_main:
        print("🎉 SUCCESS: All main keyboard keys are working!")
        if numpad_detected == 0:
            print("   (Numpad not detected - expected for short keyboards)")
    else:
        print("⚠️  WARNING: Some main keyboard keys are missing!")
        print("   Check the missing keys listed above.")