import os
import subprocess

def handler(event, context):
    # 安装依赖
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

    # 构建站点
    subprocess.check_call(['mkdocs', 'build'])

    # 返回成功响应
    return {
        'statusCode': 200,
        'body': 'Build successful'
    }
