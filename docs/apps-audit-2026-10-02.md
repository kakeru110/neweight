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

---

## 追記: 有料アプリ4つの実測と解約判断

「実際に何か読み込んでいるか」「画面に何か描画しているか」をPlaywrightで確認した。

### 判定

| アプリ | 月額 | 読み込んでいるもの | 画面への描画 | 判定 |
|---|---|---|---|---|
| **Sami Product Labels** | $5.00 | アプリ拡張JS **22本**＋1ページ33リクエスト | 赤い%バッジ | **解約可**（テーマ側に移植済み） |
| **EX Show Variants** | $4.99 | **なし**（Liquidスニペットのみ） | 検索結果ページのバリエーション分割 | **解約可**（後述） |
| **Social Login** | $2.99 | `d1pzjdztdxpvck.cloudfront.net/resource/resource.js` を全ページ | **0要素** | **解約推奨** |
| **GO Product Page Gallery + Zoom** | $2.99 | **なし** | 商品ページの拡大はテーマ内蔵 | **解約候補** |

合計 **$15.97/月 ≈ ¥2,400/月 ≈ ¥29,000/年**

### 根拠

**Sami Product Labels**
`cdn.shopify.com/extensions/.../product-label-4-403/` から
`samita.ProductLabels.bundle.*.js` を22本読み込んでいる。
2026-10-02に `snippets/sumif-color-card.liquid` へ移植済みで、グリッド内のラベルはCSSで隠してある。

**EX Show Variants (eosh)**
JSを一切読み込まない。テーマに置かれたLiquidスニペット2本だけ。
- `snippets/eosh-product-grid-item-variants.liquid` … **どこからも呼ばれていない**（コレクションは自作に置換済み）
- `snippets/eosh-search-result-variants.liquid` … `templates/search.liquid` から使用中
**純粋なLiquidなので、アンインストールしてもスニペットは残り、検索結果ページはそのまま動く。**

**Social Login**
`layout/theme.liquid` から全ページで `resource.js` を読み込んでいるが、
`[class*=social-login]` 等の要素は商品ページ・検索結果ページとも **0個**。
さらに `/account/login` は新しい顧客アカウント（Shopifyホスト）へ飛んでおり、
**テーマのログインページ自体が使われていない**（リクエスト57件、cloudfrontの読み込みなし）。
構造的に機能していない。

**GO Product Page Gallery + Zoom**
商品ページで該当する外部ホスト・アプリ拡張の読み込みが**一切見つからない**。
商品画像の拡大は Minimal テーマ内蔵の機能（`theme.strings.zoomClose/zoomPrev/zoomNext` が
`layout/theme.liquid` に定義されている）。停止しているか未設定の可能性が高い。
解約後に商品画像の拡大が動くかだけ一度確認すること。

### 解約の手順

**スマホ（Shopifyアプリ）**
1. 下部の「≡」→「アプリ」
2. 対象アプリの右の「…」
3. 「アプリを削除」→ 確認

**PC（管理画面）**
1. 「設定」→「アプリと販売チャネル」
2. 対象アプリの「…」→「アンインストール」→ 確認

**課金**
アンインストールすれば以後の課金は止まる。
すでに請求済みの期間ぶんが返金されるかはアプリ・プランによるので、
確実にしたいなら次の請求日の直前に解約する。請求日は「設定」→「請求」で確認できる。

### 解約後に必ずやること

**アンインストールしてもテーマのコードは消えない。**
今日見つかった ProductWiz（商品ページで159KB）と BSS Product Labels（毎ページ3リクエスト）が
まさにその状態だった。解約したら、そのアプリのスニペット・アセットと
`layout/theme.liquid` の include が残っていないか必ず確認する。

| 解約したら消すもの | |
|---|---|
| Sami Product Labels | `templates/search.samitaLabelsProductsJson.liquid`／`sumif-card-style.liquid` の `.samita_productLabel-content` を隠すCSS（不要になる） |
| EX Show Variants | `snippets/eosh-product-grid-item-variants.liquid`（未使用）。`eosh-search-result-variants.liquid` は**残す**（検索結果で使用中） |
| Social Login | `snippets/social-login.liquid` と `layout/theme.liquid` の `{% include 'social-login' %}` |
| GO Gallery + Zoom | テーマ内に該当ファイルなし。確認のみ |

---

## 追記: 有料4つのアンインストール後の実測と、無料アプリの判断

ユーザーが有料4つ（Sami Product Labels / EX Show Variants / Social Login /
GO Product Page Gallery + Zoom）をアンインストール済み。

