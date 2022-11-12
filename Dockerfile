# 建立 python3.9 环境
FROM python:3.9

# 镜像作者
MAINTAINER Hella

# 更新依赖
RUN apt-get -y update

# 设置python环境变量
ENV PYTHONUNBUFFERED 1

# 在容器内创建mes文件夹
RUN mkdir -p /hellas

# 设置容器内工作目录
WORKDIR /hellas

# 将当前目录文件加入到容器工作目录中
ADD . /hellas

# 更新pip版本
RUN /usr/local/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/

# pip安装依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 安装supervisor
# RUN apt-get install supervisor

# 设置环境变量
ENV SPIDER=/hellas


RUN chmod +x ./start.sh