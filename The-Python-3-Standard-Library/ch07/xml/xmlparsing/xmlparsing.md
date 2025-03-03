# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.5 xml.etree.ElementTree — XML Manipulation API](https://pymotw.com/3/xml.etree.ElementTree/index.html)

### [7.5.1 Parsing an XML Document](https://pymotw.com/3/xml.etree.ElementTree/parse.html)

Parsed XML documents are represented in memory by ElementTree and Element objects connected in a tree structure based on the way the nodes in the XML document are nested.

Parsing an entire document with parse() returns an ElementTree instance. The tree knows about all of the data in the input document, and the nodes of the tree can be searched or manipulated in place. While this flexibility can make working with the parsed document more convenient, it typically takes more memory than an event-based parsing approach since the entire document must be loaded at one time.

The memory footprint of small, simple documents such as this list of podcasts represented as an OPML outline is not significant:

**podcasts.opml**

```
<?xml version="1.0" encoding="UTF-8"?>
<opml version="1.0">
<head>
    <title>My Podcasts</title>
    <dateCreated>Sat, 06 Aug 2016 15:53:26 GMT</dateCreated>
    <dateModified>Sat, 06 Aug 2016 15:53:26 GMT</dateModified>
</head>
<body>
  <outline text="Non-tech">
    <outline
        text="99% Invisible" type="rss"
        xmlUrl="http://feeds.99percentinvisible.org/99percentinvisible"
        htmlUrl="http://99percentinvisible.org" />
  </outline>
  <outline text="Python">
    <outline
        text="Talk Python to Me" type="rss"
        xmlUrl="https://talkpython.fm/episodes/rss"
        htmlUrl="https://talkpython.fm" />
    <outline
        text="Podcast.__init__" type="rss"
        xmlUrl="http://podcastinit.podbean.com/feed/"
        htmlUrl="http://podcastinit.com" />
  </outline>
</body>
</opml>
```

To parse the file, pass an open file handle to parse().

```
# ElementTree_parse_opml.py
from xml.etree import ElementTree

with open("podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

print(tree)
```

It will read the data, parse the XML, and return an ElementTree object.

```
$ python3 ElementTree_parse_opml.py
<xml.etree.ElementTree.ElementTree object at 0x7fe9f401cfd0>
```

### 7.5.2 Traversing the Parsed Tree

To visit all of the children in order, use iter() to create a generator that iterates over the ElementTree instance.

```
# ElementTree_dump_opml.py
from xml.etree import ElementTree
import pprint

with open("podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

for node in tree.iter():
    print(node.tag)
```

This example prints the entire tree, one tag at a time.

```
$ python3 ElementTree_dump_opml.py
opml
head
title
dateCreated
dateModified
body
outline
outline
outline
outline
outline
```

To print only the groups of names and feed URLs for the podcasts, leaving out of all of the data in the header section by iterating over only the outline nodes and print the text and xmlUrl attributes by looking up the values in the attrib dictionary.

```
# ElementTree_show_feed_urls.py
from xml.etree import ElementTree

with open("podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

for node in tree.iter("outline"):
    name = node.attrib.get("text")
    url = node.attrib.get("xmlUrl")
    if name and url:
        print("  %s" % name)
        print("    %s" % url)
    else:
        print(name)
```

The 'outline' argument to iter() means processing is limited to only nodes with the tag 'outline'.

```
$ python3 ElementTree_show_feed_urls.py
Non-tech
  99% Invisible
    http://feeds.99percentinvisible.org/99percentinvisible
Python
  Talk Python to Me
    https://talkpython.fm/episodes/rss
  Podcast.__init__
    http://podcastinit.podbean.com/feed/
```

### 7.5.3 Finding Nodes in a Document

Walking the entire tree like this, searching for relevant nodes, can be error prone. The previous example had to look at each outline node to determine if it was a group (nodes with only a text attribute) or podcast (with both text and xmlUrl). To produce a simple list of the podcast feed URLs, without names or groups, the logic could be simplified using findall() to look for nodes with more descriptive search characteristics.

As a first pass at converting the first version, an XPath argument can be used to look for all outline nodes.

```
# ElementTree_find_feeds_by_tag.py
from xml.etree import ElementTree

with open("podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

for node in tree.findall(".//outline"):
    url = node.attrib.get("xmlUrl")
    if url:
        print(url)
```

The logic in this version is not substantially different than the version using getiterator(). It still has to check for the presence of the URL, except that it does not print the group name when the URL is not found.

```
$ python3 ElementTree_find_feeds_by_tag.py
http://feeds.99percentinvisible.org/99percentinvisible
https://talkpython.fm/episodes/rss
http://podcastinit.podbean.com/feed/
```

It is possible to take advantage of the fact that the outline nodes are only nested two levels deep. Changing the search path to .//outline/outline means the loop will process only the second level of outline nodes.

```
# ElementTree_find_feeds_by_structure.py
from xml.etree import ElementTree

with open("podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

for node in tree.findall(".//outline/outline"):
    url = node.attrib.get("xmlUrl")
    print(url)
```

All of the outline nodes nested two levels deep in the input are expected to have the xmlURL attribute referring to the podcast feed, so the loop can skip checking for the attribute before using it.

```
$ python3 ElementTree_find_feeds_by_structure.py
http://feeds.99percentinvisible.org/99percentinvisible
https://talkpython.fm/episodes/rss
http://podcastinit.podbean.com/feed/
```