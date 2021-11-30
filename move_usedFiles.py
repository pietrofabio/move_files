import os
import shutil
from datetime import date, datetime
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

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# ------------------------------------------------------------------

src = f"//db-rb-fs001/data_qlik_desktop/data_source_apps/expected_otb_room_nights/H.ostel/"
file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and date.fromtimestamp(entry.stat().st_mtime) != date.today():
            os.remove(src + entry.name)
            file_counter += 1

logger.info(f"{file_counter} H.ostel OTB file(s) has been removed")

src_list = [f"//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006/",
            f"//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/FOR_006_Ttl/"]
file_counter = 0
for src in src_list:
    with os.scandir(src) as it:
        for entry in it:
            if entry.is_file() and date.fromtimestamp(entry.stat().st_mtime) != date.today():
                shutil.move(src + entry.name, src + 'Store/' + entry.name)
                file_counter += 1

logger.info(f"{file_counter} FOR_006 file(s) has been stored")

src = f"//db-rb-fs001/data_qlik_desktop/data_source_apps/go_green/con_055/"
file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file():
            shutil.move(src + entry.name, src + 'store/' + entry.name)
            file_counter += 1

logger.info(f"{file_counter} Go_Green_Log file(s) has been stored")
