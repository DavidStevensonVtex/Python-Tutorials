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
