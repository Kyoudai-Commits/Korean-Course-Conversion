# Japanese — Language Notes for Localization Agents

## Register and speaker habits
- Instructors speak polite です/ます form. Render as friendly, direct instructor English, not stiff.
- Frequent fillers: えっと / まあ / なんか / ちょっと / ですね / はい / こう / まあまあ / そうですね.
  Drop unless they carry emphasis or pacing value.
- ちょっと usually softens, not "a little": ちょっと違う = "that's not quite right".
- Subjects are omitted; pronouns must be inferred from what is on screen.
- 〜てあげる / 〜てやる about lines or shapes means "give it (some X)" / "go ahead and X", not a favor.
- 〜感じ / 〜イメージ = "the feel / the idea of", often best rendered as "kind of like…" or dropped.
- Sentence-final ね / よ / かな → tone only. "〜かなと思います" = "I think… / I'd say…".
- Instructors address students as 皆さん. Use "you" or "everyone" naturally.

## Core art vocabulary (default English; context overrides)
| Japanese | Preferred English | Notes |
|---|---|---|
| ラフ | rough / rough sketch | |
| 下書き | underdrawing / rough | |
| 線画 | line art | |
| ペン入れ / 清書 | inking / clean lines | |
| 主線 | main lines / outer contour lines | |
| アタリ | construction lines / guidelines | ASR may write 当たり ("hit") — resolve to アタリ in drawing context |
| 塗り | coloring / painting / rendering | 厚塗り = painterly rendering; アニメ塗り = cel shading; ブラシ塗り = brush/soft rendering; 水彩塗り = watercolor-style |
| 塗り分け | separating color areas / flatting | |
| 描き込み | detailing / rendering in detail | |
| 影 | shadow | 陰 (form shadow) vs 影 (cast shadow) — ASR cannot distinguish (both かげ). Decide from context. 陰影 = shading / light and shadow |
| 明暗 | light and dark / values | |
| 立体感 / 立体 | sense of volume / form / 3D form | |
| 奥行き | depth | |
| 面 | plane | homophone with 麺 (noodle) — ASR trap |
| 重心 | center of gravity / balance | |
| 動き / 流れ | movement / flow | |
| ポーズ / ポージング | pose / posing | |
| シルエット | silhouette | |
| 情報量 | amount of detail / visual information | |
| 密度 | density (of detail) | |
| メリハリ | contrast / punch / variation | no single English word; "give it more contrast", "vary the line weight" |
| 抜け感 / 抜き | breathing room / lightness; line tapering (入り抜き = line taper in/out) | |
| 目線誘導 / 視線誘導 | leading the eye / eye flow | |
| 色味 | color / hue / color cast | |
| 彩度 / 明度 / 色相 | saturation / value (brightness) / hue | |
| 固有色 | local color | |
| 環境光 / 反射光 | ambient light / reflected light | |
| 補色 | complementary color | |
| 馴染ませる | blend in / integrate | |
| 締める | tighten up / add darker accents | |
| 飛ばす (色を) | blow out (highlights) / lose | |
| 潰す (影を) | crush (the darks) / fill in solid | |
| 添削 | critique / redline / paint-over | Saito uses this constantly |
| 画力 | drawing skill / ability | |
| 上達 | improvement / getting better | |
| 惜しい | "so close" / almost there / a near miss | |
| 違和感 | looks off / feels wrong | |
| デッサン | drawing accuracy / observational drawing | デッサンが狂う = the drawing is off / proportions are off; not "sketch" |
| デフォルメ | stylization / simplification | not "deform" |
| 三面図 | turnaround / character sheet (front, side, back) | |
| 差分 | variants / alternate versions (expressions, outfits) | |

