#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from typing import List

from bs4 import BeautifulSoup
import requests

from common import smart_comparing_names, USER_AGENT, get_norm_text, get_uniques, get_logger


log = get_logger(__file__)


def get_game_genres(game_name: str, need_logs=False) -> List[str]:
    need_logs and log.info(f'Search {game_name!r}...')

    headers = {
        'User-Agent': USER_AGENT,
        'X-Requested-With': 'XMLHttpRequest',
    }
    form_data = {
        'mode': '11',
        's': '1',
        'p': '1',
        'fg': 'all',
        'fp': 'all',
        'fn': game_name
    }

    url = 'https://www.igromania.ru/-Engine-/AJAX/games.list.v2/index.php'
    rs = requests.post(url, headers=headers, data=form_data)
    if not rs.ok:
        need_logs and log.warning(f'Something went wrong...: status_code: {rs.status_code}\n{rs.text}')
        return []

    root = BeautifulSoup(rs.content, 'html.parser')

    for game_block in root.select('.gamebase_box'):
        title = get_norm_text(game_block.select_one('.release_name'))
        if not smart_comparing_names(title, game_name):
            continue

        genres = [get_norm_text(a) for a in game_block.select('.genre > a')]

        # Сойдет первый, совпадающий по имени, вариант
        genres = get_uniques(genres)

        need_logs and log.info(f'Genres: {genres}')
        return genres

    need_logs and log.info(f'Not found game {game_name!r}')
    return []


if __name__ == '__main__':
    from common import _common_test
    _common_test(get_game_genres)

    # Search 'Hellgate: London'...
    #     Genres: ['Боевик', 'Боевик от первого лица', 'Боевик от третьего лица', 'Ролевая игра']
    #
    # Search 'The Incredible Adventures of Van Helsing'...
    #     Genres: ['Ролевая игра', 'Боевик', 'Боевик от третьего лица']
    #
    # Search 'Dark Souls: Prepare to Die Edition'...
    #     Genres: []
    #
    # Search 'Twin Sector'...
    #     Genres: ['Боевик', 'Боевик от первого лица']
    #
    # Search 'Call of Cthulhu: Dark Corners of the Earth'...
    #     Genres: ['Боевик', 'Ужасы', 'Боевик от первого лица', 'Приключение']
