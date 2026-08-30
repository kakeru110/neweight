# OpenLogi × Shopify 在庫連携 照合レポート

- OpenLogi 出力日: 2026-08-29（配送可在庫）
- Shopify 取得日: 2026-08-30
- 元データ: `docs/data/openlogi-2026-08-29.csv`

> **結論：連携はズレています。** SKUで突合できた134件のうち **61件（46%）が不一致**。
> 正常に連携していれば0件のはずです。しかも大半が「Shopifyのほうが多い」＝**在庫がないのに売れてしまう**方向です。

## 1. 全体サマリー

| 項目 | 件数 |
|---|---|
| OpenLogi 商品行（SKUあり） | 147 |
| Shopify バリアント（SKUあり） | 160 |
| SKUで突合できた | 134 |
| **数量一致** | **73** |
| **数量不一致** | **61** |
| └ Shopify > OpenLogi（オーバーセルrisk） | 57 |
| └ Shopify < OpenLogi（売り逃し） | 4 |

> OpenLogiの「出荷依頼中数」は全行 0 のため、**配送可在庫数 = 総数**。
> つまりこのズレは「出荷準備中の一時的な差」では説明できません。

## 2. 🔴 Shopifyのほうが多い ＝ 在庫がないのに売れてしまう（57件）

在庫切れ商品を注文されると、キャンセル・返金・謝罪が発生します。SNSで露出を増やす前に必ず直すこと。

