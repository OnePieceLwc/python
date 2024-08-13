# DrissionPage 是一个基于 python 的网页自动化工具。  DrissionPage官方的文档：https://www.drissionpage.cn/
# 可兼顾浏览器自动化的便利性和 requests 的高效率。它功能强大，内置无数人性化设计和便捷功能。它的语法简洁而优雅，代码量少，对新手友好。

# page = SessionPage() / WebPage() / ChromiumPage()
#   ChromiumPage：单纯用于操作浏览器的页面对象  登录
#   WebPage：整合浏览器控制和收发数据包于一体的页面对象  页面分析  d 模式和 s 模式
#             d 模式用于控制浏览器，不仅可以读取浏览器获取到的信息，还能对页面进行操作，如点击、填写、开关标签页、改变元素属性、执行 js 脚本等等。
#             d 模式功能强大，但运行速度受浏览器制约非常缓慢，而且需要占用大量内存。
#             s 模式的运行速度比 d 模式快几个数量级，但只能基于数据包进行读取或发送，不能对页面进行操作，不能运行 js。
#             爬取数据时，如网站数据包较为简单，应首选 s 模式。
#   SessionPage：单纯用于收发数据包的页面对象  爬取  不会跳出

# page.change_mode()  切换到收发数据包模式 切换的时候程序会在新模式重新访问当前 url  有验证码和页面数据由 js 产生先d后s

# page.get(f'url')  跳转url
# page.ele('a***')  # 定位元素
# #表示按id属性查找元素 @表示按属性名查找 .表示按class属性查找元素  t:字的大小，例如t:h3 tag:a 获取其子元素中所有 a 元素
# ele.input('您的密码')  # 输入文本
# ele.click()  # 点击元素
# page.eles('t:button@tx():')  搜索表示选择一个类型为按钮的元素，且其文本内容为搜索
# page.s_eles 更快的获取元素
# s_eles()与eles()的区别在于前者会把整个页面或动态元素转变成一个静态元素，再在其中获取下级元素或信息。因为静态元素是纯文本的，没有各种属性、交互等消耗资源的部分，所以运行速度非常快。
# ele.next()  # 获取后一个元素
# ele.prev(index=2)  # 获取前面第二个元素
# page.quit() 关闭

# from TimePinner import Pinner  # 导入计时工具
# pinner = Pinner()  # 创建计时器对象
# pinner.pin()  # 标记开始记录
# pinner.pin('用时')  # 记录并打印时间

from DrissionPage import ChromiumPage

# ##操控浏览器
#
# 导入库
# from DrissionPage import ChromiumPage
#
# # 创建页面对象，并启动或接管浏览器
# page = ChromiumPage()
# # 跳转到登录页面
# page.get('https://gitee.com/login')
#
# # 定位到账号文本框，获取文本框元素
# ele = page.ele('#user_login')   # #表示按id属性查找元素
# # 输入对文本框输入账号
# ele.input('您的账号')
# # 定位到密码文本框并输入密码
# page.ele('#user_password').input('您的密码')
# # 点击登录按钮
# page.ele('@value=登 录').click()  # @表示按属性名查找
#
#
# ## 爬取
# # 收发数据包
#
# from DrissionPage import SessionPage
#
# # 创建页面对象
# page = SessionPage()
#
# # 爬取3页
# for i in range(1, 4):
#     # 访问某一页的网页
#     page.get(f'https://gitee.com/explore/all?page={i}')
#     # 获取所有开源库<a>元素列表
#     links = page.eles('.title project-namespace-path')
#     # 遍历所有<a>元素
#     for link in links:
#         # 打印链接信息
#         print(link.text, link.link)
#
# # 页面分析
#
# from DrissionPage import WebPage
#
# # 创建页面对象
# page = WebPage()
# # 访问网址
# page.get('https://gitee.com/explore/all')
# # 切换到收发数据包模式
# page.change_mode()
# # 获取所有行元素
# items = page.ele('.ui relaxed divided items explore-repo__list').eles('.item')
# # 遍历获取到的元素
# for item in items:
#     # 打印元素文本
#     print(item('t:h3').text)
#     print(item('.project-desc mb-1').text)
#     print()
