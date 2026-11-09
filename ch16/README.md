# 第16章　SSRF（サーバーに内部へ接続させる）

本の第16章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch16/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- SSRF を直し、取得先を許可した宛先だけに絞るようにした

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

- http://localhost:8000/ … 内部サービスの URL を渡しても 400 で拒否されることを確かめる

動作しないときは、本の第16章の「うまくいかないとき」を見てください。

<details>
<summary>第15章からの変更（追加・変更したファイル 2 個）</summary>

- 追加: [`attacker/tests/test_ch16.py`](attacker/tests/test_ch16.py)
- 変更: [`app/routers/preview.py`](app/routers/preview.py)

</details>

← [ch15](../ch15)　｜　[一覧](../README.md)　｜　[ch17](../ch17) →