### 効果（スマホ390px・JPY・js/css/xhrのみ）

| ページ | 解約前 | 解約後 |
|---|---|---|
| トップ | 97件 / 1,052 KB | **84件 / 945 KB** |
| コレクション | 129件 / 1,104 KB | **85件 / 942 KB** |
| 商品ページ | 158件 / 1,312 KB | **121件 / 1,330 KB** |

- Sami Product Labels は **33リクエスト → 0件**
- テーマ製の割引率バッジは **コレクション48カード中48枚**で正常に表示。欠けなし
- **Social Login はアンインストール後も `resource.js` を全ページで読み続けていた**
  （`layout/theme.liquid` にスニペットが残っていたため）。下書き `166260867310` で撤去済み

### いまも残っているアプリ由来の読み込み（1ページあたり）

| | 件数 | 容量 |
|---|---:|---:|
| Google Tag | 3件 | **345 KB** |
| Meta Pixel | 2件 | 110〜202 KB |
| qikify Quick View | 1件 | 98 KB |
| Hextom 翻訳 | 2件 | 72 KB |
| BSS（残骸） | 3件 | 0 KB ← 下書きで撤去済み |
| Social Login（残骸） | 1件 | 0 KB ← 下書きで撤去済み |
| GLO Color Swatch | 1件 | 0 KB |
| POWR Image Slider | 1件 | 0 KB |
| TikTok / Pinterest 計測 | 5〜7件 | 0 KB |

### 無料アプリ 20個の判断

**残す（止めると業務が止まる・ストアフロントに読み込みゼロ）**

| アプリ | 理由 |
|---|---|
| OPENLOGI | 物流。出荷が止まる |
| NP後払い配送伝票番号登録アプリ | 決済 |
| かんたん会計freee売上データ連携 | 会計 |
| Shopify Claude Connector App | このセッションの接続元 |
| Flow | Shopify公式。自動化 |
| Order Printer (legacy) | Shopify公式。納品書 |
| Messaging | 問い合わせ受信 |
| Translate & Adapt | Shopify公式・無料。翻訳はこれ1本に寄せる |

**残す（先に消すとSEOが壊れる）**

| BOOSTER SEO |
|---|
| **これだけは先に消さないこと。** `layout/theme.liquid` のテーマ本来の `<title>` と `<meta name="description">` はコメントアウトされたままで、**いまタイトルと説明文を出しているのはこのアプリ**。アンインストールすると全ページのタイトルと説明文が消える。JSもネットワークリクエストも0件なのでストアフロントの負荷はほぼゼロ。外すなら、先にコメントを解除し、Shopify側のSEO欄に文言を移してから。theme.liquid に注意書きを残した |

**消す（ストアフロントを重くしているだけ）**

| アプリ | 理由 |
|---|---|
| Hextom: Translate and Currency | 72KB/ページ。翻訳が4重 |
| T Lab - AI Language Translate | 翻訳が4重 |
| ATranslate: Native Translate | 翻訳が4重。`NATIVE_TRANSLATE_CDN_THEME` という未公開テーマまで残している |
| GLO Color Swatch | 色チップは2026-09-23に自作へ置換済み |
| POWR Image Slider | ヒーローを feature-row に替えたので未使用 |
| Page Speed Booster | アプリ20個の状態で速度改善アプリを足すのは本末転倒 |
| GetSale Discounts | 値引きは価格の直接変更で実施済み。未使用 |

**要確認（こちらからは判断できない）**

| アプリ | 確認すること |
|---|---|
| **Sellbrite** | Amazon/eBay等とのマルチチャネル在庫連携。**使っているなら絶対に消さない。** OpenLogiと二重に在庫を書き換えると在庫事故になる。他チャネルで売っていないなら消す |
| qikify Quick View | 98KB/ページ。カードの虫眼鏡。カラー分割カードで色が直接選べるので価値は下がった。好みで判断 |
| Trusted FAQ | FAQページを出しているなら残す。ストアフロントの読み込みには出てこなかった |
| WB:Multi Converter | 用途不明。読み込みなし。心当たりがなければ消す |

### アプリではないが一番重い

Google Tag **345KB** ＋ Meta Pixel 110〜202KB ＋ TikTok ＋ Pinterest
＝ **1ページの重量の半分近く**。広告を回していないなら、測定のためだけに毎ページ450KB以上払っている。
これは「設定 → 販売チャネル・アプリ」ではなく各チャネル／カスタムピクセル側の設定。
広告の予定がないなら外す価値がある。**ユーザーの判断待ち。**
