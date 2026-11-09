# 第17章　レースコンディション（同時のリクエストで二重に使う）

本の第17章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch17/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- レースコンディションを直し、原子的な更新で二重に使えないようにした

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

- http://localhost:8000/ … 同時のリクエストでもクーポンが1回だけ成功することを確かめる

動作しないときは、本の第17章の「うまくいかないとき」を見てください。

<details>
<summary>第16章からの変更（追加・変更したファイル 3 個）</summary>

- 追加: [`attacker/race.py`](attacker/race.py)
- 追加: [`attacker/tests/test_ch17.py`](attacker/tests/test_ch17.py)
- 変更: [`app/routers/coupons.py`](app/routers/coupons.py)

</details>

← [ch16](../ch16)　｜　[一覧](../README.md)　｜　[ch18](../ch18) →
