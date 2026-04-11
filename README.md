# code-de-tsukuru-python

**「コードで創る — Python×創作 入門10講」** の読者用リポジトリです。

## このリポジトリの使い方

### 1. ダウンロード

**Git が使える方**

```bash
git clone git@github.com:imin-minnade/code-de-tsukuru-python.git
cd python-playground
```

**Git がわからない方**

ページ上部の緑色の「Code」ボタン → 「Download ZIP」でダウンロードし、好きな場所に展開してください。

### 2. Python の準備

Python のインストールがまだの方は、以下の無料記事を参照してください。

- macOS: [Python環境構築ガイド（Mac編）](https://note.com/mikai_daichi/n/nd127acffeac6)
- Windows: [Python環境構築ガイド（Windows編）](https://note.com/mikai_daichi/n/n1b314d7eae03)

### 3. 作業する

```bash
cd workspace/01-turtle
```

各回の記事を読みながら、`workspace/` 内の対応フォルダーでコードを書いてください。
詰まったときは `examples/` に完成コードがあります。答え合わせではなく、参考用です。

---

## フォルダー構成

```
code-de-tsukuru-python/
├── workspace/           ← あなたの作業場所
│   ├── 01-turtle/
│   ├── 02-matplotlib/
│   ├── ...
│   └── 10-ai-publisher/
├── examples/            ← 完成コードの見本（参考用）
│   ├── 01-turtle/
│   │   └── turtle_art.py
│   ├── 02-matplotlib/
│   │   └── math_art.py
│   ├── ...
│   └── 10-ai-publisher/
│       └── ai_novel_factory.py
├── images/              ← スクリーンショット等
│   ├── 01-turtle/
│   ├── ...
│   └── 10-ai-publisher/
├── .gitignore
└── README.md
```

## 講座一覧

| 回 | タイトル | 学ぶ概念 |
|---|---|---|
| 第1回（無料） | 線を引く、世界が動く — turtleで図形を描く | 変数、forループ、関数（導入） |
| 第2回 | 数式がアートになる — Matplotlibで描く数学の美 | リスト、タプル、辞書 |
| 第3回 | コードが奏でる — 電子楽器を作る | 関数(def)、条件分岐(if) |
| 第4回 | ピクセルに魂を込める — ドット絵エディタを作る | イベント処理、2次元配列 |
| 第5回 | 次元を超える — Panda3Dで3Dの世界へ | モジュール、import |
| 第6回 | 写真を手術する — Pillow + Photoshop風画像編集 | ライブラリ(pip)、ファイル操作 |
| 第7回 | 鏡の中の自分 — カメラ＋姿勢推定で人形を踊らせる | 外部ライブラリ連携、エラー処理 |
| 第8回 | 敵を倒せ — ミニ・インベーダーゲーム | クラス、インスタンス |
| 第9回 | 3Dの冒険 — Panda3Dでゲームを作る | 統合（クラス＋イベント＋3D） |
| 第10回 | AI出版社の社長になる — マルチエージェント小説工房 | API連携、総合 |

## 必要な環境

- Python 3.12 以上
- パソコン（macOS または Windows）
- 第9回まで使うライブラリは全て無料です
- 第10回のみ OpenAI API キーが必要です（有料）

## ライセンス

コードは MIT License で公開しています。記事本文の著作権は著者に帰属します。
