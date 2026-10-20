# codexの大肥鱼替身 🐟

[简体中文](README.md) · [English](README.en.md) · **日本語**

macOS 向けの独立したデスクトップペットアプリと Codex プラグインです。Codex 公式 Pets と併用でき、デスクトップ上に別のペットとして表示されます。

大肥魚のキャラクターデザインと下のメインイラストは、本プロジェクトのために制作したオリジナル作品です。デスクトッププレイヤーを動かすには、アニメーションのフレームとタイミング設定も必要です。形式はビルド手順を参照してください。本プロジェクトは非公式のコミュニティ制作物であり、OpenAI 公式 Pets を置き換えるものではありません。

<p align="center"><img src="docs/images/big-fat-fish.png" alt="青い髪と魚の尾を持つメイド風デスクトップペット、大肥魚" width="420"></p>

## 機能

- タスクの受け付け、作業中、入力待ち、完了、修正などに応じてアニメーションを切り替えます。
- 通常のウィンドウより前面に表示され、移動、サイズ変更、非表示、アニメーションのプレビューができます。
- Codex から送られた要約を吹き出しに表示し、Codex に戻る操作を提供します。
- 重要なタスクの節目で状態を送信します。すべてのチャットを自動監視することはありません。

## Codex にインストールを頼む

Mac の **Codex ローカルチャット**に、次のプロンプトをコピーして送信してください。

```text
「codexの大肥鱼替身」Codex プラグインをインストールしてください。
https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen

リポジトリの説明を読んで、プロジェクトを独立したディレクトリにダウンロードし、プラグインマーケットプレイスを登録して dsl-pet をインストールしてください。
既存の公式 Pets、選択中のペット、その他のプラグイン設定は維持し、変更や置き換えをしないでください。
アニメーション素材がなくデスクトップペットをビルドできない場合は、必要な利用許諾済み素材を教えてください。再配布が許可されていない画像やアニメーションを他のリポジトリからコピーしないでください。
素材が揃っていればペットを起動し、プラグインとの接続を確認して、Codex の再読み込みが必要か教えてください。
```

## ビルド要件

macOS 13 以降、Python 3、Xcode Command Line Tools が必要です。アプリはソースからビルドします。Apple による公証は未取得です。Windows と Linux には対応していません。

```bash
python3 apps/dsl-pet/scripts/build.py
mkdir -p "$HOME/Applications"
cp -R apps/dsl-pet/dist/DSLPet.app "$HOME/Applications/"
open "$HOME/Applications/DSLPet.app"
```

ビルド前に `apps/dsl-pet/assets/` に `animations.json`、`待机.png`、各アニメーションの `animation.json` とフレーム PNG を用意してください。本リポジトリのイラストはキャラクターのメインビジュアルであり、プレイヤーに必要なアニメーションフレームの代わりにはなりません。

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

`animation.json` の形式は `apps/dsl-pet/Sources/Engine.swift` の `Animation` 定義と、プラグインの状態ルールを参照してください。追加する素材の利用権を必ず確認してください。

## Codex プラグインのインストール

Mac 上の Codex ローカルチャットで、このリポジトリをプラグインマーケットプレイスとして登録し、`dsl-pet` をインストールします。

```bash
codex plugin marketplace add https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen
codex plugin add dsl-pet@q-ai-local
```

ローカルのチェックアウトを登録する場合は、リポジトリのルートで `codex plugin marketplace add .` を実行してください。コマンドは Codex クライアントのバージョンによって異なる場合があります。

## ソースコードのライセンスと作品のクレジット

プレイヤーとプラグインのコードは [Knox-zki/fat-fish-at-gpt](https://github.com/Knox-zki/fat-fish-at-gpt) を基に改変し、[MIT License](LICENSE) に基づいて公開しています。大肥魚のキャラクターデザインと `docs/images/big-fat-fish.png` のメインビジュアルは本プロジェクトの作者が制作したもので、元プロジェクトのキャラクター素材をコピーしたものではありません。

MIT ライセンスはソースコードに適用され、大肥魚の美術素材の再利用許可を自動的に与えるものではありません。Codex、ChatGPT など第三者の名称や標章は各権利者に帰属します。

---

[简体中文](README.md) · [English](README.en.md)
