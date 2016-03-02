from bs4 import BeautifulSoup
import requests
import insert

r = requests.get(
    'http://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=&all=all&ascii=html')

soup = BeautifulSoup(r.text, 'html5lib')

for row in soup.tbody.find_all('tr'):
	val = row.find_all('td')
	if len(val) > 1 and val[0].text != "":
		if len(val) == 7:
			# no fancy tricks needed
			first = int(val[0].text)
			second = val[1].text
			third = val[2].text
			fourth = val[3].text
			fifth = val[4].text
			sixth = val[5].text
			seventh = val[6].text
		else:
			count = -1
			first_temp = row.find('td', {'valign': 'top', 'align': 'right'})
			if first_temp is not None:
				first = int(first_temp.text)
				count += 1
			else
				first = None
			if val[count+1]['align'] == "center":
				second = val[count+1].text
				count += 1
			else:
				second = None
			if first_temp is None:
				third = row.find('td', {'align': 'right'}).text
			else:
				third = row.find_all('td', {'align': 'right'})[1].text
			count += 1
			fourth = val[count+1].text
			count += 1
			if len(val) > count + 1:
				fifth = val[count+1].text
				# if sixth is present, seventh is always present (even if empty)
				if len(val) > count+2:
					sixth = val[count+2].text
					seventh = val[count+3].text
				else:
					sixth = None
					seventh = None
			else:
				fifth = None

		insert.insertvals(first, second, third, fourth, fifth, sixth, seventh)
		print (first," ",second," ",third," ",fourth," ",fifth," ",sixth," ",seventh)
print(" Values inserted ")
