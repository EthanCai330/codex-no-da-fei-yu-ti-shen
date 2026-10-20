# codexの大肥鱼替身 🐟

[简体中文](README.md) · **English** · [日本語](README.ja.md)

An independent macOS desktop companion and Codex plugin. It can run alongside Codex's official Pets and appears as a separate floating desktop pet.

Big Fat Fish's character design and the key illustration below were made for this project. The desktop player also needs animation frames and timing configuration to run; see the build instructions for the required format. This is an unofficial community project and does not replace OpenAI's official Pets.

<p align="center"><img src="docs/images/big-fat-fish.png" alt="Big Fat Fish, a blue-haired mermaid maid desktop pet" width="420"></p>

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

Before building, provide `animations.json`, `待机.png`, and each animation's `animation.json` and frame PNG files under `apps/dsl-pet/assets/`. The illustration in this repository is the custom character key art and does not replace the animation frames required by the player:

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

## Code license and artwork attribution

The player and plugin code are adapted from [Knox-zki/fat-fish-at-gpt](https://github.com/Knox-zki/fat-fish-at-gpt) and distributed under the [MIT License](LICENSE). Big Fat Fish's character design and the key art at `docs/images/big-fat-fish.png` were created by this project's author and are not copied from the upstream project's character assets.

The MIT license applies to source code and does not automatically grant permission to reuse Big Fat Fish artwork. Third-party names and marks such as Codex and ChatGPT belong to their respective rights holders.

---

[简体中文](README.md) · [日本語](README.ja.md)
