# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PySimpleGUI as sg
import re
import binascii

base64_main_icon = b'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'

def conversion(filepath):
    err_s = ''

    if filepath.find('.txt') < 0:
        err_s = 'error:file fomart error'
        return err_s

    with open(filepath, 'r') as f:
        hex_str = f.read()

    pttn = re.findall(r'value: \(0x\).*\n', hex_str)

    #去掉value: (0x)
    hex_list_temp = []
    for _, v in enumerate(pttn):
        v = v.lstrip('value: (0x)')
        v = v.rstrip('\n')
        hex_list_temp.append(v)
        
    #去掉'-'
    hex_list = []
    for _, v in enumerate(hex_list_temp):
        hex_list.append(v.split('-'))
    #连接字符串
    asc_str = ""
    for _, v_list in enumerate(hex_list):
        for _, v in enumerate(v_list):
            try:
                asc_str = asc_str + str(binascii.a2b_hex(v), encoding='utf8')
            except:
                err_s = 'error:'
                for _,e in enumerate(v_list):
                   err_s =  err_s + e + ' '      
                return err_s

    #写入文件
    write_file = filepath.rstrip('.txt')
    write_file = write_file + '-conversion.txt'
    with open(write_file, 'w') as f:
        f.write(asc_str)

    return err_s


def main():
    layout = [[sg.Input(key='-FILE_PATH-'),sg.FileBrowse('打开文件')],
              [sg.Button('转换',key='-SW-',size=(10,2)),sg.T('等待转换',size=(40,4),key='-STATE-')]]
    window = sg.Window('Nordic APP Log Conversion tool v1.1', layout, icon=base64_main_icon)

    while True:
        event, values = window.read()

        if event == '-SW-':
            file_path = window['-FILE_PATH-'].get()
            if file_path == '':
                sg.popup('没有选中文件')
            else:
                window['-STATE-'].update('转换开始......')
                result = conversion(file_path)
                if result.startswith('error:'):
                    window['-STATE-'].update('转换失败')
                    sg.popup(result)
                else:
                    window['-STATE-'].update('转换完成:'+ file_path.rstrip('.txt') + '-conversion.txt')
                    sg.popup('转换成功')

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
