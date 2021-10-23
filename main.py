# example input:
sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

wordlist = []
frequencies = []

for sentence in sentences:
    # ''.join(char for char in sentence if (char.isalnum() or char == ' '))
    # deletes not alphanumeric (plus ' ') characters
    for word in ''.join(char for char in sentence if (char.isalnum() or char == ' ')).lower().split():
        wordlist.append(word)

for word in wordlist:
    frequencies.append(wordlist.count(word))

# create unique list of pair (word, occurrences)
res = list(set(zip(wordlist, frequencies)))
res.sort(key=lambda x: x[1], reverse=True)

for i in range(3):
    print(res[i])
