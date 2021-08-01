"""
You are given a valid XML document, and you have to print its score.
The score is calculated by the sum of the score of each element.
For any element, the score is equal to the number of attributes it has.

Input Format

The first line contains , the number of lines in the XML document.
The next  lines follow containing the XML document.

Output Format

Output a single line, the integer score of the given XML document.
"""

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    return etree.tostring(node).count(b"=")


if __name__ == "__main__":
    sys.stdin.readline()
    tree = etree.ElementTree(etree.fromstring(sys.stdin.read())).getroot()
    print(get_attr_number(tree))
