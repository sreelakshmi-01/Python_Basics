import pywhatkit
import pyautogui
import time

# Initial message setup to open WhatsApp Web at 11:00 AM
phone_number = "+919526310726"
message = "Dear Chippy, we've detected unusual activity on your whatsapp account. Please click the link to verify your identity: https://slcyber.io/dark-web-hub/ "


# Send the first message to open WhatsApp Web
pywhatkit.sendwhatmsg(phone_number, message, 12, 7)

# Wait a few seconds to ensure the WhatsApp Web session is active
#time.sleep(15)

# Send repeated messages every 5 minutes for the next 30 minutes
for _ in range(5):  # 5 repetitions, change as needed
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    #time.sleep(5)
