from collections import OrderedDict
from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler
from six.moves.urllib.parse import urlparse
from background_task import background
# from .json_rm_dupe import json_rm
import base64
import os
import json

import multiprocessing as mp


mp.process

INDEX = 0
FINAL = {}

class MyImageDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        global INDEX

        # 여기부터는 파일명.jpg를 만들기 위한 코드
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                    'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext
        filename = base64.b64encode(url_path.encode()).decode()
        name = '{}.{}'.format(filename, extension)


        dictionary = {INDEX: {'file_url': task['file_url'], 'name': name}}
        INDEX += 1
        FINAL.update(dictionary)

        return '{}.{}'.format(filename, extension)


@background(schedule=1)
def get_json(keyword, save, num, save_dir):
    global FINAL
    if not os.path.exists(save):
        os.makedirs(save)

    number_of_idx = 0
    count = 0

    # 2010년 1월부터 크롤링
    years = 2019
    months = 1

    while number_of_idx < num:
        count += 1

        print("*************************************************")
        print('year: {}, month: {}~{} started..!'.format(years, months, months + 2))
        print("*************************************************")
        print("")

        #basenum = 500
        #if num > basenum:
        #    iteration = (num // 500) + 3
        #else:
        #    iteration = 2

        #for i in range(iteration):
        google_crawler = GoogleImageCrawler(
            downloader_cls=MyImageDownloader,
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': save})

        for year in range(years, years + 1):
            for month in [months]:
                filters = dict(
                    size='large',
                    type='photo',
                    date=((year, month, 1), (year, month + 2, 30)))

                if num <= 100:
                    max_num = 20
                elif num > 100 and num <= 1000:
                    max_num = 100
                else:
                    max_num = 700

                google_crawler.crawl(keyword=keyword,
                                     filters=filters,
                                     max_num=max_num)#num)

        with open(save+'/{}.json'.format(save_dir), 'w', encoding="utf-8") as make_file:
            json.dump(FINAL, make_file, ensure_ascii=False, indent="\t")

        # 여기다가 중복 제거 기능 넣고
        # json_rm(save+'/{}.json'.format(save_dir))
        class_idx_path = save+'/{}.json'.format(save_dir)
        json_data = open(class_idx_path).read()
        json_data = json.loads(json_data)
        # print(json_data)

        dictlist = []

        for key, value in json_data.items():
            temp = [key, value]     # 원래도 list인데 이중 list로 처리해줌
            dictlist.append(temp)

        new = []
        for i in range(0, len(json_data)):
            for j in range(i + 1, len(json_data)):
                if dictlist[i][1] == dictlist[j][1]:
                    new.append(j)

        # print('중복제거 전{}: {}'.format(count, len(new)))
        # print('중복제거{}: {}'.format(count, len(set(new))))
        new = set(new)

        new2 = []

        for i in range(0, len(json_data)):
            if i not in new:
                new2.append(i)

        newdict2 = {}

        for i in range(len(new2)):
            newdict2.update({i: dictlist[i][1]})

        with open(save+'/{}.json'.format(save_dir), 'w', encoding="utf-8") as make_file:
            json.dump(newdict2, make_file, ensure_ascii=False, indent="\t")


        # number_of_idx값 구하기
        json_path = save+'/{}.json'.format(save_dir)
        json_data = open(json_path).read()
        json_data = json.loads(json_data)

        dictlist = []

        for key, value in json_data.items():
            temp = [key, value]  # 원래도 list인데 이중 list로 처리해줌
            dictlist.append(temp)

        print("")
        print("*************************************************")
        print('year: {}, month: {}~{} finished..!'.format(years, months, months + 2))
        print("*************************************************")
        print("")


        number_of_idx = len(dictlist)

        print(number_of_idx)

        # next year
        # repeat 1, 4, 7, 10 month
        if months == 10:
            years -= 1
            months = 1
        else:
            months += 3

# 실행
#get_json('love', '/Users/user/Downloads/get_json_test4/', 10000, 'like')