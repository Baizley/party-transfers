import functools
from copy import deepcopy
from functools import reduce

from pycirclize import Circos
from pycirclize.utils import ColorCycler

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

party_transfers = {'A': {'B': 0, 'C': 0, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 1, 'UFG': 0}, 'B': {'A': 1, 'C': 0, 'D': 0, 'F': 0, 'I': 1, 'M': 0, 'O': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 1}, 'C': {'A': 0, 'B': 0, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 4}, 'D': {'A': 0, 'B': 0, 'C': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 1, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 1}, 'F': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'I': 0, 'M': 0, 'O': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 0}, 'I': {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'F': 0, 'M': 0, 'O': 0, 'Q': 0, 'V': 1, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 2}, 'M': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0, 'I': 0, 'O': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 0}, 'O': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 16}, 'Q': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 0}, 'V': {'A': 0, 'B': 0, 'C': 2, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 0, 'Q': 0, 'Æ': 0, 'Ø': 0, 'Å': 0, 'UFG': 5}, 'Æ': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 0, 'Q': 0, 'V': 0, 'Ø': 0, 'Å': 0, 'UFG': 0}, 'Ø': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Å': 0, 'UFG': 0}, 'Å': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0, 'I': 0, 'M': 0, 'O': 0, 'Q': 0, 'V': 0, 'Æ': 0, 'Ø': 0, 'UFG': 4}, 'UFG': {'A': 0, 'B': 1, 'C': 1, 'D': 0, 'F': 1, 'I': 0, 'M': 1, 'O': 1, 'Q': 3, 'V': 0, 'Æ': 0, 'Ø': 0, 'Å': 0}}

s = {'A': [0, 0], 'B': [0, 0], 'C': [0, 0], 'D': [0, 0], 'F': [0, 0], 'I': [0, 0], 'M': [0, 0], 'O': [0, 0], 'Q': [0, 0], 'V': [0, 0], 'Æ': [0, 0], 'Ø': [0, 0], 'Å': [0, 0], 'UFG': [0, 0]}

for party_letter, transfers in party_transfers.items():
    number_of_other_parties = reduce(lambda a, b: a + 1 if b > 0 else a, transfers.values())
    s[party_letter][0] = number_of_other_parties
    for letter, number_of_transfers in transfers.items():
        if number_of_transfers == 0:
            continue
        s[letter][1] = s[letter][1] + 1

total_number_of_transfers = functools.reduce(lambda a, b: a + b[0] + b[1], s.values(), 0)

sectors = {party_letter: a+b if a+b > 1 else 2 for party_letter, (a, b) in s.items()}
circos = Circos(sectors, space=5)
ColorCycler.set_cmap("Set3")
sector_colors = {
    'A': '#b42722ff',
    'B': '#713380ff',
    'C': '#9EBA26ff',
    'D': '#044F5Bff',
    'F': '#DE0878ff',
    'I': '#20C6CFff',
    'M': '#6C3AE4ff',
    'O': '#F4CC40ff',
    'Q': '#01E669ff',
    'V': '#006697ff',
    'Æ': '#89C3FFff',
    'Ø': '#EE8119ff',
    'Å': '#3B9645ff',
    'UFG': '#000000ff'
}

for sector in circos.sectors:
    track = sector.add_track((90, 100))
    color = sector_colors[sector.name]
    track.axis(fc=color)
    sector_colors[sector.name] = color
    track.text(sector.name, color='white', size=12)

c = deepcopy(s)
for old_party, transfers in party_transfers.items():
    for new_party, number_of_transfers in transfers.items():
        if number_of_transfers == 0:
            continue

        old_c = c[old_party][0]
        old_s = s[old_party][0]
        new_c = c[new_party][1]
        new_s = s[new_party][1]

        sector_size = s[new_party][0] + s[new_party][1]
        incoming_start = sector_size - (new_s - new_c)

        p = (number_of_transfers / total_number_of_transfers) * 2

        circos.link((old_party, old_s - old_c, (old_s - old_c) + p), (new_party, incoming_start, incoming_start - p), color = sector_colors[old_party])

        c[old_party][0] = old_c - 1
        c[new_party][1] = new_c - 1

circos.savefig("example02.png")