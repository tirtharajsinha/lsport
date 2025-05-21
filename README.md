
# lsport

`lsport` is a simple Python command-line tool that lists serial devices connected to your system, specifically those found in the `/dev/serial/by-id/` directory. It displays device names and their corresponding ports. You can also format the output with a table or as plain text, and it handles different paths gracefully.

## Features

- **List serial devices** connected to your system.
- **Flexible output**: Display as a plain list or as a table.
- **Cross-platform**: Should work on Linux systems with serial devices.

## Installation

### Via PyPI (Coming Soon)

You will be able to install it from PyPI once published:

```bash
pip install lsport
````

### Install from source

To install `lsport` directly from the source, run:

```bash
git clone https://github.com/yourusername/lsport.git
cd lsport
pip install .
```

For editable installation (useful during development):

```bash
pip install -e .
```

## Usage

Once installed, you can run the `lsport` command from anywhere in your terminal.

### Basic Usage:

To list connected serial devices with a simple text output:

```bash
lsport
```

### Usage with Table:

To display the output as a formatted table (requires `tabulate` package):

```bash
lsport --no-table
```

### Raw Symlink Paths:

To show raw symlink paths (without `/dev` normalization):

```bash
lsport --raw
```

### Output Examples:

1. **Plain Text Output:**

   ```
   Device Name    -> Port
   -------------   -----------
   usb-...        -> /dev/ttyUSB0
   usb-...        -> /dev/ttyUSB1
   ```

2. **Table Output:**

   ```
   Device Name        Port
   ---------------    ----------
   usb-...            /dev/ttyUSB0
   usb-...            /dev/ttyUSB1
   ```

## Dependencies

* `tabulate` (for formatted table output)

To install all dependencies, run:

```bash
pip install lsport[table]
```

### Optional dependencies:

* You can install `tabulate` separately if you only want table output:

  ```bash
  pip install tabulate
  ```

## Troubleshooting

If no serial devices are listed, run the following command to check if drivers are installed:

```bash
lsusb -t
```

Make sure the serial devices are properly connected, and that the necessary drivers are installed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

* **Name**: Tirtharaj Sinha
* **Email**: [sinhatirtharaj@gmail.com](mailto:sinhatirtharaj@gmail.com)



