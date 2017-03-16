#Will ask for input of two html files. Will prettify the file and parse it using a regex to find the names.
#Compares the names from the two classes and prints the names that are in both the classes.

import re
from BeautifulSoup import BeautifulSoup


def remove_dup(seq):
	Set = set(seq)
	return list(Set)

def main():
	user = raw_input('Enter your name: ').strip()
	html_first = raw_input("Enter the name of the first file: ").strip()
	html_second = raw_input("Enter the name of the second file ").strip()

	first = open(html_first, 'r')
	second = open(html_second, 'r')

	soup_first = BeautifulSoup(first.read())
	soup_second = BeautifulSoup(second.read())

	first.close()
	second.close()

	output_first = open("output_first.txt", 'w')
	output_second = open("output_second.txt", 'w')

	output_first.write(soup_first.prettify())
	output_second.write(soup_second.prettify())

	output_first.close()
	output_second.close()


	output_first = open("output_first.txt", 'r')
	output_second = open("output_second.txt", 'r')


	names_first = re.findall('alt="Picture of (.*)" t', output_first.read())
	names_second = re.findall('alt="Picture of (.*)" t', output_second.read())

	
	
	names_first = remove_dup(names_first)
	names_second = remove_dup(names_second)

	counter = 0

	for i in names_first:
		for j in names_second:
			if i == j:
				if i.lower() != user.lower():
					counter = counter + 1
					print(j)
	print(counter)
main()