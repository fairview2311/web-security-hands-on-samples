# 第11章　JWTの不備（弱い鍵と期限の無視）

本の第11章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch11/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- JWT の不備を直し、長い鍵と期限の確認で偽造・期限切れを拒否するようにした

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

- http://localhost:8000/docs … JWT を使う API で、偽造したトークンが拒否されることを確かめる

動作しないときは、本の第11章の「うまくいかないとき」を見てください。

<details>
<summary>第10章からの変更（追加・変更したファイル 4 個）</summary>

- 追加: [`attacker/forge.py`](attacker/forge.py)
- 追加: [`attacker/tests/test_ch11.py`](attacker/tests/test_ch11.py)
- 変更: [`app/routers/jwt_api.py`](app/routers/jwt_api.py)
- 変更: [`compose.yaml`](compose.yaml)

</details>

← [ch10](../ch10)　｜　[一覧](../README.md)　｜　[ch12](../ch12) →
