espnet3

独立的 espnet3 框架。本项目基于 [ESPnet](https://espnet.github.io/espnet/)，旨在提供一个更轻量、更现代化的语音处理库。

## 简介

本项目从官方 ESPnet 仓库中提取了 `espnet3` 模块，并进行了独立打包。它移除了对旧版本代码的依赖，专注于提供简洁、高效的语音识别（ASR）、语音合成（TTS）等任务的训练和推理流程。

本项目内嵌了 espnet_model_zoo 的源代码以避免依赖冲突 。

## 安装

1.  克隆仓库：
    ```bash
    git clone https://github.com/jeffchen0325/espnet3.git
    cd espnet3
    ```

2.  安装依赖：to be updated later


## 🚀 快速开始

以下是一个简单的示例，展示如何运行一个基础的 ASR 实验：

```bash
cd espnet3/egs3/mini_an4/asr
python run.py \
    --stages train \
    --training_config conf/train.yaml
```
