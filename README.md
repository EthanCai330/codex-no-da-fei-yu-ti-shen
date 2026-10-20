# codexの大肥鱼替身 🐟

**简体中文** · [English](README.en.md) · [日本語](README.ja.md)

这是一个面向 macOS 的 Codex 桌宠插件与独立悬浮桌宠应用。它可以与 Codex 的官方 Pets 同时使用，独立显示在桌面上。

大肥鱼的角色设定、主视觉图和桌宠动画均为本项目制作的自定义作品。仓库已包含播放器所需素材，构建后即可运行同款桌宠。本项目是社区制作，并非 OpenAI 官方产品，也不替代官方 Pets。

<p align="center"><img src="docs/images/big-fat-fish.png" alt="大肥鱼：蓝发、鱼尾的女仆风桌宠" width="420"></p>

## 功能

- 根据任务状态切换动画，例如接单、工作、等待输入、完成和纠正。
- 桌宠悬浮在普通窗口上方，支持拖动、调整大小、隐藏和动作预览。
- 通过消息气泡显示 Codex 发送的摘要，并可返回 Codex。
- 插件只在重要任务节点发送状态，不会自动监听所有聊天。

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

播放器及插件代码基于 [Knox-zki/fat-fish-at-gpt](https://github.com/Knox-zki/fat-fish-at-gpt) 改造，并按 [MIT License](LICENSE) 发布。大肥鱼的角色设定、`docs/images/big-fat-fish.png` 主视觉图和桌宠动画均由本项目作者自行创作，不是从上游项目复制的角色素材。

MIT 许可适用于源代码。作者允许大肥鱼美术素材随本项目复制、分发和运行；脱离本项目单独使用或改编需另行取得作者许可。Codex、ChatGPT 等第三方名称与标识归各自权利人所有。

---

[English](README.en.md) · [日本語](README.ja.md)