## Software terms (Clip Studio Paint / Photoshop Japanese UI)
| Japanese | English UI |
|---|---|
| レイヤー / フォルダー | layer / folder (CSP) or group (PS) |
| 乗算 | Multiply |
| スクリーン | Screen |
| オーバーレイ | Overlay |
| ソフトライト / ハードライト | Soft Light / Hard Light |
| 加算 / 加算(発光) | Add / Add (Glow) — CSP; Linear Dodge (Add) in PS |
| 覆い焼き / 覆い焼きカラー | Dodge / Color Dodge — ASR may produce 覆い焼き as おおいやき, or garble |
| 焼き込み / 焼き込みカラー | Burn / Color Burn |
| 比較(明) / 比較(暗) | Lighten / Darken |
| 色相・彩度・明度 | Hue/Saturation/Lightness |
| トーンカーブ | Curves (Tone Curve in CSP) |
| レベル補正 | Levels |
| 色調補正 | color adjustment / Correction layer (CSP: 色調補正レイヤー = Correction Layer) |
| グラデーションマップ | Gradient Map |
| クリッピング / 下のレイヤーでクリッピング | clipping / Clip to Layer Below |
| 透明ピクセルをロック / 透明度保護 | Lock Transparent Pixels |
| レイヤーマスク | layer mask |
| 選択範囲 | selection |
| 自由変形 | Free Transform |
| メッシュ変形 | Mesh Transform (CSP) |
| ゆがみ | Liquify |
| ぼかし / ガウスぼかし | blur / Gaussian Blur |
| 定規 / パース定規 / 対称定規 | ruler / Perspective Ruler / Symmetry Ruler (CSP) |
| 3Dデッサン人形 | 3D drawing figure (CSP) |
| 素材 | material / asset (CSP Assets) |
| ベクターレイヤー | vector layer |
| 消しゴム | eraser |
| スポイト | Eyedropper |
| 塗りつぶし / バケツ | Fill / bucket |
| 手ブレ補正 | Stabilization |
| 筆圧 | pen pressure |
| キャンバス / 解像度 / dpi | canvas / resolution |
| 左右反転 | flip horizontal |

## 3D vocabulary (for JA-02)
ポリゴン polygon · 頂点 vertex · エッジ/辺 edge · フェース/面 face · ループカット loop cut ·
押し出し Extrude · ベベル Bevel · サブディビジョン(サーフェス) Subdivision Surface ·
ミラー Mirror · リトポ retopology · トポロジー topology · ローポリ/ハイポリ low-poly/high-poly ·
UV展開 UV unwrap · シーム seam · ベイク bake · 法線 normal · ウェイト(塗り) weight (painting) ·
ボーン bone · リグ rig · スキニング skinning · ブレンドシェイプ/シェイプキー blend shape / shape key ·
テクスチャ texture · マテリアル material · シェーダー shader · セルルック/トゥーン toon / cel-look shading ·
輪郭線/アウトライン outline · スカルプト sculpt · ブラシ brush · マスク mask · ダイナメッシュ DynaMesh ·
Zリメッシャー ZRemesher · サブツール SubTool · ポリペイント PolyPaint

## Homophone / ASR traps
- かげ: 影 vs 陰 (see above).
- せん: 線 (line) vs 千 / 先 / 選.
- め: 目 (eye) vs 芽; めん: 面 vs 麺.
- いろ / しろ: 色 vs 白 confusion in noisy audio.
- ぬり (塗り) vs のり; ぬく (抜く) vs ぬぐ.
- はい (yes/okay) frequently transcribed as 灰 (gray) or vice versa in color lessons.
- あたり (アタリ construction lines) vs 当たり / 辺り.
- リグ vs リング; メッシュ vs メッセージ; ベベル vs レベル.
- Numbers: 一 vs 位置 (いち), 二 vs に particle; ASR often drops counters.
- Katakana loanwords: ASR sometimes outputs the English word, sometimes katakana, sometimes garbage
  (e.g., クリスタ = Clip Studio Paint; フォトショ = Photoshop; ペンタブ = pen tablet; 液タブ = pen display).
