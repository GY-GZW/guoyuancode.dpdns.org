import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def generate_sitemap():
    # 获取当前目录下所有html文件（包括子目录）
    html_files = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                # 标准化路径为URL格式（Unix风格）
                url_path = full_path.replace(os.sep, '/').lstrip('./')
                html_files.append(url_path)
    
    if not html_files:
        print("未找到任何HTML文件！")
        return
    
    # 创建XML结构
    urlset = Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for url_path in html_files:
        url = SubElement(urlset, 'url')
        loc = SubElement(url, 'loc')
        loc.text = f"https://gystu.top/{url_path}"  # 替换为你的域名
    
    # 生成格式化XML
    rough_xml = tostring(urlset, 'utf-8')
    dom = parseString(rough_xml)
    pretty_xml = dom.toprettyxml(indent="  ")
    
    # 写入文件
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"成功生成站点地图，包含 {len(html_files)} 个URL！")

if __name__ == '__main__':
    generate_sitemap()