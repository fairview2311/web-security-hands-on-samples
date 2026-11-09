# 第4章　認可の不備（URL の番号を変更すると他人のメモが見える）

本の第4章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch04/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- 認可の不備を直し、他人のメモを URL の番号で読めないようにした

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

- http://localhost:8000/ … ログインして自分のメモだけが見えることを確かめる

動作しないときは、本の第4章の「うまくいかないとき」を見てください。

<details>
<summary>第3章からの変更（追加・変更したファイル 2 個）</summary>

- 追加: [`attacker/tests/test_ch04.py`](attacker/tests/test_ch04.py)
- 変更: [`app/routers/notes.py`](app/routers/notes.py)

</details>

← [ch03](../ch03)　｜　[一覧](../README.md)　｜　[ch05](../ch05) →
