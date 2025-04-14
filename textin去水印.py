import requests
import json
import base64
import os

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

class CommonOcr(object):
    def __init__(self, img_path=None, is_url=False, output_folder="output_images"):

        self._url = 'https://api.textin.com/ai/service/v1/image/watermark_remove'
        # https://www.textin.com/document/watermark-remove
        self._app_id = '15b34431cb4829e78489e0d132102a40'  # 替换为你的x-ti-app-id
        self._secret_code = '6a3609d617ea3d1f924c002520e579ac'  # 替换为你的x-ti-secret-code
        self._img_path = img_path
        self._is_url = is_url
        self._output_folder = output_folder # 保存文件夹

    def recognize(self):
        head = {}
        try:
            head['x-ti-app-id'] = self._app_id
            head['x-ti-secret-code'] = self._secret_code
            if self._is_url:
                head['Content-Type'] = 'text/plain'
                body = self._img_path
            else:
                image = get_file_content(self._img_path)
                head['Content-Type'] = 'application/octet-stream'
                body = image

            result = requests.post(self._url, data=body, headers=head)
            result_json = json.loads(result.text)

            if "result" in result_json and "image" in result_json["result"]:
                base64_data = result_json["result"]["image"]
                # 构建输出文件路径，包含文件夹
                file_name = os.path.basename(self._img_path) # 获取文件名
                name, ext = os.path.splitext(file_name) # 分离文件名和扩展名
                output_path = os.path.join(self._output_folder, f"{name}_processed{ext}")
                self.save_image(base64_data, output_path)
                return output_path  # 返回保存的文件路径
            else:
                return result.text  # 返回原始 API 响应
        except Exception as e:
            return str(e) # 返回错误信息


    def save_image(self, base64_string, output_path):
        try:
            os.makedirs(self._output_folder, exist_ok=True) # 创建文件夹，如果不存在
            image_data = base64.b64decode(base64_string)
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"Image saved to {output_path}")
        except Exception as e:
            print(f"Error saving image: {e}")


if __name__ == "__main__":
    image_path = r"C:\\Users\\xiazhi\\Desktop\\14f8fae7bda8c73764171c98cd584ff.png"
    output_folder = "C:\\Users\\xiazhi\\Desktop"
    response = CommonOcr(img_path=image_path, output_folder=output_folder)
    response.recognize()

