# 第19章　プロンプトインジェクション（AI 機能を追加したアプリの穴）

本の第19章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch19/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- プロンプトインジェクションを直し、AI の応答をエスケープして画面で実行させないようにした

## この章での使い方

起動には Docker Desktop が必要です。コマンドは、Windows は PowerShell、Mac はターミナルで実行します。サンプルコードはホームのフォルダーなどに展開してください。

1. このフォルダーでターミナル（Windows は PowerShell）を開き、みどりメモを起動します。初回はイメージの作成に数分かかります。

   ```text
   docker compose up -d --build
   ```

2. ブラウザで下の URL を開いて確かめます。

3. 確かめ終わったら、同じフォルダーでコンテナを停止します。

   ```text
   docker compose down
   ```

## うまくいったかの確かめ方

- http://localhost:8000/board … AI の要約に混ざったタグが文字として表示されることを確かめる

動作しないときは、本の第19章の「うまくいかないとき」を見てください。

<details>
<summary>第18章からの変更（追加・変更したファイル 2 個）</summary>

- 追加: [`attacker/tests/test_ch19.py`](attacker/tests/test_ch19.py)
- 変更: [`app/templates/summary.html`](app/templates/summary.html)

</details>

← [ch18](../ch18)　｜　[一覧](../README.md)　｜　[ch20](../ch20) →
