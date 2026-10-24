@echo off
chcp 65001 >nul
title Scrcpy 新拟态远控助手 - 单窗口 EXE 打包脚本
echo =====================================================================
echo   Scrcpy 新拟态远控助手 v3.2 — 单窗口独立 EXE 重新打包脚本
echo =====================================================================
echo.
echo [提示] 目录中已包含可直接双击运行的 ScrcpyNeumorphicStudio.exe！
echo 若您修改了界面或源码，可通过本脚本使用 PyInstaller 重新生成 EXE：
echo.
pip install pyinstaller --quiet
pyinstaller --noconfirm --onefile --windowed ^
    --name "ScrcpyNeumorphicStudio" ^
    --add-data "scrcpy_neumorphic_app.hta;." ^
    main.py
echo.
echo 打包完成！输出路径: dist\ScrcpyNeumorphicStudio.exe
pause
