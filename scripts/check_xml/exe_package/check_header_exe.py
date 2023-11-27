import os
import time
from lxml import etree
import xml.etree.ElementTree as ET
import sys

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
    tree = ET.parse('../jens xml validering Indented.xml')
    # Find the ItemCode node
    item_code_node = tree.find('Envelope/Header/Security/Signature/SignedInfo/CanonicalizationMethod/InclusiveNamespaces')
    # Get the value of the ItemCode node
    item_code = item_code_node.text
    print(item_code)

def get_xsd_path():
    if getattr(sys, 'frozen', False):  # Check if script is bundled into an EXE
        exe_dir = sys._MEIPASS  # Get the directory of the EXE
        xsd_path = os.path.join(exe_dir, 'jens.xsd')  # Adjust the filename accordingly
    else:
        # If not bundled, use a relative path or other method to locate the XSD file.
        xsd_path = 'jens.xsd'  # Adjust the path as needed

    return xsd_path


if __name__ == "__main__":
    xml_filename = input("Enter the path for the xml file containing the envelope: ")
    # xsd_filename = input("Enter the path for the xsd file: ")
    xsd_filename = 'C:/Users/jtf/OneDrive - Netcompany/PycharmProjects/API_playing/scripts/check_xml/unrestrictive/jens.xsd'
    validate_xml_with_xsd(xml_filename, xsd_filename)
    input("Press anything to close the program")
    while True:
        time.sleep(5)
