from pathlib import Path
import xml.etree.ElementTree as ET


def parse_xml_file(xml_file: Path):
    root = ET.parse(xml_file).getroot()
    return [h.text for h in root.findall(".//headword[@charset='sc']") if h.text]
