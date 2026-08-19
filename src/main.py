#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def extract_text(pdf_path):
    # Minimal placeholder for PDF text extraction.
    return f'extracted:{Path(pdf_path).stem}'

def main(argv=None):
    args = argv if argv is not None else sys.argv[1:]
    results = {}
    for p in args:
        results[p] = extract_text(p)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()
