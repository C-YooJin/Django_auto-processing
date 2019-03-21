from icrawler.builtin import GoogleImageCrawler
from background_task import background
from .filter_images import filter
import os
import base64

@background(schedule=1)
def google_crawler_real(save, keyword, num, save_dir):      # save, keyword, max_num 값 사용자로부터 받을 예정

    if not os.path.exists(save):
        os.makedirs(save)

    #save_dir = {이름_사번_keyword}

    # 현재 크롤링 된 데이터 수
    num_of_data = next(os.walk(save))[2]  # dir is your directory path as string

    # 2010년 1월부터 크롤링
    years = 2019
    months = 1

    while len(num_of_data) < num:

        print("*************************************************")
        print('year: {}, month: {}~{} started..!'.format(years, months, months + 2))
        print("*************************************************")
        print("")

        google_crawler = GoogleImageCrawler(
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
                    max_num = 1000

                google_crawler.crawl(keyword=keyword,
                                     filters=filters,
                                     max_num=max_num,               # defalut값인 1000이 들어가면 100개만 다운 받고 싶을 때,
                                     file_idx_offset='auto',        # 100 언저리에서 멈추지 않고 거의 1000가까이 크롤링 됨
                                     min_size=(512, 512))

        # directory에 저장된 파일 수
        num_of_data = next(os.walk(save))[2]

        print("")
        print("*************************************************")
        print('year: {}, month: {}~{} finished..!'.format(years, months, months + 2))
        print("*************************************************")
        print("")

        # next year
        # repeat 1, 4, 7, 10 month
        if months == 10:
            years -= 1
            months = 1
        else:
            months += 3

    # 이미지 클리너
    os.system('image-cleaner /Users/user/Downloads/Google_crawling/unfiltered/'+save_dir)
    # 이미지 중복 제거 (fdupes (md5sum))
    os.system('fdupes -d -N -r /Users/user/Downloads/Google_crawling/unfiltered/'+save_dir)

    # 만약에 keyword가 json파일 value값으로 있으면 돌려야됨. 안 그러면 오류남.
    # dir 수정

    # keyword_fix = keyword.replace(' ', '_')

    try:
        filter(keyword, save_dir)
    except KeyError:
        print('your keyword is not in imagenet class index!')
        f = open('/Users/user/Downloads/Google_crawling/filtered/'+save_dir+'/imagenet class에 없는 키워드라 필터링이 불가합니다.txt', 'w')
        f.close

    print("Crawling is complete!")

# directory 파일 개수 확인 후 num과 비교해서 NUm보다 작으면 while loop.

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