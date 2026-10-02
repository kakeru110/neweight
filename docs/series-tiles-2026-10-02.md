# シリーズタイルの表記そろえ（2026-10-02）

ユーザー指摘:「Tシャツとか抜けているシリーズがある。」

## 調べたこと

まず「本当に商品が漏れていないか」を確認した。**漏れていなかった。**

販売中（ACTIVE）23商品が、9枚のタイルにちょうど全部入っている:

| タイル | 商品数 | 内訳 |
|---|---|---|
| British Dogs Tシャツ | 3 | 大人・子ども・愛犬 |
| British Dogs シャツ | 3 | 大人・子ども・愛犬 |
| RinTinTin | 3 | 大人・子ども・愛犬 |
| Flanders Tシャツ | 3 | 大人・子ども・愛犬 |
| Flanders シャツ | 3 | 大人・子ども・愛犬 |
| Brittany Spaniel | 3 | 大人・子ども・愛犬 |
| Various dogs | 3 | 大人・子ども・愛犬 |
| Playing Dog | 1 | 愛犬 |
| Two of a kind | 1 | 愛犬 |
| **合計** | **23** | = ACTIVE商品数と一致 |

タイル下の「大人・子ども・愛犬」も商品タグから自動生成していて、9枚とも実態と合っていた。

## 本当の問題: 表記がそろっていなかった

9枚のうち4枚だけ種類（Tシャツ/シャツ）が付いていて、5枚は付いていなかった。

```
British Dogs Tシャツ   British Dogs シャツ   RinTinTin        ← 種類が抜けて見える
Flanders Tシャツ       Flanders シャツ       Brittany Spaniel ← 同上
Various dogs           Playing Dog           Two of a kind    ← 同上
```

並べて見ると「RinTinTinのTシャツが抜けている」ように読めてしまう。
実際にはRinTinTinはTシャツしかないシリーズで、抜けているのは**商品ではなく表記**だった。

さらに、ナビの「シリーズ」ドロップダウンは
すでに「Playing Dog スウェット」「Two of a kind スウェット」と種類付きになっていて、
**トップのタイルとナビで名前が食い違っていた。**

## やったこと

コレクション名を5件変更。**ハンドルは変わらないのでURLはそのまま。**

| コレクション | 変更前 | 変更後 | ハンドル（不変） |
|---|---|---|---|
| 476660269294 | RinTinTin | RinTinTin Tシャツ | `rintintin` |
| 476660334830 | Brittany Spaniel | Brittany Spaniel Tシャツ | `brittany-spaniel` |
| 476660367598 | Various dogs | Various dogs シャツ | `various-dogs` |
| 481888633070 | Playing Dog | Playing Dog スウェット | `playing-dog` |
| 481888665838 | Two of a kind | Two of a kind スウェット | `two-of-a-kind` |

あわせてナビの「シリーズ」ドロップダウン3件も同じ表記に変更
（RinTinTin / Brittany Spaniel / Various dogs。残り6件は元から一致）。

タイルの文字は `snippets/collection-grid-item.liquid` が
`collections[featured].title` をそのまま出しているので、
コレクション名を変えるだけでトップもコレクションページの見出しも直る。テーマの公開は不要。

### 検証

- トップの9枚すべてが種類付きになったことを確認
- 旧URL 5本すべて 200 で、見出しも新しい名前で表示されることを確認
  （`/collections/rintintin` `/collections/brittany-spaniel` `/collections/various-dogs`
    `/collections/playing-dog` `/collections/two-of-a-kind`）
- ナビのドロップダウン9件が同じ表記になったことを確認

### 戻し方

上の表の「変更前」で `collectionUpdate(input:{id, title})` を打てば戻る。
ナビは `menuUpdate` で該当3件のtitleを戻す（menuUpdateは全置換なので全項目を送ること）。

## ついでに見つけたこと: 出荷できる在庫が下書きに眠っている

下書き・アーカイブの11商品について、OpenLogi倉庫の在庫を全部確認した。

| 商品 | 状態 | OpenLogi在庫 | 判断 |
|---|---|---|---|
| **Sumif×TheTENT British Dogs マルチマット** | **下書き** | **2** | **出荷できるのに買えない。¥9,350×2＝¥18,700** |
| Playing Dog Sweat（アダルト） | 下書き | 0 | 出せない |
| Two of a kind Sweat（アダルト） | 下書き | 0 | 出せない |
| Sumif × NOI Exclusive Order Tee | 下書き | 0 | 出せない |
| British Dogs サーモボトル | 下書き | 0 | 出せない |
| Sumif×TheTENT Flanders マルチマット | 下書き | 0 | 出せない |
| Sumif×The TENT Drawstring Bag | 下書き | 0 | 出せない |
| Sumif×The TENT Drawstring Bag 第二弾 | 下書き | 0 | 出せない |
| 【受注生産】Eat up your dinner Sweat | アーカイブ | 0（原田家に5） | 出荷不可 |
| 【受注生産】Let's Play Long Sleeve Tee | アーカイブ | 0（原田家に3） | 出荷不可 |
| 【受注生産】Let's Play Sweat For Dog | アーカイブ | 0（原田家に1） | 出荷不可 |

受注生産3点は原田家にしか在庫がなく、CLAUDE.mdの大原則どおり販売数に入れられない。
売るならOpenLogiに入庫してから。

**マルチマットだけは今すぐ売れる状態なのに下書きのまま。**
ただしThe TENTとのコラボ品なので、コラボ契約がまだ販売を許しているかは
こちらでは確認できない。問題なければ公開する。
