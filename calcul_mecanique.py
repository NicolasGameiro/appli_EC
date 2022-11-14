

class Section():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.inertia_y = self.height * self.width ** 3 / 12
        self.inertia_z = self.width * self.height ** 3 / 12
        self.area = self.height * self.width

    def get_section_area(self):
        return round(self.area, 2)

    def get_inertia_y(self):
        return round(self.inertia_y, 2)

    def get_inertia_z(self):
        return round(self.inertia_z, 2)


class Material():
    def __init__(self, classe):
        self.classe = classe
        # http://www.freelem.com/eurocode/eurocode5/ELU-bois.htm
        self.dict_resistance = {"C24" :
                                    {"fm,k" : 24,
                                     "ft,0,k" : 14,
                                     "ft,90,k" : 0.5,
                                     "fc,0,k" : 21,
                                     "fc,90,k" : 2.5,
                                     "fv,k" : 2.5,
                                     "E0,mean" : 11,
                                     "Gmean" : 0.69,
                                     "rho_k" : 350}
                                }


class Calcul_solive():
    def __init__(self, section, Q, G, portee, entraxe, W = 0, S = 0):
        self.section = section
        self.Q = Q * 1000 # convert from kN to N
        self.G = G * 1000 # convert from kN to N
        self.wind_load = W * 1000 # convert from kN to N
        self.snow_load = S * 1000 # convert from kN to N
        self.entraxe = entraxe
        self.portee = portee

    def calculate_load(self):
        q = self.Q * self.entraxe
        g = self.G * self.entraxe
        self.total_load = q + g

        self.moment_max = self.total_load * self.portee ** 2 / 8
        self.sigma_flexion_max = self.moment_max / self.section.inertia_z * self.section.height / 2
        self.sigma_cisaillement_max = self.total_load * self.portee / self.section.area

        return round(self.moment_max / 1000, 2), round(self.sigma_flexion_max, 2) # convert from N to kN



class Calcul():
    def __init__(self):
        # donnees d'entree
        self.section = section
        self.chargement = {"permanent": P,
        "variable": V}
        # TODO : construire une structure de chargement en dict et list pour faire les combinaisons
        self.bande_de_chargement = e
        self.portee = L
        self.angle = alpha

        # resultats
        self.total_load = 0
        self.M_max = 0 # moment max
        self.T_max = 0 # effort tractio/compression max
        self.V_max = 0 # effort tranchant max

        self.sigma_flexion_max = 0
        self.sigma_cisaillement_max = 0
        self.sigma_tc_max = 0
        self.sigma_combinaison = 0

        self.taux_travail_flexion = 0
        self.taux_travail_cisaillement = 0

    def admissible(self):
        k_mod = 0.8
        coeff_partiel = 1.3
        pass

    def combinaison_ELS(self):
        pass

    def combinaison_ELU(self):
        pass

    def detection_mode_sollicitation(self):
        pass