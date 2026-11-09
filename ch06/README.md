# 第6章　SQLインジェクション

本の第6章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch06/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- SQL インジェクションを直し、プレースホルダーで入力を安全に扱うようにした

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

- http://localhost:8000/search … 記号を入れても他人のメモが出ないことを確かめる

動作しないときは、本の第6章の「うまくいかないとき」を見てください。

<details>
<summary>第5章からの変更（追加・変更したファイル 2 個）</summary>

- 追加: [`attacker/tests/test_ch06.py`](attacker/tests/test_ch06.py)
- 変更: [`app/routers/search.py`](app/routers/search.py)

</details>

← [ch05](../ch05)　｜　[一覧](../README.md)　｜　[ch07](../ch07) →
