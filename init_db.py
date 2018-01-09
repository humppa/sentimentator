#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sentimentator.app import app
from sentimentator.model import db, Language, Sentence


with open('en_lines.txt') as File:
    en_data = File.readlines()

DADA = {
    'en': en_data,
    'fi': [
        'Tämä on testivirke',
        'Toinen testivirke',
        'Testivirkkeistä viimeisin',
    ],
    'fr': [
        'Wikipédia est un projet d’encyclopédie collective en ligne, universelle, multilingue et fonctionnant sur le principe du wiki.',
    ],
    'it': [
        'Wikipedia è un\'enciclopedia online, collaborativa e libera.',
    ],
    'ru': [
        'Википедия — энциклопедия, которая совместно пишется сообществом читателей.',
    ],
    'sv': [
        'Wikipedia är en encyklopedi med öppet och fritt innehåll, som utvecklas av frivilliga bidragsgivare från hela världen.',
    ],
}

with app.app_context():
    db.create_all()
    for i, lang in enumerate(DADA):
        db.session.add(Language(id=i, language=lang))
        for sentence in DADA[lang]:
            db.session.add(Sentence(sentence=sentence, language_id=i))
    db.session.commit()
