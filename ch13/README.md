# 第13章　OSコマンドインジェクション（入力がコマンドになる）

本の第13章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch13/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- OS コマンドインジェクションを直し、引数を分けて渡してシェルを通さないようにした

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

- http://localhost:8000/ … 「便利な道具」の ping に記号を入れても実行されないことを確かめる

動作しないときは、本の第13章の「うまくいかないとき」を見てください。

<details>
<summary>第12章からの変更（追加・変更したファイル 2 個）</summary>

- 追加: [`attacker/tests/test_ch13.py`](attacker/tests/test_ch13.py)
- 変更: [`app/routers/tools.py`](app/routers/tools.py)

</details>

← [ch12](../ch12)　｜　[一覧](../README.md)　｜　[ch14](../ch14) →
