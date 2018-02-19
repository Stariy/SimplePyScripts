#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""
Скрипт для уведомления о появлении новых серий аниме My Hero Academia.

"""


# Чтобы можно было импортировать all_common.py, находящийся уровнем выше
import sys
sys.path.append('..')


from all_common import make_backslashreplace_console, get_logger, simple_send_sms, wait


make_backslashreplace_console()


log = get_logger('new video My Hero Academia')


# https://github.com/gil9red/SimplePyScripts/blob/e3279dcf83a2e88ffc5248cf54a14b6e3c81c1f9/online.anidub.com/get%20video%20list%20My%20Hero%20Academia.py
def search_video_list():
    url = 'https://online.anidub.com/index.php?do=search'

    data = {
        'do': 'search',
        'subaction': 'search',
        'search_start': '1',
        'full_search': '0',
        'result_from': '1',
        'story': 'Моя геройская академия',
    }

    import requests
    rs = requests.post(url, data)

    from bs4 import BeautifulSoup
    root = BeautifulSoup(rs.content, 'html.parser')

    return [a.text.strip() for a in root.select('.newstitle a')]


FILE_NAME_CURRENT_ITEMS = 'video'


def save_items(items):
    open(FILE_NAME_CURRENT_ITEMS, mode='w', encoding='utf-8').write(str(items))


if __name__ == '__main__':
    notified_by_sms = True

    # Загрузка текущих элементов
    try:
        import ast
        current_items = ast.literal_eval(open(FILE_NAME_CURRENT_ITEMS, encoding='utf-8').read())

    except:
        current_items = []

    log.debug('Current items(%s): %s', len(current_items), current_items)

    while True:
        try:
            log.debug('get items')

            items = search_video_list()
            log.debug('items: %s', items)

            # Если список текущих игр
            if not current_items:
                log.debug('Обнаружен первый запуск')

                current_items = items
                save_items(current_items)

            else:
                new_items = set(items) - set(current_items)
                if new_items:
                    current_items = items
                    save_items(current_items)

                    for item in new_items:
                        text = 'Новая серия "{}"'.format(item)
                        log.debug(text)

                        if notified_by_sms:
                            simple_send_sms(text, log)

                else:
                    log.debug('Изменений нет')

            wait(weeks=2)

        except:
            log.exception('Ошибка:')
            log.debug('Через 5 минут попробую снова...')

            # Wait 5 minutes before next attempt
            import time
            time.sleep(5 * 60)
