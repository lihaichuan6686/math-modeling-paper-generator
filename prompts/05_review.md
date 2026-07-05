# Phase 5 Prompt: Review

根据 `docs/review-checklist.md` 审查当前论文、代码和图表，生成 `reviews/review-current.md`。

同时参考：

- `knowledge/quality/quality-rubric-plan.md`
- `knowledge/algorithms/algorithm-cards.md`

审查报告格式：

```text
# Review

## Blocking Issues

## Important Issues

## Minor Issues

## Suggested Revisions

## Human Verification Needed
```

发现高风险问题后，应先修复再重新编译。

重点检查：

- 是否每个算法都有使用理由。
- 是否每个子问题都有清晰输入、输出和验证。
- 是否存在公式、变量或结论无法闭合。
- 是否存在 AI 式空泛表达、过度自信或结果不可复现。
