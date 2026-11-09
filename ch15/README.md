# 第15章　危ないファイルのアップロード（画像のふりの HTML）

本の第15章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch15/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- 危ないファイルのアップロードを直し、種類を絞ってダウンロードとして返すようにした

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

- http://localhost:8000/ … 画像のふりの HTML のアップロードが拒否されることを確かめる

動作しないときは、本の第15章の「うまくいかないとき」を見てください。

<details>
<summary>第14章からの変更（追加・変更したファイル 2 個）</summary>

- 追加: [`attacker/tests/test_ch15.py`](attacker/tests/test_ch15.py)
- 変更: [`app/routers/upload.py`](app/routers/upload.py)

</details>

← [ch14](../ch14)　｜　[一覧](../README.md)　｜　[ch16](../ch16) →
