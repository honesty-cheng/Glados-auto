import os
from check_in import GLaDOS_CheckIn


def handler(event, context):
    checkIn()
    return "Done"


def checkIn():
    COOKIES = os.getenv('COOKIES')
    # COOKIES = '_ga=GA1.2.1471779015.1662441243; _gid=GA1.2.2081561511.1662441243; koa:sess=eyJ1c2VySWQiOjEyNTc5NCwiX2V4cGlyZSI6MTY4ODM2MTQwNzg3OSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=ca7_5AKGh3-L1NjGxuw6loR6XSw; __cf_bm=RFgwjpe4yqWWMgPLIUM0CuUfPzGAfEQ_jJhOySn7RV4-1662516383-0-AWQ1u9nCd6i2a5nT4xSNIj2CC/HwXwCE0hk7wgxHW3z8EJ/xCjqPn3eRT/RimBP9FqGz/4kgN40j+GU0rxFIwSJXSRBUqVgBIBm7BxcYHrhlWFbrgJEIZiX9K2Nb4ibzKw=='
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')
    if COOKIES is None:
        raise EnvironmentError('Environment COOKIES not found!')
    if BOT_TOKEN is None:
        raise EnvironmentError('Environment BOT_TOKEN not found!')
    if CHAT_ID is None:
        raise EnvironmentError('Environment CHAT_ID not found!')
    GLaDOS_CheckIn(COOKIES, BOT_TOKEN, CHAT_ID).run()


if __name__ == '__main__':
    checkIn()
