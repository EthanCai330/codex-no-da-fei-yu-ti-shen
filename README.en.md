# Codex Big Fat Fish Pet | codexの大肥鱼替身 🐟

[简体中文](README.md) · **English** · [日本語](README.ja.md)

**Codex Big Fat Fish** is a macOS companion project with a pet you can select in Codex Pets and a separate floating desktop app connected through a Codex plugin. Choose either experience or use both.

Big Fat Fish's character design, key illustration, and desktop pet animations were created for this project. The repository includes the frames and timing configuration needed to build and run the same pet. This is an unofficial community project and does not replace OpenAI's official Pets.

<p align="center"><img src="docs/images/big-fat-fish.png" alt="Codex Big Fat Fish desktop pet, blue-haired fish-tailed maid character" width="360"></p>

## Animation preview

| Idle | Working | Waiting | Complete | Dragging | Appearing | Failed | Hover |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ![Codex Big Fat Fish idle](docs/images/preview/idle.gif) | ![Codex Big Fat Fish working](docs/images/preview/running.gif) | ![Codex Big Fat Fish waiting](docs/images/preview/waiting.gif) | ![Codex Big Fat Fish complete](docs/images/preview/review.gif) | ![Codex Big Fat Fish dragging](docs/images/preview/running-right.gif) | ![Codex Big Fat Fish appearing](docs/images/preview/waving.gif) | ![Codex Big Fat Fish failed](docs/images/preview/failed.gif) | ![Codex Big Fat Fish hover](docs/images/preview/jumping.gif) |

## Codex Pets and desktop app

This repository offers two ways to use the character: install the V2 pet sheet and select Big Fat Fish in Codex Pets, or install the `dsl-pet` plugin and run the standalone desktop companion. They can run together without replacing your existing Pets or selection.

Animations include breathing and blinking at rest, left and right movement while dragging, a greeting on appearance, a hover jump, working, waiting for input, task completion, a failure reaction, and 16-direction gaze tracking.

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

## Install in Codex Pets

Place the [V2 pet sheet](docs/images/big-fat-fish-spritesheet.webp) and [pet metadata](docs/images/pet.json) in a folder under Codex's custom pets directory:

```text
~/.codex/pets/codex-big-fat-fish/
├── pet.json
└── spritesheet.webp
```

Name the sheet `spritesheet.webp`. Restart Codex and select **Codex Big Fat Fish** in Pets settings. To update the same pet ID, replace the folder and fully restart Codex to refresh the sprite cache.
