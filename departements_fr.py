# source : https://gist.github.com/mlorant

REGIONS = {
    'Auvergne-Rhône-Alpes': ['01', '03', '07', '15', '26', '38', '42', '43', '63', '69', '73', '74'],
    'Bourgogne-Franche-Comté': ['21', '25', '39', '58', '70', '71', '89', '90'],
    'Bretagne': ['35', '22', '56', '29'],
    'Centre-Val de Loire': ['18', '28', '36', '37', '41', '45'],
    'Corse': ['2A', '2B'],
    'Grand Est': ['08', '10', '51', '52', '54', '55', '57', '67', '68', '88'],
    'Guadeloupe': ['971'],
    'Guyane': ['973'],
    'Hauts-de-France': ['02', '59', '60', '62', '80'],
    'Île-de-France': ['75', '77', '78', '91', '92', '93', '94', '95'],
    'La Réunion': ['974'],
    'Martinique': ['972'],
    'Normandie': ['14', '27', '50', '61', '76'],
    'Nouvelle-Aquitaine': ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87'],
    'Occitanie': ['09', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82'],
    'Pays de la Loire': ['44', '49', '53', '72', '85'],
    'Provence-Alpes-Côte d\'Azur': ['04', '05', '06', '13', '83', '84'],
}

DEPARTMENTS = {
    '01': 'Ain',
    '02': 'Aisne',
    '03': 'Allier',
    '04': 'Alpes-de-Haute-Provence',
    '05': 'Hautes-Alpes',
    '06': 'Alpes-Maritimes',
    '07': 'Ardèche',
    '08': 'Ardennes',
    '09': 'Ariège',
    '10': 'Aube',
    '11': 'Aude',
    '12': 'Aveyron',
    '13': 'Bouches-du-Rhône',
    '14': 'Calvados',
    '15': 'Cantal',
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '18': 'Cher',
    '19': 'Corrèze',
    '2A': 'Corse-du-Sud',
    '2B': 'Haute-Corse',
    '21': 'Côte-d\'Or',
    '22': 'Côtes-d\'Armor',
    '23': 'Creuse',
    '24': 'Dordogne',
    '25': 'Doubs',
    '26': 'Drôme',
    '27': 'Eure',
    '28': 'Eure-et-Loir',
    '29': 'Finistère',
    '30': 'Gard',
    '31': 'Haute-Garonne',
    '32': 'Gers',
    '33': 'Gironde',
    '34': 'Hérault',
    '35': 'Ille-et-Vilaine',
    '36': 'Indre',
    '37': 'Indre-et-Loire',
    '38': 'Isère',
    '39': 'Jura',
    '40': 'Landes',
    '41': 'Loir-et-Cher',
    '42': 'Loire',
    '43': 'Haute-Loire',
    '44': 'Loire-Atlantique',
    '45': 'Loiret',
    '46': 'Lot',
    '47': 'Lot-et-Garonne',
    '48': 'Lozère',
    '49': 'Maine-et-Loire',
    '50': 'Manche',
    '51': 'Marne',
    '52': 'Haute-Marne',
    '53': 'Mayenne',
    '54': 'Meurthe-et-Moselle',
    '55': 'Meuse',
    '56': 'Morbihan',
    '57': 'Moselle',
    '58': 'Nièvre',
    '59': 'Nord',
    '60': 'Oise',
    '61': 'Orne',
    '62': 'Pas-de-Calais',
    '63': 'Puy-de-Dôme',
    '64': 'Pyrénées-Atlantiques',
    '65': 'Hautes-Pyrénées',
    '66': 'Pyrénées-Orientales',
    '67': 'Bas-Rhin',
    '68': 'Haut-Rhin',
    '69': 'Rhône',
    '70': 'Haute-Saône',
    '71': 'Saône-et-Loire',
    '72': 'Sarthe',
    '73': 'Savoie',
    '74': 'Haute-Savoie',
    '75': 'Paris',
    '76': 'Seine-Maritime',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '79': 'Deux-Sèvres',
    '80': 'Somme',
    '81': 'Tarn',
    '82': 'Tarn-et-Garonne',
    '83': 'Var',
    '84': 'Vaucluse',
    '85': 'Vendée',
    '86': 'Vienne',
    '87': 'Haute-Vienne',
    '88': 'Vosges',
    '89': 'Yonne',
    '90': 'Territoire de Belfort',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': 'Val-d\'Oise',
    '971': 'Guadeloupe',
    '972': 'Martinique',
    '973': 'Guyane',
    '974': 'La Réunion',
    '976': 'Mayotte',
}

Region_EC5 = {
    '01': 'C2',
    '02': 'C1',
    '03': 'A2',
    '04': 'C1',
    '05': 'C1',
    '06': 'C1',
    '07': 'C2',
    '08': 'C1',
    '09': 'C2',
    '10': 'A1',
    '11': 'D',
    '12': 'A2',
    '13': 'A2',
    '14': 'A1',
    '15': 'A2',
    '16': 'A2',
    '17': 'A2',
    '18': 'A1',
    '19': 'A2',
    '2B': 'A2',
    '2A': 'A2',
    '21': 'A1',
    '22': 'A1',
    '23': 'A2',
    '24': 'A2',
    '25': 'E',
    '26': 'C2',
    '27': 'A1',
    '28': 'A1',
    '29': 'A1',
    '30': 'B2',
    '31': 'C2',
    '32': 'A2',
    '33': 'A2',
    '34': 'C2',
    '35': 'A1',
    '36': 'A1',
    '37': 'A1',
    '38': 'C2',
    '39': 'C1',
    '40': 'A2',
    '41': 'A1',
    '42': 'A2',
    '43': 'A2',
    '44': 'A1',
    '45': 'A1',
    '46': 'A2',
    '47': 'A2',
    '48': 'A2',
    '49': 'A1',
    '50': 'A1',
    '51': 'A1',
    '52': 'A1',
    '53': 'A1',
    '54': 'C1',
    '55': 'C1',
    '56': 'A1',
    '57': 'C1',
    '58': 'A1',
    '59': 'C1',
    '60': 'A1',
    '61': 'A1',
    '62': 'A1',
    '63': 'A2',
    '64': 'A2',
    '65': 'A2',
    '66': 'D',
    '67': 'C1',
    '68': 'C1',
    '69': 'A2',
    '70': 'C1',
    '71': 'B1',
    '72': 'A1',
    '73': 'E',
    '74': 'E',
    '75': 'A1',
    '76': 'A1',
    '77': 'A1',
    '78': 'A1',
    '79': 'A1',
    '80': 'A1',
    '81': 'C2',
    '82': 'A2',
    '83': 'C2',
    '84': 'C2',
    '85': 'A1',
    '86': 'A1',
    '87': 'A2',
    '88': 'C1',
    '89': 'A1',
    '90': 'C2',
    '91': 'A1',
    '92': 'A1',
    '93': 'A1',
    '94': 'A1',
    '95': 'A1',
}

Charge_neige_caract_region = {
    'A1': 0.45,
    'A2': 0.45,
    'B1': 0.55,
    'B2': 0.55,
    'C1': 0.65,
    'C2': 0.65,
    'D': 0.9,
    'E': 1.4,
}

Charge_neige_except_region = {
    'A1': 0,
    'A2': 1,
    'B1': 1,
    'B2': 1.35,
    'C1': 0,
    'C2': 1.35,
    'D': 1.8,
    'E': 0,
}

charge_expoitation = {
    'Catégotie A : Habitation (Plancher)' : 1.5,
    'Catégotie A : Habitation (Balcon)' : 2.5,
    'Catégotie A : Habitation (Escalier)' : 3.5,
    'Catégorie B : Bureau' : 2.5,
    'Catégorie C1 Locaux avec tables (écoles, restaurants, etc.)' : 2.5,
    'Catégorie C2 Locaux avec sièges fixes (théâtres, cinémas, etc.) ' : 4,
    'Catégorie C3 Locaux sans obstacles à la circulation (musées, salles d’exposition, etc.) ' : 4,
    'Catégorie C4 Locaux pour activités physiques (dancings, salles de gymnastique, etc.) ' : 5,
    'Catégorie C5 Locaux susceptibles d’être surpeuplés (salles de concert, terrasses, etc.)' : 5,
    'Catégorie D1 : Commerces de détail courants' : 5,
    'Catégorie D2 Grands magasins' : 5,
    'Catégorie E1 Surfaces de stockage (entrepôts, bibliothèques)' : 7.5,
    'Catégorie E2 Usage industriel' : 'voir CCTP',
    'Catégorie H Toitures: Si pente ≤ 15 % + étanchéité' : 0.8,
    'Autres toitures' : 0,
    'Catégorie I Toitures accessibles : Pour les usages des catégories A à D' : 'Charges identiques à la catégorie de l’usage',
    'Si aménagement paysager' : '≥ 3',
}

proprietes_resineux = {"C24" :
                                    {"fm,k" : 24,
                                     "ft,0,k" : 14,
                                     "ft,90,k" : 0.5,
                                     "fc,0,k" : 21,
                                     "fc,90,k" : 2.5,
                                     "fv,k" : 2.5,
                                     "E0,mean" : 11,
                                     "Gmean" : 0.69,
                                     "rho_k" : 350},
                       "C27" :
                           {"fm,k": 27,
                            "ft,0,k": 14,
                            "ft,90,k": 0.5,
                            "fc,0,k": 21,
                            "fc,90,k": 2.5,
                            "fv,k": 2.5,
                            "E0,mean": 11,
                            "Gmean": 0.69,
                            "rho_k": 350},
                                }