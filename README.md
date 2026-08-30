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
| [`docs/templates/`](docs/templates/) | 週次カレンダー / キャンペーン企画書 / 週次レポートの雛形 |

---

## まず読むべきもの

**[`docs/findings-2026-08.md`](docs/findings-2026-08.md)** から読んでください。

実際のストアデータを確認したところ、SNSで注目を集めても売上に変換されない構造的な課題が
いくつか見つかっています。特に重要なのは次の3点です。

1. **「Two of a kind」「Playing Dog」の大人用が非公開・在庫0**
   — 犬用だけ在庫が残り、sumifの核である「お揃い」が成立していない
2. **NOIコラボTeeが在庫116点でドラフトのまま**
   — 実在庫なら即売れる資産。数値の誤りなら分析が全部狂う。実物確認が必要
3. **2024年以降の商品にタグが未設定**
   — 自動コレクションが機能せず、SNSからの導線が作れない

在庫が潤沢で3者が揃っている **Brittany Spaniel / RinTinTin / British Dogs** が
いますぐ推せるシリーズです。

---

## 前提

- Shopify MCP がこのセッションに接続されていること（商品・在庫・注文・分析の取得に使用）
- ストアへの書き込み（商品更新・割引コード発行）は、**エージェントが必ず事前承認を求めます**
