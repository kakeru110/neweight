# 棚の整理 — 在庫0の確認と、コレクションを在庫順に並べ替え

実施: 2026-09-23 / 在庫はすべて **Open Logi 倉庫** のみで集計（原田家・鎌倉・高輪は除外）

---

## 1. 在庫の全体像（2026-09-23 時点・OpenLogiロケーション）

**ACTIVE 23商品 / 151SKU / 合計 827点。うち 24SKU が在庫0。**

| # | 商品 | OL在庫 | 在庫0のSKU |
|---|---|---:|---|
| 1 | Brittany Spaniel Short Sleeve Tee（アダルト） | **80** | — |
| 2 | Brittany Spaniel Short Tank Top For Dog | **79** | ピンク/L、グリーン/L |
| 3 | Two of a kind Sweat For Dog | **64** | — |
| 4 | RinTinTin Tank Top For Dog | **62** | — |
| 5 | Brittany Spaniel Short Sleeve Tee For Kids | **58** | オフホワイト/120 |
| 6 | British Dogs Tank Top For Dog | **57** | オフホワイト/L |
| 7 | Flanders Long Sleeve Tee For Kids | **55** | — |
| 8 | RinTinTin Short Sleeve Tee For Kids | 50 | — |
| 9 | Flanders Tank Top For Dog | 46 | オフホワイト/M、スミクロ/L |
| 10 | RinTinTin Short Sleeve Tee（アダルト） | 45 | — |
| 11 | Flanders Short Sleeve Shirts（アダルト） | 38 | — |
| 12 | British Dogs Long Sleeve Tee For Kids | 35 | — |
| 13 | Flanders Shirts For Dog | 27 | テラコッタ/L |
| 14 | British Dogs Long Sleeve Tee（アダルト） | 26 | **スミクロ/M、スミクロ/L** |
| 15 | Playing Dog Sweat For Dog | 16 | グリーンXS/M/L、ブラック/L |
| 16 | Flanders Long Sleeve Tee（アダルト） | 14 | オフホワイト/M、スミクロ/L |
| 17 | British Dogs Long Sleeve Shirts For Kids | 14 | 130 |
| 18 | Flanders Short Sleeve Shirts For Kids | 14 | — |
| 19 | Various dogs Long Sleeve Shirts（アダルト） | 12 | M |
| 20 | British Dogs Long Sleeve Shirts（アダルト） | 11 | オフホワイト/M |
| 21 | Various dogs Shirts For Dog | 11 | M、L |
| 22 | British Dogs Shirts For Dog | 9 | M、L |
| 23 | Various dogs Long Sleeve Shirts For Kids | **4** | 110、130 |

---

## 2. 確認した結果、直す必要がなかったこと

### 2.1 「全サイズ在庫0」の商品は1つもない

棚から下ろす（ARCHIVE / 下書きに戻す）対象は **ゼロ件**だった。
在庫0は24SKUあるが、いずれも同じ商品の別の色・サイズには在庫がある。
在庫0のSKUは商品ページのプルダウンに「売り切れ」と出て選べない状態になっており、
これは正しい挙動なので触っていない。

### 2.2 在庫切れでも購入できてしまう設定は1つもない

151SKU すべて `inventoryPolicy: DENY`（在庫切れ時は販売停止）だった。
売り越しのリスクはない。

### 2.3 OpenLogi以外の在庫は、そもそも販売数に入っていない

ロケーション設定を確認したところ：

| ロケーション | オンライン注文の出荷 |
|---|---|
| Open Logi 倉庫 | **ON** |
| 原田家 / 鎌倉 / 高輪 | **OFF** |

つまりストアが販売できるのは OpenLogi の在庫だけで、
`CLAUDE.md` の 🔴 在庫の大原則は**設定としては既に守られている**。

実際に、Shopify全ロケーション合計では在庫がある4SKUを確認したところ、
すべて正しく「売り切れ」表示になっていた。

| SKU | 全拠点合計 | OpenLogi | サイトの表示 |
|---|---:|---:|---|
| Various dogs Kids 110 | 1 | 0 | 売り切れ ✅ |
| RinTinTin Dog オフホワイト/XS | 10 | 5 | 在庫あり（5点ぶん） |
| Flanders Dog テラコッタ/XS | 9 | 5 | 在庫あり（5点ぶん） |
| Various dogs Dog XS | 9 | 4 | 在庫あり（4点ぶん） |

