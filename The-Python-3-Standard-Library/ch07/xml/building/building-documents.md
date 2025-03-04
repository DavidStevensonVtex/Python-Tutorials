# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.5 xml.etree.ElementTree — XML Manipulation API](https://pymotw.com/3/xml.etree.ElementTree/index.html)

### 7.5.8 Building Documents With Element Nodes

In addition to its parsing capabilities, xml.etree.ElementTree also supports creating well-formed XML documents from Element objects constructed in an application. The Element class used when a document is parsed also knows how to generate a serialized form of its contents, which can then be written to a file or other data stream.

There are three helper functions useful for creating a hierarchy of Element nodes. Element() creates a standard node, SubElement() attaches a new node to a parent, and Comment() creates a node that serializes using XML’s comment syntax.

```
# ElementTree_create.py
from xml.etree.ElementTree import (
    Element,
    SubElement,
    Comment,
    tostring,
)

top = Element("top")

comment = Comment("Generated for PyMOTW")
top.append(comment)

child = SubElement(top, "child")
child.text = "This child contains text."

child_with_tail = SubElement(top, "child_with_tail")
child_with_tail.text = "This child has text."
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, "child_with_entity_ref")
child_with_entity_ref.text = "This & that"

print(tostring(top))
```

The output contains only the XML nodes in the tree, not the XML declaration with version and encoding.

```
$ python3 ElementTree_create.py
b'<top><!--Generated for PyMOTW--><child>This child contains text.</child><child_with_tail>This child has text.</child_with_tail>And "tail" text.<child_with_entity_ref>This &amp; that</child_with_entity_ref></top>'
```

The & character in the text of child_with_entity_ref is converted to the entity reference `&amp;` automatically.

### 7.5.9 Pretty-Printing XML

ElementTree makes no effort to format the output of tostring() to make it easy to read because adding extra whitespace changes the contents of the document. To make the output easier to follow, the rest of the examples will use xml.dom.minidom to re-parse the XML then use its toprettyxml() method.

```
# ElementTree_pretty.py
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ElementTree.tostring(elem, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
```

The updated example now looks like

```
# ElementTree_create_pretty.py
from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettify

top = Element("top")

comment = Comment("Generated for PyMOTW")
top.append(comment)

child = SubElement(top, "child")
child.text = "This child contains text."

child_with_tail = SubElement(top, "child_with_tail")
child_with_tail.text = "This child has text."
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, "child_with_entity_ref")
child_with_entity_ref.text = "This & that"

print(prettify(top))
```

and the output is easier to read.

```
$ python3 ElementTree_create_pretty.py
<?xml version="1.0" ?>
<top>
  <!--Generated for PyMOTW-->
  <child>This child contains text.</child>
  <child_with_tail>This child has text.</child_with_tail>
  And &quot;tail&quot; text.
  <child_with_entity_ref>This &amp; that</child_with_entity_ref>
</top>
```

In addition to the extra whitespace for formatting, the xml.dom.minidom pretty-printer also adds an XML declaration to the output.