# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg
import re
import binascii

def conversion(filepath):

    if filepath.find('.txt') < 0:
        return -1

    with open(filepath, 'r') as f:
        hex_str = f.read()

    pttn = re.findall(r'value: \(0x\).*', hex_str)
    #去掉value: (0x)
    hex_list_temp = []
    for _, v in enumerate(pttn):
        hex_list_temp.append(v.strip('value: (0x)'))
    #去掉'-'
    hex_list = []
    for _, v in enumerate(hex_list_temp):
        hex_list.append(v.split('-'))
    # 连接字符串
    asc_str = ""
    for _, v_list in enumerate(hex_list):
        for _, v in enumerate(v_list):
            try:
                asc_str = asc_str + str(binascii.a2b_hex(v), encoding='utf8')
            except:
                #print("error:",v_list)
                return -2

    #写入文件
    write_file = filepath.rstrip('.txt')
    write_file = write_file + '-conversion.txt'
    with open(write_file, 'w') as f:
        f.write(asc_str)

    return 1


def main():
    layout = [[sg.Input(key='-FILE_PATH-'),sg.FileBrowse('打开文件')],
              [sg.Button('转换',key='-SW-',size=(10,2)),sg.T('等待转换',size=(10,2),key='-STATE-')]]
    window = sg.Window('HEX Conversion tool', layout)

    while True:
        event, values = window.read()

        if event == '-SW-':
            file_path = window['-FILE_PATH-'].get()
            if file_path == '':
                sg.popup('没有选中文件')
            else:
                window['-STATE-'].update('转换开始......')
                result = conversion(file_path)
                if result == -1:
                    window['-STATE-'].update('转换失败')
                    sg.popup('文件格式错误,请选择txt文件')
                elif result == -2:
                    window['-STATE-'].update('转换失败')
                    sg.popup('字符内容存在错误')
                else:
                    window['-STATE-'].update('转换完成')
                    sg.popup('转换成功')


        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
