import logging
import os
from datetime import datetime, date
import requests

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
# Start of task reload

# Header
requests.packages.urllib3.disable_warnings()
xrf = 'iX83QmNlvu87yzAB'
headers = {'X-Qlik-xrfkey': xrf,
           "Content-Type": "application/json",
           "X-Qlik-User": "UserDirectory=hospinet;UserId=felix.kraemer"}
cert = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_scripts/ExternalTaskTrigger/clientandkey.pem'

# ------------------------------------------------------------------
# Duetto Forecast Monitor
task_id = 'db247283-0759-4832-8e97-97c13cc716e7'

# Last execution check

url = f"https://dwa-hq-ql001.hospinet.net:4242/qrs/reloadtask/{id}?xrfkey={xrf}"
resp = requests.get(url, headers=headers, verify=False, cert=cert)
print(resp.json())

status = resp.json()['operational']['lastExecutionResult']['status']
stop_date = date.fromisoformat(resp.json()['operational']['lastExecutionResult']['stopTime'][:10])

if stop_date != date.today() or status != 7:

    # Source data validation
    src = "//db-rb-fs001/data_qlik_desktop/data_source_apps/duetto_forecast_dev/monthly/"

    snapshots = []

    with os.scandir(src) as it:
        for entry in it:
            if entry.is_file() and entry.name.find('ForecastSnapshotMonthly') != -1:
                snapshots.append(datetime.strptime(entry.name[24:34], '%d.%m.%Y').date())
    src_actual = sorted(snapshots, reverse=True)[0] == date.today()

    # Reload Trigger

    if src_actual:
        url = f"https://dwa-hq-ql001.hospinet.net:4242/qrs/task/{task_id}/start/synchronous?xrfkey={xrf}"
        resp = requests.post(url, headers=headers, verify=False, cert=cert)

        logger.info(f"Duetto Forecast Monitor Task has been triggered")
    else:
        logger.info(f"Duetto Forecast Monitor Task has not been triggered (src not actual)")
