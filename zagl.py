import FileManager
import json
import re

a = input()
src_match = re.search(r'src="([^"]+)"', a)
if src_match:
    src = src_match.group(1)
playlistNumber = src.split('/')[-2]
print(playlistNumber)