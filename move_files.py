import os
from os import remove
import shutil
import time
import sys
from datetime import datetime, timedelta

# TOTAL FCST

# Alte Dateien verschieben

source = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006_Ttl/'
newsource = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006_Ttl/Store/'
i = 0
files = os.listdir(source)

for file in files:
    modificationTime = time.strftime('%d/%m/%Y', time.localtime(os.path.getmtime(source + file)))
    if modificationTime == datetime.strftime(datetime.now() - timedelta(2), '%d/%m/%Y') or modificationTime == datetime.strftime(datetime.now() - timedelta(4), '%d/%m/%Y'):
        shutil.move(source + file, newsource + file)
        i = i + 1

print(i)

if i == 0:
    print("Die FOR_006_TTL Dateien fehlen.")
    sys.exit()

# Neue Dateien reinkopieren

source = 'T:/Analyse/'
newsource = 'U:/data_source_apps/drr_pilot/FOR_006_Ttl/'
i = 0
files = os.listdir(source)

for file in files:
    if '_T_' in file:
        shutil.move(source + file, newsource + file)
        i = i + 1

print(i)

# FCST

# Alte Dateien verschieben

source = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006/'
newsource = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006/Store/'
i = 0
files = os.listdir(source)

for file in files:
    modificationTime = time.strftime('%d/%m/%Y', time.localtime(os.path.getmtime(source + file)))
    if modificationTime == datetime.strftime(datetime.now() - timedelta(2), '%d/%m/%Y') or modificationTime == datetime.strftime(datetime.now() - timedelta(4), '%d/%m/%Y'):
        shutil.move(source + file, newsource + file)
        i = i + 1

print(i)

if i == 0:
    print("Die FOR_006_TTL Dateien fehlen.")
    sys.exit()

source = '//dwa-bu-sftp001/Datevdownloads/transport.h-hotels.com/Revenue/Analyse/'
dest_block_deposit = '//db-rb-fs001/data_qlik_desktop/data_source_apps/block_conversion_analysis/bus_022_deposits/'
dest_potential_groups = '//db-rb-fs001/data_qlik_desktop/data_source_apps/potential_groups/'
dest_FOR_006 = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006/'
dest_FOR_006_Ttl = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006_Ttl/'
dest_BUS_055 = '//db-rb-fs001/data_qlik_desktop/data_source_apps/block_conversion_analysis/bus_055/actual_period/'

remove_files = os.listdir(dest_BUS_055)

for file in remove_files:
    os.remove(dest_BUS_055 + file)

files = os.listdir(source)

for file in files:
    if 'block_deposit' in file:
        os.rename(source + file, source + 'block_deposit.xml')
    if 'CH_rep_bh_short' in file:
        os.rename(source + file, source + 'CH.xml')
    if 'D_A_rep_bh_short' in file:
        os.rename(source + file, source + 'D_A.xml')
    print(file) 


files = os.listdir(source)

for file in files:
    if 'block_deposit' in file:
        shutil.move(os.path.join(source, file), os.path.join(dest_block_deposit, file))
    if 'CH' in file:
        shutil.move(os.path.join(source, file), os.path.join(dest_potential_groups, file))
    if 'D_A' in file:
        shutil.move(os.path.join(source, file), os.path.join(dest_potential_groups, file))
    if '_T_history_forecast' in file:
        shutil.move(os.path.join(source, file), os.path.join(dest_FOR_006_Ttl, file))
    if 'history_forecast' in file:
        try:
            shutil.move(os.path.join(source, file), os.path.join(dest_FOR_006, file))
        except: FileNotFoundError
    if 'ramada_conversion' in file and 'sales' not in file:
        shutil.move(os.path.join(source, file),os.path.join(dest_BUS_055,file))

files = os.listdir(dest_BUS_055)

for file in files:
    try:
        f= open(dest_BUS_055+file,'r',encoding="utf-8",errors = 'ignore')
        content=f.read()
        f.close()
        f=open(dest_BUS_055+file[0:],'w',encoding="utf-8")
        f.write(content)
        f.close()
    except UnicodeDecodeError:
        print("Fehler:"+" "+file)

print('abgeschlossen')