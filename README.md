# Math Modeling Paper Generator

一个面向 Claude Code 的数模论文研究生成器。项目目标是把赛题复盘、研究构思、建模实验、代码出图、LaTeX 排版和自我审查组织成可长期维护的工程流程。

本项目的长期研究方向是分析人类与 AI 生产的数学建模论文在结构、推理、实验、表达和可复现性上的差异，并探索将来作为论文品质检查助手、赛后复盘助手或教学辅助工具的可能性。

> 使用边界：本项目仅用于学习、赛后复盘、课程研究、授权研究和写作方法实验。请不要将它用于正在进行的竞赛违规提交、冒名写作或其他违反规则的场景。

## 能做什么

- 读取题面材料并生成结构化问题理解。
- 形成多套建模路线，比较适用条件、风险和可解释性。
- 生成可复现实验代码、图表、表格和中间数据。
- 按 CUMCM 风格组织 LaTeX 论文。
- 对模型假设、推导、代码、图表、引用和排版做多轮自查。
- 输出一份可继续人工修改的完整研究论文草稿。

## 推荐工作流

1. 把题面放入 `problems/problem.md`。
2. 在 Claude Code 中打开本仓库。
3. 让 Claude Code 按 `CLAUDE.md` 的阶段流程执行。
4. 代码、数据处理和图表放在 `src/`、`paper/figures/`、`paper/tables/`。
5. 论文正文写入 `paper/sections/`。
6. 编译 `paper/main.tex`，生成最终 PDF。
7. 按 `docs/review-checklist.md` 完成自查和人工复核。

## 项目结构

```text
.
├── CLAUDE.md                 # Claude Code 的总控工作说明
├── docs/
│   ├── architecture.md        # 项目架构
│   ├── workflow.md            # 阶段化生成流程
│   └── review-checklist.md    # 自我审查清单
├── paper/
│   ├── main.tex               # LaTeX 主文件
│   ├── cumcmthesis.cls        # CUMCM LaTeX 模板类
│   ├── sections/              # 论文分节
│   ├── figures/               # 生成图
│   └── tables/                # 生成表
├── prompts/                   # 分阶段提示词
├── problems/                  # 题面与输入材料
├── reviews/                   # 审查记录
├── runs/                      # 每次生成运行记录
├── scripts/                   # 编译和维护脚本
└── src/                       # 建模、仿真、绘图代码
```

## 快速开始

准备题面：

```powershell
Copy-Item path\to\problem.md problems\problem.md
```

编译论文：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

## 长期维护建议

- 每个题目使用一个独立分支或 `runs/YYYYMMDD-topic/` 记录。
- 重要实验保留数据来源、随机种子和运行说明。
- 图表必须由代码生成，不手工截图替代。
- 任何结论都要能追溯到假设、公式、代码或数据。
- 每次生成后都保留一份审查记录。

## 研究路线

- 比较人类论文和 AI 论文的问题拆解方式。
- 比较模型选择、假设表达、推导严密性和代码复现质量。
- 建立论文质量审查指标，包括逻辑一致性、结果可复现性、图表可信度和格式规范性。
- 形成面向教学、赛后复盘和官方质量检查的辅助流程。
