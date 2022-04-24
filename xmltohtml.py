import xml.etree.ElementTree as ET


def main():
	root = ET.parse('answer.xml').getroot()


if __name__ == '__main__':
	main()