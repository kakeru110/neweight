# 削除したコレクションの記録 2026-10-02

削除は元に戻せないため、削除前の中身をここに保存する。
再作成する場合は、この一覧の商品を手で入れ直すこと。
`status` が ACTIVE 以外の商品はストアフロントに出ていなかった。

## スマートコレクション（条件が分かっているので再作成は容易）

| コレクション | handle | 条件 |
|---|---|---|
| アダルト用 | `アダルト用` | 商品名が「アダルト」を含む |
| キッズ用 | `キッズ用` | 商品名が「キッズ」を含む |
| 愛犬用ウェア | `愛犬用ウェア` | 商品タイプが「犬用ウェア」と一致 |

いずれも `Adult` / `Kids` / `Dog` と内容が重複していた。

## 手動コレクション（商品の割り当てを記録）

### New（`new`）
DRAFT: British Dogs サーモボトル / Sumif×TheTENT British Dogs マルチマット /
Playing Dog Sweat（アダルト）/ Two of a kind Sweat（アダルト）/ Sumif × NOI Exclusive Order Tee
ACTIVE: Playing Dog Sweat For Dog / Two of a kind Sweat For Dog / Various dogs Shirts For Dog /
Various dogs Long Sleeve Shirts(アダルト) / Various dogs Long Sleeve Shirts For Kids
ARCHIVED: 【受注生産】Eat up your dinner Sweat / 【受注生産】Let's Play Long Sleeve Tee / 【受注生産】Let's Play Sweat For Dog

### 22 S/S（`22-s-s`）
ACTIVE 18点: British Dogs LS Shirts(アダルト) / Flanders Shirts For Dog / Flanders SS Shirts(アダルト) /
Flanders LS Tee(アダルト) / British Dogs LS Tee(アダルト) / Brittany Spaniel Tank For Dog /
Brittany Spaniel SS Tee(アダルト) / British Dogs Shirts For Dog / British Dogs Tank For Dog /
British Dogs LS Shirts For Kids / Flanders Tank For Dog / RinTinTin SS Tee(アダルト) /
Flanders LS Tee For Kids / Brittany Spaniel SS Tee For Kids / Flanders SS Shirts For Kids /
RinTinTin Tank For Dog / RinTinTin SS Tee For Kids / British Dogs LS Tee For Kids
DRAFT 1点: Sumif × NOI Exclusive Order Tee

### TOP（`top`）/ Sumif（`sumif`）
ほぼ全商品（ACTIVE 23点＋DRAFT・ARCHIVED）が入っていた、実質 All Items の重複。
TOP は 34点、Sumif は 31点。内容は `All Items` でカバーできる。

### Shirt（`shirt`）
ACTIVE 9点（シャツ全点）: British Dogs LS Shirts(アダルト) / Various dogs Shirts For Dog /
Various dogs LS Shirts(アダルト) / Flanders Shirts For Dog / Flanders SS Shirts(アダルト) /
British Dogs Shirts For Dog / British Dogs LS Shirts For Kids /
Various dogs LS Shirts For Kids / Flanders SS Shirts For Kids

### T-shirt（`t-shirt`）
ACTIVE 15点: Playing Dog Sweat For Dog / Flanders LS Tee(アダルト) / British Dogs LS Tee(アダルト) /
Brittany Spaniel Tank For Dog / Brittany Spaniel SS Tee(アダルト) / British Dogs Tank For Dog /
Flanders Tank For Dog / RinTinTin SS Tee(アダルト) / Two of a kind Sweat For Dog /
Flanders LS Tee For Kids / Brittany Spaniel SS Tee For Kids / RinTinTin Tank For Dog /
RinTinTin SS Tee For Kids / British Dogs LS Tee For Kids
DRAFT 2点: Two of a kind Sweat（アダルト）/ Playing Dog Sweat（アダルト）/ Sumif × NOI Exclusive Order Tee

**注意**: `Shirt` と `T-shirt` は「シャツだけ見たい」「Tシャツだけ見たい」という
カテゴリ軸としては有効だった。どこからもリンクされていなかったため提案どおり削除したが、
必要になったらこの一覧から作り直せる。
