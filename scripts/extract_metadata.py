#!/usr/bin/env python3

from pprint import pprint

from yaml import load, load_all, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import json

from pathlib import Path

content_dir = Path("./content")
content_files = content_dir.glob("*.md")

metadata = []
for filename in content_files:
    with open(filename) as f:
        docs = load_all(f, Loader=Loader)
        record = next(docs)
        record["filename"] = str(filename)
        if "type" in record:
            metadata.append(record)

with open("metadata.json", "w") as output:
    json.dump(metadata, output)
