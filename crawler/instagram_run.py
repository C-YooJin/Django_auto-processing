from background_task import background
import os
import subprocess

@background(schedule=1)
def run_image_only(keyword, num, save):
    num = int(num)
    if not os.path.exists(save):
        os.makedirs(save)
    os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --maximum {} -d "{}"'.format(keyword, num, save))

@background(schedule=1)
def run_meta(keyword, num, save):
    num = int(num)
    if not os.path.exists(save):
        os.makedirs(save)
    os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --media-types story-image --maximum {} -d "{}" --media-metadata'.format(keyword, num, save))



# 실행
#run_image_only('1000일 2000일', '10', '/Users/user/Downloads/insta_meta_test2/')
#run_meta('tiger birthday dog rabbit mother', '10', '/Users/user/Downloads/insta_meta_test/')