import csv

election_years = ['1998', '2001', '2005', '2007', '2015', '2019', '2022']

party_to_party_letter = {
    'Socialdemokratiet': 'A',
    'Radikale Venstre': 'B',
    'Det Konservative Folkeparti': 'C',
    'Nye Borgerlige': 'D',
    'Socialistisk Folkeparti': 'F',
    'Liberal Alliance': 'I',
    'Moderaterne': 'M',
    'Dansk Folkeparti': 'O',
    'Frie Grønne': 'Q',
    'Venstre': 'V',
    'Danmarksdemokraterne': 'Æ',
    'Enhedslisten': 'Ø',
    'Alternativet': 'Å',
    'Løsgænger': 'UFG'
}

party_renamings = {
    'Ny Alliance': 'Liberal Alliance',
    'Det Radikale Venstre': 'Radikale Venstre'
}

parties_in_parlament = party_to_party_letter.keys()

def find_parties():
    parties = set()
    for election_year in election_years:
        with open('elected-members/' + election_year + '.csv', 'r', newline='') as file:
            elected_members_reader = csv.reader(file, delimiter=',')

            # Skip the headers
            next(elected_members_reader, None)

            for elected_member in elected_members_reader:
                parties.add(elected_member[1])

    print(parties)

#find_parties()

def initialize_transfer_counter(party_letter):
    return {letter: 0 for letter in party_to_party_letter.values() if letter is not party_letter}

def lookup_party_name(party):
    return party if party_renamings.get(party) is None else party_renamings.get(party)

def find_party_transfer():
    transfers = {letter: initialize_transfer_counter(letter) for letter in party_to_party_letter.values()}
    for election_year in election_years:
        with open('party-transfer/' + election_year + '.csv', 'r', newline='') as file:
            party_transfer_reader = csv.reader(file, delimiter=',')

            # Skip the headers
            next(party_transfer_reader, None)

            for transfer in party_transfer_reader:
                old_party_letter = party_to_party_letter.get(lookup_party_name(transfer[1]))
                new_party_letter = party_to_party_letter.get(lookup_party_name(transfer[2]))

                if old_party_letter is None or new_party_letter is None:
                    continue

                party_transfers = transfers.get(old_party_letter)
                party_transfer = party_transfers.get(new_party_letter)
                party_transfers[new_party_letter] = party_transfer + 1

    print(transfers)

find_party_transfer()

