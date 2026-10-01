# トップの商品48枚をシリーズ5枚に置き換え（2026-10-01）

## やったこと

トップページの `featured-collection`（All Items 全48カード）をトップの並びから外し、
代わりに **シリーズ5枚のコレクションタイル** をヒーローの直後に置いた。

| 変更前 | 変更後 |
|---|---|
| ヒーロー → 商品48枚 → GIFバナー → Another line up → GIFバナー | ヒーロー → **シリーズ5枚** → GIFバナー → Another line up → GIFバナー |

`featured-collection` のセクション定義は残してあるので、テーマエディタで戻せる。
`/collections/all` は48カードのまま変わらない（ヒーローの「商品を見る」がそこへ行く）。

## 先にコレクション画像を直した

シリーズ5枚をそのまま置こうとしたら、**5枚とも平置きの物撮りで、しかも全部クリーム色**だった。
ヒーローの家族写真の直下に並べたら「選べない壁」が「見分けのつかない5枚」に変わるだけなので、
先に差し替えた。

| シリーズ | 変更前 | 変更後 |
|---|---|---|
| British Dogs | `DSC01636…`（平置き） | `sumif_card_00_offwhite`（オフホワイト・長袖） |
| RinTinTin | `DSC01632`（平置き） | `sumif_card_06_pink`（ピンク・半袖） |
| Flanders | `DSC01631`（平置き） | `sumif_card_09_sumikuro`（スミクロ・長袖） |
| Brittany Spaniel | `DSC01637`（平置き） | `sumif_card_15_green`（グリーン・半袖） |
| Various dogs | `sm1_83244`（平置き） | `sumif_main_20260930_18`（総柄シャツ） |

5枚が**クリーム / ピンク / スミクロ / グリーン / 総柄**に分かれ、タイルサイズでも見分けがつく。
コレクション画像はコレクションページでは使っていないので、影響はタイル表示だけ。

タイル幅は PC 235px・スマホ約180px。この幅では「大人・キッズ・犬の3枚並べ」は小さすぎるため、
大人の着用カット1枚に絞った。

## 効果（実測）

| | 変更前 | 変更後 |
|---|---|---|
| PC 全高 | 5,737px | **2,494px**（−57%） |
| スマホ 全高 | 9,820px | **3,142px**（−68%） |
| トップの商品カード | 48枚 | 0枚 |

スマホでは、ヒーロー（写真＋コピー＋ボタン）が1画面目に収まり、
**その直後に「シリーズから選ぶ」が来る**。狙いどおり。

Liquidエラー0 / JSエラー0。シリーズ5枚・Another line up 4枚とも正しいリンク先。

## テーマ

ドラフト **`166237569262`「Minimal — シリーズ5枚 2026-10-01」**。
変更は `config/settings_data.json` の2か所（`sumif-series` の追加、`content_for_index` の差し替え）。
変更前後を `docs/data/theme-series-2026-10-01/` に保存。

## 申し送り: 対象軸が3回出ている

ページが短くなったぶん、**同じ4つの行き先が3回繰り返されている**のが目立つようになった。

1. GIFバナー `9859eb6c…`（All / Adult / Kids / Dogs）
2. 「Another line up」`975b4f4b…`（All Items / Adult / Dog / Kids）
3. GIFバナー `24df10f7…` — **1と完全に同じHTML**

提案: **GIFバナー2つ（1と3）を外し、「Another line up」だけ残す。**
タイルの写真（家族・大人・犬・キッズの着用カット）のほうが、
文字だけの小さなGIFよりはるかに情報量がある。
見出しも英語の「Another line up」より「対象から選ぶ」等に変えたい。

これは今回の依頼の範囲外なので手をつけていない。

---

## シリーズの中でシャツを分けた（2026-10-01）

### 答えはタグ体系にあった

`docs/tagging.md` の **`セット:` タグ**が、8/30の時点で「シャツを分けた組」として定義済みだった。
実データで確認したところ、**7つとも過不足なく3点（大人・キッズ・ドッグ）**。

| セットタグ | 商品数 |
|---|---|
| `セット:British Dogs Tee` | 3 |
| `セット:British Dogs Shirts` | 3 |
| `セット:Flanders Tee` | 3 |
| `セット:Flanders Shirts` | 3 |
| `セット:RinTinTin` | 3 |
| `セット:Brittany Spaniel` | 3 |
| `セット:Various dogs` | 3 |

商品名の文字列マッチではなく**このタグでコレクションを組んだ**。
タイトルが変わってもルールが壊れない。

### 作ったコレクション（4件）

Tシャツとシャツの両方を持つのは British Dogs と Flanders の2シリーズだけなので、新規は4件。
RinTinTin / Brittany Spaniel / Various dogs は1種類しかないので既存をそのまま使った。

