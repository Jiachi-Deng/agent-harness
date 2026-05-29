---
type: output
output_type: command-prompt
status: compiled
target_reader: AI 编程新手 / 独立开发者 / 产品和运营
use_case: 让 AI 按明确审美、价值主张和 CTA 生成高质量 Landing Page
version_date: 2026-05-28
compiled: 2026-05-28
upstream_wiki:
  - "[[Wiki/Vibe Coding/20-SaaS Build/Vibe Coding全栈SaaS开发闭环|Vibe Coding全栈SaaS开发闭环]]"
source_title: "VIBE CODING FULL COURSE: Gemini 3.1 + Antigravity (6 Hrs)"
source_clipping: "Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md"
review_note: "Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md"
source_prompt: "Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/prompts/Website Design Prompts.md"
merged_from_title: "高质量LandingPage提示词结构"
merged_on: 2026-05-28
compiled_style: bilingual_editable
tags:
  - VibeCoding
  - Prompt
  - LandingPage
  - WebDesign
  - Frontend
---

# Cinematic Landing Page Builder Prompt中英对照

## 使用场景

这个 prompt 用于让 AI 从 4 个输入生成一个高完成度 Landing Page：品牌名、审美方向、3 个价值主张、CTA。它的价值不只是“写得华丽”，而是把视觉生成拆成角色、提问、设计系统、组件架构、技术约束和构建顺序。

建议把它当作 **Landing Page 生成框架**，不要逐字照搬所有风格和动效。

## 为什么有价值

很多新手让 AI 做网页时只会说“做得高级一点”“像苹果官网一样”。结果通常是空泛、同质化、组件堆砌。

课程配套的 `Website Design Prompts.md` 有价值的地方在于：它不是只给 AI 一个审美形容词，而是把网站生成拆成角色、问题、风格预设、设计系统、组件结构、技术约束和构建顺序。它把“审美判断”变成可复用的操作结构。

这个页面已经合并了原来的 `高质量LandingPage提示词结构.md`。以后 Landing Page prompt 的结构分析、可复制版本、风险和验收都维护在这一页，不再拆成两个同粒度页面。

## 可替换变量

| 变量 | 用法 |
| --- | --- |
| `{BRAND_NAME}` | 品牌名 |
| `{ONE_LINE_PURPOSE}` | 一句话用途 |
| `{AESTHETIC_PRESET}` | 审美方向 |
| `{VALUE_PROP_1}` | 第一个价值主张 |
| `{VALUE_PROP_2}` | 第二个价值主张 |
| `{VALUE_PROP_3}` | 第三个价值主张 |
| `{PRIMARY_CTA}` | 主行动按钮 |
| `{STACK}` | 技术栈，例如 React + Tailwind + GSAP |

## Prompt结构中英对照

### 1. 角色 / Role

| English | 中文 |
| --- | --- |
| Act as a world-class senior creative technologist and lead frontend engineer. Build high-fidelity, cinematic, pixel-precise landing pages where every scroll, transition, and interaction feels intentional. | 扮演世界级高级创意技术专家和前端负责人。构建高保真、电影感、像素精确的 Landing Page，让每一次滚动、转场和交互都有明确意图。 |
| Avoid generic AI patterns, placeholder sections, and decorative components that do not support conversion. | 避免泛化 AI 风格、占位区块，以及不服务转化目标的装饰组件。 |

### 2. 一次只问 4 个问题 / Ask Exactly Four Questions

| English | 中文 |
| --- | --- |
| What is the brand name and one-line purpose? | 品牌名和一句话用途是什么？ |
| Pick an aesthetic direction from the presets. | 从预设中选择一个审美方向。 |
| What are the 3 key value propositions? | 3 个核心价值主张是什么？ |
| What should visitors do? | 访客应该执行什么行动？ |

### 3. 审美预设 / Aesthetic Presets

