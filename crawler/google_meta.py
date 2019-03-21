from collections import OrderedDict
from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler
from six.moves.urllib.parse import urlparse
from background_task import background
import base64
import os
import json

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
        # FINAL[INDEX]['file_url'].append(task['file_url'])
        # FINAL[INDEX]['name'].append(name)
        print(FINAL)

        '''
        dictionary = {{'file_url': task['file_url'], 'name': name}}
        print(name)
        print(dictionary)
        # INDEX += 1
        FINAL.update(dictionary)
        '''
        return '{}.{}'.format(filename, extension)


@background(schedule=1)
def get_json(keyword, save, num, save_dir):
    global FINAL
    if not os.path.exists(save):
        os.makedirs(save)

    basenum = 500
    if num > basenum:
        iteration = (num // 500) +1
    else:
        iteration =1

    for i in range(iteration):
        google_crawler = GoogleImageCrawler(
            downloader_cls=MyImageDownloader,
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': save})

        google_crawler.crawl(keyword=keyword, max_num=num)#500)

    with open(save+'/{}.json'.format(save_dir), 'w', encoding="utf-8") as make_file:
        json.dump(FINAL, make_file, ensure_ascii=False, indent="\t")

# 실행
#if __name__ == '__main__':
#    get_json('sugar glider', '/Users/user/Downloads/Google_crawler/meta/', 10, 'result')