| SKU | OpenLogi | Shopify | 差 | 商品 / バリアント |
|---|---:|---:|---:|---|
| `eu22-D117-M-tera` | 7 | 15 | **+8** | Flanders Shirts For Dog（ドッグ） / テラコッタ / M |
| `eu22-D110-XS-off` | 5 | 11 | **+6** | RinTinTin Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D122-L-wht` | 3 | 8 | **+5** | Two of a kind Sweat For Dog（ドッグ） / L / ホワイト |
| `eu22-D122-XS-blk` | 8 | 13 | **+5** | Two of a kind Sweat For Dog（ドッグ） / XS / ブラック |
| `eu22-D125-XS-mlt` | 4 | 9 | **+5** | Various dogs Shirts For Dog（ドッグ） / XS |
| `eu22-D117-XS-tera` | 5 | 9 | **+4** | Flanders Shirts For Dog（ドッグ） / テラコッタ / XS |
| `eu22-K107-110-off` | 10 | 13 | **+3** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 110 / オフホワイト |
| `eu22-K107-110-pin` | 7 | 10 | **+3** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 110 / ピンク |
| `eu22-K107-120-pin` | 3 | 6 | **+3** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 120 / ピンク |
| `eu22-K107-130-off` | 5 | 8 | **+3** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 130 / オフホワイト |
| `eu22-K107-130-pin` | 4 | 7 | **+3** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 130 / ピンク |
| `eu22-K107-110-gr` | 10 | 12 | **+2** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 110 / グリーン |
| `eu22-K107-120-gr` | 4 | 6 | **+2** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 120 / グリーン |
| `eu22-K107-130-gr` | 1 | 3 | **+2** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 130 / グリーン |
| `eu22-A100-L-off` | 15 | 16 | **+1** | British Dogs Long Sleeve Tee（アダルト・ユニセックス） / オフホワイト / L |
| `eu22-A100-M-off` | 11 | 12 | **+1** | British Dogs Long Sleeve Tee（アダルト・ユニセックス） / オフホワイト / M |
| `eu22-A103-M-off` | 10 | 11 | **+1** | Brittany Spaniel Short Sleeve Tee(アダルト-ユニセックス) / M / オフホワイト |
| `eu22-D108-L-sumi` | 4 | 5 | **+1** | British Dogs Tank Top For Dog（ドッグ） / スミクロ / L |
| `eu22-D108-M-off` | 7 | 8 | **+1** | British Dogs Tank Top For Dog（ドッグ） / オフホワイト / M |
| `eu22-D108-M-sumi` | 10 | 11 | **+1** | British Dogs Tank Top For Dog（ドッグ） / スミクロ / M |
| `eu22-D108-S-off` | 8 | 9 | **+1** | British Dogs Tank Top For Dog（ドッグ） / オフホワイト / S |
| `eu22-D108-S-sumi` | 10 | 11 | **+1** | British Dogs Tank Top For Dog（ドッグ） / スミクロ / S |
| `eu22-D108-XS-off` | 9 | 10 | **+1** | British Dogs Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D108-XS-sumi` | 9 | 10 | **+1** | British Dogs Tank Top For Dog（ドッグ） / スミクロ / XS |
| `eu22-D109-L-blk` | 4 | 5 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / スミクロ / L |
| `eu22-D109-L-off` | 4 | 5 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / L |
| `eu22-D109-M-blk` | 8 | 9 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / スミクロ / M |
| `eu22-D109-M-off` | 10 | 11 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / M |
| `eu22-D109-M-pin` | 4 | 5 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / ピンク / M |
| `eu22-D109-S-blk` | 7 | 8 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / スミクロ / S |
| `eu22-D109-S-off` | 12 | 13 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / S |
| `eu22-D109-S-pin` | 6 | 7 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / ピンク / S |
| `eu22-D109-XS-off` | 3 | 4 | **+1** | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D111-L-off` | 2 | 3 | **+1** | Flanders Tank Top For Dog（ドッグ） / オフホワイト / L |
| `eu22-D111-L-pin` | 4 | 5 | **+1** | Flanders Tank Top For Dog（ドッグ） / ピンク / L |
| `eu22-D111-M-pin` | 2 | 3 | **+1** | Flanders Tank Top For Dog（ドッグ） / ピンク / M |
| `eu22-D111-S-blk` | 4 | 5 | **+1** | Flanders Tank Top For Dog（ドッグ） / スミクロ / S |
| `eu22-D111-S-off` | 5 | 6 | **+1** | Flanders Tank Top For Dog（ドッグ） / オフホワイト / S |
| `eu22-D111-S-pin` | 8 | 9 | **+1** | Flanders Tank Top For Dog（ドッグ） / ピンク / S |
| `eu22-D111-XS-blk` | 8 | 9 | **+1** | Flanders Tank Top For Dog（ドッグ） / スミクロ / XS |
| `eu22-D111-XS-off` | 7 | 8 | **+1** | Flanders Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D111-XS-pin` | 5 | 6 | **+1** | Flanders Tank Top For Dog（ドッグ） / ピンク / XS |
| `eu22-K104-110-blk` | 7 | 8 | **+1** | British Dogs Long Sleeve Tee For Kids（キッズ） / スミクロ / 110 |
| `eu22-K104-110-off` | 4 | 5 | **+1** | British Dogs Long Sleeve Tee For Kids（キッズ） / オフホワイト / 110 |
| `eu22-K104-120-blk` | 9 | 10 | **+1** | British Dogs Long Sleeve Tee For Kids（キッズ） / スミクロ / 120 |
| `eu22-K104-120-off` | 9 | 10 | **+1** | British Dogs Long Sleeve Tee For Kids（キッズ） / オフホワイト / 120 |
| `eu22-K105-110-blk` | 8 | 9 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / スミクロ / 110 |
| `eu22-K105-110-off` | 13 | 14 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / オフホワイト / 110 |
| `eu22-K105-110-pin` | 10 | 11 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / ピンク / 110 |
| `eu22-K105-120-blk` | 7 | 8 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / スミクロ / 120 |
| `eu22-K105-120-off` | 2 | 3 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / オフホワイト / 120 |
| `eu22-K105-120-pin` | 4 | 5 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / ピンク / 120 |
| `eu22-K105-130-off` | 2 | 3 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / オフホワイト / 130 |
| `eu22-K105-130-pin` | 4 | 5 | **+1** | Flanders Long Sleeve Tee For Kids（キッズ） / ピンク / 130 |
| `eu22-K106-110-off` | 8 | 9 | **+1** | RinTinTin Short Sleeve Tee For Kids（キッズ） / 110 / オフホワイト |
| `eu22-K107-120-off` | 0 | 1 | **+1** | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 120 / オフホワイト |
| `eu22-K124-110-off` | 0 | 1 | **+1** | Various dogs Long Sleeve Shirts For Kids（キッズ） / 110 |

## 3. 🟡 Shopifyのほうが少ない ＝ 売れるのに売り逃している（4件）

| SKU | OpenLogi | Shopify | 差 | 商品 / バリアント |
|---|---:|---:|---:|---|
| `eu22-D117-S-tera` | 15 | 7 | **-8** | Flanders Shirts For Dog（ドッグ） / テラコッタ / S |
| `eu22-D122-S-blk` | 9 | 4 | **-5** | Two of a kind Sweat For Dog（ドッグ） / S / ブラック |
| `eu22-D122-S-wht` | 13 | 9 | **-4** | Two of a kind Sweat For Dog（ドッグ） / S / ホワイト |
| `eu22-D122-M-wht` | 9 | 8 | **-1** | Two of a kind Sweat For Dog（ドッグ） / M / ホワイト |

## 4. 🔴 SKU表記ゆれで、そもそも紐付いていない（8件）

同じ現物なのに、OpenLogiとShopifyでSKUの綴りが違うため**連携対象から外れている**もの。
在庫が動いても永久に同期されません。

