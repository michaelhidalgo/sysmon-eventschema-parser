import xml.etree.ElementTree as ET
from xml.etree import ElementTree
import os


def parse_sysmon_events():
    print("+ Extracting XML ")
    tree = ET.parse('./data/schema.xml')

    root = tree.getroot()
    
    for event in root.findall('./events/event'):
        event_content = ElementTree.tostring(event, encoding="utf-8", method="xml").decode()
        event_name    = "[ " + event.get("value") + " ] - "  + event.get("name");
        print("Parsing " + event_name)
        save_xml(event_name, event_content)
    print("+ Done")

def save_xml(name, content):
    dest_folder  = "./events/"
    target_file  = name + ".xml"
    fw = open(os.path.join(dest_folder, target_file), "w")
    fw.write(content)
    fw.flush()

#main method
parse_sysmon_events()