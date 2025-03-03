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