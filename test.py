
import csv


def data_check(filepath,err_list,sn_index = 1):
    err_cnt = 0
    total_len = 0
    with open('test.csv','r') as csvFile:
        spamreader = csv.reader(csvFile)
        old = -1
        for row in spamreader:
            if old == -1:
                old = new = int(row[sn_index])
            else:
                new = int(row[sn_index])
            delta = new - old
            if delta < 0 or delta > 1:
                err_cnt = err_cnt + abs(delta)
                err_list.append(new)
            old = new
            total_len += 1

    return [err_cnt,total_len]

def fun(s):
    s = '123'

s = '456'
fun(s)
print(s)