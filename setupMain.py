# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service

import os
import subprocess
import pytest

from bin.script.logs import LogConfig
from bin.script.writeCase import write_case

# 取绝对路径
PATH = os.path.split(os.path.realpath(__file__))[0]
xml_report_path = PATH + "/aff/report/xml"
html_report_path = PATH + "/aff/report/html"
har_path = PATH + "/aff/data"


def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o


if __name__ == '__main__':
    # 程序日志输出到根目录的log文件夹下，会有两个日志文件，分别为info，error！
    LogConfig(PATH)
    write_case(har_path)
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)
    invoke(cmd)

