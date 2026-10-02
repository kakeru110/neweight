# インストール済みアプリの棚卸し 2026-10-02

ユーザーから管理画面の「アプリ」一覧のスクリーンショットを受領し、
テーマ内のコードと、実際のページ読み込み（Playwright実測）を突き合わせた。

## インストール済み 24個

| # | アプリ | 月額 | 状況 |
|---|---|---|---|
| 1 | EX Show Variants | **$4.99** | 検索結果ページでのみ使用。コレクションは自作に置換済み → **解約候補** |
| 2 | T Lab - AI Language Translate | — | 翻訳アプリ① |
| 3 | Messaging | — | |
| 4 | Sami Product Labels | **$5.00** | 赤い%バッジ。**テーマ側に移したので解約可** |
| 5 | Shopify Claude Connector App | — | このセッションの接続元 |
| 6 | Flow | — | Shopify公式 |
| 7 | OPENLOGI | — | 物流。必須 |
| 8 | Trusted FAQ | — | |
| 9 | Translate & Adapt | 無料 | Shopify公式。翻訳アプリ② |
| 10 | NP後払い配送伝票番号登録アプリ | — | 決済。必須 |
| 11 | かんたん会計freee売上データ連携 | — | 会計 |
| 12 | qikify Quick View | — | カードの虫眼鏡。98KB/ページ |
| 13 | Sellbrite | — | |
| 14 | GO Product Page Gallery + Zoom | **$2.99** | |
| 15 | GLO Color Swatch | — | テーマ側は2026-09-23に自作へ置換済み → **要確認** |
| 16 | BOOSTER SEO | — | `snippets/booster-seo.liquid` 43KB |
| 17 | ATranslate: Native Translate | — | 翻訳アプリ③ |
| 18 | Social Login | **$2.99** | |
| 19 | POWR Image Slider | — | ヒーローを feature-row に替えたので未使用のはず → **要確認** |
| 20 | Hextom: Translate and Currency | — | 翻訳アプリ④。`tms-translator.js` 72KB/ページ |
| 21 | Order Printer (legacy) | — | |
| 22 | GetSale Discounts | — | 割引。今回は価格直接変更なので未使用 |
| 23 | Page Speed Booster | — | アプリ24個の状態で速度改善アプリは本末転倒 |
| 24 | WB:Multi Converter | — | |

**見えている有料ぶんの合計 $15.97/月 ≈ ¥2,400/月 ≈ ¥29,000/年。**

## 問題1: 翻訳アプリが4つ入っている

T Lab / Translate & Adapt / ATranslate / Hextom。
毎ページ読まれている `tms-translator.js`（72KB）は Hextom のもの
（`layout/theme.liquid` のコメント `Hextom TMS Translator` で確認）。

**1つに絞るべき。** Shopify公式の Translate & Adapt は無料で、Marketsの通貨・言語とも素直に連動する。

## 問題2: アンインストール済みアプリのコードがテーマに残っていた

管理画面の一覧に存在しないのに `layout/theme.liquid` から読み込まれていたもの:

| 残骸 | 実測の影響 |
|---|---|
| **ProductWiz** (`productwiz-rio`) | **商品ページで毎回 159KB** 読み込み |
| **BSS Product Labels** (`bss-product-labels-configs`) | 毎ページ **3リクエスト** |
| AVADA HelpCenter FAQs (`avada-faqs-app`) | include 1行 |
| StarApps (`starapps-core`) | include 1行 |

テーマ内に残っているファイル実体は BSS 12本（508KB）+ ProductWiz 3本（597KB）= 約1.1MB。

### 対処（下書きテーマ `166260867310`）

`layout/theme.liquid` から上記4本の読み込みを削除。
あわせて `bss-product-label-js` / `bss-label-style-css` / `bss-product-label-fonts` も撤去
（`content_for_header contains 'product_label'` のガードがあり、もともと発火していなかった）。

**ファイル実体の削除はできなかった。** `themeFilesDelete` はMCPの安全ポリシーで禁止。
管理画面のコードエディタから手で消すしかない。
ただし読み込みを外したのでブラウザは取りに行かない。**ページ速度上の効果はもう出ている。**

### 検証（スマホ幅390px / JPY）

| ページ | ProductWiz | BSS |
|---|---|---|
| 商品ページ 現行 | 2件 / 159KB | 3件 |
| 商品ページ 掃除後 | **0** | **0** |
| コレクション 現行 | 0件 | 3件 |
| コレクション 掃除後 | 0件 | **0** |

商品ページの描画も確認済み: 商品名・価格（¥3,575）・画像4枚・カートボタンすべて正常、
Liquidエラーなし、JSエラーなし。

**注意**: 総KBの単純比較はできない。`preview_theme_id` を付けると
Shopifyの管理プレビューバーのスクリプトが乗るため、掃除後のほうが数字が大きく出る。
アプリ別の数字（ProductWiz 159KB→0、BSS 3件→0）が実際の差。

## 現状のページ重量（実測・スマホ390px・js/css/xhrのみ）

| ページ | リクエスト | 容量 |
|---|---:|---:|
| トップ | 97件 | 1,052 KB |
| コレクション | 129件 | 1,104 KB |
| 商品ページ | 158件 | 1,312 KB |

うち **Sami Product Labels だけで33リクエスト**（コレクション・商品ページ）。

## やること

1. **Sami Product Labels を解約**（$5.00/月）。バッジはテーマ側に移した
2. **翻訳アプリを1つに絞る**。Translate & Adapt（無料・公式）を残す案
3. **EX Show Variants**（$4.99/月）— `templates/search.liquid` の
   `eosh-search-result-variants` を自作に置き換えれば解約できる。未着手
4. GLO Color Swatch / POWR Image Slider が本当に使われていないか確認し、不要なら解約
5. 管理画面のコードエディタから、BSS 12本・ProductWiz 3本・
   `snippets/avada-faqs-app.liquid`・`snippets/starapps-core.liquid`・
   `templates/product.starapps.liquid`（どの商品もテンプレートサフィックス未使用、確認済み）を削除
