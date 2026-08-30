# 在庫棚卸し実行ログ（2026-08-30）

OpenLogi配送可在庫（2026-08-29出力）を正として、Shopifyの `Open Logi 倉庫` ロケーションを上書きした全記録。
`inventorySetQuantities`（name=on_hand / reason=correction / CASチェック付き）で実行。
Shopify管理画面の在庫履歴にも `correction` として残っている。

戻す必要が生じた場合は、下表の「変更前」列の値に戻せばよい。

## 【2】増やした 4件（+18点）— 売り逃していた分

| SKU | 変更前 | 変更後 | 差 | 商品 / バリアント |
|---|---:|---:|---:|---|
| `eu22-D117-S-tera` | 7 | 15 | **+8** | Flanders Shirts For Dog（ドッグ） / テラコッタ / S |
| `eu22-D122-S-blk` | 4 | 9 | **+5** | Two of a kind Sweat For Dog（ドッグ） / S / ブラック |
| `eu22-D122-S-wht` | 9 | 13 | **+4** | Two of a kind Sweat For Dog（ドッグ） / S / ホワイト |
| `eu22-D122-M-wht` | 8 | 9 | **+1** | Two of a kind Sweat For Dog（ドッグ） / M / ホワイト |

## 【1】減らした 57件（-91点）— 実在しないのに売れていた分

