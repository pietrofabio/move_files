import os
import shutil
import time
import sys
from datetime import date, datetime, timedelta

# Alte Dateien verschieben

# TOTAL FCST

hotels = [
'05304', '05313', '05314', '05700', '05705', '05708', '05715', '05719', '05721', '05725', '05729',
'05730', '05992', '08073', '08075', '08076', '15703', '15709', '15712', '15714', '15717',
'15722', '15723', '15735', '15738', '15740', '15742', '15743', '15756', '16289', '19117', '19950',
'19955', '20001', '20002', '20004', '20005','20006', '20007', '20374', '32621', '32623', '32623', '32624', '32625',
'32626', '32628', '32629','32630', '42451', '46393', '60001', '71222', 'HDE71001', 'HDE71002', 'HDE71003'
]

dest_BUS_055 = '//db-rb-fs001/data_qlik_desktop/data_source_apps/block_conversion_analysis/bus_055/actual_period/'
#dest_BUS_055 = '//db-rb-fs001/data_qlik_desktop/data_source_apps/sales_group_performance/opera_bus_055/'

files = os.listdir(dest_BUS_055)

for file in files:
    try:
        f = open(dest_BUS_055+file, 'r', encoding="utf-8", errors='ignore')
        content = f.read()
        if content[-29:] != '/RAMADA_CONVERSION_CREATION>\n':
            print('BUS_055: ' + file)
        f.close()
        f = open(dest_BUS_055+file[0:], 'w', encoding="utf-8")
        f.write(content)
        f.close()
        if file[0] == 'H':
            hotels.remove(file[0:8])
        else:
            hotels.remove(file[0:5])
    except UnicodeDecodeError:
        print("Fehler: "+file)


if len(hotels) > 0:
    print(hotels)
print('Abgeschlossen')