from exchangelib import Credentials, Account, DELEGATE, Configuration, FileAttachment
import os.path
import logging
from datetime import datetime

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
# mailbox details
username = 'HOSPINET\\revenue-reports'
password = 'muu7z_TrjZiAj2G8Zb2fFqfe-iqhqvFP-'
server = 'webmail.h-hotels.com'
primary_smtp_address = 'revenue-reports@h-hotels.com'

# ------------------------------------------------------------------
# mailbox connecting
credentials = Credentials(username=username, password=password)
config = Configuration(server=server, credentials=credentials)
account = Account(primary_smtp_address=primary_smtp_address,
                  config=config, autodiscover=False, access_type=DELEGATE)

logger.debug(f"Connected to: {server}")
logger.debug(f"Active user: {primary_smtp_address}")

# ------------------------------------------------------------------
# Saving attachments from qualified email addresses
logger.info(f"Start fetching attachments")

item_counter = 0
logger.debug(f"Item counter set equal zero")
item_attach_counter = 0
logger.debug(f"Attachment item counter set equal zero")

for item in account.inbox.all():
    item_counter += 1
    sender_mail = str(item.sender).split(',')[1].strip().split("'")[1]

    for attachment in item.attachments:
        if isinstance(attachment, FileAttachment):

            if sender_mail == "Portal@oracleindustry.com":
                subject = str(item.subject)
                received = item.datetime_received.strftime('%Y-%m-%d')
                file_name = received + '_' + subject
                local_path = \
                    os.path.join('//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/', file_name)
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                logger.info(f"Attachment from {sender_mail} saved to {local_path}")
                item_attach_counter += 1

            elif sender_mail == "hostel.muenster@h-hotels.com":
                attach_name = str(attachment.name)
                received = item.datetime_received.strftime('%Y-%m-%d')
                file_name = attach_name
                local_path = \
                    os.path.join('//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/suite8/', file_name)
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                logger.info(f"Attachment from {sender_mail} saved to {local_path}")
                item_attach_counter += 1

            elif sender_mail == "donotreply@duettoresearch.com":
                attach_name = str(attachment.name)
                received = item.datetime_received.strftime('%Y-%m-%d')
                file_name = received + '_' + attach_name
                local_path = \
                    os.path.join('//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/duetto/', file_name)
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                logger.info(f"Attachment from {sender_mail} saved to {local_path}")
                item_attach_counter += 1

            elif 'oaky.com' in sender_mail:
                attach_name = str(attachment.name)
                received = item.datetime_received.strftime('%Y-%m-%d')
                file_name = received + '_' + attach_name
                local_path = \
                    os.path.join('//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/oaky/', file_name)
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                logger.info(f"Attachment from {sender_mail} saved to {local_path}")
                item_attach_counter += 1
            elif sender_mail == "Hplus.Berlin@h-hotels.com":
                attach_name = str(attachment.name)
                received = item.datetime_received.strftime('%Y-%m-%d')
                file_name = received + '_' + attach_name
                local_path = \
                    os.path.join('//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/h+_4youth/', file_name)
                with open(local_path, 'wb') as f:
                    f.write(attachment.content)
                logger.info(f"Attachment from {sender_mail} saved to {local_path}")
                item_attach_counter += 1
    item.move_to_trash()

logger.info(f"Finish fetching attachments")
logger.info(f"{item_attach_counter} item(s) processed")
logger.info(f"{item_counter} item(s) moved to trash folder")
