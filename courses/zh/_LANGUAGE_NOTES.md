# Mandarin Chinese — Language Notes for Localization Agents

## Dialect and script
- Taiwan (zh-TW, traditional script, Taiwanese Mandarin): Krenz, Evan Lee (very likely), possibly Tenten.
- Mainland (zh-CN, simplified, often northern colloquial): PANDA, 52hertzC/You Shan (likely).
- ASR may output either script regardless of speaker. Do not infer dialect from script alone.
- Taiwan vs mainland vocabulary (same concept, different word):
  軟體/软件 software · 滑鼠/鼠标 mouse · 繪圖板/数位板 tablet · 螢幕/屏幕 screen · 檔案/文件 file ·
  影片/视频 video · 網路/网络 · 品質/质量 · 資料/资料·数据 · 彩度/饱和度 saturation · 圖層/图层 (same) ·
  筆刷/笔刷 · 快速鍵/快捷键 shortcut · 程式/程序 · 預設/默认 default · 解析度/分辨率 resolution ·
  同學 (students, used by Taiwanese teachers = "you guys") · 大家 (everyone).
- Photoshop UI terms differ by locale (see table). Prefer the English UI name.

## Register and speaker habits
- Independent Chinese courses are frequently live-recorded, long, with student Q&A and dense filler.
- Fillers to drop or compress: 然後 (then — chronic), 就是 (it's just / like), 那個 (um), 這個 (this — filler),
  對 / 對不對 (right / right?), 這樣子 / 這樣 (like this), 其實 (actually), 基本上 (basically), 比較 (relatively —
  usually "more", "pretty", or nothing), 一下 (softener — "just", "a bit", or nothing), 嘛 / 啊 / 喔 / 欸 particles,
  OK, 好 (okay), 好那 (okay so), 我們 (we — instructors say "we" meaning "you/I"; use "we" or "you").
- 你會發現 / 你會看到 = "you'll notice / you'll see". 我們來 = "let's". 去 + verb = just verb (去畫 = draw).
- Instructor nicknames: Krenz is called K大 / K老師 → "Krenz". Evan Lee 李老師 → "Evan".
- Sarcasm and blunt critique are common in Chinese art teaching; keep the directness, soften nothing
  into corporate English.

## Core art vocabulary (default English; context overrides)
| Chinese | Preferred English | Notes |
|---|---|---|
| 結構 / 结构 | structure | pervasive: "the structure is off" = form/construction is wrong |
| 體積 / 体积 | volume | |
| 體塊 / 体块 | form blocks / masses | |
| 型 / 形 | shape / form / likeness | 型不準 = the shape/proportions are off. ASR merges 型/形/行/性 (xíng) |
| 造型 | design / shape design / form | |
| 比例 | proportions | |
| 剪影 | silhouette | |
| 動態 / 动态 | gesture / pose / dynamic | |
| 動勢 / 动势 | line of action / movement | |
| 節奏 / 节奏 | rhythm | |
| 疏密 | density variation / spacing (tight vs loose) | |
| 虛實 / 虚实 | soft vs sharp / lost-and-found edges / rendered vs loose | no single word; choose by context |
| 主次 | hierarchy / primary vs secondary | |
| 黑白灰 | value groups / value structure | |
| 三大面 | three planes (light, halftone, shadow) | |
| 五大調 / 五大调 | five value zones (light, halftone, terminator, reflected light, cast shadow) | |
| 明暗交界線 / 交界线 | terminator / core shadow | |
| 亮面 / 灰面 / 暗面 | light side / halftone / shadow side | |
| 反光 | reflected light | |
| 投影 | cast shadow | not "projection" unless projector/perspective context |
| 高光 | highlight | |
| 固有色 | local color | |
| 環境色 / 环境色 | ambient / environment color | |
| 光源色 | light source color | |
| 冷暖 | warm/cool | |
| 色相 / 明度 / 彩度(飽和度) | hue / value / saturation | |
| 灰階 / 灰阶 | grayscale | |
| 對比 / 对比 | contrast | |
| 過渡 / 过渡 · 銜接 / 衔接 | transition / gradation | |
| 透視 / 透视 | perspective | |
| 視平線 / 视平线 | eye level / horizon line | |
| 消失點 / 消失点 | vanishing point | |
| 近大遠小 | closer is bigger, farther is smaller | |
| 透視縮短 / 縮短 | foreshortening | |
| 空氣透視 / 大氣透視 | atmospheric perspective | |
| 視角 / 焦段 / 廣角 / 長焦 | field of view / focal length / wide-angle / telephoto | |
| 速寫 / 速写 | gesture drawing / quick sketch | |
| 素描 | drawing (academic value drawing) | NOT "sketch" |
| 線稿 / 线稿 | line art | |
| 草稿 / 草圖 | rough / thumbnail | |
| 起稿 / 起形 | start the sketch / block in the shapes | |
| 抓型 / 抓形 | capture the shape / get the likeness | |
| 鋪色 / 铺色 · 鋪大色 | block in color / lay base colors | |
| 上色 | coloring | |
| 厚塗 / 厚涂 | painterly rendering (opaque painting) | |
| 平塗 / 平涂 | flat coloring | |
| 賽璐璐 | cel shading | |
| 疊色 / 叠色 | layering colors | |
| 塑造 | rendering form / modeling (in the drawing sense) | |
| 刻畫 / 刻画 | render (detail) | |
| 深入 | refine further / push | |
| 概括 · 歸納 / 归纳 | simplify / summarize forms | |
| 質感 / 质感 | texture / material quality | |
| 氛圍 / 氛围 · 氛圍感 | atmosphere / mood | |
| 畫面 / 画面 | the image / the picture / the composition | "畫面太平" = the image is flat |
| 視覺中心 / 视觉中心 | focal point | |
| 引導 / 引导 | leading the eye | |
| 留白 | negative space / breathing room | |
| 平衡 / 統一 / 變化 | balance / unity / variety | |
| 構圖 / 构图 | composition | |
| 布料 / 皺褶 / 褶皺 | fabric / folds | |
| 拉扯 / 張力 | tension (in fabric) | |
| 垂墜 / 下垂 | drape / hang | |
| 堆積 | bunching / stacking folds | |
| 支點 / 受力點 | anchor / stress point | |
| 骨架 / 骨骼 / 肌肉 | armature / skeleton / muscle | |
| 參考 / 参考 | reference | |
| 臨摹 / 临摹 | master copy / copying | |
| 默寫 / 默写 | drawing from memory | |
| 寫生 / 写生 | drawing from life | |
| 基本功 / 基礎 | fundamentals | |
| 效果 | effect / result / look | |
| 感覺 / 感觉 | feel / look | often drop |

## Photoshop UI (Taiwan / Mainland → English)
| zh-TW | zh-CN | English |
|---|---|---|
| 圖層 | 图层 | layer |
| 群組 | 组 | group |
| 色彩增值 | 正片叠底 | Multiply |
| 濾色 | 滤色 | Screen |
| 覆蓋 | 叠加 | Overlay |
| 柔光 | 柔光 | Soft Light |
| 實光 | 强光 | Hard Light |
| 加亮顏色 | 颜色减淡 | Color Dodge |
| 線性加亮(增加) | 线性减淡(添加) | Linear Dodge (Add) |
| 加深顏色 | 颜色加深 | Color Burn |
| 明度 (混合模式) | 明度 | Luminosity |
| 顏色 | 颜色 | Color |
| 剪裁遮色片 | 剪贴蒙版 | clipping mask |
| 圖層遮色片 | 图层蒙版 | layer mask |
| 鎖定透明像素 | 锁定透明像素 | Lock Transparent Pixels |
| 選取範圍 | 选区 | selection |
| 套索 | 套索 | Lasso |
| 滴管 | 吸管 | Eyedropper |
| 筆刷 | 画笔 | Brush |
| 橡皮擦 | 橡皮擦 | Eraser |
| 塗抹 | 涂抹 | Smudge |
| 仿製印章 | 仿制图章 | Clone Stamp |
| 液化 | 液化 | Liquify |
| 高斯模糊 | 高斯模糊 | Gaussian Blur |
| 動態模糊 | 动感模糊 | Motion Blur |
| 曲線 | 曲线 | Curves |
| 色階 | 色阶 | Levels |
| 色相/飽和度 | 色相/饱和度 | Hue/Saturation |
| 色彩平衡 | 色彩平衡 | Color Balance |
| 選取顏色 | 可选颜色 | Selective Color |
| 漸層對應 | 渐变映射 | Gradient Map |
| 任意變形 | 自由变换 | Free Transform |
| 彎曲 | 变形 | Warp |
| 操控彎曲 | 操控变形 | Puppet Warp |
| 調整圖層 | 调整图层 | adjustment layer |
| 智慧型物件 | 智能对象 | Smart Object |
| 濾鏡 | 滤镜 | Filter |
| 水平翻轉 | 水平翻转 | flip horizontal |
| 快速鍵 | 快捷键 | shortcut |
| 筆壓 | 压感 | pen pressure |
| 數位板 / 繪圖板 | 数位板 | tablet |
CSP: 對稱尺/对称尺 Symmetry Ruler · 透視尺/透视尺 Perspective Ruler · 向量圖層/矢量图层 vector layer.
SAI (mainland favorite): 水彩笔 Watercolor brush · 马克笔 Marker · 铅笔 Pencil · 二值笔 Binary pen · 发光 Luminosity · 阴影 Shade.

## Homophone / ASR traps
- xíng: 型 / 形 / 行 / 性 — "shape" in drawing context.
- huà: 畫 (draw) / 話 (speak) — 畫一下 vs 話一下.
- xiàn: 線 (line) / 現 (now) / 限 — 線條 vs 現在.
- miàn: 面 (plane/face) / 麵 (noodle) — simplified 面 covers both; always "plane/side".
- guāng: 光 (light) / 廣 (wide) — 廣角 (wide-angle) vs 光角.
- sè: 色 (color) / 澀; 彩度 / 採度; 飽和 / 抱和.
- gǎo: 稿 (draft) / 搞 (do/mess) — 草稿 / 搞定 (done); "搞" itself = "do/handle".
- biān / biàn: 邊 (edge) / 變 (change); 邊緣 (edge) / 變形 (transform).
- shēn: 深 (dark/deep) / 身 (body); 深一點 (darker) vs 身體.
- liàng: 亮 (bright) / 量 (amount); 亮部 (light side) / 量.
- huī: 灰 (gray) / 回; 灰面 / 回面.
- yīn: 陰 (shade) / 音 (sound); 陰影 / 音影.
- tóu: 頭 (head) / 投 (cast); 頭部 / 投影.
- gǔ: 骨 (bone) / 鼓; 骨架 / 股.
- 透視 vs 投射 vs 頭視 (ASR garble).
- 的/地/得 confusion (mainland ASR) — irrelevant to meaning, ignore.
- 一下 / 一點 / 一些 — softeners, not literal amounts.
- Numbers: 二/兩 both "two"; 一 vs 衣 (clothing) in Evan Lee course; 十 vs 是.
- Loanwords spoken in English mid-sentence: "layer", "OK", "value", "PS", "SAI", "brush", "overlay" — ASR may
  render as random characters (e.g., 累的 for "layer", 歐威雷 for "overlay"). Resolve to the English term.
