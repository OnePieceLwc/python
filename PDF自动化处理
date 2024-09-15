# PDF自动化处理
#  1.导入库：pip install PyPDF2 FPDF reportlab
import PyPDF2

# # 2.打开 PDF文件并提取输出文本内容
# with open('产品测试.pdf', 'rb') as file:
#     # 创建一个 PDF 阅读器对象
#     reader = PyPDF2.PdfReader(file)
#
#     # 获取 PDF 文件中的页数
#     num_pages = len(reader.pages)
#
#     # 逐页提取文本内容并打印
#     for page_num in range(num_pages):
#         page = reader.pages[page_num]
#         text = page.extract_text()
#         print(text)

# # 3.将PDF转为图像
# from pdf2image import convert_from_path
#
# def pdf_to_image(input_file, output_file):
#     images = convert_from_path(input_file)
#     for i, image in enumerate(images):
#         image.save(f'{output_file}_{i}.jpg', 'JPEG')
#
# pdf_to_image('input.pdf', 'output_image')

# 4.将PDF转为HTML
# from PyPDF2 import PdfReader
# def pdf_to_html(input_file, output_file):
#     with open(input_file, 'rb') as file:
#         reader = PdfReader(file)
#         text = ""
#         # 逐页提取文本内容
#         for page in reader.pages:
#             text += page.extract_text()
#         # 保存为HTML文件
#         with open(output_file, 'w') as html_file:
#             html_file.write(f"<html><body>{text}</body></html>")
#
# pdf_to_html('产品测试.pdf', '产品测试.html')

# # 5. 文本转为 纯文本
# from pdfminer.high_level import extract_text_to_fp
#
# def pdf_to_text(input_file, output_file):
#     with open(output_file, 'w') as text_file:
#         with open(input_file, 'rb') as file:
#             extract_text_to_fp(file, text_file)
#
# pdf_to_text('产品测试.pdf', 'output.txt')

# # 6.将PDF转为Word文档
# from docx import Document
# from PyPDF2 import PdfReader
#
# def pdf_to_word(input_file, output_file):
#     with open(input_file, 'rb') as file:
#         reader = PdfReader(file)
#         text = ""
#
#         # 逐页提取文本内容
#         for page in reader.pages:
#             text += page.extract_text()
#
#         # 创建Word文档
#         doc = Document()
#         doc.add_paragraph(text)
#
#         # 保存为Word文档
#         doc.save(output_file)
#
# pdf_to_word('input.pdf', 'output.docx')

# # 7. PDF 水印和签章
# from PyPDF2 import PdfReader, PdfWriter
# from reportlab.pdfgen import canvas
# import io
#
# # 添加水印到 PDF
# def add_watermark(input_file, output_file, watermark_text):
#     reader = PdfReader(input_file)
#     writer = PdfWriter()
#
#     watermark_buffer = io.BytesIO()
#
#     # 创建带有水印的 PDF
#     c = canvas.Canvas(watermark_buffer)
#     c.setFont("Helvetica", 48) # 注意字体的选择
#     c.rotate(45)
#     c.translate(-500, -500)
#     c.setFillAlpha(0.3)
#     c.drawString(400, 400, watermark_text)
#     c.save()
#
#     watermark_buffer.seek(0)
#     watermark_pdf = PdfReader(watermark_buffer)
#
#     # 遍历每个页面
#     for i, page in enumerate(reader.pages, start=1):
#         watermark_page = watermark_pdf.pages[0]
#
#         # 添加水印到页面
#         page.merge_page(watermark_page)
#         writer.add_page(page)
#
#     # 保存带水印的文件
#     with open(output_file, 'wb') as file:
#         writer.write(file)
#
# # 添加数字签章到 PDF
# def add_signature(input_file, output_file, signature_image):
#     reader = PdfReader(input_file)
#     writer = PdfWriter()
#
#     # 遍历每个页面
#     for i, page in enumerate(reader.pages, start=1):
#         # 在页面右下角添加签章图像
#         page.merge_page(signature_image)
#         writer.add_page(page)
#
#     # 保存带签章的文件
#     with open(output_file, 'wb') as file:
#         writer.write(file)
#
# # 使用 add_watermark() 和 add_signature() 函数添加水印和签章
# watermark_text = "机密文件，请勿泄露"
# signature_image = PdfReader("signature.pdf").pages[0]
#
# add_watermark('part_21-30.pdf', 'document_with_watermark.pdf', watermark_text)
# add_signature('document_with_watermark.pdf', 'document_with_watermark_and_signature.pdf', signature_image)
#
# print("水印和签章魔法完成！你现在可以让 PDF 文件更安全更专业了！")


# # 8. PDF 表格生成器
# import matplotlib.pyplot as plt
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Table, Image
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.platypus import Paragraph, Spacer
#
# # 创建报表内容
# def create_report(output_file, data):
#     # 创建 PDF 文档对象
#     doc = SimpleDocTemplate(output_file, pagesize=A4)
#
#     # 加载样式表
#     styles = getSampleStyleSheet()
#
#     # 创建报表内容元素
#     elements = []
#
#     # 添加标题
#     title = Paragraph("销售报表", styles["Title"])
#     elements.append(title)
#     elements.append(Spacer(1, 20))
#
#     # 添加表格
#     table_data = data
#     table = Table(table_data)
#     elements.append(table)
#     elements.append(Spacer(1, 20))
#
#     # 生成图表并保存为 PNG 图片
#     plt.plot(data[1][1:], marker='o')
#     plt.xlabel("日期")
#     plt.ylabel("销售额")
#     plt.title("销售趋势图")
#     plt.savefig("sales_plot.png")
#     plt.close()
#
#     # 添加图表到报表内容
#     image = Image("sales_plot.png", width=400, height=300)
#     elements.append(image)
#
#     # 生成报表
#     doc.build(elements)
#
# # 创建报表数据
# report_data = [
#     ["日期", "销售额"],
#     ["1/1", 100],
#     ["1/2", 200],
#     ["1/3", 150],
#     ["1/4", 300],
# ]
#
# # 生成报表
# create_report('sales_report.pdf', report_data)
#
# print("报表生成完成！现在您可以查看生成的报表文件。")

# #  9.OCR（光学字符识别）
# import pdf2image
# import pytesseract
# 
# 
# # 将 PDF 转为图像
# def pdf_to_image(input_file):
#     images = pdf2image.convert_from_path(input_file)
#     return images
# 
# 
# # 使用 OCR 将图像转为文本
# def image_to_text(image):
#     text = pytesseract.image_to_string(image)
#     return text
# 
# 
# # 将文本保存到文件
# def save_text_to_file(text, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write(text)
# 
# 
# # 从 PDF 提取文本
# def extract_text_from_pdf(input_file, output_file):
#     # 将 PDF 转为图像
#     images = pdf_to_image(input_file)
# 
#     extracted_text = ""
# 
#     # 提取每个图像中的文本
#     for image in images:
#         text = image_to_text(image)
#         extracted_text += text + "\n"
# 
#     # 将提取的文本保存到文件
#     save_text_to_file(extracted_text, output_file)
# 
# 
# # 从扫描的 PDF 中提取文本
# extract_text_from_pdf('C:\\Users\\lx\\Desktop\\刘文昌产品测试.pdf', 'C:\\Users\\lx\\Desktop\\output.txt')
# 
# print("OCR（光学字符识别）魔法完成！现在你可以将扫描的 PDF 文档转换为可编辑的文本了！")