| Preset | English | 中文 |
| --- | --- | --- |
| Organic Tech | A bridge between a biological research lab and an avant-garde luxury magazine. Earthy, clinical, tactile, editorial. | 生物实验室和先锋奢华杂志之间的混合气质。自然、临床、触感强、杂志感。 |
| Midnight Luxe | A private members club meets a high-end watchmaker atelier. Dark, precise, premium, architectural. | 私人会员俱乐部加高级制表工坊。深色、精准、高端、建筑感。 |
| Brutalist Signal | A future control room with no decoration and high information density. Raw, direct, structured. | 未来控制室，没有多余装饰，信息密度高。粗粝、直接、结构化。 |
| Vapor Clinic | A genome sequencing lab inside a Tokyo nightclub. Neon, biotech, surreal, high contrast. | 东京夜店里的基因测序实验室。霓虹、生物科技、超现实、高对比。 |

### 4. 固定设计系统 / Fixed Design System

| English | 中文 |
| --- | --- |
| Use a consistent token system: palette, typography, radius, shadows, borders, image mood, and motion rules. | 使用一致的设计 token：色彩、字体、圆角、阴影、边框、图片氛围和动效规则。 |
| Add visual texture intentionally, such as subtle noise or material overlays, to avoid flat digital surfaces. | 有目的地加入视觉质感，例如微弱噪声或材质层，避免页面过于扁平。 |
| Buttons should have clear hover states and tactile micro-interactions. | 按钮要有清楚的 hover 状态和有触感的微交互。 |
| Animations must have lifecycle cleanup and should not make the page hard to read or slow on mobile. | 动画必须有生命周期清理，并且不能让页面难读或拖慢移动端。 |

### 5. 组件架构 / Component Architecture

| Section | English | 中文 |
| --- | --- | --- |
| Navbar | Floating, compact, readable navigation with logo, links, and one CTA. It may change appearance after the hero scroll. | 浮动、紧凑、可读的导航，包含 logo、链接和一个 CTA。滚过 hero 后可以改变样式。 |
| Hero | Full-bleed opening section with strong visual direction, bottom-left or editorial layout, high-contrast headline, and one primary CTA. | 全幅首屏，视觉方向强，采用左下或杂志式布局，高对比标题和一个主 CTA。 |
| Features | Three interactive cards derived from the value propositions. Each card should demonstrate product value, not just state a benefit. | 三个由价值主张生成的互动卡片。每张卡要演示产品价值，而不是只陈述卖点。 |
| Manifesto | Contrast the common industry approach with the brand's differentiated approach. | 对比行业常规做法和品牌差异化做法。 |
| Protocol | Three process cards or steps that explain how the product works. | 三个流程卡或步骤，解释产品如何工作。 |
| Pricing / CTA | Pricing grid if relevant; otherwise a focused get-started section. | 如果适合就做价格区，否则做聚焦的行动区。 |
| Footer | Brand, links, legal, and a small operational/status signal. | 品牌、链接、法律信息和一个小型状态提示。 |

### 6. 构建顺序 / Build Sequence

| English | 中文 |
| --- | --- |
| Map the selected preset to design tokens. | 把所选审美预设映射成设计 token。 |
| Generate hero copy from brand, purpose, and preset line pattern. | 根据品牌、用途和预设句式生成 hero 文案。 |
| Map the 3 value propositions to feature interactions. | 把 3 个价值主张映射成 feature 交互。 |
| Generate manifesto contrast statements. | 生成 manifesto 对比句。 |
| Generate process/protocol steps from the product method. | 根据产品方法生成流程步骤。 |
| Scaffold the project, install dependencies, implement, and verify responsive behavior. | 初始化项目、安装依赖、实现页面并验证响应式行为。 |
| Confirm images load, animations work, text fits, and CTA paths are valid. | 确认图片加载、动画可用、文字不溢出、CTA 路径有效。 |

## 可复制精简版 Prompt

