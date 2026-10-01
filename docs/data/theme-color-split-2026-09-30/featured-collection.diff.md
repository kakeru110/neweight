# sections/featured-collection.liquid の変更点（2026-10-01）

トップページの「特集コレクション」セクション。スキーマが全言語のラベルを持っていて
長いため、ここにはファイル全体ではなく**変更した3か所だけ**を記録する。
正はテーマ側のファイル。

## 1. カード用CSSの読み込みを追加

`{% endcase %}` の直後に追加。

```liquid
  {% include 'sumif-card-style' %}
```

## 2. グリッドに `grid-link__container` を付ける

CSSがこのクラス配下にスコープされているため、付けないと販売元が出たままになる。

```diff
-  <div class="grid-uniform">
+  <div class="grid-uniform grid-link__container">
```

## 3. ループの中身を色別カードに差し替え

```diff
     {% for product in collections[featured].products limit: total_products %}
-      {% assign featured = product %}
-      <div class="grid__item {{grid_item_width}}" {{ block.shopify_attributes }}>
-        {% include 'product-grid-item' %}
-      </div>
+      {% include 'sumif-collection-item' %}
     {% else %}
```

`sumif-collection-item` が `<div class="grid__item {{ grid_item_width }}">` を
自分で出すため、外側のラップは不要。`block.shopify_attributes` はこのセクションに
ブロックが無く常に空だったので落とした。

**`limit: total_products` は「商品数」の上限**であり、カード枚数の上限ではない。
色で分かれたぶんカードは増える（23商品 → 48枚）。
