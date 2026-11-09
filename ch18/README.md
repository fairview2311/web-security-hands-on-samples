# 第18章　秘密情報の漏えいと古いライブラリ

本の第18章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch18/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- 秘密情報の漏えいを直し、デバッグ画面を外して古いライブラリを更新した

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

- http://localhost:8000/map … ページのソースに秘密の鍵が出ないことを確かめる

動作しないときは、本の第18章の「うまくいかないとき」を見てください。

<details>
<summary>第17章からの変更（追加・変更したファイル 5 個）</summary>

- 追加: [`attacker/tests/test_ch18.py`](attacker/tests/test_ch18.py)
- 変更: [`app/main.py`](app/main.py)
- 変更: [`app/requirements.txt`](app/requirements.txt)
- 変更: [`app/routers/map_page.py`](app/routers/map_page.py)
- 変更: [`app/templates/map.html`](app/templates/map.html)

</details>

← [ch17](../ch17)　｜　[一覧](../README.md)　｜　[ch19](../ch19) →
