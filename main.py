#I am a script boy, add me to wechat, note to the group: TVZMV1kyVEJJNUxIS1laU0taVkE9PT09
import argparse
import os
import pandas as pd
from docx import Document

# 创建命令行参数解析器
print('''
 \033[31m  ____                              _ _            \033[0m
 \033[31m | __ ) _   _  __ _  __      ___ __(_| |_ ___ _ __ \033[0m
 \033[31m |  _ \| | | |/ _` | \ \ /\ / | '__| | __/ _ | '__|\033[0m     
 \033[31m | |_) | |_| | (_| |  \ V  V /| |  | | ||  __| |   \033[0m     Look: \033[33m公众号—燕云实验室 \033[0m
 \033[31m |____/ \__,_|\__, |   \_/\_/ |_|  |_|\__\___|_|   \033[0m     Version: \033[33m公测版本 \033[0m
 \033[31m              |___/\033[0m                                     Tools: \033[33m漏洞报告辅助工具By-逸尘\033[0m      
            \033[34mgithub.com/yichensec/Bug_writer\033[0m     

一款面向用于安服，渗透测试人员，网络安全从业者等人群的漏洞报告辅助工具可以生成漏洞测试简报，可自己私人定制。
注：未来版本优先用于团队成员与交流群内部分享，公开时间随缘。''')
print('''\033[33m================================== 渗透漏洞报告书写员的开始 =========================================\033[0m''')
class VulReportGenerator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='\033[33m漏洞报告生成器\033[0m')
        self.df = pd.read_excel('./config/WEB.xlsx')

    def parse_args(self):
        self.parser.add_argument('-c', type=str, help='指定模糊查询漏洞名称.')
        self.parser.add_argument('-t', action="store_true", help='指定生成漏洞报告')
        self.parser.add_argument('-list', action='store_true', help='列出漏洞名称')
        self.parser.add_argument('-p', type=int, default=5, help='指定页面数量')
        self.parser.add_argument('-s', type=int, default=10, help='指定每页显示的项目数')
        self.args = self.parser.parse_args()

    def run(self):
        self.parse_args()

        if self.args.list:
            self.list_vul_names()
        elif self.args.c:
            self.search_vuls()
        else:
            print('\033[31m<<无效的参数--您可以输入"-h"查看使用说明>>\033[0m')

    def search_vuls(self):
        search_name = self.args.c.lower()
        result = self.df[self.df['漏洞名称'].str.lower().str.contains(search_name)]
        result_count = result.count()[0]

        if result.empty:
            print('\033[31m<<这里并没有发现结果--您可以去查看是否输入错误>>\033[0m')
        else:
            print(f'\033[31m查询到 {result_count} 条记录：\033[0m')

            total_count = result_count
            page_count = self.args.p
            rows_per_page = self.args.s
            current_page = 1
            while True:
                page_result = result[(current_page-1) * rows_per_page : current_page * rows_per_page]
                if page_result.empty:
                    break

                print(f'\033[0m\033[33m第{current_page}页:\033[0m')
                for row in page_result.itertuples(index=False):
                    print('\033[0m\033[33m漏洞名称:\033[0m\033[32m  {}\n\033[0m\033[33m风险级别:\033[0m\033[31m  {}\033[0m\n\033[33m漏洞描述:\033[0m  \n\t\033[34m  {}\033[0m\n\033[33m加固建议:\033[0m\033[35m \n\t {}\033[0m\n\n\033[33m=====================================================================================\033[0m\n'.format(row.漏洞名称, row.风险级别, row.漏洞描述, row.加固建议))

                if self.args.t:
                    self.generate_report(page_result)

                current_page += 1
                if current_page > page_count:
                    break

    def list_vul_names(self):
        ld_names = self.df['漏洞名称']
        if not ld_names.empty:
            for index, ld_name in enumerate(ld_names):
                page_num = (index + 1) // self.args.s + 1
                if index % self.args.s == 0:
                    print(f'\033[0m\033[33m第{page_num}页:\033[0m')
                print(f'{ld_name}\t', end='')
                if (index + 1) % self.args.s == 0:
                    print()

            print()
        else:
            print('\033[31m<<这里并没有发现结果--您可以去查看是否输入错误>>\033[0m')

    def generate_report(self, page_result):
        doc_path = './config/web.docx'
        if os.path.exists(doc_path):
            doc_output_path = './output/001.docx'
            counter = 1
            while os.path.exists(doc_output_path):
                counter += 1
                doc_output_path = f'./output/{counter:03}.docx'

            doc = Document(doc_path)
            for index, row in page_result.iterrows():
                for para in doc.paragraphs:
                    if '%S1' in para.text:
                        para.text = para.text.replace('%S1', row['漏洞名称'])
                    if '%S2' in para.text:
                        para.text = para.text.replace('%S2', row['风险级别'])
                    if '%S3' in para.text:
                        para.text = para.text.replace('%S3', row['漏洞描述'])
                    if '%S4' in para.text:
                        para.text = para.text.replace('%S4', row['加固建议'])
            try:
                doc.save(doc_output_path)
                print(f'\033[33m已将查询结果写入到" {doc_output_path} "文件中\033[0m')
            except Exception as e:
                print(f'\033[31m写入文件"{doc_output_path}"时出错：{e}\033[0m')
        else:
            print(f'\033[31m指定的文件"{doc_path}"不存在\033[0m')
if __name__ == '__main__':
    generator = VulReportGenerator()
    generator.run()