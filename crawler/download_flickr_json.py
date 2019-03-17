# pip install flickrapi
import flickrapi
import urllib.request
import os
import json
from collections import OrderedDict
from datetime import datetime
from background_task import background

@background(schedule=1)
def flickr_json(keyword, save, num, save_dir):
    # license dict
    license = {
        "cc-by-nc-sa": {
            "id": 1, "name": "Attribution-NonCommercial-ShareAlike License (CC BY-NC-SA)",
            "url": "https://creativecommons.org/licenses/by-nc-sa/2.0/"},
        "cc-by-nc": {
            "id": 2, "name": "Attribution-NonCommercial License (CC BY-NC)",
            "url": "https://creativecommons.org/licenses/by-nc/2.0/"},
        "cc-by": {
            "id": 4, "name": "Attribution License (CC BY)",
            "url": "https://creativecommons.org/licenses/by/2.0/"},
        "cc-by-sa": {
            "id": 5, "name": "Attribution-ShareAlike License (CC BY-SA)",
            "url": "https://creativecommons.org/licenses/by-sa/2.0/"},
        "cc0": {
            "id": 9, "name": "Public Domain Dedication (CC0)",
            "url": "https://creativecommons.org/publicdomain/zero/1.0/"},
        "public": {
            "id": 10, "name": "Public Domain Mark",
            "url": "https://creativecommons.org/publicdomain/mark/1.0/"}}

    # flickr api key
    flickr = flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

    # For information about arguments, see https://www.flickr.com/services/api/flickr.photos.search.html
    min_upload_date = '2000-1-1'
    max_upload_date = str(datetime.now())       # 현재 시간까지
    url_type = 'o'  # (1) 수정포인트: 고화질 -> 범위 확장 필요함
    max_title_len = 30

    # license test
    license_type = 'cc-by-sa'
    license_id = license[license_type]['id']
    license_name = license[license_type]['name']
    license_url = license[license_type]['url']
    print('License name: {}'.format(license_name))
    print('License url: {}'.format(license_url))

    # per_page는 가만히 두고, pages 수정

    photo_loader = flickr.walk(
        text=keyword,
        # tags=tag,
        # tag_mode='all',
        extras='description, owner_name, date_upload, url_{}'.format(url_type),
        sort='relevance',
        content_type=1,  # photos only
        min_upload_date=min_upload_date,  # 위에
        max_upload_date=max_upload_date,  # 위에
        license=license_id,
        pages= num + 20,
        per_page=500,  # 500 is maximum
        safe_search=1)

    photos = OrderedDict()
    photo_idx = 0
    # crawl photo urls and metadata
    for i, photo in enumerate(photo_loader):
        url = photo.get('url_{}'.format(url_type))
        title = photo.get('title').lower()
        if (url is not None) and len(title) < max_title_len:
            photos[photo_idx] = OrderedDict()

            # metadata
            photos[photo_idx]['photo_url'] = url
            photos[photo_idx]['photo_title'] = photo.get('title')
            photos[photo_idx]['author'] = photo.get('ownername')

            time_stamp = int(photo.get('dateupload'))
            date = datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d')
            photos[photo_idx]['date_uploaded'] = date

            # pixel size
            height = int(photo.get('height_{}'.format(url_type)))
            width = int(photo.get('width_{}'.format(url_type)))
            photos[photo_idx]['pixel_size'] = [height, width]

            # license info
            photos[photo_idx]['license'] = license_name
            photos[photo_idx]['license_url'] = license_url

            photo_idx += 1

        if (i + 1) % 100 == 0:
            print('Iterations: {}, Number of photos: {}'.format(i + 1, photo_idx))  # enumerate에 의해

        # comment out the below lines for real usage
        # if (i + 1) > num_fix:
        #     break

        if num < 500:
            num_fix = num + 100
        elif num >= 500 and num < 1000:
            num_fix = num + 200
        elif num >= 1000 and num < 10000:
            num_fix = num + 1000
        elif num > 10000:
            num_fix = num + 3000


        if photo_idx > num_fix:
            break

            # Write JSON
    if not os.path.exists(save):
        os.makedirs(save)
    with open(save + '/{}.json'.format(save_dir), 'w', encoding="utf-8") as make_file:
        json.dump(photos, make_file, ensure_ascii=False, indent="\t")


# 실행
#if __name__ == "__main__":
#   flickr_json('tiger', '/Users/user/Downloads/Flick_test', 1000, 'test')
