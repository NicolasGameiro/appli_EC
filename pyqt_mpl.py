import os
import sys
from os.path import dirname, realpath, join
import matplotlib
matplotlib.use('Qt5Agg')

from mesh import Mesh

### PyQt5 Modules ###
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QColorDialog
from PyQt5.QtWidgets import QMessageBox, QHeaderView, QMenu, QComboBox, QTableWidgetItem
from PyQt5.QtCore import QTimer, QEvent, QRect, Qt
from PyQt5.QtGui import QIcon, QCursor, QColor, QPalette
from PyQt5.uic import loadUiType, loadUi

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from functools import partial

scriptDir = dirname(realpath(__file__))
From_Main, _ = loadUiType(join(dirname(__file__), "mpl.ui"))



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




def catch_exceptions(type, value, traceback):
    QMessageBox.critical(None, 'Exception raised', '{}'.format(value))
    old_hook(type, value, traceback)


class Sheet(QMainWindow, From_Main):
    def __init__(self):
        super(Sheet, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.pb_calcul_section.clicked.connect(self.calculate_section)
        self.pb_solive.clicked.connect(self.calculate_solive)

        header = self.tw_results.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.cb_type_bois.currentTextChanged.connect(self.on_combobox_changed)

        print(self.treeWidget.currentItem())

        self.treeWidget.currentChanged = self.selection_changed
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.popupmenu)

    def popupmenu(self, position):

        menu = QMenu(self)

        actionDepliertout = menu.addAction("Déplier tout")
        # actionDepliertout.triggered.connect(self.expandAll)

        actionRepliertout = menu.addAction("Replier tout")
        # actionRepliertout.triggered.connect(self.collapseAll)

        menu.addSeparator()

        actionDeplier = menu.addAction("Déplier")
        actionDeplier.triggered.connect(partial(self.expandItem, self.currentItem()))

        actionReplier = menu.addAction("Replier")
        actionReplier.triggered.connect(partial(self.collapseItem, self.currentItem()))

        menu.exec_(self.mapToGlobal(position))

    def selection_changed(self, new, old):
        # print("selection_changed:", new, old)
        # print(new.row())
        print(new.data())
        if new.data() == "Calcul sabot 1":
            print("just do it !")


    def on_combobox_changed(self, value):
        self.cb_classe_resistance.clear()
        if value == "Résineux":
            self.cb_classe_resistance.addItems(["C14", "C16", "C18", "C20", "C22", "C24"])
        elif value == "Feuillus":
            self.cb_classe_resistance.addItems(["D30", "D35", "D40"])
        else :
            self.cb_classe_resistance.addItems(["GL24h", "GL28h"])

    def calculate_section(self):
        h, b = float(self.le_h.text()), float(self.le_b.text())

        section = Section(h, b)

        self.le_Iy.setText(str(section.get_inertia_y()))
        self.le_Iz.setText(str(section.get_inertia_z()))
        self.le_A.setText(str(section.get_section_area()))

    def calculate_solive(self):
        G, Q = float(self.le_G.text()), float(self.get_value_from_categorie(self.cb_Q.currentText()))
        portee, entraxe = float(self.le_portee.text()), float(self.le_entraxe.text())

        h, b = float(self.le_h.text()), float(self.le_b.text())

        section = Section(h, b)

        calcul_solive = Calcul_solive(section, Q, G, portee, entraxe)

        moment_max, stress_max = calcul_solive.calculate_load()

        bois = Material("C24")

        taux_travail_flexion = round(stress_max/bois.dict_resistance["C24"]["fm,k"] * 100, 2)

        self.le_moment_max.setText(str(moment_max))
        self.le_contrainte_max.setText(str(stress_max))
        self.le_t_f.setText(str(taux_travail_flexion))

        if taux_travail_flexion > 100:
            self.le_t_f.setStyleSheet("background-color: #FFCCCB")
        else:
            self.le_t_f.setStyleSheet("background-color: lightgreen")

        table = self.tw_results
        table.setRowCount(2)
        item_type = QTableWidgetItem("contrainte de flexion")
        item_stress = QTableWidgetItem(str(stress_max))
        item_tt = QTableWidgetItem(str(taux_travail_flexion))
        if taux_travail_flexion > 100:
            item_tt.setBackground(QColor(255, 143, 155))
        else :
            item_tt.setBackground(QColor(235, 255, 235))
        item_tt.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 0, item_type)
        table.setItem(0, 1, item_stress)
        table.setItem(0, 2, item_tt)

        # table.resizeColumnsToContents()
        table.resizeRowsToContents()

        # table.horizontalHeader().setSortIndicatorShown(True)
        # table.horizontalHeader().setStretchLastSection(True)

        # update graph
        x = [1, 2, 3]
        y = x

        mesh = Mesh(2, debug=False)
        mesh.add_node([0, 0])
        mesh.add_node([0, 1])  # inches
        mesh.add_node([1, 1])  # inches
        mesh.add_element([1, 2], "barre", "b", 15, 15, 5)
        mesh.add_element([2, 3], "barre", "b", 15, 15, 5)
        mesh.add_element([3, 1], "bracon", "r", 10, 10, 4)
        self.MplWidget.canvas.axes = mesh.plot_mesh(self.MplWidget.canvas.axes)

        annotation = self.MplWidget.canvas.axes.annotate(
                        text='',
                        xy=(0,0),
                        xytext=(1,1),
                        textcoords='offset points',
                        bbox={'boxstyle': 'round', 'fc':'w'},
                        arrowprops={'arrowstyle': '->'}
                    )

        annotation.set_visible(True)

        #self.MplWidget.canvas.axes.clear()
        #scatter = self.MplWidget.canvas.axes.scatter(x, y)
        #self.MplWidget.canvas.axes.legend('cosinus',loc='upper right')
        #self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.MplWidget.canvas.draw()

        def motion_hover(event):
            annotation_visibility = annotation.get_visible()
            if event.inaxes == self.MplWidget.canvas.axes:
                scatter = self.MplWidget.canvas.axes.scatter
                is_contained, annotation_index = scatter.contains(event)
                # print(is_contained, annotation_index)
                if is_contained:
                    data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                    annotation.xy = data_point_location

                    text_label = '({0:.2f}, {0:.2f})'.format(data_point_location[0], data_point_location[1])
                    annotation.set_text(text_label)
                    annotation.set_visible(True)
                    self.MplWidget.canvas.draw_idle()
                else:
                    if annotation_visibility:
                        annotation.set_visible(False)
                        self.MplWidget.canvas.draw_idle()

        def onclick(event):
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
                  ('double' if event.dblclick else 'single', event.button,
                   event.x, event.y, event.xdata, event.ydata))

        self.MplWidget.canvas.mpl_connect('button_press_event', onclick)
        self.MplWidget.canvas.mpl_connect('motion_notify_event', motion_hover)




    def get_value_from_categorie(self, text):
        value = text.split(':')[-1]
        print(value)
        return value


app = QApplication(sys.argv)
app.setStyle('Fusion')

sheet = Sheet()
sheet.show()


old_hook = sys.excepthook

sys.excepthook = catch_exceptions

sys.exit(app.exec_())
