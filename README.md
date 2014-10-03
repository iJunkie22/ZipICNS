ZipICNS
============
A python tool to port icons from a linux icon theme into a .icns file for use in OSX

[About](#about) • [CLI](#running-from-cli) • [py-module](#python-module) • [GUI](#gui) • [Notes](#notes)

=========
## About
Although XQuartz and MacPorts allows linux applications to use a shared icon theme, the application's launcher should not rely on that for it's app icon. When they do, the icon is only temporary. They will show up as blank icons in Finder, Open-with, when pinned to the dock, in the launcher, etc.

This tool will read the theme, gather all the available sizes of the icon, and package them into a iconset, which once converted to a .icns file, can be applied so OSX will display it properly.

## Running from CLI
This is the usage skeleton when running from a terminal or shell script:
`./zipicns.py` `icon` `[theme]` `[Context]`

An Example:
`./zipicns.py kate oxygen Applications`

This will assemble the iconset like this:
`/var/tmp/[icon-name].iconset/`

If you are happy with the result, go ahead and convert the .iconset to .icns by running:
`iconutil -c icns /var/tmp/[icon-name].iconset`

That's it! You now have a .icns file that can be used for OSX apps, mimetypes, etc.

## Python Module

_\*This feature is still in development_


## GUI
_This feature is still in development_


## Notes
The CLI tool currently only looks in the default icons directory used by MacPorts
(/opt/local/share/icons)