**ただし `inventoryQuantity` を読むと最大2倍以上ズレる**ことは変わらないので、
判断には引き続き `inventoryLevels` の Open Logi 倉庫だけを使うこと。

---

## 3. 実施したこと: コレクションを在庫順に並べ替え

### 並べ替えの方針

1. **柄ライン単位でまとめる**（大人・キッズ・ドッグの3点は離さない）
   — sumifの強みは「家族3者が同じ絵柄で揃う」ことなので、在庫順でバラバラにしない
2. **ラインの合計在庫が多い順**に上から並べる
3. ライン内は **大人 → キッズ → ドッグ**

### ライン別の合計在庫

| ライン | 合計 |
|---|---:|
| Brittany Spaniel | **217** |
| RinTinTin | **157** |
| British Dogs（ロングスリーブTee） | 118 |
| Flanders（ロングスリーブTee） | 115 |
| 犬用スウェット2型 | 80 |
| Flanders（ショートスリーブシャツ） | 79 |
| British Dogs（シャツ） | 34 |
| Various dogs | **27** |

### 変更した4コレクション

| コレクション | 変更前の先頭 | 変更後の先頭 |
|---|---|---|
| **All Items**（トップページもここを参照） | Brittany Spaniel（偶然よかった） | Brittany Spaniel → RinTinTin → British Dogs … |
| **Adult** | British Dogs Long Sleeve Shirts（**在庫11＝最下位**） | Brittany Spaniel（80） |
| **Kids** | Flanders Long Sleeve Tee（55） | Brittany Spaniel（58） |
| **Dog** | Flanders Shirts For Dog（27） | Brittany Spaniel（79） |

Adult は**いちばん在庫の薄い商品が先頭**という最悪の並びだった。

シリーズ別コレクション（British Dogs / RinTinTin / Flanders / Brittany Spaniel / Various dogs）は
既に「ライン単位 → 大人・キッズ・ドッグ」の順に並んでおり、在庫順の観点でも妥当だったため**変更していない**。

### ページ送りの副作用が1つ解消した

コレクションページは **20件でページ送り**される。
変更前の All Items では、1ページ目に入れなかった3商品が

- British Dogs Tank Top For Dog（**57点**）
- Two of a kind Sweat For Dog（**64点**）
- Playing Dog Sweat For Dog（16点）

だった。**在庫137点ぶんが2ページ目に隠れていた。**
変更後は、1ページ目から外れるのは Various dogs の3商品（合計27点＝最も薄い）だけになった。

変更前の並び順は `docs/data/collection-order-backup-2026-09-23.json` に保存済み。

---

## 4. 残る課題（今回は触っていない）

### 4.1 行き止まりの色が1つある

**British Dogs Long Sleeve Tee（アダルト）の「スミクロ」は M・L とも在庫0。**
色を選んでも全サイズ売り切れになる、唯一の完全な行き止まり。

バリアントを削除すれば消せるが、

- 削除は**元に戻せない**
- SKU（`eu22-A100-M-blk` / `-L-blk`）が消えると **OpenLogiとの139SKU突合が崩れる**

ため、今回は残した。削除するかどうかは要判断。

### 4.2 実質終了している商品

| 商品 | 状態 |
|---|---|
| Various dogs Long Sleeve Shirts For Kids | **120の4点のみ**。110・130は0 |
| Playing Dog Sweat For Dog | グリーンは**Sの2点のみ**。ブラックは13点 |
| British Dogs Shirts For Dog | オフホワイトのXS1点・S8点のみ。M・Lは0 |
| British Dogs Long Sleeve Shirts（アダルト） | **Lの11点のみ**。Mは0 |

いずれも並べ替えで下に移動済み。売り切ったら下ろす。

### 4.3 在庫順は自動で追随しない

Shopifyのコレクションに「在庫の多い順」というソートは存在しないため、
今回は**手動の並び順**を在庫順に設定した。
売れて在庫が変われば実態とズレるので、**月初の棚卸しのタイミングで並べ直す**のがよい。
