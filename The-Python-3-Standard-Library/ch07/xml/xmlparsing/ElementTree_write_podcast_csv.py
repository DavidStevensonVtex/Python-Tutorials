# ElementTree_write_podcast_csv.py
import csv
from xml.etree.ElementTree import iterparse
import sys

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

group_name = ""

parsing = iterparse("podcasts.opml", events=["start"])

for event, node in parsing:
    if node.tag != "outline":
        # Ignore anything not part of the outline
        continue
    if not node.attrib.get("xmlUrl"):
        # Remember the current group
        group_name = node.attrib["text"]
    else:
        # Output a podcast entry
        writer.writerow(
            (
                group_name,
                node.attrib["text"],
                node.attrib["xmlUrl"],
                node.attrib.get("htmlUrl", ""),
            )
        )
