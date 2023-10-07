import re

name_data = {
    "Pekka Haavisto": [],
    "Alexander Stubb": [],
    "Olli Rehn": [],
    "Mika Aaltola": [],
    "Jussi Halla-aho": [],
    "Li Andersson": [],
    "Jutta Urpilainen": [],
    "Sari Essayah": [],
    "Harry Harkimo": [],
}

sentences = [
    "Ainoastaan Alexander Stubb tai hänen avustajansa eivät vastanneet yhteydenottoihin.",
    "Lähes kaikki Ylen tavoittamat ehdokkaat kertovat, että heidät tullaan vielä näkemään kampanjan aikana Tiktokissa.",
    "Jussi Halla-Aho puolestaan suhtautuu Tiktokiin kriittisesti.– En ole kokenut tarpeelliseksi luoda profiilia Tiktokiin.",
    "Suhtaudun koko alustaan hiukan skeptisesti turvallisuuspoliittisten ulottuvuuksien takia.",
    "Muut ehdokkaat voivat itse arvioida, onko järkevää käyttää Tiktokin kaltaista alustaa.",
    "Aaltola kertoi 8 minuuttia -ohjelmassaan presidentinvaalikampanjastaan.",
    "Hjallis Harkimo kertoi 8 minuuttia -ohjelmassa omasta kampanjastaan.",
    "Voit keskustella aiheesta 31.8. klo 23 asti. #Kristillisdemokraatit ovat nimittäneet puolueensa presidenttiehdokkaaksi puolueen puheenjohtajan Sari Essayahin.",
    "Päätös oli odotettu. Kristillisdemokraattien puoluehallitus päätti jo viime torstaina esittää, että oma presidenttiehdokas nimitetään ja että tämä on Essayah.",
    "56-vuotias Sari Essayah on johtanut kristillisdemokraatteja vuodesta 2015."
]


for sentence in sentences:
    for name, sentence_list in name_data.items():
        pattern = re.compile(r'\b' + re.escape(name) + r'\b|\b' + re.escape(name.split()[0]) + r'\b|\b' + re.escape(name.split()[1]) + r'\b', re.IGNORECASE)
        if pattern.search(sentence):
            sentence_list.append(sentence)

for name, sentence_list in name_data.items():
    print(f"{name}:")
    for sentence in sentence_list:
        print(f" - {sentence}")
    print()
