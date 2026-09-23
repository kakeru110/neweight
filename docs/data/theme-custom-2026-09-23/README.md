# テーマに追加した自作ファイル（2026-09-23 / カラースウォッチ）

テーマを入れ替えるとこれらは失われるので、原本をここに置いてある。

| ファイル | 置き場所 | 役割 |
|---|---|---|
| `sumif-swatch-card.liquid` | `snippets/` | 商品カードの色の丸。Liquidのみ・JS不要 |
| `sumif-swatches.liquid` | `snippets/` | 共通CSS + 商品ページの色チップ（JS） |

## 併せて変更した既存ファイル（2箇所だけ）

### `snippets/product-grid-item.liquid`
```diff
-{% include 'swatch-globo' %}
+{% include 'sumif-swatch-card' %}
```

### `layout/theme.liquid`
```diff
-{{ content_for_header }}{% include 'globo.swatch.script' %}
+{{ content_for_header }}

 ...（</body> の直前）
+{% include 'sumif-swatches' %}
 </body>
```

## Globoアプリを再導入する場合

1. `product-grid-item.liquid` の include を `swatch-globo` に戻す
2. `layout/theme.liquid` の `{% include 'globo.swatch.script' %}` を戻し、`sumif-swatches` を外す

テーマ内のGlobo関連ファイル（`globo.swatch.*` / `swatch-globo.liquid`）は**削除していない**ので、
戻すだけで元の構成になる。
