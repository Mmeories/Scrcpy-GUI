#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrcpy 新拟态远控助手 — 单窗口独立桌面版 (Native Windows Host)
支持直接调用本地 adb.exe 与 scrcpy.exe 执行真实设备扫描、参数配置、投屏、录屏与按键控制。
"""
import os
import sys
import subprocess
import shutil


def get_resource_path(rel_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), rel_path)


def main():
    hta_path = get_resource_path("scrcpy_neumorphic_app.hta")
    # Launch via Windows native mshta.exe so WScript.Shell ActiveX can directly run adb.exe & scrcpy.exe
    mshta_bin = shutil.which("mshta") or r"C:\Windows\System32\mshta.exe"
    if os.path.exists(mshta_bin):
        subprocess.Popen([mshta_bin, hta_path])
        return

    # Fallback to Edge App mode (465x820 compact single window)
    for b in ["msedge", "chrome"]:
        bp = shutil.which(b)
        if bp:
            subprocess.Popen([bp, f"--app=file:///{hta_path.replace(os.sep, '/')}", "--window-size=465,820"])
            return


if __name__ == "__main__":
    main()