```text
EN:
Act as a senior creative technologist and lead frontend engineer.
Build a high-fidelity landing page for:

Brand: {BRAND_NAME}
Purpose: {ONE_LINE_PURPOSE}
Aesthetic direction: {AESTHETIC_PRESET}
Value propositions:
1. {VALUE_PROP_1}
2. {VALUE_PROP_2}
3. {VALUE_PROP_3}
Primary CTA: {PRIMARY_CTA}
Stack: {STACK}

Requirements:
- Use the aesthetic direction to define palette, typography, layout rhythm, image mood, and motion style.
- Build sections: navbar, hero, 3 feature cards, manifesto, process/protocol, pricing or get-started CTA, footer.
- Each feature card must show product value through an interaction or micro-demo.
- Use real, relevant images or generated procedural visuals. No placeholders.
- Keep animations intentional, performant, and responsive.
- Mobile must be readable and usable.
- CTA paths must work.
- Do not create a generic SaaS template. Make every section support the product's actual promise.

Before coding, output the design tokens, section plan, and interaction plan. Then implement.
```

```text
中文：
请扮演高级创意技术专家和前端负责人。
为下面这个产品构建一个高保真 Landing Page：

品牌：{BRAND_NAME}
一句话用途：{ONE_LINE_PURPOSE}
审美方向：{AESTHETIC_PRESET}
核心价值主张：
1. {VALUE_PROP_1}
2. {VALUE_PROP_2}
3. {VALUE_PROP_3}
主 CTA：{PRIMARY_CTA}
技术栈：{STACK}

要求：
- 根据审美方向定义色彩、字体、布局节奏、图片氛围和动效风格。
- 页面包含：导航、首屏、3 个 feature card、manifesto、流程/protocol、价格或行动区、footer。
- 每个 feature card 都要用交互或微型 demo 展示产品价值，不要只写卖点。
- 使用真实相关图片或程序化视觉，不要占位图。
- 动画要有意图、性能可控、响应式可用。
- 移动端必须可读可用。
- CTA 路径必须能点击到正确位置。
- 不要生成泛化 SaaS 模板，每个 section 都要服务产品真实承诺。

写代码前，先输出 design tokens、section plan 和 interaction plan。确认后再实现。
```

## 使用时必须改的地方

- 可以保留 4 个输入问题、风格预设写法、设计系统、组件结构、构建顺序，以及“不要占位，要完整可运行”的要求。
- 风格预设不要一成不变。每个行业都要重新定义 palette、typography、image mood 和交互强度。
- 原 prompt 里的重型 GSAP、sticky stacking、复杂 canvas/particle 等适合视觉 demo，不一定适合 B2B SaaS 转化页。
- 如果已有项目使用 Next.js、shadcn、Tailwind v4 或其他体系，不要硬套 Vite 单文件结构。
- `rounded-[2rem]` 到 `rounded-[3rem]` 这类大圆角不是所有产品都适合，后台、工具和运营界面应更克制。
- 不要让动画遮挡文字、拖慢移动端或削弱 CTA。

## 验收清单

- [ ] 首屏能讲清产品给谁、解决什么、带来什么结果。
- [ ] 3 个 feature 不只是卡片，而是能演示价值。
- [ ] 审美不是单色堆叠，有清晰视觉语言。
- [ ] 字体、圆角、间距、图像、动效一致。
- [ ] 移动端文字不溢出、不遮挡。
- [ ] CTA 链路可用。
- [ ] 图片来源、版权和加载稳定性已检查。
- [ ] 页面没有泛化 AI 模板感。

## 可生成 Outputs

- `AI 生成高质量 Landing Page 的提示词模板`
- `落地页审美风格预设库`
- `Landing Page 生成后验收清单`

## 证据锚点

- 原始 prompt：`Raw/CourseKits/youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs/prompts/Website Design Prompts.md`
- 原始 transcript：`Clippings/VIBE CODING FULL COURSE Gemini 3.1 + Antigravity (6 Hrs).md` 中网站生成和 Netlify 部署段落。
- 人工审片记录：`Raw/NotebookLM/2026-05-28--youtube--vibe-coding--vibe-coding-full-course-gemini-3-1-antigravity-6hrs.review.md`
- 已合并旧页标题：`高质量LandingPage提示词结构`
