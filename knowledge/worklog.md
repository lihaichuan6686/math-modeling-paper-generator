# Worklog

## 2026-07-06 Structure and Figure Chain

- Added explicit CUMCM structure/page-allocation rules to `knowledge/cumcm/paper-generation-playbook.md`.
- Added figure-generation requirements to the modeling and implementation phases.
- Added `docs/figure-plan-template.md` so every run can plan route diagrams, explanatory schematics, evidence plots, and validation figures before writing.
- Updated `docs/artifact-ledger-template.md` to distinguish evidence, explanatory, and format figures.
- Updated `docs/workflow.md` and `CLAUDE.md` so future runs treat structure and figures as first-class workflow items.

## 2026-07-06 Playbook and Review Gate

- Added `knowledge/cumcm/paper-generation-playbook.md` as an executable CUMCM paper-generation workflow.
- Added `knowledge/algorithms/cumcm-routing-rules.md` to map problem signals to model chains.
- Added `docs/review-checklist.md` as a reusable paper quality gate.
- Updated `CLAUDE.md` so future runs know which knowledge files to read first.
- Continued local-only work; no GitHub upload was performed.

## 2026-07-06 Continued Local Study

- Completed first-pass visual reading notes for 2021 CUMCM official excellent papers A-E.
- Added `knowledge/cumcm/2021-official-first-pass.md`.
- Extracted five generator routing cases:
  - FAST active reflector: geometry and engineering mechanics.
  - C4 olefin preparation: statistics, chemical optimization, experiment design.
  - Raw material ordering and transport: supplier evaluation plus planning.
  - Continuous cutting: online integer optimization and abnormal-scenario adjustment.
  - Chinese medicine spectra: preprocessing, feature extraction, classifier comparison.
- No GitHub upload was performed, following the user's instruction that unattended learning should stay local.
- Inspected the 2024 CUMCM Word/LaTeX template bundle as a formatting and compliance resource.
- Added `knowledge/quality/reproducibility-and-ai-difference-framework.md`.
- Recorded a template-risk case: rendered cover year can follow current compile year while manual date fields remain stale, so date/season consistency must become a preflight check.

## 2026-07-06

### 已完成

- 建立长期知识库目录：
  - `knowledge/inventory`
  - `knowledge/cumcm`
  - `knowledge/algorithms`
  - `knowledge/latex`
  - `knowledge/quality`
- 建立资料盘点脚本：
  - `scripts/build-inventory.ps1`
  - 输出全量文件索引、按目录统计、按扩展名统计。
- 建立 PDF 概览脚本：
  - `scripts/extract-pdf-overview.py`
  - 对国赛论文目录下 79 个 PDF 抽取页数和首页文本片段。
- 建立 PDF 渲染脚本：
  - `scripts/render-pdf-pages.py`
  - 用于扫描型 PDF 的页面观察。
- 深读用户一等奖样例：
  - `LATEX/model1.tex`
  - `LATEX/model1.pdf`
  - 形成 `knowledge/latex/model1-case-study.md`。
- 首轮观察 2023 年官方优秀论文 A-E：
  - A：定日镜场输出功率优化
  - B：测线设计
  - C：蔬菜动态定价与补货
  - D：湖羊空间利用率优化
  - E：小浪底水库监测方案
  - 形成 `knowledge/cumcm/2023-official-first-pass.md`。
- 建立算法卡片：
  - TOPSIS
  - K-means/K-means++
  - 遗传算法
  - 模拟退火
  - 灰色预测 GM(1,1)
  - AHP
  - 蒙特卡洛
  - 0-1 规划/整数规划
- 建立题型到方法映射：
  - 评价决策
  - 数据分析与预测
  - 优化规划
  - 几何与工程机理
  - 生产计划与调度
  - 图与网络
  - 仿真
- 更新 `CLAUDE.md` 和阶段提示词，让智能体在生成论文前主动查阅知识库。

### 当前认识

- 国赛优秀论文通常不是单算法论文，而是“题型识别 -> 模型链 -> 结果验证”的组合。
- 摘要应采用逐问题写法，每个问题给出方法和关键结果。
- 20-30 页完整论文需要图、表、公式、算法解释、结果验证和附录共同支撑。
- 扫描型官方 PDF 需要页面渲染或 OCR，不能只依赖文本抽取。

### 下一步

1. 深读 2022 官方优秀论文 A-E。
2. 深读 2021 官方优秀论文 A-E。
3. 对 2024 A-E 成品论文进行“生成式论文风险”和“可复现性”分析。
4. 为每类题型补充更细的算法选择规则。
5. 升级 LaTeX 主模板，使其默认接近 20-30 页完整论文结构。
6. 建立论文质量检查 Rubric 2.0。
