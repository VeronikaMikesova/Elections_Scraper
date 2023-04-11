"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Veronika Mikešová
email: veronikamikesova@gmail.com
discord: Veronika M.#2692
"""

import requests
import bs4
from bs4 import BeautifulSoup
from pprint import pprint
import sys
import csv
import traceback


# vložit správný počet agumentů v příkazové řádce. Kontrola zadání argumentů a jejich pořadí
       
def main(url, csv):
	if url_checker(url) is True and csv_checker(csv) is True:
		print(f"Stahuji data z vybraného URL:{url}")
		zapis_data(final_vysledky(html_soubor(url), html_soubor_obce(url_obce(url)), strany_obce(url_obce(url))), csv)
		print(f"Ukládám do souboru:{csv}")
		print("Ukončuji program.")
		
	else:
		print("Zadány nesprávné argumenty. Ukončuji program.")
		quit
		
	
def url_checker(url):
	try:
		response = requests.head(url)
		if response.status_code == 200:
			return True
		else:
			return False
    
	except requests.exceptions.RequestException:
            raise SystemExit(f"{url}: neodpovídá. Ukončuji program.")

def csv_checker(csv):
	if csv.endswith(".csv"):
		return True
	else:
		return False

def html_soubor(url):
	odpoved_get = requests.get(url)
	soup = BeautifulSoup(odpoved_get.text, "html.parser")
	all_vysledky = []
	for i in range(3):
		table = soup.find_all("table", {"class": "table"})[i]
		all_tr = table.find_all("tr")
		vysledky = []	
	
		for tr in all_tr[2:33]:
			all_td_on_tr = tr.find_all("td")
			data_obce1 = vyber_atributy_z_radku01(all_td_on_tr)
			vysledky.append(data_obce1)
		all_vysledky.extend(vysledky)
	
	return all_vysledky

def url_obce(url):
	odpoved_get = requests.get(url)
	soup = BeautifulSoup(odpoved_get.text, "html.parser")
	tab_url_obce = []
	
	for i in range(3):
		table = soup.find_all("table", {"class": "table"})[i]
		all_tr = table.find_all("tr")

		for tr in all_tr[2:33]:
			all_td_on_tr = tr.find_all("a", href = True)[0]
			#print(all_td_on_tr)
			href_obce = all_td_on_tr.get("href")
			#print(href_obce)
			url_obce = "https://www.volby.cz/pls/ps2017nss/"+href_obce
			tab_url_obce.append(url_obce)
			
	return tab_url_obce
	
def html_soubor_obce(seznam):
	vysledky_obce = []
	
	for link in seznam:
		odpoved_get = requests.get(link)
		soup = BeautifulSoup(odpoved_get.text, "html.parser")
		table = soup.find("table", {"class": "table"})
		tr_all = table.find_all("tr")
		td_all = tr_all[2].find_all("td")
		data_obce2 = vyber_atributy_z_radku02(td_all)
		vysledky_obce.append(data_obce2)

	return(vysledky_obce)

def strany_obce(seznam):
	
	all_vysledky_stran = []
	for link in seznam:
		odpoved_get = requests.get(link)
		soup = BeautifulSoup(odpoved_get.text, "html.parser")
		vysledky_obce = []

		for i in range(2):
			table = soup.find_all("div", {"class": "t2_470"})[i]
			all_tr = table.find_all("tr")[2:]
			vysledky = []

			for tr in all_tr:
				all_td_on_tr = tr.find_all("td")
				data_obce1 = vyber_atributy_z_radku03(all_td_on_tr)
				vysledky.append(data_obce1)

			vysledky_obce.extend(vysledky)
		
		all_vysledky_stran.append(vysledky_obce)

	return(all_vysledky_stran)


def final_vysledky(seznam01, seznam02, seznam03):
	final_vysledky = seznam01

	for i in range (0, len(seznam01)):
		for j in range (0,len(seznam03[i])):
			final_vysledky[i].update(**seznam02[i], **seznam03[i][j])
	
	return(final_vysledky)

	
def vyber_atributy_z_radku01(tr_tag: "bs4.element.ResultSet"):
    
    return {
        "cislo": tr_tag[0].get_text(),
        "název": tr_tag[1].get_text(),
		}

def vyber_atributy_z_radku02(tr_tag: "bs4.element.ResultSet"):
    
    return {
        "voliči": tr_tag[3].get_text(),
		"obálky": tr_tag[4].get_text(),
		"platné hlasy celkem": tr_tag[7].get_text(),
		}

def vyber_atributy_z_radku03(tr_tag: "bs4.element.ResultSet"):
   
    return {
        tr_tag[1].get_text(): tr_tag[2].get_text()
		}


def zapis_data(data: list, jmeno_souboru: str) -> str:
	     
	with open(jmeno_souboru, mode="w", encoding="utf-8", newline="") as csv_soubor:
		sloupce = data[0].keys()
		
		zapis = csv.DictWriter(csv_soubor, fieldnames=sloupce)
		zapis.writeheader()
		zapis.writerows(data)


	
print(sys.argv)
if len(sys.argv) != 3:
	print("Není zadán dostatečný počet argumentů. Ukončuji program.")
	quit
else: 
	main(sys.argv[1], sys.argv[2])



    