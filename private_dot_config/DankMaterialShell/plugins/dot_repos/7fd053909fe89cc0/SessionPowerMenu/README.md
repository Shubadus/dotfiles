# Session Power Menu Plugin

A simple Dank Material Shell plugin that provides quick access to session power options from the panel.

## Features

- Power button widget for the panel bar
- Click to open a popup menu with power options:
  - Log Out
  - Reboot  
  - Shutdown
  - Lock (if supported)
  - Suspend (if supported)
- Clean, minimal design matching DMS aesthetics

## Installation

1. Copy this plugin folder to your DMS plugins directory:

   ```bash
   mkdir -p ~/.config/DankMaterialShell/plugins/PowerMenu
   # Copy plugin files here
   ```

2. The plugin will be automatically detected by DMS

3. Add the `sessionPower` widget to your bar configuration

## Usage

- Click the power button in your panel to open the menu
- Select the desired power action
- The menu will close automatically after selection

## Configuration

Add `"sessionPower"` to your bar widgets in the DMS settings. For example:

```json
{
  "rightWidgets": [
    "clock",
    "sessionPower"
  ]
}
```

## Permissions

This plugin requires no special permissions.

## Version

1.0.0 - Initial release

## Author

brad

## License

MIT
