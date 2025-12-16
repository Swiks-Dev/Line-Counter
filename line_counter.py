#!/usr/bin/env python3
"""
Line Counter - A simple utility to count lines in text files
"""

import sys
import os
import argparse


def count_lines(filepath):
    """
    Count lines in a file.
    
    Args:
        filepath: Path to the file to count lines in
        
    Returns:
        Dictionary with line counts:
        - total: Total number of lines
        - blank: Number of blank lines
        - non_blank: Number of non-blank lines
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        total_lines = len(lines)
        blank_lines = sum(1 for line in lines if line.strip() == '')
        non_blank_lines = total_lines - blank_lines
        
        return {
            'total': total_lines,
            'blank': blank_lines,
            'non_blank': non_blank_lines
        }
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filepath}'.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: File '{filepath}' is not a valid text file.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to handle CLI arguments and display results."""
    parser = argparse.ArgumentParser(
        description='Count lines in a text file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s file.txt              Count lines in file.txt
  %(prog)s --verbose file.txt    Show detailed line counts
        '''
    )
    
    parser.add_argument(
        'file',
        help='Path to the text file to count lines in'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed line counts (blank and non-blank lines)'
    )
    
    args = parser.parse_args()
    
    # Check if it's a file (not a directory)
    if os.path.exists(args.file) and not os.path.isfile(args.file):
        print(f"Error: '{args.file}' is not a file.", file=sys.stderr)
        sys.exit(1)
    
    # Count lines
    counts = count_lines(args.file)
    
    # Display results
    if args.verbose:
        print(f"Line count for '{args.file}':")
        print(f"  Total lines:     {counts['total']}")
        print(f"  Non-blank lines: {counts['non_blank']}")
        print(f"  Blank lines:     {counts['blank']}")
    else:
        print(counts['total'])


if __name__ == '__main__':
    main()
