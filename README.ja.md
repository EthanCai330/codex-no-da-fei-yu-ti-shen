# Codex 大肥魚｜codexの大肥鱼替身 🐟

[简体中文](README.md) · [English](README.en.md) · **日本語**

**Codex 大肥魚**は、Codex ネイティブ Pets 向けに制作したオリジナルの V2 カスタムペットです。インストール後、Codex Pets の設定から選択できます。OpenAI 公式製品ではなく、コミュニティ制作のプロジェクトです。

キャラクターデザイン、メインイラスト、ペットのスプライトシートは本プロジェクトのオリジナル作品です。シートには9種類のアニメーション状態と16方向の視線が含まれています。

## Codex にインストールを頼む

Mac の **Codex ローカルチャット**に、次のプロンプトをコピーして送信してください。

```text
「codexの大肥鱼替身」を Codex ネイティブ Pets のカスタムペットとして追加してください。
https://github.com/EthanCai330/codex-no-da-fei-yu-ti-shen

リポジトリ README の Pets インストール手順を読み、ペット設定と V2 スプライトシートを Codex がサポートするカスタムペット用ディレクトリにインストールしてください。
既存の公式 Pets、現在の選択、その他の設定は維持してください。変更、上書き、自動切り替えはしないでください。
完了後、Codex の再起動が必要か、Pets 設定から「Codex 大肥魚」を手動で選択する方法を教えてください。
```

<p align="center"><img src="docs/images/big-fat-fish.png" alt="Codex 大肥魚デスクトップペット、青い髪と魚の尾を持つキャラクター" width="360"></p>

## Codex ネイティブ Pets へのインストール

[V2 ペットスプライトシート](docs/images/big-fat-fish-spritesheet.webp)と[ペット設定](docs/images/pet.json)を Codex のカスタムペット用ディレクトリに配置します。

```text
~/.codex/pets/codex-big-fat-fish/
├── pet.json
└── spritesheet.webp
```

シートのファイル名は `spritesheet.webp` にしてください。Codex を再起動し、Pets 設定から「Codex 大肥魚」を選択します。追加によって既存のペットが置き換わることはありません。同じ ID のシートを更新した場合は、キャッシュ更新のため Codex を完全に終了して再起動してください。

## 作品とライセンス

プロジェクトのコードは [MIT License](LICENSE) に基づいて公開しています。大肥魚のキャラクターデザイン、`docs/images/big-fat-fish.png` のメインビジュアル、V2 ペットスプライトシートは本プロジェクトの作者が制作しました。美術素材は本プロジェクトの一部として複製、配布、実行できます。本プロジェクト外での個別利用や改変には作者の許可が必要です。Codex、ChatGPT などの名称と商標は各権利者に帰属します。
