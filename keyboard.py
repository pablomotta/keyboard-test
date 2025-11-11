from pynput import keyboard
import time

# ANSI US layout list; tweak for ISO/JIS as needed
expected = {
    'esc','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12',
    '`','1','2','3','4','5','6','7','8','9','0','-','=','backspace',
    'tab','q','w','e','r','t','y','u','i','o','p','[',']','\\',
    'caps_lock','a','s','d','f','g','h','j','k','l',';',"'",'enter',
    'shift','z','x','c','v','b','n','m',',','.','/','shift_r',
    'ctrl','alt','cmd','space','cmd_r','alt_r','ctrl_r',
    'up','down','left','right','delete'
}

seen = set()
print("Key scan started. Press ESC to finish.\n")

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
                'key.left':'left','key.right':'right'
            }
            if k in mapping: return mapping[k]
            if k.startswith('key.f'): return k.replace('key.','')
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

try:
    while listener.running:
        time.sleep(0.05)
except KeyboardInterrupt:
    pass

missing = sorted(expected - seen)
extra = sorted(seen - expected)

print("\n=== Summary ===")
print("Seen keys ({}): {}".format(len(seen), ", ".join(sorted(seen))))
print("Missing keys ({}): {}".format(len(missing), ", ".join(missing) if missing else "None 🎉"))
if extra:
    print("Unrecognized keys ({}): {}".format(len(extra), ", ".join(extra)))