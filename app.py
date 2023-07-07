import os
from dotenv import load_dotenv
import pywhatkit

def main():
    load_dotenv()
    # print(os.getenv("WHATSAPP_GROUP_LINK_ID_ANNOUNCEMENT"))

    # message for community announcement group only for seperate group in community seperate code is there sepereate , 11th line should be written
    link = os.getenv("WHATSAPP_GROUP_LINK_ID_ANNOUNCEMENT")
    pywhatkit.sendwhatmsg_to_group(link,'message',14,26)
    
if __name__ == '__main__':
    main()