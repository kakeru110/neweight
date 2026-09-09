# 英語翻訳の修正ログ（2026-09-08）

## 実行済み：作家名 norahi の誤訳を修正（9件）

英語の商品説明で、アーティスト **norahi** の名前が **「quantity：」** と誤訳されていた問題を修正。
`translationsRegister` で `body_html` の該当箇所のみを置換（`quantity：` → `norahi:`）。
他の文言・HTMLタグは一切変更していない。

| 商品ID | 商品 |
|---|---|
| 7461688082670 | Flanders Long Sleeve Tee（アダルト・ユニセックス） |
| 7461695258862 | Flanders Long Sleeve Tee For Kids（キッズ） |
| 7461700927726 | Flanders Tank Top For Dog（ドッグ） |
| 7461723504878 | Flanders Short Sleeve Shirts For Kids（キッズ） |
| 7461726028014 | Flanders Shirts For Dog（ドッグ） |
| 7461727699182 | Brittany Spaniel Short Sleeve Tee(アダルト-ユニセックス) |
| 7461864341742 | Brittany Spaniel Short Sleeve Tee For Kids（キッズ） |
| 7461871747310 | Brittany Spaniel Short Tank Top For Dog（ドッグ） |
| 7880443822318 | Sumif×TheTENT Flanders マルチマット（DRAFT） |

**検証済み**: 全34商品の英語翻訳を再取得し、9件すべてで `norahi:` を確認。

> なお `Flanders Short Sleeve Shirts（アダルト）`（7461721309422）は元から
> `norahi: illustrator/artist` と正しく入っていたため対象外。

---

## ✅ 対応済み：英語翻訳が「別商品のもの」になっていた問題（9件・2026-09-09）

**方針B（書き直す）で対応完了。** 日本語原文から正しい英語を新規に作成し、
`title` / `body_html` / `meta_title` を差し替えた。

| 日本語（実際の商品） | 修正後の英語タイトル | 状態 |
|---|---|---|
| Various dogs Long Sleeve Shirts(アダルト) | Various dogs Long Sleeve Shirt (Adult / Unisex) | ACTIVE |
| Various dogs Long Sleeve Shirts For Kids | Various dogs Long Sleeve Shirt for Kids | ACTIVE |
| Various dogs Shirts For Dog | Various dogs Shirt for Dogs | ACTIVE |
| Playing Dog Sweat For Dog | Playing Dog Sweatshirt for Dogs | ACTIVE |
| Two of a kind Sweat For Dog | Two of a kind Sweatshirt for Dogs | ACTIVE |
| Playing Dog Sweat（アダルト） | Playing Dog Sweatshirt (Adult / Unisex) | DRAFT |
| Two of a kind Sweat（アダルト） | Two of a kind Sweatshirt (Adult / Unisex) | DRAFT |
| Sumif × NOI Exclusive Order Tee | Sumif × NOI Exclusive Order Tee | DRAFT |
| Sumif×The TENT Drawstring Bag | **翻訳を削除**（下記） | DRAFT |

### 書き直しの方針

- 日本語原文の**素材・サイズ・着用モデル（犬種と体重）を1つも落とさず**英訳
- 作家名は正しい人物を記載（Various dogs = Nelson Mirei / Playing Dog = norahi /
  Two of a kind・NOI Tee = NOI）
- legacy な `data-mce-fragment` だらけのHTMLをやめ、
  `Description / Material / Size / Sumif / Art` の清潔な構造に統一
- NOI Tee は受注期間が終了しているため、その事実を明記

### Drawstring Bag だけ「削除」にした理由

**日本語の商品説明が空だった**（`descriptionHtml` は `<meta charset="UTF-8">` のみ）。
翻訳元が存在しないのに英語だけマルチマットの説明文が入っていた状態。

新しい英語を書くには素材・サイズ等の事実が必要だが、**日本語側に情報がないため
捏造せずに削除**した。英語では日本語原文（＝空）が表示される。

> **要対応**: この商品は日本語の説明文自体が空。公開するなら**まず日本語を書く**必要がある。

### 検証

全34商品の英語翻訳を再取得し、
- 9件すべてで日本語商品と英語タイトルが一致することを確認
- `quantity` の誤訳は **0件**

---

## （旧記載）未修正だった内容

norahiの調査中に、**より深刻な事故**が見つかりました。
`quantity：` が残っている6件は、すべてこの問題に該当します。

**英語で見ると、まったく別の商品として表示されます。**

| 商品ID | 日本語（実際の商品） | 英語で表示される名前 | 状態 |
|---|---|---|---|
| 7952864739566 | Various dogs Long Sleeve Shirts(アダルト) | **British Dogs Long Sleeve Shirts** | 🔴 ACTIVE |
| 7952870277358 | Various dogs Long Sleeve Shirts For Kids | **British Dogs Long Sleeve Shirts For Kids** | 🔴 ACTIVE |
| 7952877912302 | Various dogs Shirts For Dog | **British Dogs Shirts For Dog** | 🔴 ACTIVE |
| 7952928473326 | Playing Dog Sweat For Dog | **Brittany Spaniel Short Tank Top For Dog** | 🔴 ACTIVE |
| 7952946987246 | Two of a kind Sweat For Dog | **Brittany Spaniel Short Tank Top For Dog** | 🔴 ACTIVE |
| 7952886759662 | Playing Dog Sweat（アダルト） | Flanders Long Sleeve Tee | DRAFT |
| 7952919953646 | Two of a kind Sweat（アダルト） | Flanders Long Sleeve Tee | DRAFT |
| 9439221842158 | Sumif × NOI Exclusive Order Tee | Brittany Spaniel Short Sleeve Tee | DRAFT |
| 7975371833582 | Sumif×The TENT Drawstring Bag | Sumif×TheTENT Flanders Multi Mat | DRAFT |

### なぜ深刻か

**公開中（ACTIVE）が5件あります。** 英語で見た海外のお客様には、

- 商品名が違う
- 説明文・サイズ・素材が違う商品のもの
- **作家名まで違う**（Playing Dog / Two of a kind の作家は norahi・NOI なのに「Nelson Mirei」と表示）

つまり **別商品として売っている状態**です。注文されれば確実にトラブルになります。

### なぜ今回は直さなかったか

`quantity：` だけ直しても、**中身が別商品である事実は変わらない**からです。
「間違った説明文の中の誤字を直す」ことになり、意味がありません。

### 対応の選択肢（判断が必要）

| 案 | 内容 | 向いている場合 |
|---|---|---|
| **A. 削除する** | 英語翻訳を消す。英語では日本語原文が表示される | すぐ事故を止めたい。**ACTIVEの5件はこれが最短** |
| **B. 書き直す** | 各商品の正しい英語説明を作る | 海外販売を本気でやるなら必要 |
| C. 放置 | ❌ 推奨しない。ACTIVEの5件は誤情報を出し続ける |

> **推奨は「ACTIVEの5件を今すぐA、その後Bで書き直す」。**
> DRAFTの4件は販売されていないので急ぎません。

---

## 🟡 残っている英語の不備（未対応）

| 箇所 | 内容 |
|---|---|
| **British Dogs系 8商品** | 作家紹介が `Active as a ter.` で文が壊れている（検証で8件確認） |
| コレクション「ホームページ」 | `home page` と直訳されている |
| 全体 | 機械翻訳ベースで、`100% polyester%` のような表記ゆれが残る |

海外販売を本格化する前に、**英語の商品説明を一度きちんと整える**価値があります。
詳細は `docs/overseas-2026-09-08.md`。
