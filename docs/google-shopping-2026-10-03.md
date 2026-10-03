# Googleショッピング 無料リスティング 調査と是正（2026-10-03）

## 経緯

楽天などへの出店を検討する前に、**すでに接続済みで無料のチャネル**を確認した。

## 🔴 Googleアカウントの接続が切れていた

Google & YouTube チャネルを開くと：

> `sumifofficial@gmail.com` は Google & YouTube アプリにアクセスできなくなっています。
> これにより、**商品が Google に同期されなかったり**…

**「確認」ボタンから再ログインして復旧。**（「リンクを解除」を押すとMerchant Center・
Google広告・YouTubeの接続が全部切れるので押さないこと）

> **誤判断の記録**: アプリの権限ページに「最近のアクティビティ 44分前」と出ていたので
> 「動いている」と判断したが、**あれはアプリがShopify側のデータを読んだ記録**で、
> Google側への送信とは別物だった。訂正済み。

## 復旧後の状態

| 合計 | 承認済み | 制限付き | 不承認 | 審査中 |
|---:|---:|---:|---:|---:|
| 152 | **150** | 0 | **2** | 0 |

**150件が承認済み。** 商品データ自体は問題なく通っていた。接続だけが切れていた。

## 残っている警告 2件

### ① Invalid business name

> The provided business name doesn't comply with Google policies

**原因はストア名が `sumif_official` のままであること**と考えられる。
商品ページの構造化データ（JSON-LD）にも出ている：

```json
"brand": { "@type": "Brand", "name": "sumif_official" }
```

ブランド名は2026-09-27に `Sumif` に統一すると決めたが、**ストア名だけ未変更**だった。
Googleの検索結果・ショッピングタブに `sumif_official` と表示される。

**是正**: 設定 → 一般設定 → ストア名を `Sumif` に変更。
`https://admin.shopify.com/store/sumif-official/settings/general`

> ストア名は**注文確認メールの差出人名などにも出る**ので、変更すると表示が一斉に変わる。

### ② Invalid square logo

> Square logos must be viewable at a small scale, have an aspect ratio of 1:1,
> and be in SVG, PNG, or WebP format

**是正**: `docs/data/brand-assets/` に正方形ロゴを作成した。

| ファイル | サイズ |
|---|---|
| `sumif-square-logo-1000.png` | 1000×1000 |
| `sumif-square-logo-512.png` | 512×512 |

ヘッダーロゴ（1276×709）から **`Sumif` のワードマークだけを切り出し**、
白地の正方形に中央配置した。
`SINCE 2022 JAPAN,TOKYO` の行は**小さく表示すると潰れて読めない**ので落とした。

Merchant Center → ビジネス情報 → ブランディング からアップロードする。

## Google広告のエラーは無視してよい

> Google 広告アカウントが無効になっています／お支払い情報の設定を確認する

**広告を出していないので実害なし。** 無料リスティングは Google広告アカウントと無関係。
いま触る必要はない。

## 次に確認すること

- [ ] Merchant Center → 成長 → プログラムを管理 → **無料リスティングが有効か**
      （オプトインが必要。オフだと承認済みでも載らない）
- [ ] **不承認の2件**が何か（Merchant Center → 商品 → 診断）
- [ ] 1週間後、`FROM sessions ... GROUP BY referrer_source` で search が
      34（30日）から動いたか

## 教訓

**Shopify側が繋がっていても、相手側で止まっていることがある。**

| | 症状 |
|---|---|
| Meta | 商品タグの選択肢に大人用が出なかった（カタログ側のラグ） |
| **Google** | **アカウント接続が切れて同期停止** |
| Pinterest | マーチャントステータス承認済み。現状は正常 |

**接続済み＝機能している、ではない。** 定期的に各チャネルの管理画面を開いて確認する。
