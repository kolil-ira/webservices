from xml import etree


xml_data = '''
<book>
    <title>the beginning after the end</title>
    <author>turtle me</author>
    <year>2024</year>
</book>
'''

xsd_data = '''
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="book">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="title" type="xs:string"/>
        <xs:element name="author" type="xs:string"/>
        <xs:element name="year" type="xs:int"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
'''


xsd_tree = etree.XMLSchema(etree.fromstring(xsd_data))
xml_tree = etree.fromstring(xml_data)


if xsd_tree.validate(xml_tree):
    print("XML is valid")
else:
    print("XML is invalid")
