#!/usr/bin/env python3
"""
Script to initialize a FileStorage instance and reload stored data.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
