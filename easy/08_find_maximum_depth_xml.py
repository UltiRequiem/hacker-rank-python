"""
You are given a valid XML document, and you have to print the
maximum level of nesting in it. Take the depth of the root as 0.

Input Format

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.
"""

import xml.etree.ElementTree as etree


def depth(elem, level):
    maxdepth: int = -1
    if level == maxdepth:
        maxdepth += 1

    for child in elem:
        depth(child, level + 1)
    return maxdepth


if __name__ == "__main__":
    xml = ""
    for i in range(int(input())):
        xml = xml + input() + "\n"
    print(depth(etree.ElementTree(etree.fromstring(xml)).getroot(), -1))
