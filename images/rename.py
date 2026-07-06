import os
import re

pattern = re.compile(r"^imgi_\d+_")

for filename in os.listdir("."):
    if os.path.isfile(filename):
        new_name = pattern.sub("", filename)

        # Skip if nothing changed
        if new_name == filename:
            continue

        # Skip if destination already exists
        if os.path.exists(new_name):
            print(f"Skipping (already exists): {new_name}")
            continue

        os.rename(filename, new_name)
        print(f"Renamed: {filename} -> {new_name}")

print("Done!")