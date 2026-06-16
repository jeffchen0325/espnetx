espnetx

独立的 ESPnet3 框架。本项目基于 [ESPnet](https://espnet.github.io/espnet/)，旨在提供一个更轻量、更现代化的语音处理库。

## 简介

本项目从官方 ESPnet 仓库中提取了 `egs3`和`espnet3` 模块，并进行了独立打包。它移除了对旧版本代码的依赖，专注于提供简洁、高效的语音识别（ASR）、语音合成（TTS）等任务的训练和推理流程。

本项目准备内嵌 espnet_model_zoo 和 espnet-tts-frontend 简洁包依赖（ongoing） 。

## 安装

1.  （可选）如果是windows系统，安装 WSL2 + Ubuntu-22.04

    管理员身份打开PowerShell，启用虚拟机平台和WSL功能：
    ```bash
    $ dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    $ dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```
    安装成功后重启电脑，再次以管理员身份打开PS，输入：
    ```bash
    $ wsl --install						    # 安装最新版本WSL
    $ wsl --list --online					# 列出可用的发行版版本
    $ wsl --install -d Ubuntu-22.04 --location D:\WSL\Ubuntu-22.04		# 下载安装注册启动
    ```
    在 Windows 用户目录（C:\Users\<用户名>）下创建 .wslconfig 文件，添加网络配置（让WSL也可以用windows的代理）：
    ```bash
    [wsl2]
    networkingMode=mirrored
    dnsTunneling=true
    autoProxy=true
    ```
    关掉wsl再重启即生效

2.  Ubuntu环境安装

    (可选)建议在Ubuntu环境安装ffmpeg cmake sox flac
    ```bash
    $ sudo apt update 
    $ sudo apt install -y ffmpeg cmake sox flac
    $ cmake --version && sox --version && flac –version
    ```
    安装miniconda
    ```bash
    $ cd ~ 
    $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    $ bash Miniconda3-latest-Linux-x86_64.sh
    $ source ~/.bashrc
    ```
3.  conda激活虚拟环境

    创建虚拟环境并激活
    ```bash
    $ conda create -n espnet python=3.10
    $ conda activate espnet
    $ conda install -c conda-forge uv -y    # 安装 uv 用于后续包安装
    ```
    安装torch+cuda（选取合适的pytorch+cuda版本， 例如5060ti至少cuda12.8支持sm120）
    ```bash
    $ uv pip install torch==2.9.1 torchaudio==2.9.1 --index-url https://download.pytorch.org/whl/cu128
    ```
4.  安装ESPnet3

    克隆仓库：
    ```bash
    $ cd ~
    $ git clone https://github.com/jeffchen0325/espnet3.git
    ```
    安装ESPnet3
    ```bash
    $ cd <ESPnet3-root>
    $ uv pip install -e .[all]    
    ```
    检查ESPnet版本
    ```bash
    $ uv pip show espnet3
    ```
    或
    ```bash
    $ cd <ESPnet3-root>/tools
    $ python3 check_install.py
    ```

## 🚀 快速开始

以下是一个简单的示例，展示如何运行一个基础的 ASR 实验：
```bash
$ bash ~/espnet3/tools/installers/install_warp-transducer.sh    # ASR模型依赖
$ cd espnet3/egs3/mini_an4/asr
$ python3 run.py dry_run=True
```
