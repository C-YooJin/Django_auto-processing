# pip install icrawler
from icrawler.builtin import GoogleImageCrawler
from background_task import background
import os
from datetime import date
import argparse


@background(schedule=1)
def google_crawler_real(save, keyword, num):      # save, keyword, max_num 값 사용자로부터 받을 예정

    if not os.path.exists(save):
        os.makedirs(save)

    # 현재 크롤링 된 데이터 수
    num_of_data = next(os.walk(save))[2]  # dir is your directory path as string

    # 2010년 1월부터 크롤링
    year = 2010
    month = 1

    while len(num_of_data) < num:

        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': save})

        for year in range(2018, 2018+1):
            # for month in month_lst:
            # for month in [1, 4, 7, 10]:
            filters = dict(
                size='large',
                type='photo',
                license='noncommercial,modify',           # license
                date=((year, 1, 1), (year, 12, 30)))

        # directory에 저장된 파일 수
        num_of_data = next(os.walk(save))[2]

        # next year
        year += 1

        # repeat 1, 4, 7, 10 month
        if month == 10:
            month = 1
        else:
            month += 3

            google_crawler.crawl(keyword=keyword,           # config.target_class -> keyword
                                filters=filters,
                                max_num=1000,            # config.max_num -> max_num
                                file_idx_offset='auto',
                                min_size=(512, 512))

            print('year: {}, month: {}~{} finished..!'.format(year, 1, 12))


# directory 파일 개수 확인 후 num과 비교해서 NUm보다 작으면 while문 돌리기.

'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='/Users/user/Documents/document/test', help='directory where images are downloaded')
    # parser.add_argument('--target_class', type=str, default='dog', help='keyword to crawl images from google')
    # parser.add_argument('--max_num', type=int, default=10, help='maximum number of images to download')
    
    config = parser.parse_args()
    print(config)
    google_crawler_real(config)
'''