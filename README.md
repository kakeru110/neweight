# sumif SNSグロースチーム

アパレルブランド **[sumif](https://sumifofficial.com)** の商品を、SNS運用を起点に売るための
**Claude Code AIエージェントチーム**です。

sumifは「大人・子ども・愛犬が同じ絵柄で揃う」ファミリーリンクコーデブランド。
この3者が揃う画は他ブランドには作れない資産であり、SNSでの最大の武器です。
このリポジトリは、その武器を毎週きちんと使い切るための運用基盤です。

---

## 使い方

Claude Code でこのリポジトリを開き、やりたいことを日本語で話しかけてください。
内容に応じて適切なエージェントが自動的に立ち上がります。明示的に指名することもできます。

```
「今週何を推すべき？在庫見て決めて」          → sumif-merchandiser
「来月のInstagramの投稿計画を作って」          → sumif-sns-planner
「Brittany Spanielの3者リンク投稿の撮影企画」  → sumif-creative-director
「このキャプション、公開前にチェックして」      → sumif-brand-guardian
「11月1日の犬の日のキャンペーン企画して」      → sumif-campaign-producer
「先週の売上どうだった？」                     → sumif-growth-analyst
「UGCを集めたい。DMの文面を作って」            → sumif-community-manager
```

---

## チーム構成

| エージェント | 役割 | こんなときに |
|---|---|---|
| 🎯 `sumif-sns-planner` | コンテンツカレンダー設計、企画の交通整理 | 「今月/今週何を出す？」 |
| 📸 `sumif-creative-director` | 撮影企画、カット表、キャスティング、絵コンテ | 「どう撮る？」 |
| ✍️ `sumif-copywriter` | キャプション、リール台本、ハッシュタグ | 「原稿書いて」 |
| 🛡️ `sumif-brand-guardian` | 公開前のブランド・法令チェック（最終関門） | 「これ出して大丈夫？」 |
| 🏷️ `sumif-merchandiser` | 商品ページ・コレクション・在庫と推し商品選定 | 「ストア側を整えて」 |
| 🎉 `sumif-campaign-producer` | 受注生産・コラボ・プレゼント企画・割引設計 | 「キャンペーンやりたい」 |
| 🤝 `sumif-community-manager` | UGC収集・許諾、インフルエンサー開拓、DM | 「ファンを増やしたい」 |
| 📊 `sumif-growth-analyst` | ShopifyQL分析、週次レポート、効果測定 | 「数字はどう？」 |

定義は `.claude/agents/` にあります。役割を変えたいときは該当ファイルを編集してください。

---

## ドキュメント

| ファイル | 内容 |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | チーム全体の運用ルール（全エージェントが従う） |
| [`docs/brand-context.md`](docs/brand-context.md) | ブランドの世界観、ターゲット、トーン&マナー、NG表現 |
| [`docs/sns-playbook.md`](docs/sns-playbook.md) | チャネル戦略、投稿の型A〜I、KPI、年間フック |
| [`docs/catalog-snapshot.md`](docs/catalog-snapshot.md) | 商品ラインの構造とファミリーセット表 |
| [`docs/findings-2026-08.md`](docs/findings-2026-08.md) | **初期診断：SNSを始める前に潰すべき課題** |
| [`docs/openlogi-sync-2026-08-30.md`](docs/openlogi-sync-2026-08-30.md) | **OpenLogi × Shopify 在庫照合レポート** |
| [`docs/tagging.md`](docs/tagging.md) | タグ体系（8軸）と、次に組むべきコレクション |
| [`docs/creative-assets-audit-2026-08-30.md`](docs/creative-assets-audit-2026-08-30.md) | **既存画像166点の棚卸し。何が使えて何が足りないか** |
| [`docs/instagram-audit-2026-08-30.md`](docs/instagram-audit-2026-08-30.md) | **Instagram診断（2,856フォロワー）と今日できる3つの改善** |
| [`docs/sales-reality-2026-09-06.md`](docs/sales-reality-2026-09-06.md) | 🔴 **売上の実態。3ヶ月半で5件。戦略の重心を企画へ移す根拠** |
| [`docs/calendar/2026-09.md`](docs/calendar/2026-09.md) | **9月のコンテンツカレンダー** |
| [`docs/templates/`](docs/templates/) | 週次カレンダー / キャンペーン企画書 / 週次レポートの雛形 |
| [`docs/data/`](docs/data/) | OpenLogi在庫CSV、タグ適用前のバックアップ |

---

## 在庫の大原則

> **Shopifyで売っていいのは `Open Logi 倉庫` にある在庫だけ。**
> `原田家` `鎌倉` `高輪` にも現物はあるが、出荷できないので販売数に入れない。
> 売る場合は先にOpenLogiへ入庫してから。

Shopify APIの `inventoryQuantity` は全ロケーション合計を返すため、販売可能在庫として使えません。
チームのエージェントは全員このルールに従います。

## 現在のフェーズ：売り切り

**新規入荷は基本的にありません。いまある在庫を売り切ることが目的です。**
そのため「新作を出して認知を積む」通常のブランド運用とは前提が違い、
チーム全体が「在庫が多く、捌きたいものから露出させる」方針で動きます。

## まず読むべきもの

**[`docs/openlogi-sync-2026-08-30.md`](docs/openlogi-sync-2026-08-30.md)** →
**[`docs/findings-2026-08.md`](docs/findings-2026-08.md)** の順で読んでください。

実データを確認したところ、SNSで注目を集めても売上に変換されない課題が見つかっています。

1. **連携済みSKUで61件ズレていた原因が依然不明** — 数量の棚卸しは完了（139SKU全件一致）、
   未連携22件の一括連携も完了。だが61件のズレは連携済みSKUで起きていたため原因未特定。
   **1週間後の再照合**で「連携が壊れているのか／過去の事故が溜まっていただけか」を切り分ける
2. **「Two of a kind」「Playing Dog」の大人用が非公開・在庫0**
   — 犬用だけ在庫が残り（64点・16点）、sumifの核である「お揃い」が成立していない
3. **NOIコラボTeeの在庫116点はOpenLogiに存在しない**
   — 実在庫でない可能性が高い。かつSKUがBrittany Spanielの体系を流用しており事故のもと

在庫が潤沢で3者が揃っている **Brittany Spaniel / RinTinTin / British Dogs** が
いますぐ推せるシリーズです。

## 完了済み

- ✅ **タグ体系の整備**（2026-08-30）— ACTIVE23商品に8軸のタグを適用。
  シリーズ / 対象 / アイテム / 素材 / 季節 / セット / セット状態 / アーティスト / 販売方針。
  詳細は [`docs/tagging.md`](docs/tagging.md)
- ✅ **SKU表記ゆれの統一**（2026-08-30）— Shopify側8件をOpenLogi表記に合わせ、
  OpenLogiとの突合を134→142SKUに改善。その結果、Flanders大人シャツLで
  **20点（約20万円分）が売り場に出ていなかった**ことが判明。
  詳細は [`docs/openlogi-sync-2026-08-30.md`](docs/openlogi-sync-2026-08-30.md) の追記
- ✅ **Flanders大人 半袖シャツ L の在庫を 4→24 に修正**（2026-08-30、+20点＝約20万円分）
- ✅ **ロケーション設定の是正**（2026-08-30）— `原田家` `鎌倉` の「オンライン注文で販売する」をOFF。
  出荷できない在庫15点が売り物に入っていた状態を解消
- ✅ **在庫の棚卸し**（2026-08-30）— OpenLogiを正として61件を上書き（−91点 / +18点）。
  **139SKU全件が一致、不一致0件**。販売可能在庫 943点 / うちACTIVE 827点
- ✅ **オープンロジの商品連携**（2026-08-30）— 未連携22件を一括連携（22→0 / 連携済み171）。
  原因は「後から追加したバリアントが紐付いていなかった」こと。実行後の在庫変動なしを検証済み

---

## 前提

- Shopify MCP がこのセッションに接続されていること（商品・在庫・注文・分析の取得に使用）
- ストアへの書き込み（商品更新・割引コード発行）は、**エージェントが必ず事前承認を求めます**
