# Codex Big Fat Fish Pet | codexの大肥鱼替身 🐟

[简体中文](README.md) · **English** · [日本語](README.ja.md)

**Codex Big Fat Fish** is an original V2 custom pet made for native Codex Pets. After installation, you can select her in Codex Pets settings. This is an unofficial community project, not an OpenAI product.

Big Fat Fish's character design, key illustration, and pet spritesheet were created for this project. The sheet includes nine animation states and 16 gaze directions.

## Ask Codex to install it

Copy this prompt into a **local Codex chat on your Mac**:

```text
Please add “codexの大肥鱼替身” as a custom pet in native Codex Pets:
https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen

Read the native Pets installation instructions in the repository README, then install the pet configuration and V2 spritesheet in a custom pet directory supported by Codex.
Preserve my existing official Pets, current selection, and other settings. Do not modify, overwrite, or automatically switch them.
When finished, tell me whether Codex needs to be restarted and how to select “Codex Big Fat Fish” manually in Pets settings.
```

<p align="center"><img src="docs/images/big-fat-fish.png" alt="Codex Big Fat Fish pet, blue-haired fish-tailed maid character" width="360"></p>

## Install in native Codex Pets

Place the [V2 pet spritesheet](docs/images/big-fat-fish-spritesheet.webp) and [pet configuration](docs/images/pet.json) in Codex's custom pet directory:

```text
~/.codex/pets/codex-big-fat-fish/
├── pet.json
└── spritesheet.webp
```

Name the sheet `spritesheet.webp`. Restart Codex, then select “Codex Big Fat Fish” in Pets settings. Adding the pet does not replace existing pets. After updating a sheet with the same ID, fully quit and reopen Codex to refresh its cache.

## Artwork and license

The project code is distributed under the [MIT License](LICENSE). Big Fat Fish's character design, key illustration at `docs/images/big-fat-fish.png`, and V2 pet spritesheet were created by this project's author. The artwork may be copied, distributed, and run as part of this project; separate use or adaptation requires the author's permission. Third-party names and marks such as Codex and ChatGPT belong to their respective rights holders.
