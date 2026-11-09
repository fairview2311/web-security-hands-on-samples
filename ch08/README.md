# 第8章　CSRF（罠のページを開くと勝手に投稿される）

本の第8章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch08/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- CSRF を直し、トークンの無い投稿を拒否するようにした

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

- http://localhost:8000/board … 罠のページからの投稿が拒否されることを確かめる

動作しないときは、本の第8章の「うまくいかないとき」を見てください。

<details>
<summary>第7章からの変更（追加・変更したファイル 6 個）</summary>

- 追加: [`app/csrf.py`](app/csrf.py)
- 追加: [`attacker/tests/test_ch08.py`](attacker/tests/test_ch08.py)
- 追加: [`trap/pages/csrf.html`](trap/pages/csrf.html)
- 変更: [`app/routers/board.py`](app/routers/board.py)
- 変更: [`app/templates/board.html`](app/templates/board.html)
- 変更: [`attacker/tests/test_ch07.py`](attacker/tests/test_ch07.py)

</details>

← [ch07](../ch07)　｜　[一覧](../README.md)　｜　[ch09](../ch09) →
