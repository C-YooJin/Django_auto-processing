from background_task import background
import os
from subprocess import call

@background(schedule=1)
def run_image_only(keyword, num, save):
    # num = int(num)
    if not os.path.exists(save):
        os.makedirs(save)
    #os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! ' + keyword + ' --tag --maximum ' + num + ' -d ' + save)
    os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --maximum {} -d {}'.format(keyword, num, save))
    # call('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --maximum {} -d {}'.format(keyword, num, save))

@background(schedule=1)
def run_meta(keyword, num, save):
    # num = int(num)
    if not os.path.exists(save):
        os.makedirs(save)
    #os.system(
    #    'instagram-scraper -u yoojin.choi.dm -p dbwldchl312! ' + keyword + ' --tag --maximum ' + num + ' -d ' + save + ' --media-metadata')
    #os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --media-types story-image --maximum {} -d {} --media-metadata'.format(keyword, num, save))
    call('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --media-types story-image --maximum {} -d {} --media-metadata'.format(keyword, num, save))


# 실행
#run_image_only('손글씨', 10000, '/Users/user/Downloads/Instagram_crawling/Image/sungrae/')
#run_meta('influencer brand', '80000', '/Users/user/Downloads/instagram_crawling/junhee/')