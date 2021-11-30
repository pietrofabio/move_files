import os
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
# remove old BUS_055_Sales files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/sales_group_performance/opera_bus_055/'

if date.weekday(date.today()) == 4:
    file_counter = 0
    with os.scandir(src) as it:
        for entry in it:
            if entry.is_file() and entry.name.find("ramada_conversion_creation") != -1 \
                    and entry.name.find(".xml") != -1 \
                    and date.fromtimestamp(entry.stat().st_mtime) < date.today() - timedelta(days=1):
                os.remove(src + entry.name)
                file_counter += 1

    logger.info(f"{file_counter} old BUS_055_Sales file(s) has been removed")
else:
    logger.info(f"0 old BUS_055_Sales file(s) has been removed (weekday != 4)")
