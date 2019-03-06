# pip install icrawler
from icrawler.builtin import GoogleImageCrawler
from background_task import background
import os
from datetime import date
import argparse


@background(schedule=1)
def google_crawler_real(save, keyword, max_num):      # save, keyword, max_num 값 사용자로부터 받을 예정

    if not os.path.exists(save):
        os.makedirs(save)

    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': save})
    
    for year in range(2018, 2018+1):
        for month in [1, 4, 7, 10]:
            filters = dict(
                size='large',
                type='photo',
                date=((year, month, 1), (year, month+2, 30)))

            google_crawler.crawl(keyword=keyword,           # config.target_class -> keyword
                                filters=filters,
                                max_num=max_num,            # config.max_num -> max_num
                                file_idx_offset='auto',
                                min_size=(512, 512))
        
        print('year: {}, month: {}~{} finished..!'.format(year, month, month+2))

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