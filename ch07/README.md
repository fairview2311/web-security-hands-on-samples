# 第7章　クロスサイトスクリプティング（XSS）

本の第7章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch07/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- XSS を直し、投稿をエスケープして HttpOnly・CSP でセッションを守るようにした

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

- http://localhost:8000/board … スクリプトが文字として表示されることを確かめる

動作しないときは、本の第7章の「うまくいかないとき」を見てください。

<details>
<summary>第6章からの変更（追加・変更したファイル 4 個）</summary>

- 追加: [`attacker/tests/test_ch07.py`](attacker/tests/test_ch07.py)
- 変更: [`app/routers/auth.py`](app/routers/auth.py)
- 変更: [`app/routers/board.py`](app/routers/board.py)
- 変更: [`app/templates/board.html`](app/templates/board.html)

</details>

← [ch06](../ch06)　｜　[一覧](../README.md)　｜　[ch08](../ch08) →
