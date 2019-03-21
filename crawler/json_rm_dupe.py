import json

def json_rm(path):
    # class_idx_path = '/Users/user/Downloads/Google_crawling/meta/구글메타_만개테스트_pug/구글메타_만개테스트_pug.json'
    class_idx_path = path
    json_data = open(class_idx_path).read()
    json_data = json.loads(json_data)
    # print(json_data)

    temp = []
    dictlist = []

    for key, value in json_data.items():
        temp = [key, value]  # 원래도 list인데 이중 list로 처리해줌
        dictlist.append(temp)

    new = []
    for i in range(0, len(json_data)):
        for j in range(i + 1, len(json_data)):
            if dictlist[i][1] == dictlist[j][1]:
                new.append(j)

    print('중복제거 전: {}'.format(len(new)))
    print('중복제거: {}'.format(len(set(new))))
    new = set(new)

    new2 = []

    for i in range(0, len(json_data)):
        if i not in new:
            new2.append(i)

    newdict2 = {}

    for i in range(len(new2)):
        newdict2.update({i: dictlist[i][1]})

    print(newdict2)

    with open(path, 'w', encoding="utf-8") as make_file:
        json.dump(newdict2, make_file, ensure_ascii=False, indent="\t")

    return path


# 실행
# json_rm_dupe('/Users/user/Downloads/Google_crawling/meta/구글메타_만개테스트_pug/구글메타_만개테스트_pug.json')
