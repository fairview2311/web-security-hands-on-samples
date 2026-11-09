# 第9章　認証の不備（総当たりとパスワードの保存）

本の第9章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch09/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- 認証の不備を直し、遅いハッシュと回数制限で総当たりを止めるようにした

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

- http://localhost:8000/login … 連続してログインに失敗すると止まることを確かめる

動作しないときは、本の第9章の「うまくいかないとき」を見てください。

<details>
<summary>第8章からの変更（追加・変更したファイル 4 個）</summary>

- 追加: [`attacker/brute.py`](attacker/brute.py)
- 追加: [`attacker/tests/test_ch09.py`](attacker/tests/test_ch09.py)
- 変更: [`app/db.py`](app/db.py)
- 変更: [`app/routers/auth.py`](app/routers/auth.py)

</details>

← [ch08](../ch08)　｜　[一覧](../README.md)　｜　[ch10](../ch10) →
