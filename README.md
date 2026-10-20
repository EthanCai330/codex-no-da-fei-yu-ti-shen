# codexの大肥鱼替身 🐟

**简体中文** · [English](README.en.md) · [日本語](README.ja.md)

这是一个面向 macOS 的 Codex 桌宠插件与独立悬浮桌宠应用。它可以与 Codex 的官方 Pets 同时使用，独立显示在桌面上。

本仓库发布的是可构建的应用和插件源代码。原项目角色图片和动画素材未获再分发授权，因此未包含在本仓库中。要运行桌宠，请自行准备有权使用的素材，并按下方格式放入 `apps/dsl-pet/assets/`。本项目不代表 OpenAI 官方产品，也不替代官方 Pets。

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
如果桌宠构建因缺少动画素材而无法完成，请告诉我需要提供哪些有授权的素材；不要从其他仓库复制未获再分发授权的图片或动画。
完成后启动桌宠（如果已具备素材），检查插件与桌宠是否连接成功，并告诉我是否需要重载 Codex。
```

## 构建环境

支持 macOS 13 及以上，需要 Python 3 和 Xcode Command Line Tools。当前应用由源码构建，尚未经过 Apple 公证；Windows 和 Linux 暂不支持。

```bash
python3 apps/dsl-pet/scripts/build.py
mkdir -p "$HOME/Applications"
cp -R apps/dsl-pet/dist/DSLPet.app "$HOME/Applications/"
open "$HOME/Applications/DSLPet.app"
```

构建前，需在 `apps/dsl-pet/assets/` 提供 `animations.json`、`待机.png`，以及每个动画目录下的 `animation.json` 和逐帧 PNG。结构示例：

```text
apps/dsl-pet/assets/
├── animations.json
├── 待机.png
└── 01-example/
    ├── animation.json
    └── 逐帧PNG/
        ├── frame-01.png
        └── frame-02.png
```

`animation.json` 格式可参考 `apps/dsl-pet/Sources/Engine.swift` 中的 `Animation` 定义，以及插件中的状态规则。请确保你拥有这些素材的使用权。

## 安装 Codex 插件

在 Codex 本地聊天中从此仓库添加插件市场，然后安装 `dsl-pet`：

```bash
codex plugin marketplace add https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen
codex plugin add dsl-pet@q-ai-local
```

如果你使用本地仓库路径注册市场，请在项目根目录运行 `codex plugin marketplace add .`。具体命令取决于 Codex 客户端版本。由于本公开仓库不含动画素材，桌宠需要在构建前补充自有素材。

## 代码许可与来源

本仓库中的源代码按原项目的 [MIT License](LICENSE) 发布。插件及应用代码源自 [Knox-zki/fat-fish-at-gpt](https://github.com/Knox-zki/fat-fish-at-gpt)，本项目为独立维护的社区衍生项目。

原项目已声明角色形象、图片、动画、Logo、截图及其他视觉素材不在 MIT 许可范围内，且没有授予使用或再分发许可。因此本仓库不包含这些素材；本仓库的代码许可也不涵盖使用者自行添加的素材。第三方名称与标识归各自权利人所有。

---

[English](README.en.md) · [日本語](README.ja.md)
