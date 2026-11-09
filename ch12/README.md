# 第12章　CORSの設定ミス（別のサイトから本人の情報を読む）

本の第12章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch12/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- CORS の設定ミスを直し、許可するオリジンを絞るようにした

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

- http://localhost:8000/ … 別のオリジンに本人の情報を返さないことを確かめる

動作しないときは、本の第12章の「うまくいかないとき」を見てください。

<details>
<summary>第11章からの変更（追加・変更したファイル 4 個）</summary>

- 追加: [`attacker/cors.py`](attacker/cors.py)
- 追加: [`attacker/tests/test_ch12.py`](attacker/tests/test_ch12.py)
- 追加: [`trap/pages/cors.html`](trap/pages/cors.html)
- 変更: [`app/cors.py`](app/cors.py)

</details>

← [ch11](../ch11)　｜　[一覧](../README.md)　｜　[ch13](../ch13) →
