import time
from lxml import etree
import xml.etree.ElementTree as ET


# from xsd_validator import XsdValidator

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


def lxml_print(xml):
    # Parse the XML document
    tree = ET.parse(xml)
    # Find the ItemCode node
    item_code_node = tree.find(
        'Envelope/Header/Security/Signature/SignedInfo/CanonicalizationMethod/InclusiveNamespaces')
    # Get the value of the ItemCode node
    # item_code = item_code_node.text
    print(item_code_node)


def lxml_xsd(xml, xsd):
    # TODO: kender ikke tree.validate. Find ud af hvordan man så validerer
    tree = ET.parse(xml)
    tree.validate(xsd)


# def xsd_validator(xml, xsd):
#     validator = XsdValidator(xsd)
#     validator.assert_valid(xml)

if __name__ == "__main__":
    xml_filename = 'header.xml'
    xsd_filename = 'unrestrictive/jens.xsd'  # VIGTIGT: brug new XSD
    # xsd_filename = 'Jens02/jens.xsd'  # VIGTIGT: brug new XSD

    validate_xml_with_xsd(xml_filename, xsd_filename)
    # lxml_xsd(xml_filename)
    # xsd_validator(xml_filename, xsd_filename)

    # tree = ET.parse('jens xml validering Indented.xml')
    # root = tree.getroot()
    # att = root.attrib
    # for child in root[0][0][0][0][0]:
    #     print(child.tag, child.text)