| ハンドル | タイトル | ルール | 画像 |
|---|---|---|---|
| `british-dogs-tee` | British Dogs Tシャツ | タグ = `セット:British Dogs Tee` | 大人 オフホワイト 長袖 |
| `british-dogs-shirts` | British Dogs シャツ | タグ = `セット:British Dogs Shirts` | 大人 オフホワイト シャツ |
| `flanders-tee` | Flanders Tシャツ | タグ = `セット:Flanders Tee` | 大人 スミクロ 長袖 |
| `flanders-shirts` | Flanders シャツ | タグ = `セット:Flanders Shirts` | 大人 テラコッタ シャツ |

**`collectionCreate` だけでは販売チャネルに公開されない**（`resourcePublicationsV2` が空のまま）。
そのままだと storefront で404になるため、`publishablePublish` でオンラインストアに公開した。
今後スマートコレクションを作るときも同じ手順が要る。

既存の `british-dogs` / `flanders`（シリーズ全体）はヘッダーナビが指しているので残した。
ナビ＝シリーズ全体、タイル＝買える組、という役割分担になる。

### テーマ側

`sections/collection-list.liquid` は **`max_blocks: 5`** で、`case` も `when 1..5` しかなかった。
7枚にすると `collection_item_width` が未定義になって崩れるため、

- `max_blocks` を 8 に
- `when 6`（PC3列）と `else`（PC4列）を追加

に変更した。多言語ラベルは en / ja に整理（`feature-row` と同じ扱い）。

### 検証

| ページ | H1 | カード枚数 |
|---|---|---|
| `/collections/british-dogs-tee` | British Dogs Tシャツ | 5 |
| `/collections/british-dogs-shirts` | British Dogs シャツ | 3 |
| `/collections/flanders-tee` | Flanders Tシャツ | 9 |
| `/collections/flanders-shirts` | Flanders シャツ | 3 |
| `/collections/british-dogs`（ナビ） | British Dogs | 8（= 5+3） |
| `/collections/flanders`（ナビ） | Flanders | 12（= 9+3） |

分割後の合計が分割前と一致している。Liquidエラー0 / JSエラー0。

タイルは PC 4+3（1枚313px）、スマホ2列。全高は PC 2,970px / スマホ 3,401px。

### テーマ

ドラフト **`166238814446`「Minimal — シリーズ7枚 2026-10-01」**。

### 申し送り

- **Playing Dog Sweat 犬 / Two of a kind Sweat 犬 の2点はどのシリーズタイルにも入らない。**
  `セット欠品`（対になる大人用がDRAFT・在庫0）のため3点セットが成立せず、
  タグ上もセットから外れている。トップから商品の壁を外したので、
  いまこの2点は All Items 経由でしか辿り着けない。
- RinTinTin / Brittany Spaniel は Tシャツのみ、Various dogs はシャツのみ。
  タイル名を `RinTinTin Tシャツ` のように揃えることもできるが、
  ラベルが長くなるので今回はそのままにした。

---

## スウェット2点にもタイルを追加（2026-10-01）

どのシリーズタイルにも入らなかった2点にコレクションを作った。
`セット:` タグは「3点セット」の単位なので、**セット欠品の2点はシリーズ軸のタグを使った**。

| ハンドル | タイトル | ルール | 画像 |
|---|---|---|---|
| `playing-dog` | Playing Dog | タグ = `Playing Dog` | 愛犬 グリーン |
| `two-of-a-kind` | Two of a kind | タグ = `Two of a kind` | 愛犬 ホワイト |

どちらも `publishablePublish` でオンラインストアに公開済み。

タイルは9枚になった。`collection-list.liquid` の `max_blocks` を 9 に上げ、
**9枚のときはPC5列（5+4）**にした。4列だと最終行が1枚だけ残って見栄えが悪いため。

検証: 9枚・リンク先9本とも正しい・PC2行・全高2,820px・Liquid/JSエラー0。

ドラフト **`166251102446`「Minimal — シリーズ9枚 2026-10-01」**。

### 残った課題: 「大人用しかないように見える」

9枚のうち**7枚が大人の着用カット、2枚が犬、キッズは0枚**。
実際は7セットとも大人・キッズ・ドッグの3点が揃っているのに、見出しが「シリーズから選ぶ」
なので大人用の分類に見える。

`docs/brand-context.md` §2 は
「すべてのコンテンツ設計は『3者が揃っている画』を中心に置く。単体カットだけの投稿は
sumifの強みを捨てている」と書いており、**いまのタイルはブランド自身のルールに反している**。

対応案はチャットで提示。未決。
