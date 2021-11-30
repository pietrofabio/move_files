import logging
import subprocess
from datetime import datetime
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
# Start of daily data process

logger.info(f"Daily data process has been started")

# Download Email Attachments

run_getMailAttachments = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/get_mailAttachments.py', shell=True,
                   capture_output=True)

if run_getMailAttachments.returncode != 0:
    logger.error(f"Module get_mailAttachments did not ran successfully")
else:
    logger.info(f"Module get_mailAttachments did ran successfully")


# Move Email Attachments

run_moveMailAttachments = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/move_mailAttachments.py', shell=True,
                   capture_output=True)

if run_moveMailAttachments.returncode != 0:
    logger.error(f"Module move_mailAttachments did not ran successfully")
else:
    logger.info(f"Module move_mailAttachments did ran successfully")


# Move Opera Schedule Files

run_moveOperaSchedule = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/move_OperaSchedule.py', shell=True,
                   capture_output=True)

if run_moveOperaSchedule.returncode != 0:
    logger.error(f"Module move_OperaSchedule did not ran successfully")
else:
    logger.info(f"Module move_OperaSchedule did ran successfully")


# Remove old BUS_055 Files in actual_period

run_remove_old_BUS_055 = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/remove_old_BUS_055.py', shell=True,
                   capture_output=True)

if run_remove_old_BUS_055.returncode != 0:
    logger.error(f"Module remove_old_BUS_055 did not ran successfully")
else:
    logger.info(f"Module remove_old_BUS_055 did ran successfully")


# Remove old BUS_055_Sales Files only fridays

run_remove_old_BUS_055_Sales = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/remove_old_BUS_055_Sales.py',
                   shell=True, capture_output=True)

if run_remove_old_BUS_055_Sales.returncode != 0:
    logger.error(f"Module remove_old_BUS_055_Sales did not ran successfully")
else:
    logger.info(f"Module remove_old_BUS_055_Sales did ran successfully")


# Update encoding in fup & opt activity file

run_encoding_activities = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/encoding_activities.py',
                   shell=True, capture_output=True)

if run_encoding_activities.returncode != 0:
    logger.error(f"Module encoding_activities did not ran successfully")
else:
    logger.info(f"Module encoding_activities did ran successfully")

logger.info(f"Daily data process has been finished")


# ------------------------------------------------------------------
# End of daily data process

# ------------------------------------------------------------------
# Reload Trigger Daily Data Processing Task

requests.packages.urllib3.disable_warnings()

# Header
xrf = 'iX83QmNlvu87yzAB'
headers = {'X-Qlik-xrfkey': xrf,
           "Content-Type": "application/json",
           "X-Qlik-User": "UserDirectory=hospinet;UserId=felix.kraemer"}

cert = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_scripts/ExternalTaskTrigger/clientandkey.pem'
task_id = 'cb2f07b3-8570-4970-ab15-8f8b083bbf89'
url = f"https://dwa-hq-ql001.hospinet.net:4242/qrs/task/{task_id}/start/synchronous?xrfkey={xrf}"
resp = requests.post(url, headers=headers, verify=False, cert=cert)


# ------------------------------------------------------------------
# Notification Email

run_sendEmailNotification = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/send_emailNotification.py', shell=True,
                   capture_output=True)

if run_sendEmailNotification.returncode != 0:
    logger.error(f"Module send_emailNotification did not ran successfully")
else:
    logger.info(f"Module send_emailNotification did ran successfully")

