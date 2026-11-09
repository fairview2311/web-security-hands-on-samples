# 第10章　セッション管理の不備（セッション固定）

本の第10章を終えた時点の演習アプリ「みどりメモ」です。本のコードの枠の上の「サンプルコード　ch10/…」は、このフォルダーのファイルを指します。

この章でできるようになること:

- セッション固定を直し、ログインのたびにセッション ID を再発行するようにした

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

- http://localhost:8000/login … ログインの前後でセッション ID が変わることを確かめる

動作しないときは、本の第10章の「うまくいかないとき」を見てください。

<details>
<summary>第9章からの変更（追加・変更したファイル 3 個）</summary>

- 追加: [`attacker/fix.py`](attacker/fix.py)
- 追加: [`attacker/tests/test_ch10.py`](attacker/tests/test_ch10.py)
- 変更: [`app/routers/auth.py`](app/routers/auth.py)

</details>

← [ch09](../ch09)　｜　[一覧](../README.md)　｜　[ch11](../ch11) →
