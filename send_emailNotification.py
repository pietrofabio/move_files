from exchangelib import Credentials, Account, DELEGATE, Configuration, FileAttachment, Message, Mailbox
from datetime import datetime

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


# ------------------------------------------------------------------
# send notification email
m = Message(
    account=account,
    subject=f"Daily data processing {datetime.today().strftime('%d.%m.%Y %H:%M')} has been completed",
    body=f"https://qlik.hospinet.net/sense/app/fa29d1a5-987b-4389-b0a5-7961c06c8310/"
         f"sheet/11b56f0c-d77c-456e-9ce8-0b02d5710936/state/analysis",
    to_recipients=[Mailbox(email_address='felix.kraemer@h-hotels.com'),
                   Mailbox(email_address='peter.fabian@h-hotels.com')]
)

m.send()
