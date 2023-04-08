import csv
import os

import requests
from bs4 import BeautifulSoup

base_url = "https://da.wikipedia.org/wiki/Folketingsmedlemmer_valgt_i_"

def scrape_1998():
    election_year = "1998"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[2]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td'])
            member = data[0].text.strip()
            party = data[1].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti', 'Dato'])

        member = ''

        for items in party_transfer.find_all('tr')[1::]:
            data = items.find_all(['td'])
            if len(data) == 4:
                member = data[0].text.strip()
                data = data[1::]
            old_party = data[0].text.strip()
            new_party = data[1].text.strip()
            transfer_date = data[2].text.strip()

            writer.writerow([member, old_party, new_party, transfer_date])

def scrape_2001():
    election_year = "2001"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[2]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td'])
            member = data[0].text.strip()
            party = data[1].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti', 'Dato'])

        member = ''

        for items in party_transfer.find_all('tr')[1::]:
            data = items.find_all(['td'])
            if len(data) == 5:
                member = data[0].text.strip()
                data = data[1::]
            old_party = data[0].text.strip()
            new_party = data[2].text.strip()
            transfer_date = data[3].text.strip()

            writer.writerow([member, old_party, new_party, transfer_date])

def scrape_2005():
    election_year = "2005"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[2]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td', 'th'])
            member = data[0].text.strip()
            party = data[2].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti', 'Dato'])

        member = ''

        for items in party_transfer.find_all('tr')[1::]:
            data = items.find_all(['td'])
            if len(data) == 5:
                member = data[0].text.strip()
                data = data[1::]
            old_party = data[0].text.strip()
            new_party = data[2].text.strip()
            transfer_date = data[3].text.strip()

            writer.writerow([member, old_party, new_party, transfer_date])

def scrape_2007():
    election_year = "2007"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[2]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td'])
            member = data[0].text.strip()
            party = data[1].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti', 'Dato'])

        member = ''

        for items in party_transfer.find_all('tr')[1::]:
            data = items.find_all(['td'])
            if len(data) == 5:
                member = data[0].text.strip()
                data = data[1::]

            if len(data) == 4:
                del data[1]

            old_party = data[0].text.strip()
            new_party = data[1].text.strip()
            transfer_date = data[2].text.strip()

            writer.writerow([member, old_party, new_party, transfer_date])

def scrape_2011():
    election_year = "2011"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[2]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td'])
            member = data[0].text.strip()
            party = data[1].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti', 'Dato'])

        member = ''

        for items in party_transfer.find_all('tr')[1::]:
            data = items.find_all(['td'])
            if len(data) == 5:
                member = data[0].text.strip()
                data = data[1::]
            old_party = data[0].text.strip()
            new_party = data[2].text.strip()
            transfer_date = data[3].text.strip()

            writer.writerow([member, old_party, new_party, transfer_date])

def scrape_2015():
    election_year = "2015"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[2]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td'])
            member = data[0].a.text.strip()
            party = data[2].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti'])

        for items in party_transfer.find_all('tr')[1::]:
            data = items.find_all(['td'])

            member = data[0].text.strip()
            old_party = data[1].text.strip()
            new_party = data[3].text.strip()

            writer.writerow([member, old_party, new_party])

def scrape_2019():
    election_year = "2019"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[3]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td'])
            member = data[0].text.strip()
            party = data[3].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti', 'Dato'])

        member = ''
        for items in party_transfer.find_all('tr')[1::]:
            data = items.find_all(['td'])
            if len(data) == 6:
                member = data[0].text.strip()
                data = data[1::]

            if len(data) == 5:
                del data[0]

            old_party = data[0].text.strip()
            new_party = data[1].text.strip()
            transfer_date = data[2].text.strip().replace('\n', ' ')

            writer.writerow([member, old_party, new_party, transfer_date])

def scrape_2022():
    election_year = "2022"
    URL = base_url + election_year

    res = requests.get(URL).text
    soup = BeautifulSoup(res, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    members = tables[1]
    party_transfer = tables[2]

    filename = 'elected-members/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Parti'])

        for items in members.find_all('tr')[1::]:
            data = items.find_all(['td'])

            if len(data) == 1:
                continue

            member = data[0].text.strip()
            party = data[1].text.strip()
            writer.writerow([member, party])

    filename = 'party-transfer/' + election_year + '.csv'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Navn', 'Gammelt Parti', 'Nyt Parti', 'Dato'])

        items = party_transfer.find_all('tr')[1::];

        data = items[0].find_all(['td'])
        member = data[0].text.strip()[:-3]
        old_party = data[1].text.strip()
        new_party = data[2].text.strip()
        transfer_date = data[3].text.strip()
        writer.writerow([member, old_party, new_party, transfer_date])

        data = items[1].find_all(['td'])
        member = data[0].text.strip()[:-3]
        new_party = data[1].text.strip()
        transfer_date = data[2].text.strip()
        writer.writerow([member, old_party, new_party, transfer_date])

        data = items[2].find_all(['td'])
        member = data[0].text.strip()[:-3]
        old_party = data[1].text.strip()
        transfer_date = data[2].text.strip()
        writer.writerow([member, old_party, new_party, transfer_date])


scrape_1998()
scrape_2001()
scrape_2005()
scrape_2007()
scrape_2011()
scrape_2015()
scrape_2019()
scrape_2022()