import json

import cv2
import requests
LIMIT_PX = 1024
LIMIT_BYTE = 1024*1024  # 1MB
LIMIT_BOX = 40


def kakao_ocr_resize(image_path: str):

    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        cv2.imwrite(image_path, image)

        return image_path
    return None


def kakao_ocr(image_path: str, appkey: str):
    """
    OCR api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()


    return requests.post(API_URL, headers=headers, files={"image": data})


def main():
    
    image_path = '/Users/baeksujin/Desktop/allergy/samdasu/backend/gfg.png'
    app_key = '25c2569db9057649e482e1ba35a1f3a6'

    resize_impath = kakao_ocr_resize(image_path)


    if resize_impath is not None:
        image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")
    
    output = kakao_ocr(image_path, app_key).json()
    print(output.keys())
    print(len(output['result']))
    words = ''
    for i in range(0,len(output['result'])):
        print(output['result'][i])
        print(output['result'][i]['recognition_words'])
        print(type(output['result'][i]['recognition_words'][0]))
        words = words+output['result'][i]['recognition_words'][0]

    print(words)

    # print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2,ensure_ascii=False)))


if __name__ == "__main__":
    main()