import xml.etree.ElementTree as ET
import xml.dom.minidom, os
from xml.etree import ElementTree
from os import walk


def parse_sysmon_events():
    print("+ Extracting XML ")
    for root, dirs, files in os.walk("schemas"):
        for filename in files:
            
            
            file_path                   = "schemas" + "/" + filename
            file_name_without_extension = os.path.splitext(os.path.basename(filename))[0]
            
            tree = ET.parse(os.path.realpath(file_path))
            root = tree.getroot()
            
            for event in root.findall('./events/event'):
                event_content = ElementTree.tostring(event, encoding="utf-8", method="xml").decode()
                event_name    = "[ " + event.get("value") + " ] - "  + event.get("name");
                print("Parsing " + event_name)
                save_xml(file_name_without_extension, event_name, event_content)
    print("+ Done")

def save_xml(source, name, content):
    content_as_xml     = xml.dom.minidom.parseString(content).toprettyxml()
    xml_string         = os.linesep.join([s for s in content_as_xml.splitlines() if s.strip()]) # remove the weird newline issue
    dest_folder        = "./events/" + source
    print("Destination" + dest_folder)
    target_file        = name + ".xml"
    fw = open(os.path.join(dest_folder, target_file), "w")
    fw.write(xml_string)
    fw.flush()

#main method
parse_sysmon_events()
