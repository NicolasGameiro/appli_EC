# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

import departements_fr


class snow_widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('snow_widget.ui', self)
        self.show()

        self.cb_region.addItems(departements_fr.REGIONS.keys())

        self.cb_region.currentTextChanged.connect(self.on_region_changed)
        self.cb_departement.currentTextChanged.connect(self.on_departement_changed)

    def on_region_changed(self, value):
        self.cb_departement.clear()
        self.cb_departement.addItems(departements_fr.REGIONS[value])

    def on_departement_changed(self, value):
        depmt = self.cb_departement.currentText()
        zone = q_caract = q_except = ""
        try :
            zone = departements_fr.Region_EC5[depmt]
            q_caract = departements_fr.Charge_neige_caract_region[zone]
            q_except = departements_fr.Charge_neige_except_region[zone]
        except:
            pass
        self.le_zone.setText(zone)
        self.le_charge_caract.setText(str(q_caract))
        self.le_charge_except.setText(str(q_except))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    sheet = snow_widget()
    sheet.show()

    sys.exit(app.exec_())



