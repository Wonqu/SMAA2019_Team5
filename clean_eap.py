import uuid

from extract_sentences import extract_sentences, extract_chapters

TOME_2_TITLES = {
    x.upper().strip() for x in
    """The Purloined Letter
        The Thousand-and-Second Tale of Scheherazade
        A Descent into the Maelström
        Von Kempelen and his Discovery
        Mesmeric Revelation
        The Facts in the Case of M. Valdemar
        The Black Cat
        The Fall of the House of Usher
        Silence--a Fable
        The Masque of the Red Death
        The Cask of Amontillado
        The Imp of the Perverse
        The Island of the Fay
        The Assignation
        The Pit and the Pendulum
        The Premature Burial
        The Domain of Arnheim
        Landor’s Cottage
        William Wilson
        The Tell-Tale Heart
        Berenice
        Eleonora
    """.split('\n') if x.upper().strip()
}


if __name__ == '__main__':
    sentences = [
        sentence
        for poem in extract_chapters(TOME_2_TITLES, 'eap_clean.txt')
        for sentence in extract_sentences(poem)
    ]

    with open('./data/out/eap.csv', 'w', encoding='UTF-8') as eap:
        newline = '\n'
        eap.write(f'"id","text","author"{newline}')
        for s in sentences:
            eap.write(f'"{uuid.uuid4()}","{s}","EAP"{newline}')
