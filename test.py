import requests
from urllib.parse import urlparse


def get_webpage_info(url):
    """获取网页信息并以更结构化的方式展示"""
    # 确保URL包含协议
    if not url.startswith('http'):
        url = 'https://' + url

    try:
        # 添加User-Agent头以模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 如果请求失败则抛出异常

        # 尝试检测编码
        response.encoding = response.apparent_encoding

        # 获取网页标题 (简单方法)
        title = None
        if '<title>' in response.text and '</title>' in response.text:
            title_start = response.text.find('<title>') + 7
            title_end = response.text.find('</title>', title_start)
            title = response.text[title_start:title_end].strip()

        # 获取域名信息
        domain = urlparse(url).netloc

        # 打印信息
        print(f"网站域名: {domain}")
        print(f"网页标题: {title}")
        print(f"响应状态: {response.status_code}")
        print(f"内容类型: {response.headers.get('Content-Type', '未知')}")
        print(f"内容长度: {len(response.text)} 字符")

        # 打印内容预览
        content_preview = response.text[:200] + '...' if len(response.text) > 200 else response.text
        print("\n内容预览:")
        print(content_preview)

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


# 测试代码
if __name__ == "__main__":
    url = input("请输入要访问的网址: ")
    get_webpage_info(url)