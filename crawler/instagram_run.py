from background_task import background
import os

@background(schedule=1)
def run_image_only(keyword, num, save):
    if not os.path.exists(save):
        os.makedirs(save)
    os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --maximum {} -d {}'.format(keyword, num, save))
    return 0

@background(schedule=1)
def run_meta(keyword, num, save):
    if not os.path.exists(save):
        os.makedirs(save)
    os.system('instagram-scraper -u yoojin.choi.dm -p dbwldchl312! {} --tag --maximum {} -d {} --media-metadata'.format(keyword, num, save))
    return 0