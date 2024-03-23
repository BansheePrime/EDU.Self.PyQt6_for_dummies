#

## PyQt6

### Solution for error

*qt.qpa.plugin: From 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.*

```bash
sudo apt install libxcb-cursor0
```

### Solution for error with PyQt5:

*qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.*

```bash
sudo apt remove qtchooser
sudo apt install libqt5gui5
```

### Qt Designer and Python
Install Qt Designer on Windows or Mac. 
https://build-system.fman.io/qt-designer-download