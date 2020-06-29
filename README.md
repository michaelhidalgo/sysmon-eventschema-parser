# Sysmon Individual Event Schemas

This is a short script that pulls out individual XML events out of the Sysmon Schemas v10.42 (Schema 4.22) and Schema v11.10 (4.23).

Having events separated per schema allows to compare them.


# Why this?

Sysmon Schema is not well-formed in the sense that cannot be used with XSD toolset, and in order to undertand it and the
relationship between their events, I found it was easier to look at each event individually.

This is not rocket science, it is just to pull out individual events as XML :), you get surprise what ideas lazy people can get :)

