第一步  安装# pip install gradio_client
第二步  wav文件上传github
第三步  raw方式获取


from gradio_client import Client, handle_file

client = Client("https://s5k.cn/api/v1/studio/iic/SenseVoice/gradio/")
result = client.predict(
		input_wav=handle_file('https://github.com/OnePieceLwc/zxm86/raw/main/123.wav'),
		language="auto",
		api_name="/model_inference"
)
print(result)
