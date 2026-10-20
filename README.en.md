# codexの大肥鱼替身 🐟

[简体中文](README.md) · **English** · [日本語](README.ja.md)

An independent macOS desktop companion and Codex plugin. It can run alongside Codex's official Pets and appears as a separate floating desktop pet.

This repository contains buildable application and plugin source code. The original character images and animations are not included because their redistribution was not authorized. To run the pet, provide assets that you are entitled to use under `apps/dsl-pet/assets/`, following the format below. This is an unofficial community project and does not replace OpenAI's official Pets.

## Features

- Changes animations for task events such as acceptance, work, requests for input, completion, and corrections.
- Floats above ordinary windows and supports dragging, resizing, hiding, and animation previews.
- Shows Codex summaries in message bubbles and provides a way back to Codex.
- Sends task updates at important transitions; it does not automatically monitor every chat.

## Ask Codex to install it

Copy this prompt into a **local Codex chat on your Mac**:

```text
Please install the “codexの大肥鱼替身” Codex plugin:
https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen

Read the repository docs, download the project into a separate directory, register its plugin marketplace, and install dsl-pet.
Preserve my existing official Pets, selected pet, and other plugin settings. Do not modify or replace them.
If the desktop pet cannot be built because animation assets are missing, tell me which licensed assets I need to provide. Do not copy images or animations that are not authorized for redistribution.
If assets are available, launch the pet, check that the plugin connects to it, and tell me whether Codex needs to be reloaded.
```

## Build requirements

Requires macOS 13 or later, Python 3, and Xcode Command Line Tools. The app builds from source and has not been notarized by Apple. Windows and Linux are not supported.

```bash
python3 apps/dsl-pet/scripts/build.py
mkdir -p "$HOME/Applications"
cp -R apps/dsl-pet/dist/DSLPet.app "$HOME/Applications/"
open "$HOME/Applications/DSLPet.app"
```

Before building, provide `animations.json`, `待机.png`, and each animation's `animation.json` and frame PNG files under `apps/dsl-pet/assets/`:

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

For the `animation.json` format, see the `Animation` definition in `apps/dsl-pet/Sources/Engine.swift` and the plugin's state rules. Make sure you have the rights to use any assets you add.

## Install the Codex plugin

From a local Codex chat, add this repository as a plugin marketplace and install `dsl-pet`:

```bash
codex plugin marketplace add https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen
codex plugin add dsl-pet@q-ai-local
```

To register a local checkout instead, run `codex plugin marketplace add .` from the repository root. Exact commands may vary by Codex client version.

## Code license and attribution

The source code in this repository is distributed under the original project's [MIT License](LICENSE). The application and plugin code are derived from [Knox-zki/fat-fish-at-gpt](https://github.com/Knox-zki/fat-fish-at-gpt); this is an independently maintained community fork.

The original project states that character designs, images, animations, logos, screenshots, and other visual assets are outside the MIT license and are not licensed for use or redistribution. Those assets are therefore omitted here. The code license in this repository does not cover assets supplied by users. Third-party names and marks belong to their respective rights holders.

---

[简体中文](README.md) · [日本語](README.ja.md)
