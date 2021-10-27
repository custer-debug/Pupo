import os
import shutil
import PyQt5.QtWidgets as widgets
import PyQt5.QtCore as core
import Utilities as utils
import Dvar as dv
# open
class CopyWindowClass(widgets.QMainWindow):
    log_update = core.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.log_txt = ''
        self.radio_bool = False
        self.default_variable()
        self.setWindowModality(core.Qt.ApplicationModal)
        self.show()


    # Draw window with default value
    def default_variable(self):
        self.setGeometry(dv.WIN_X,dv.WIN_Y,dv.WIN_WIDHT,dv.WIN_HEIGHT)
        self.setWindowTitle(dv.TITLE_MAIN_WINDOW)
        self.label_handle()
        self.radio_button_handle()
        self.line_edit_handle()
        self.button_handle()
        self.checkbox_handler()



    # region Redraw-window

    def show_elements(self):
        # print('show')
        self.checkbox.hide()
        self.third_line_edit.show()
        self.third_label.show()
        self.button_review.show()


    def hide_elements(self):
        # print('hide')
        self.button_review.hide()
        self.checkbox.show()
        self.third_line_edit.hide()
        self.third_label.hide()

    def change_elements_option_function(self, first_label, second_label,height, btn_y,check_box:str):
        self.radio_bool = check_box
        self.first_label.setText(first_label)
        self.second_label.setText(second_label)
        self.setGeometry(dv.WIN_X, dv.WIN_Y, dv.WIN_WIDHT, height)
        self.button_run.move(dv.X_BUTTON,btn_y)

        self.difference_func(
            check_box,
            self.hide_elements,
            self.show_elements,
            self.show_elements,
            self.hide_elements
        )

    # endregion



    # region Check-radio-buttons

    def radio_button_checked_function(self, button):
        print(f'{button.text()=}')
        self.difference_args(
            button.text(),
            self.change_elements_option_function,
            [dv.LABEL_FROM, dv.LABEL_TO,dv.WIN_HEIGHT,dv.Y_BUTTON_3, dv.COLLECT_TXT],
            [dv.LABEL_PATH, dv.LABEL_EXE,dv.WIN_HEIGHT_NEW,dv.Y_BUTTON_3 + 60, dv.SPLIT_DAT],
            [dv.LABEL_PATH, dv.LABEL_EXE,dv.WIN_HEIGHT_NEW,dv.Y_BUTTON_3 + 60, dv.SEND_OUT_EXE],
            [dv.LABEL_FROM, dv.LABEL_TO,dv.WIN_HEIGHT,dv.Y_BUTTON_3, dv.COLLECT_DAT]
        )


    def check_radio_buttons(self):
        if self.check_paths(): return

        self.difference_args(self.difference_func(
            self.radio_bool,
            self.collect_files,
            self.split_dat,
            self.send_out_file,
            self.collect_dat
        ),
        utils.success,
        [self, dv.MSG_SUCCESSFUL_COPY],
        [self, dv.MSG_SUCCESSFUL_SPLIT],
        [self, dv.MSG_SUCCESSFUL_COPY],
        [self, dv.MSG_SUCCESSFUL_COPY]
        )

    # endregion


    # region Handlers-of-elements

    def label_handle(self):
        self.first_label = utils.create_label_function(self,dv.LABEL_FROM, dv.Y_LABEL_1)
        self.second_label = utils.create_label_function(self, dv.LABEL_TO, dv.Y_LABEL_2)
        self.third_label = utils.create_label_function(self, dv.LABEL_JSON, dv.Y_LABEL_3)
        self.third_label.hide()



    def radio_button_handle(self):
        self.collect_txt = utils.radio_button_create(self, dv.COLLECT_TXT, dv.X_RADIO_BUTTON_1, dv.Y_RADIO_BUTTON) #collect txt
        self.split_dat = utils.radio_button_create(self, dv.SPLIT_DAT, dv.X_RADIO_BUTTON_2, dv.Y_RADIO_BUTTON) #split dat files
        self.send_out_exe = utils.radio_button_create(self, dv.SEND_OUT_EXE, dv.X_RADIO_BUTTON_3, dv.Y_RADIO_BUTTON) #send out exe
        self.collect_dat = utils.radio_button_create(self, dv.COLLECT_DAT, dv.X_RADIO_BUTTON_4, dv.Y_RADIO_BUTTON) #collect dat

        self.collect_txt.setChecked(True)

        group = widgets.QButtonGroup(self)
        group.addButton(self.collect_txt)
        group.addButton(self.split_dat)
        group.addButton(self.send_out_exe)
        group.addButton(self.collect_dat)
        group.buttonClicked.connect(self.radio_button_checked_function)



    def line_edit_handle(self):
        self.first_line_edit = utils.create_line_edit(self, dv.X_LINE_EDIT, dv.Y_LINE_EDIT_1, dv.LINE_WIDHT)
        self.second_line_edit = utils.create_line_edit(self, dv.X_LINE_EDIT, dv.Y_LINE_EDIT_2, dv.LINE_WIDHT)
        self.third_line_edit = utils.create_line_edit(self, dv.X_LINE_EDIT, dv.Y_LINE_EDIT_3, dv.LINE_WIDHT)
        self.third_line_edit.hide()



    def button_handle(self):
        utils.create_button(self,
            dv.TITLE_REVIEW,
            dv.X_BUTTON,
            dv.Y_BUTTON_1,
            self.select_first_directory)

        utils.create_button(self,
        dv.TITLE_REVIEW,
        dv.X_BUTTON, dv.Y_BUTTON_2,
        self.select_second_directory)

        self.button_review = utils.create_button(self,
             dv.TITLE_REVIEW,
             dv.X_BUTTON,
             dv.Y_BUTTON_3,
             self.select_third_directory)

        self.button_review.hide()
        self.button_run = utils.create_button(self,
            dv.TITLE_RUN,
            dv.X_BUTTON,
            dv.Y_BUTTON_3,
            self.check_radio_buttons)


    def checkbox_handler(self):
        self.checkbox = utils.create_check_box(self, "Txt to xslx", 160)

    # endregion




    # region logging

    def print_log(self,text):
        self.log_txt = text
        self.log_update.emit(1)

    # endregion


    # region Check-path

    def get_path(self, line):
        return line.text()


    def check_paths(self):

        if not self.get_path(self.first_line_edit):
            utils.fail(self, dv.ERROR_FROM_VALUE); return True
        elif not self.get_path(self.second_line_edit):
            utils.fail(self, dv.ERROR_TO_VALUE); return True
        elif not self.get_path(self.third_line_edit) and self.radio_send_out_dat.isChecked():
            utils.fail(self, dv.ERROR_FILE_PATH_VALUE); return True
        return False

    # endregion


    # region Move-files

    def collect_files(self):
        # '''Many to one'''
        print('Collect')
        filename_list = []
        self.print_log(dv.MSG_START_COPY)
        for root, _, files in os.walk(self.first_path):
            for file in files:
                if file.endswith(dv.TXT):
                    to_path = f'{self.second_path}\\{utils.splitName(root)[-1]}_{file}'
                    self.print_log(f"{root}\\{file} -> {to_path}")
                    shutil.copyfile(root + "\\" + file, to_path)
                    filename_list.append(to_path)

        self.print_log(dv.MSG_FINISH_COPY)

        if self.checkbox.isChecked():
            xslx = f'{self.second_path}\{dv.XSLX_NAME_FILE}'
            utils.txt_to_xslx(filename_list,xslx)
            self.print_log(f'Files concatinate to file: {xslx}')
        return dv.COLLECT_TXT




    def send_out_file(self):
        '''One to Many'''
        _exe = utils.splitName(self.second_path, '/')[-1]
        _json = utils.splitName(self.third_path, '/')[-1]
        for root, folders, _ in os.walk(self.first_path):
            for folder in folders:
                try:
                    shutil.copyfile(self.second_path, f'{root}\\{folder}\\{_exe}')
                    shutil.copyfile(self.third_path, f'{root}\\{folder}\\{_json}')
                except Exception as ex:
                    print(ex)
        return dv.SEND_OUT_EXE


    def collect_dat():
        return dv.COLLECT_DAT

    def split_dat(self):
        files = []
        files_list = []
        for root, _, files in os.walk(self.first_path):
            for file in files:
                if file.endswith(dv.DAT) and file not in [f[1] for f in files_list]:
                    files_list.append([root, file])

        Count_files = len(files_list)
        split_list = [Count_files // dv.SPLIT_NUM]*dv.SPLIT_NUM
        split_list[-1] += Count_files % dv.SPLIT_NUM
        self.print_log(utils.make_directories(
            self.first_path,
            self.second_path,
            self.third_path))

        utils.split_files(files_list,split_list)
        return dv.SPLIT_DAT

    # endregion


    # region Select

    def select_first_directory(self):
        self.first_path = utils.select_directory(self, self.first_line_edit)



    def check_radio_send_out_dat(self):
        return self.send_out_exe.isChecked() or self.split_dat.isChecked()


    def select_second_directory(self):
        if self.check_radio_send_out_dat():
            self.second_path = utils.select_file(self, self.second_line_edit, '*.exe')
        else:
            self.second_path = utils.select_directory(self, self.second_line_edit)



    def select_third_directory(self):
        self.third_path = utils.select_file(self, self.third_line_edit, '*.json')

    # endregion



    # region Match-case
    def difference_func(self, argc, function_1,function_2,function_3, function_4):

        match argc:
            case 'Collect txt':
                return function_1()
            case 'Split dat':
                return function_2()
            case 'Send out exe':
                return function_3()
            case 'Collect dat':
                return function_4()



    def difference_args(self, arg, function, args1 = [], args2 = [], args3 = [], args4 = []):
        match arg:
            case 'Collect txt':
                return function(*args1)
            case 'Split dat':
                return function(*args2)
            case 'Send out exe':
                return function(*args3)
            case 'Collect dat':
                return function(*args4)

    # endregion