| 現物 | OpenLogi SKU | Shopify SKU | OL在庫 | 原因 |
|---|---|---|---:|---|
| Brittany Spaniel 大人 L/グリーン | `eu22-A103-L-grn` | `eu22-A103-L-gr` | 11 | グリーンが `grn` / `gr` |
| Brittany Spaniel 大人 M/グリーン | `eu22-A103-M-grn` | `eu22-A103-M-gr` | 9 | 同上 |
| Brittany Spaniel キッズ 110/スミクロ | `eu22-K107-110-sumi` | `eu22-K107-110-blk` | 11 | スミクロが `sumi` / `blk` |
| Brittany Spaniel キッズ 120/スミクロ | `eu22-K107-120-sumi` | `eu22-K107-120-blk` | 1 | 同上 |
| Brittany Spaniel キッズ 130/スミクロ | `eu22-K107-130-sumi` | `eu22-K107-130-blk` | 2 | 同上 |
| Flanders 大人 半袖シャツ L/テラコッタ | `eu22-A113-L-tera` | **未設定** | 24 | Shopify側にSKUが無い |
| Flanders キッズ 半袖シャツ 120 | `eu22-K115-120-tera` | **未設定** | 8 | 同上 |
| Flanders キッズ 半袖シャツ 130 | `eu22-K115-130-tera` | **未設定** | 4 | 同上 |

> `eu22-A113-L-tera` は **24点**。ここが繋がっていないのは、そのまま売り逃しです。

## 5. 🔴 ShopifyでSKU未設定のバリアント（11件・連携不能）

| 商品 / バリアント | 状態 | Shopify在庫 |
|---|---|---:|
| Flanders Short Sleeve Shirts / L / テラコッタ | ACTIVE | 4 |
| Flanders Short Sleeve Shirts For Kids / 120 / テラコッタ | ACTIVE | 8 |
| Flanders Short Sleeve Shirts For Kids / 130 / テラコッタ | ACTIVE | 4 |
| Sumif×TheTENT British Dogs マルチマット | DRAFT | 2 |
| British Dogs サーモボトル | DRAFT | 0 |
| Playing Dog Sweat（アダルト）ホワイトL / グリーンM / グリーンL | DRAFT | 0 |
| 【受注生産】Eat up your dinner Sweat / ブラック / M | ARCHIVED | 5 |
| 【受注生産】Let's Play Long Sleeve Tee / ホワイト / M | ARCHIVED | 3 |
| 【受注生産】Let's Play Sweat For Dog / ブラック / XS | ARCHIVED | 1 |

**ACTIVEな3件（Flandersシャツ系）は今すぐSKUを設定すべき。** OpenLogi側にはSKUがあります。

## 6. 🔴 NOIコラボTee「在庫116点」の正体

前回の診断で「実物確認が必要」としていた件、答えが出ました。

- **OpenLogiの在庫リストに、NOIコラボTeeは1行も存在しない。**
- さらにShopify側のSKUが `eu22-A103-L-wht` / `eu22-A103-M-gry` / `eu22-A103-L-gry` と、
  **Brittany Spaniel 大人用（A103）のSKU体系を流用している**（正しい形式は残る1件の `eu26-A200-M-wht` のみ）

→ **この116点は倉庫の実在庫ではない可能性が非常に高い。** 受注生産の記録がShopify上に残ったものと考えられます。
　 かつSKUの流用は、今後この商品を公開した際に Brittany Spaniel の在庫と取り違える事故を招きます。

**対応（要判断）**
1. 現物が倉庫にあるか、OpenLogi管理外の場所（自社・イベント在庫）にあるかを確認する
2. 実在庫でないなら Shopify の在庫を 0 に修正する（分析が狂う原因を断つ）
3. 実在庫なら SKU を `eu26-A200-*` 体系に振り直してからOpenLogiに登録する

## 7. 対応の優先順位

| # | やること | なぜ |
|---|---|---|
| 1 | SKU表記ゆれ8件をShopify側に合わせて統一（`grn`→`gr`、`sumi`→`blk` 等、どちらに寄せるかは要決定） | 恒久的に同期されないため |
| 2 | ACTIVEなSKU未設定3件（Flandersシャツ系）にSKUを付与 | ACTIVEなのに連携不能 |
| 3 | NOI Tee 116点の実在庫確認と是正 | 全分析の前提が狂う |
| 4 | 不一致61件をOpenLogi側の数字で上書き（棚卸し） | オーバーセル防止 |
| 5 | 連携の仕組み自体を点検（アプリ設定・在庫ロケーション） | 同じズレが再発するため |

> **5が本丸です。** 1〜4で数字を合わせても、連携が止まっていれば翌週にはまたズレます。
> OpenLogi連携アプリが有効か、Shopify側の在庫ロケーションがOpenLogi倉庫に紐付いているかを確認してください。

