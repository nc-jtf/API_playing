import time
from lxml import etree
import xml.etree.ElementTree as ET

def validate_xml(xml_filename, xsd_filenames):

    xmlschema_documents = [etree.parse(xsd_filename) for xsd_filename in xsd_filenames]
    xmlschema_content = '\n'.join([etree.tostring(xsd_doc).decode() for xsd_doc in xmlschema_documents])
    xmlschema = etree.XMLSchema(etree.XML(xmlschema_content))

    xml_document = etree.parse(xml_filename)
    valid = xmlschema.validate(xml_document)

    if valid:
        print("XML is valid.")
    else:
        print("XML is not valid.")
        print("Validation errors:")
        for error in xmlschema.error_log:
            print(f"Error at line {error.line}, column {error.column}: {error.message}")
            print(f"    Element/Attribute causing the error: {error.domain}: {error.name}")

def validate_xml_with_xsd(xml_filename, xsd_filename):
    # Parse the XSD schema
    xsd_doc = etree.parse(xsd_filename)
    xsd = etree.XMLSchema(xsd_doc)

    # Parse the XML document
    xml_doc = etree.parse(xml_filename)

    # Validate the XML against the XSD
    is_valid = xsd.validate(xml_doc)

    if is_valid:
        print("XML is valid according to the XSD.")
    else:
        print("XML is not valid according to the XSD.")
        print("Validation errors:")
        for error in xsd.error_log:
            print(f"Line {error.line}, Column {error.column}: {error.message}")

def tester(xml):
    # Parse the XML document
    tree = ET.parse('jens xml validering Indented.xml')
    # Find the ItemCode node
    item_code_node = tree.find('Envelope/Header/Security/Signature/SignedInfo/CanonicalizationMethod/InclusiveNamespaces')
    # Get the value of the ItemCode node
    item_code = item_code_node.text
    print(item_code)


if __name__ == "__main__":
    # xml_filename = "jens_error.xml"
    # xsd_filename = 'jens.xsd'
    xml_filename = input("Enter the path for the xml file containing the envelope: ")
    xsd_filename = input("Enter the path for the xsd: ")
    validate_xml_with_xsd(xml_filename, xsd_filename)

    # tree = ET.parse('jens xml validering Indented.xml')
    # root = tree.getroot()
    # att = root.attrib
    # for child in root[0][0][0][0][0]:
    #     print(child.tag, child.text)

    while True:
        time.sleep(5)