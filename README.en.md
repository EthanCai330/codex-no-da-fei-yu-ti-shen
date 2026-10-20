# codexの大肥鱼替身 🐟

[简体中文](README.md) · **English** · [日本語](README.ja.md)

An independent macOS desktop companion and Codex plugin. It can run alongside Codex's official Pets and appears as a separate floating desktop pet.

Big Fat Fish's character design, key illustration, and desktop pet animations were created for this project. The repository includes the frames and timing configuration needed to build and run the same pet. This is an unofficial community project and does not replace OpenAI's official Pets.

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
The repository includes the Big Fat Fish animation assets. Follow the instructions to build and package the desktop pet.
Launch the pet, check that the plugin connects to it, and tell me whether Codex needs to be reloaded.
```

## Build requirements

Requires macOS 13 or later, Python 3, and Xcode Command Line Tools. The app builds from source and has not been notarized by Apple. Windows and Linux are not supported.

```bash
python3 apps/dsl-pet/scripts/build.py
mkdir -p "$HOME/Applications"
cp -R apps/dsl-pet/dist/DSLPet.app "$HOME/Applications/"
open "$HOME/Applications/DSLPet.app"
```

The repository includes the idle image, 25 animation sets, and timing configuration under `apps/dsl-pet/assets/`. Run the build command above to package them into the app; the installation prompt asks Codex to check the assets and build the desktop pet.
## Install the Codex plugin

From a local Codex chat, add this repository as a plugin marketplace and install `dsl-pet`:

```bash
codex plugin marketplace add https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen
codex plugin add dsl-pet@q-ai-local
```

To register a local checkout instead, run `codex plugin marketplace add .` from the repository root. Exact commands may vary by Codex client version. The repository includes the full Big Fat Fish asset set, so no extra art files are needed.

## Code license and artwork attribution

This project is distributed under the [MIT License](LICENSE). Big Fat Fish's character design, the key art at `docs/images/big-fat-fish.png`, and the desktop pet animations were created by this project's author.

The MIT license applies to source code. The author permits the Big Fat Fish artwork to be copied, distributed, and run as part of this project; separate use or adaptation outside the project requires the author’s permission. Third-party names and marks such as Codex and ChatGPT belong to their respective rights holders.

---

[简体中文](README.md) · [日本語](README.ja.md)
