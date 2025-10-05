#!/usr/bin/env python3
"""
Simple script to run the calculator application.
This can be used as an alternative to running main.py
"""

import sys
import os

# Add the current directory to Python path to ensure imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import main

if __name__ == "__main__":
    print("Starting Python Calculator App...")
    print("Press Ctrl+C at any time to exit.\n")
    main()