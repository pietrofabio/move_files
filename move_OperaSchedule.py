import os
import shutil
from datetime import date, timedelta, datetime
import logging

# ------------------------------------------------------------------
# setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(module)s;%(levelname)s;%(asctime)s;%(message)s')

file_handler = \
    logging.FileHandler(f"//db-rb-fs001/data_qlik_desktop/data_source_apps/"
                        f"_logs/data_processing_{datetime.today().strftime('%d.%m.%Y')}.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)

# ------------------------------------------------------------------
# BUS_022 file

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/block_conversion_analysis/bus_022_deposits/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("block_deposit") != -1 and entry.name.find(".xml") != -1 and \
                date.fromtimestamp(os.stat(src+str(entry.name)).st_mtime) < date.today()-timedelta(days=1):
            os.remove(src + entry.name)
            file_counter += 1

logger.info(f"{file_counter} block_deposit file(s) has been removed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("block_deposit") != -1 and entry.name.find(".xml") != -1:
            os.rename(src + entry.name, src + "block_deposit.xml")
            file_counter += 1

logger.info(f"{file_counter} block_deposit file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("block_deposit") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} block_deposit file(s) has been moved")

# ------------------------------------------------------------------
# BUS_055 files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/block_conversion_analysis/bus_055/actual_period/'
dst2 = '//db-rb-fs001/data_qlik_desktop/data_source_apps/sales_group_performance/opera_bus_055/'

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("ramada_conversion") != -1 and entry.name.find(
                "creation_Sales") == -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} BUS_055 file(s) has been moved")

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("ramada_conversion") != -1 and entry.name.find(
                "creation_Sales") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst2 + entry.name)
            file_counter += 1

logger.info(f"{file_counter} BUS_055_Sales file(s) has been moved")

# ------------------------------------------------------------------
# FOR_006 files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006/'
dst2 = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006_Ttl/'
dst3 = '//dwa-hq-ql001/QlikSenseDaten/Daily-Revenuemanagement-Summary/Opera/FOR_006_room_revenue/'
dst4 = '//dwa-hq-ql001/QlikSenseDaten/Daily-Revenuemanagement-Summary/Opera/FOR_006_total_revenue/'

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("history_forecast") != -1 and entry.name.find(
                "_T_") == -1 and entry.name.find(".xml") != -1:
            shutil.copy2(src + entry.name, dst + entry.name)
            shutil.move(src + entry.name, dst3 + entry.name)
            file_counter += 1

logger.info(f"{file_counter} FOR_006 Room Revenue file(s) has been moved")

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("history_forecast") != -1 and entry.name.find(
                "_T_") != -1 and entry.name.find(".xml") != -1:
            shutil.copy2(src + entry.name, dst2 + entry.name)
            shutil.move(src + entry.name, dst4 + entry.name)
            file_counter += 1

logger.info(f"{file_counter} FOR_006 Total Revenue file(s) has been moved")


# ------------------------------------------------------------------
# BUS_017 files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/potential_groups/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_rep_bh_short") != -1 and entry.name.find(".xml") != -1 and \
                date.fromtimestamp(os.stat(src+str(entry.name)).st_mtime) < date.today()-timedelta(days=1):
            os.remove(src + entry.name)
            file_counter += 1

logger.info(f"{file_counter} BUS_017 file(s) has been removed")

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_rep_bh_short") != -1 and entry.name.find(
                "D_A") != -1 and entry.name.find(".xml") != -1:
            os.rename(src + entry.name, src + "D_A.xml")
            file_counter += 1

        if entry.is_file() and entry.name.find("_rep_bh_short") != -1 and entry.name.find(
                "CH") != -1 and entry.name.find(".xml") != -1:
            os.rename(src + entry.name, src + "CH.xml")
            file_counter += 1

logger.info(f"{file_counter} BUS_017 file(s) has been renamed")

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("D_A.xml") != -1 or entry.name.find("CH.xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} BUS_017 file(s) has been moved")

# ------------------------------------------------------------------
# strategy sheet files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/revenue/Strategy Sheet/History_Forecast/'

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_strategysheet") != -1 and entry.name.find(".xml") != -1:
            if entry.name[0] == "H":
                os.rename(src + entry.name, src + f"{entry.name[0:8]}_strategysheet.xml")
            elif entry.name[0] == "_":
                continue
            elif entry.name[0] != "H":
                os.rename(src + entry.name, src + f"{entry.name[0:5]}_strategysheet.xml")
            file_counter += 1

logger.info(f"{file_counter} strategysheet file(s) has been renamed")

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_strategysheet") != -1 and entry.name.find(".xml") != -1\
                and entry.name[0] != "_":
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} strategysheet file(s) has been moved")

# ------------------------------------------------------------------
# cvs tff source files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/forecast_pace_analysis/Central Data Source R&A/EVE_004/'

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_CVS_TFF") != -1 and entry.name.find(".txt") != -1:
            file_counter += 1

if file_counter == 5:

    file_counter = 0

    with os.scandir(dst) as it:
        for entry in it:
            os.remove(dst + entry.name)
            file_counter += 1

    logger.info(f"{file_counter} old cvs tff source file(s) has been removed from dst")

    file_counter = 0

    with os.scandir(src) as it:
        for entry in it:
            if entry.is_file() and entry.name.find("_CVS_TFF") != -1 and entry.name.find(".txt") != -1:
                shutil.move(src + entry.name, dst + entry.name)
                file_counter += 1

    logger.info(f"{file_counter} cvs tff source file(s) has been moved")

    file_counter = 0

    with os.scandir(dst) as it:
        for entry in it:
            if entry.is_file() and entry.name.find("_CVS_TFF") != -1 and entry.name.find(".txt") != -1:
                os.rename(dst + entry.name, dst + f"{entry.name[0:6]}.txt")
                file_counter += 1

    logger.info(f"{file_counter} cvs tff source file(s) has been renamed")

else:
    logger.info(f"No new cvs tff source files on SFTP")

# ------------------------------------------------------------------
# Go_Green_Log files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/go_green/con_055/'

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("Go_Green_Log") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} Go_Green_Log file(s) has been moved")

# ------------------------------------------------------------------
# fup opt activity files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/block_conversion_analysis/block_activities/FUP_OPT/'

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("fup_opt_activity") != -1 and entry.name.find(".xml") != -1:
            os.rename(src + entry.name, src + f"fup_opt_activity.xml")
            file_counter += 1

logger.info(f"{file_counter} fup opt activity file(s) has been renamed")

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("fup_opt_activity") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} fup opt activity file(s) has been moved")

# ------------------------------------------------------------------
# Revenue Strategy files

src = '//dwa-bu-sftp001/Datevdownloads/OPERA/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/revenue_strategy_dashboard/'

file_counter = 0

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("forecast_data_deduct") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1
        if entry.is_file() and entry.name.find("forecast_data_nondeduct") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1
        if entry.is_file() and entry.name.find("transaction_data") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1
        if entry.is_file() and entry.name.find("history_data") != -1 and entry.name.find(".xml") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} Revenue Strategy files file(s) has been moved")
