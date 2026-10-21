# Codex 大肥鱼桌宠｜codexの大肥鱼替身 🐟

**简体中文** · [English](README.en.md) · [日本語](README.ja.md)

**Codex 大肥鱼**是一个 macOS Codex 桌宠项目，包含可在 Codex 官方 Pets 中选择的大肥鱼宠物，以及一个连接 Codex 插件的独立悬浮桌面应用。两种方式可按喜好使用。

大肥鱼的角色设定、主视觉图和桌宠动画均为本项目制作的自定义作品。仓库已包含播放器所需素材，构建后即可运行同款桌宠。本项目是社区制作，并非 OpenAI 官方产品，也不替代官方 Pets。

## 一句话让 Codex 安装

在 **Mac 上的 Codex 本地聊天**中复制并发送：

```text
请帮我安装“codexの大肥鱼替身”Codex 插件：
https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen

请先阅读仓库文档，将项目下载到独立目录，并注册本项目的插件市场、安装 dsl-pet。
保留我现有的官方 Pets、已选宠物和其他插件设置，不要修改或替换它们。
桌宠动画素材已随仓库提供，请直接按文档构建并打包运行。
完成后启动桌宠，检查插件与桌宠是否连接成功，并告诉我是否需要重载 Codex。
```

<p align="center"><img src="docs/images/big-fat-fish.png" alt="Codex 大肥鱼桌宠：蓝发鱼尾女仆风角色" width="360"></p>

## 动作预览

| 待机 | 工作 | 等待输入 | 任务完成 | 拖动 | 出场 | 失败 | 悬停 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ![Codex 大肥鱼待机动画](docs/images/preview/idle.gif) | ![Codex 大肥鱼工作动画](docs/images/preview/running.gif) | ![Codex 大肥鱼等待动画](docs/images/preview/waiting.gif) | ![Codex 大肥鱼完成动画](docs/images/preview/review.gif) | ![Codex 大肥鱼拖动动画](docs/images/preview/running-right.gif) | ![Codex 大肥鱼出场动画](docs/images/preview/waving.gif) | ![Codex 大肥鱼失败动画](docs/images/preview/failed.gif) | ![Codex 大肥鱼悬停动画](docs/images/preview/jumping.gif) |

## Codex Pets 宠物与桌面应用

仓库提供两种使用方式：安装 V2 宠物图集后，在 Codex 的 Pets 设置中选择“大肥鱼”；或者安装 `dsl-pet` 插件并运行独立桌宠应用。它们可以同时使用，不会覆盖已有官方 Pets 或当前选择。

动画包含待机呼吸与眨眼、拖动时左右跑动、首次显示挥手、悬停跳跃、任务工作、等待用户输入、任务完成、失败反应，以及 16 向视线跟随。

## 功能

- 根据任务状态切换动画，例如接单、工作、等待输入、完成和纠正。
- 桌宠悬浮在普通窗口上方，支持拖动、调整大小、隐藏和动作预览。
- 通过消息气泡显示 Codex 发送的摘要，并可返回 Codex。
- 插件只在重要任务节点发送状态，不会自动监听所有聊天。

## 构建环境

支持 macOS 13 及以上，需要 Python 3 和 Xcode Command Line Tools。当前应用由源码构建，尚未经过 Apple 公证；Windows 和 Linux 暂不支持。

```bash
python3 apps/dsl-pet/scripts/build.py
mkdir -p "$HOME/Applications"
cp -R apps/dsl-pet/dist/DSLPet.app "$HOME/Applications/"
open "$HOME/Applications/DSLPet.app"
```

仓库已包含 `apps/dsl-pet/assets/` 下的待机图、25 组动画帧和时序配置。运行上方构建命令即可把素材打包进应用；安装 prompt 会让 Codex 检查素材并构建桌宠。
## 安装 Codex 插件

在 Codex 本地聊天中从此仓库添加插件市场，然后安装 `dsl-pet`：

```bash
codex plugin marketplace add https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen
codex plugin add dsl-pet@q-ai-local
```

如果你使用本地仓库路径注册市场，请在项目根目录运行 `codex plugin marketplace add .`。具体命令取决于 Codex 客户端版本。仓库包含完整的大肥鱼桌宠素材，无需额外准备。

## 代码许可与作品来源

本项目代码按 [MIT License](LICENSE) 发布。大肥鱼的角色设定、`docs/images/big-fat-fish.png` 主视觉图和桌宠动画均由本项目作者创作。

MIT 许可适用于源代码。作者允许大肥鱼美术素材随本项目复制、分发和运行；脱离本项目单独使用或改编需另行取得作者许可。Codex、ChatGPT 等第三方名称与标识归各自权利人所有。

---

[English](README.en.md) · [日本語](README.ja.md)

## 官方 Pets 安装

将 [V2 宠物图集](docs/images/big-fat-fish-spritesheet.webp)、[宠物配置](docs/images/pet.json) 和图集一同放入 Codex 的自定义宠物目录：

```text
~/.codex/pets/codex-big-fat-fish/
├── pet.json
└── spritesheet.webp
```

将图集文件命名为 `spritesheet.webp`。完成后重启 Codex，并在 Pets 设置中选择“Codex 大肥鱼”。更新同 ID 宠物时，替换此目录后完全退出并重新打开 Codex，以刷新图集缓存。