## 8. この照合の再実行方法

OpenLogi管理画面から「配送可在庫」CSV/Excelをダウンロードし、
`sumif-merchandiser` に「OpenLogiの在庫リストとShopifyを照合して」と依頼すれば、
同じレポートを再生成できます。**月1回の棚卸しとして回すことを推奨。**

---

# 追記（2026-08-30）SKU表記ゆれの統一を実施

## やったこと

**Shopify側のSKUをOpenLogiの表記に合わせました**（8件）。
OpenLogiは倉庫に現物が登録されている側なので、直すなら現物を触らずに済む
Shopify側のテキストが正解。API（`productVariantsBulkUpdate`）で全自動、手作業ゼロで完了。

| 商品 / バリアント | 変更前（Shopify） | 変更後 |
|---|---|---|
| Brittany Spaniel 大人 M/グリーン | `eu22-A103-M-gr` | `eu22-A103-M-grn` |
| Brittany Spaniel 大人 L/グリーン | `eu22-A103-L-gr` | `eu22-A103-L-grn` |
| Brittany Spaniel キッズ 110/スミクロ | `eu22-K107-110-blk` | `eu22-K107-110-sumi` |
| Brittany Spaniel キッズ 120/スミクロ | `eu22-K107-120-blk` | `eu22-K107-120-sumi` |
| Brittany Spaniel キッズ 130/スミクロ | `eu22-K107-130-blk` | `eu22-K107-130-sumi` |
| Flanders 大人 半袖シャツ L/テラコッタ | （未設定） | `eu22-A113-L-tera` |
| Flanders キッズ 半袖シャツ 120/テラコッタ | （未設定） | `eu22-K115-120-tera` |
| Flanders キッズ 半袖シャツ 130/テラコッタ | （未設定） | `eu22-K115-130-tera` |

## 結果

| 指標 | 実施前 | 実施後 |
|---|---:|---:|
| 突合できたSKU | 134 | **142** |
| 数量一致 | 73 | 77 |
| 数量不一致 | 61 | 65 |
| OpenLogiにあってShopifyに無い | 13 | **5** |

> **不一致が61→65に増えたのは悪化ではありません。**
> これまで比較すらできなかった8件が比較可能になり、そのうち4件が実際にズレていた、というだけです。
> 見えていなかった問題が見えるようになった状態です。

## 🔴 直した結果、判明した実害

| SKU | OpenLogi | Shopify | 差 | 意味 |
|---|---:|---:|---:|---|
| `eu22-A113-L-tera`（Flanders大人 半袖シャツ L） | **24** | **4** | **-20** | **20点が売り場に出ていない。丸ごと機会損失** |
| `eu22-K107-110-sumi`（BSキッズ 110/スミクロ） | 11 | 14 | +3 | 在庫がないのに売れる |
| `eu22-K107-120-sumi`（BSキッズ 120/スミクロ） | 1 | 4 | +3 | 同上 |
| `eu22-K107-130-sumi`（BSキッズ 130/スミクロ） | 2 | 5 | +3 | 同上 |

残り4件（グリーン2件、Flandersキッズ2件）は**ぴったり一致**しました。

> `eu22-A113-L-tera` の20点差が今回いちばん大きな収穫です。
> ¥10,000 の商品なので、単純計算で20万円分が売り場から消えていたことになります。

## 残っている「OpenLogiにあってShopifyに無い」5件

| SKU | OL在庫 | 商品 | 判断 |
|---|---:|---|---|
| `eu22-Z131` | 2 | Sumif×TheTENT British Dogs マルチマット | DRAFT。公開するならSKU付与が必要 |
| `eu22-tentbag-bge` / `-cha` / `-olv` | 0 | Drawstring Bag 各種 | 在庫0。対応不要 |
| `shopcard` | 148 | ショップカード | 販売商品ではない。対応不要 |

**アパレルの表記ゆれはこれで解消済み。** 実質の残件はマルチマット1件（DRAFT）だけです。

## ⚠️ これ以上のSKU「整理」はしないこと

ストア全体のSKUは、色コードの綴りが揃っていません。

- スミクロ: `blk`（Brittany大人・British Dogsキッズ・Flandersキッズ 等） /
  `sumi`（British Dogsドッグ・Brittanyキッズ） / `sum`（RinTinTinドッグ）
- グリーン: `gr`（Brittanyキッズ） / `grn`（Brittany大人・Brittanyドッグ・Playing Dog）

見た目は気持ち悪いですが、**OpenLogiとShopifyの双方が同じ綴りで一致していれば連携上は何の問題もありません。**
統一しようとしてShopify側を一括リネームすると、いま繋がっている142件のリンクを壊します。

> **触るのは「両者が食い違っているSKU」だけ。** 綺麗さのためのリネームはしない。
