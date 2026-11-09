# 第5章　マスアサインメント（送るだけで管理者になる）

本の第5章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch05/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- マスアサインメントを直し、受け取る項目を絞って権限を昇格できないようにした

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

- http://localhost:8000/ … 送っても管理者になれないことを確かめる

動作しないときは、本の第5章の「うまくいかないとき」を見てください。

<details>
<summary>第4章からの変更（追加・変更したファイル 2 個）</summary>

- 追加: [`attacker/tests/test_ch05.py`](attacker/tests/test_ch05.py)
- 変更: [`app/routers/profile.py`](app/routers/profile.py)

</details>

← [ch04](../ch04)　｜　[一覧](../README.md)　｜　[ch06](../ch06) →
