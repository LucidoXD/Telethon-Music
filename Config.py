import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27589257"))
    API_HASH = os.environ.get("API_HASH", "0af78b04b48361bc117fa4e06d6d2292")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1810353153:AAHg0VaqnLvr85ZC5XYks7BtJTj5JsHmOOI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOL4Bu4XXLXWcOzco9WPT4hzeCdP7bO6Ar6xMuuPtKQJ3_-c6GOeMH8MbYYL4xPrqWBaL-UGU3dJYB-RZecvVWv-yhcoFtKXQklrRDV34mIL90EPn6PFeOD03lZytZRvuCM2Hy6DSHvjBpQ1rG-GPXEJZs_CUDt6zdUMHk5PL1UZG8GxFeagjkqNv88sWS4u8oxKC-pENyxhxP6PEoZurIP_bIXqXtRawiWJQfc_Jg5n9lyfNmKtj-LwneqsQkRSw-S5_rEPrHIphv2F0BNQQV12RTf4nvQh6juf6KWZAkpnXRU-1DxIRyka9tk2c0ueOihvmEPClZ1RseYiCdMADO7aI4Og=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@bsiskssisisi")
    SUPPORT = os.environ.get("SUPPORT", "DrewNotFound") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "DrewNotFound") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5815218439")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
