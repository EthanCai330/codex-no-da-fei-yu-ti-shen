# codexの大肥鱼替身 🐟

[简体中文](README.md) · [English](README.en.md) · **日本語**

macOS 向けの独立したデスクトップペットアプリと Codex プラグインです。Codex 公式 Pets と併用でき、デスクトップ上に別のペットとして表示されます。

このリポジトリには、ビルド可能なアプリとプラグインのソースコードを掲載しています。元プロジェクトのキャラクター画像とアニメーション素材は、再配布の許可が確認できないため含めていません。ペットを動かすには、利用権を持つ素材を所定の形式で `apps/dsl-pet/assets/` に用意してください。本プロジェクトは非公式のコミュニティ制作物であり、OpenAI 公式 Pets を置き換えるものではありません。

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

ビルド前に `apps/dsl-pet/assets/` に `animations.json`、`待机.png`、各アニメーションの `animation.json` とフレーム PNG を用意してください。

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

## ソースコードのライセンスと権利表示

本リポジトリのソースコードは、元プロジェクトの [MIT License](LICENSE) に基づいて公開しています。アプリとプラグインのコードは [Knox-zki/fat-fish-at-gpt](https://github.com/Knox-zki/fat-fish-at-gpt) を基にした、独立運営のコミュニティ派生プロジェクトです。

元プロジェクトでは、キャラクターデザイン、画像、アニメーション、ロゴ、スクリーンショットなどの視覚素材は MIT ライセンスの対象外で、使用・再配布の許可も与えていないと明記されています。そのため、これらの素材は本リポジトリに含めていません。本リポジトリのコードライセンスは、利用者が追加した素材には適用されません。第三者の名称や標章の権利は各権利者に帰属します。

---

[简体中文](README.md) · [English](README.en.md)
