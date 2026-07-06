# Workflow

## Standard Run Setup

Start every new research run with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\new-run.ps1 -Name current -Problem "problem label"
```

The script creates the standard scaffold:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `reviews/review-current.md`
- output folders for figures, tables, data, models, and generated artifacts

Then follow the phase prompts from `prompts/00_intake.md` through `prompts/05_review.md`.

## 0. 准备题面

把题面和附件说明写入：

```text
problems/problem.md
```

如果有数据文件，建议新建：

```text
problems/data/
```

## 1. 题面理解

产物：

```text
runs/current/problem-analysis.md
```

内容：

- 问题重述
- 输入与输出
- 约束条件
- 评价指标
- 可能的数据缺口
- 易错点

## 2. 建模构思

产物：

```text
runs/current/model-candidates.md
```

要求至少比较三种方案，并明确为什么采用主方案。

## 3. 建模计划

产物：

```text
runs/current/model-plan.md
```

内容：

- 变量和参数
- 假设
- 目标函数
- 约束
- 求解算法
- 验证方法

## 4. 代码实验

代码放在：

```text
src/
```

输出放在：

```text
paper/figures/
paper/tables/
```

## 5. 论文写作

正文分节放在：

```text
paper/sections/
```

主文件：

```text
paper/main.tex
```

## 6. 编译

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\compile.ps1
```

## 7. 审查

根据 `docs/review-checklist.md` 写入：

```text
reviews/review-current.md
```

高风险问题修复后重新编译。
# Workflow Addendum

For every active generation or review run, create an artifact ledger based on `docs/artifact-ledger-template.md` at `runs/current/artifact-ledger.md`. The ledger is the bridge between paper claims, code outputs, data files, figures, tables, and PDF review.

## Structure and Figure Addendum

A complete CUMCM-style paper should reach 20-30 pages through structure:

```text
abstract
-> problem restatement
-> method overview
-> problem analysis
-> assumptions
-> symbols
-> data processing
-> model establishment and solution
-> results and validation
-> sensitivity analysis
-> strengths and limitations
-> conclusion
-> references
-> appendix
```

The figure plan must be created before writing the full paper:

```text
runs/current/figure-plan.md
```

The plan should include:

- route or workflow figure
- model-specific explanatory figures
- data exploration figures
- result figures
- validation or sensitivity figures

All figures must be listed in `runs/current/artifact-ledger.md`. Data-driven figures should be reproducible from code. Explanatory diagrams or AI-generated schematic images are allowed only when their source or prompt is recorded and they are not presented as experimental evidence.
