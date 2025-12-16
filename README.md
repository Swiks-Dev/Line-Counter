# Line-Counter

A simple command-line utility for counting lines in text files.

## Features

- Count total lines in a file
- Show detailed breakdown (blank and non-blank lines)
- Simple command-line interface
- Error handling for file operations

## Usage

Basic usage (shows total line count):
```bash
python3 line_counter.py <file>
```

Verbose mode (shows detailed breakdown):
```bash
python3 line_counter.py --verbose <file>
```

Or with short option:
```bash
python3 line_counter.py -v <file>
```

## Examples

```bash
# Count lines in a file
python3 line_counter.py sample.txt
# Output: 9

# Show detailed line counts
python3 line_counter.py --verbose sample.txt
# Output:
# Line count for 'sample.txt':
#   Total lines:     9
#   Non-blank lines: 6
#   Blank lines:     3
```

## Help

For more information, use the help command:
```bash
python3 line_counter.py --help
```

## Requirements

- Python 3.x

## Sample File

A `sample.txt` file is included for testing the line counter.
