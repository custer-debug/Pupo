import PyQt5.QtWidgets as widgets
import DefaultVariable as dv
import Utilities as utils
import PyQt5.QtCore as core

class ConfigFile(widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Config")
        self.setGeometry(dv.WINDOW_CONFIG_COORDINATE ,dv.WINDOW_CONFIG_COORDINATE ,dv.WINDOW_CONFIG_SIZE ,dv.WINDOW_CONFIG_SIZE)
        self.button_handle()
        self.label_handle()
        self.radio_button_handle()
        self.setWindowModality(core.Qt.ApplicationModal)
        self.show()


    def label_handle(self):
        for item in dv.TITLE_JSON_LABEL:
            utils.create_label_function(self, item, dv.TITLE_JSON_LABEL[item])



    def create_group_button(self, firstname, secondname, y):
        group = widgets.QButtonGroup(self)
        group.addButton(utils.radio_button_create(self, firstname, 90,y))
        group.addButton(utils.radio_button_create(self, secondname, 150,y))
        return group


    def radio_button_handle(self):
        self.btn = [
            self.create_group_button('1200', '2500', 10),
            self.create_group_button('Local', 'Reson', 35),
            self.create_group_button('2', '4', 60)]


    def button_handle(self):
        utils.create_button(self, "Save", 190, 250, self.button_checked_function)


    def compile_dict(self):
        res_dict = {}
        for label,text in zip(dv.TITLE_JSON_LABEL,self.btn):
            label = label.replace(': ', '')
            try:
                temp = int(text.checkedButton().text())
            except ValueError:
                temp = text.checkedButton().text()

            res_dict[label] = temp
        return res_dict




    def button_checked_function(self):
        if utils.check_data_to_json(self.btn):
            widgets.QMessageBox.critical(self, dv.TITLE_WINDOW_ERROR, dv.MSG_ERROR_PARAM)
            return

        utils.dict_to_json(self.compile_dict())
        widgets.QMessageBox.information(self, dv.TITLE_WINDOW_SUCCESSFUL, dv.MSG_SUCCESSFUL_SAVE)
        self.close()
