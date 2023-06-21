@echo off

rem 切换编码为utf-8
chcp 65001

rem 运行脚本
python C:\myprojects\enhance\一键联网.py


rem 终止浏览器驱动进程
rem taskkill /im chromedriver.exe /f
rem 终止谷歌浏览器进程
rem taskkill /im chrome.exe /f

