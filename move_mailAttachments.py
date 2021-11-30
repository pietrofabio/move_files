import os
import shutil
from datetime import date, datetime, timedelta
import openpyxl
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
# Moving Suite8 H.ostel OTB file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/suite8/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/expected_otb_room_nights/H.ostel/'
dst2 = '//dwa-hq-ql001/QlikSenseDaten/Daily-Revenuemanagement-Summary/Hostel/hist_fore/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("OTB_h.ostel") != -1:
            shutil.copy2(src + entry.name, dst + entry.name)
            shutil.copy2(src + entry.name, dst2 + entry.name)
            shutil.move(src + entry.name, src + "store/" + entry.name)
            file_counter += 1

logger.info(f"{file_counter} Suite8 H.ostel OTB file(s) has been moved")

# ------------------------------------------------------------------
# Moving r_a rev flash files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/revenue_flash_report/new_reports/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("rev_flash") != -1:
            shutil.copy2(src + entry.name, dst + entry.name)
            shutil.move(src + entry.name, src + "store/" + entry.name)
            file_counter += 1

logger.info(f"{file_counter} r_a rev flash file(s) has been moved")

# ------------------------------------------------------------------
# duetto forecast file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/duetto/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/duetto_forecast_dev/monthly/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("ForecastSnapshot") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)
            file_date = date.fromisoformat(entry.name[0:10]).strftime("%d.%m.%Y")
            os.rename(src + entry.name,src + "ForecastSnapshotMonthly_" + file_date + ".csv")
            file_counter += 1

logger.info(f"{file_counter} duetto forecast file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("ForecastSnapshot") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} duetto forecast file(s) has been moved")

# ------------------------------------------------------------------
# duetto current rate file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/duetto/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/CurrentRate/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("CurrentRate") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)
            if date.fromisoformat(entry.name[0:10]) != date.today():
                os.remove(src + entry.name)
                file_counter += 1

logger.info(f"{file_counter} duetto current rate file(s) has been removed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("CurrentRate") != -1:
            os.rename(src + entry.name,src + "CurrentRateReport" + ".csv")
            file_counter += 1

logger.info(f"{file_counter} duetto current rate file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("CurrentRate") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} duetto current rate file(s) has been moved")

# ------------------------------------------------------------------
# revenue past 91 days Jan Heimbeck file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/revenue_Anlyse/Aktuelle Dailys/Jan Heimbeck/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_past_91_days") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_past_91_days") != -1 and entry.name.find("D_A") != -1:
            os.rename(src + entry.name, src + "revenue_past_91_days_D_A.csv")
            file_counter += 1
        elif entry.is_file() and entry.name.find("_past_91_days") != -1 and entry.name.find("CH") != -1:
            os.rename(src + entry.name, src + "rev_past_91_days_CH.csv")
            file_counter += 1
        elif entry.is_file() and entry.name.find("_past_91_days") != -1 and entry.name.find("HU") != -1:
            os.rename(src + entry.name, src + "rev_past_91_days_HU.csv")
            file_counter += 1

logger.info(f"{file_counter} revenue past 91 days file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("_past_91_days") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} revenue past 91 days file(s) has been moved")

# ------------------------------------------------------------------
# oaky performace file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/oaky/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/oaky_summary/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("Oaky Performance Data") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("Oaky Performance Data (Bookings)") != -1:
            os.rename(src + entry.name, src + "H-Hotels Oaky Performance Data (Bookings).csv")
            file_counter += 1
        if entry.is_file() and entry.name.find("Oaky Performance Data (Emails)") != -1:
            os.rename(src + entry.name, src + "H-Hotels Oaky Performance Data (Emails).csv")
            file_counter += 1

logger.info(f"{file_counter} oaky performace file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("Oaky Performance Data") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} oaky performace file(s) has been moved")

# ------------------------------------------------------------------
# hotel 4youth strategy sheet files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/h+_4youth/'
dst = '//db-rb-fs001/revenue/Strategy Sheet/non-Opera/H+ Hotel 4Youth/Sources/Forecast_2021_2022/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file():
            shutil.copy2(src + entry.name, src + "store/" + entry.name)

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file():
            filename = entry.path
            book = openpyxl.load_workbook(filename)
            sheet = book['Tabelle1']
            filecontent = sheet['A2']
            datelist = filecontent.value.split(' ')
            fromdate = datetime.strptime(datelist[2], '%d/%m/%Y').date()
            todate = datetime.strptime(datelist[7], '%d/%m/%Y').date()
            filedate = datetime.strptime(entry.name[0:10], '%Y-%m-%d').date()
            if filedate == fromdate and todate == datetime.strptime('31/12/2022', '%d/%m/%Y').date():
                os.rename(src + entry.name, src + f"Forecast_{filedate.strftime('%d.%m.%Y')}.xlsx")
                file_counter += 1
            elif filedate - timedelta(days=1) == todate and fromdate == datetime.strptime('01/01/2021', '%d/%m/%Y').date():
                os.rename(src + entry.name, src + f"History_{filedate.strftime('%d.%m.%Y')}.xlsx")
                file_counter += 1

logger.info(f"{file_counter} hotel 4youth strategy sheet file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("Forecast_") != -1 or entry.name.find("History_") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} hotel 4youth strategy sheet file(s) has been moved")

# ------------------------------------------------------------------
# OTB Forecast files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/revenue_strategy_dashboard/otb_forecast/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("forecast_segment") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name + ".csv")


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("forecast_segment") != -1:
            shutil.move(src + entry.name, dst + entry.name + ".csv")
            file_counter += 1

logger.info(f"{file_counter}  forecast segment file(s) has been moved")

# ------------------------------------------------------------------
# history segment files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/revenue_strategy_dashboard/otb_history/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("history_segment") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name + ".csv")


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.stat().st_size < 300:
            os.remove(src + entry.name)
            file_counter += 1

logger.info(f"{file_counter} history segment file(s) has been removed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("history_segment") != -1:
            shutil.move(src + entry.name, dst + entry.name + ".csv")
            file_counter += 1

logger.info(f"{file_counter} history segment file(s) has been moved")


# ------------------------------------------------------------------
# transaction results files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/revenue_strategy_dashboard/transaction_results/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("transaction_results") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name + ".csv")


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.stat().st_size < 300:
            os.remove(src + entry.name)
            file_counter += 1

logger.info(f"{file_counter} transaction results file(s) has been removed")


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("transaction_results") != -1:
            shutil.move(src + entry.name, dst + entry.name + ".csv")
            file_counter += 1

logger.info(f"{file_counter} transaction results file(s) has been moved")

# ------------------------------------------------------------------
# history segment fill up files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/revenue_strategy_dashboard/otb_history/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("history_seg_fill_up") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name + ".csv")


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.stat().st_size < 300:
            os.remove(src + entry.name)
            file_counter += 1

logger.info(f"{file_counter} history_seg_fill_up file(s) has been removed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("history_seg_fill_up") != -1:
            shutil.move(src + entry.name, dst + entry.name + ".csv")
            file_counter += 1

logger.info(f"{file_counter} history_seg_fill_up file(s) has been moved")
