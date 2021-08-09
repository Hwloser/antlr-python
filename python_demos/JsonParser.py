import json


def main():
    data = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    jsonStr = json.dumps(data)
    print("Python 原始字符串:", repr(data))
    print("Json 对象：", jsonStr)

    restoreJsonObject = json.loads(jsonStr)
    print("restore json 对象：", repr(restoreJsonObject))


if __name__ == "__main__":
    main()
