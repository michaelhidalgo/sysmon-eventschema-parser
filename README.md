# sysmon-eventschema-parser

This is a short script that pull out individual XML documents out of the Sysmon v10.4 (Schema 4.22).

# Why this?
Sysmon Schema is not well-formed in the sense that cannot be used with XSD toolset, and in order to undertand it and the
relationship between their events, I found it was easier to look at them individually.

This is not rocket science, it is just to pull out individual events as XML.