| SKU | 変更前 | 変更後 | 差 | 商品 / バリアント |
|---|---:|---:|---:|---|
| `eu22-D117-M-tera` | 15 | 7 | -8 | Flanders Shirts For Dog（ドッグ） / テラコッタ / M |
| `eu22-D122-L-wht` | 8 | 3 | -5 | Two of a kind Sweat For Dog（ドッグ） / L / ホワイト |
| `eu22-D122-XS-blk` | 13 | 8 | -5 | Two of a kind Sweat For Dog（ドッグ） / XS / ブラック |
| `eu22-K107-110-off` | 13 | 10 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 110 / オフホワイト |
| `eu22-K107-110-pin` | 10 | 7 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 110 / ピンク |
| `eu22-K107-110-sumi` | 14 | 11 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 110 / スミクロ |
| `eu22-K107-120-pin` | 6 | 3 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 120 / ピンク |
| `eu22-K107-120-sumi` | 4 | 1 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 120 / スミクロ |
| `eu22-K107-130-off` | 8 | 5 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 130 / オフホワイト |
| `eu22-K107-130-pin` | 7 | 4 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 130 / ピンク |
| `eu22-K107-130-sumi` | 5 | 2 | -3 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 130 / スミクロ |
| `eu22-K107-110-gr` | 12 | 10 | -2 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 110 / グリーン |
| `eu22-K107-120-gr` | 6 | 4 | -2 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 120 / グリーン |
| `eu22-K107-130-gr` | 3 | 1 | -2 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 130 / グリーン |
| `eu22-A100-L-off` | 16 | 15 | -1 | British Dogs Long Sleeve Tee（アダルト・ユニセックス） / オフホワイト / L |
| `eu22-A100-M-off` | 12 | 11 | -1 | British Dogs Long Sleeve Tee（アダルト・ユニセックス） / オフホワイト / M |
| `eu22-A103-M-off` | 11 | 10 | -1 | Brittany Spaniel Short Sleeve Tee(アダルト-ユニセックス) / M / オフホワイト |
| `eu22-D108-L-sumi` | 5 | 4 | -1 | British Dogs Tank Top For Dog（ドッグ） / スミクロ / L |
| `eu22-D108-M-off` | 8 | 7 | -1 | British Dogs Tank Top For Dog（ドッグ） / オフホワイト / M |
| `eu22-D108-M-sumi` | 11 | 10 | -1 | British Dogs Tank Top For Dog（ドッグ） / スミクロ / M |
| `eu22-D108-S-off` | 9 | 8 | -1 | British Dogs Tank Top For Dog（ドッグ） / オフホワイト / S |
| `eu22-D108-S-sumi` | 11 | 10 | -1 | British Dogs Tank Top For Dog（ドッグ） / スミクロ / S |
| `eu22-D108-XS-off` | 10 | 9 | -1 | British Dogs Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D108-XS-sumi` | 10 | 9 | -1 | British Dogs Tank Top For Dog（ドッグ） / スミクロ / XS |
| `eu22-D109-L-blk` | 5 | 4 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / スミクロ / L |
| `eu22-D109-L-off` | 5 | 4 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / L |
| `eu22-D109-M-blk` | 9 | 8 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / スミクロ / M |
| `eu22-D109-M-off` | 11 | 10 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / M |
| `eu22-D109-M-pin` | 5 | 4 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / ピンク / M |
| `eu22-D109-S-blk` | 8 | 7 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / スミクロ / S |
| `eu22-D109-S-off` | 13 | 12 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / S |
| `eu22-D109-S-pin` | 7 | 6 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / ピンク / S |
| `eu22-D109-XS-off` | 4 | 3 | -1 | Brittany Spaniel Short Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D110-XS-off` | 6 | 5 | -1 | RinTinTin Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D111-L-off` | 3 | 2 | -1 | Flanders Tank Top For Dog（ドッグ） / オフホワイト / L |
| `eu22-D111-L-pin` | 5 | 4 | -1 | Flanders Tank Top For Dog（ドッグ） / ピンク / L |
| `eu22-D111-M-pin` | 3 | 2 | -1 | Flanders Tank Top For Dog（ドッグ） / ピンク / M |
| `eu22-D111-S-blk` | 5 | 4 | -1 | Flanders Tank Top For Dog（ドッグ） / スミクロ / S |
| `eu22-D111-S-off` | 6 | 5 | -1 | Flanders Tank Top For Dog（ドッグ） / オフホワイト / S |
| `eu22-D111-S-pin` | 9 | 8 | -1 | Flanders Tank Top For Dog（ドッグ） / ピンク / S |
| `eu22-D111-XS-blk` | 9 | 8 | -1 | Flanders Tank Top For Dog（ドッグ） / スミクロ / XS |
| `eu22-D111-XS-off` | 8 | 7 | -1 | Flanders Tank Top For Dog（ドッグ） / オフホワイト / XS |
| `eu22-D111-XS-pin` | 6 | 5 | -1 | Flanders Tank Top For Dog（ドッグ） / ピンク / XS |
| `eu22-K104-110-blk` | 8 | 7 | -1 | British Dogs Long Sleeve Tee For Kids（キッズ） / スミクロ / 110 |
| `eu22-K104-110-off` | 5 | 4 | -1 | British Dogs Long Sleeve Tee For Kids（キッズ） / オフホワイト / 110 |
| `eu22-K104-120-blk` | 10 | 9 | -1 | British Dogs Long Sleeve Tee For Kids（キッズ） / スミクロ / 120 |
| `eu22-K104-120-off` | 10 | 9 | -1 | British Dogs Long Sleeve Tee For Kids（キッズ） / オフホワイト / 120 |
| `eu22-K105-110-blk` | 9 | 8 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / スミクロ / 110 |
| `eu22-K105-110-off` | 14 | 13 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / オフホワイト / 110 |
| `eu22-K105-110-pin` | 11 | 10 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / ピンク / 110 |
| `eu22-K105-120-blk` | 8 | 7 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / スミクロ / 120 |
| `eu22-K105-120-off` | 3 | 2 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / オフホワイト / 120 |
| `eu22-K105-120-pin` | 5 | 4 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / ピンク / 120 |
| `eu22-K105-130-off` | 3 | 2 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / オフホワイト / 130 |
| `eu22-K105-130-pin` | 5 | 4 | -1 | Flanders Long Sleeve Tee For Kids（キッズ） / ピンク / 130 |
| `eu22-K106-110-off` | 9 | 8 | -1 | RinTinTin Short Sleeve Tee For Kids（キッズ） / 110 / オフホワイト |
| `eu22-K107-120-off` | 1 | 0 | -1 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） / 120 / オフホワイト |
