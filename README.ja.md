# Codex 大肥魚｜codexの大肥鱼替身 🐟

[简体中文](README.md) · [English](README.en.md) · **日本語**

**Codex 大肥魚**は、Codex 公式 Pets で選択できるペットと、Codex プラグインに接続する独立したデスクトップアプリを含む macOS プロジェクトです。どちらか一方、または両方を利用できます。

大肥魚のキャラクターデザイン、メインイラスト、アニメーションは本プロジェクトのオリジナル作品です。非公式のコミュニティ制作物です。

## Codex にインストールを頼む

Mac の **Codex ローカルチャット**に、次のプロンプトをコピーして送信してください。

```text
「codexの大肥鱼替身」Codex プラグインをインストールしてください。
https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen

リポジトリの説明を読んで、プロジェクトを独立したディレクトリにダウンロードし、プラグインマーケットプレイスを登録して dsl-pet をインストールしてください。
既存の公式 Pets、選択中のペット、その他のプラグイン設定は維持し、変更や置き換えをしないでください。
大肥魚のアニメーション素材はリポジトリに含まれています。ドキュメントに従ってデスクトップペットをビルドしてください。
ペットを起動し、プラグインとの接続を確認して、Codex の再読み込みが必要か教えてください。
```

<p align="center"><img src="docs/images/big-fat-fish.png" alt="Codex 大肥魚デスクトップペット、青い髪と魚の尾を持つキャラクター" width="360"></p>

## アニメーションプレビュー

| 待機 | 作業中 | 入力待ち | 完了 | ドラッグ | 登場 | 失敗 | ホバー |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ![Codex 大肥魚 待機](docs/images/preview/idle.gif) | ![Codex 大肥魚 作業中](docs/images/preview/running.gif) | ![Codex 大肥魚 入力待ち](docs/images/preview/waiting.gif) | ![Codex 大肥魚 完了](docs/images/preview/review.gif) | ![Codex 大肥魚 ドラッグ](docs/images/preview/running-right.gif) | ![Codex 大肥魚 登場](docs/images/preview/waving.gif) | ![Codex 大肥魚 失敗](docs/images/preview/failed.gif) | ![Codex 大肥魚 ホバー](docs/images/preview/jumping.gif) |

## Codex Pets とデスクトップアプリ

本リポジトリには2つの利用方法があります。V2 ペットシートをインストールして Codex Pets から大肥魚を選ぶ方法と、`dsl-pet` プラグインをインストールして独立アプリを起動する方法です。両方を同時に使っても、既存の Pets や選択状態は置き換わりません。

待機中の呼吸とまばたき、ドラッグ時の左右移動、登場時の挨拶、ホバー時のジャンプ、作業中、入力待ち、完了、失敗、16方向の視線追従に対応しています。

## 機能

- タスクの受け付け、作業中、入力待ち、完了、修正などに応じてアニメーションを切り替えます。
- 通常のウィンドウより前面に表示され、移動、サイズ変更、非表示、アニメーションのプレビューができます。
- Codex から送られた要約を吹き出しに表示し、Codex に戻る操作を提供します。
- 重要なタスクの節目で状態を送信します。すべてのチャットを自動監視することはありません。

## ビルド要件

macOS 13 以降、Python 3、Xcode Command Line Tools が必要です。アプリはソースからビルドします。Apple による公証は未取得です。Windows と Linux には対応していません。

```bash
python3 apps/dsl-pet/scripts/build.py
mkdir -p "$HOME/Applications"
cp -R apps/dsl-pet/dist/DSLPet.app "$HOME/Applications/"
open "$HOME/Applications/DSLPet.app"
```

リポジトリには `apps/dsl-pet/assets/` に待機画像、25 種類のアニメーションフレームとタイミング設定が含まれています。上記のビルドコマンドを実行すると、素材がアプリにパッケージされます。
## Codex プラグインのインストール

Mac 上の Codex ローカルチャットで、このリポジトリをプラグインマーケットプレイスとして登録し、`dsl-pet` をインストールします。

```bash
codex plugin marketplace add https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen
codex plugin add dsl-pet@q-ai-local
```

ローカルのチェックアウトを登録する場合は、リポジトリのルートで `codex plugin marketplace add .` を実行してください。コマンドは Codex クライアントのバージョンによって異なる場合があります。大肥魚の素材一式はリポジトリに含まれているため、追加の画像は不要です。

## ソースコードのライセンスと作品のクレジット

本プロジェクトのコードは [MIT License](LICENSE) に基づいて公開しています。大肥魚のキャラクターデザイン、`docs/images/big-fat-fish.png` のメインビジュアルとデスクトップペットのアニメーションは本プロジェクトの作者が制作しました。

MIT ライセンスはソースコードに適用されます。作者は、本プロジェクトの一部として大肥魚の美術素材を複製、配布、実行することを許可します。本プロジェクト外での単独利用や改変には作者の許可が必要です。Codex、ChatGPT など第三者の名称や標章は各権利者に帰属します。

---

[简体中文](README.md) · [English](README.en.md)

## Codex Pets へのインストール

[V2 ペットシート](docs/images/big-fat-fish-spritesheet.webp) と[メタデータ](docs/images/pet.json)を、Codex のカスタムペットフォルダーに配置します。

```text
~/.codex/pets/codex-big-fat-fish/
├── pet.json
└── spritesheet.webp
```

シートのファイル名は `spritesheet.webp` にします。Codex を再起動し、Pets 設定から「Codex 大肥魚」を選択してください。同じ ID のペットを更新する場合はフォルダーを置き換え、画像キャッシュ更新のため Codex を完全に再起動します。
