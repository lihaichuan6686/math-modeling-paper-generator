# Problem Type to Method Map

> 2026-07-06 update: 2021 CUMCM excellent papers add five confirmed routing cases: FAST active reflector -> geometry/engineering mechanics; C4 olefin preparation -> statistics + chemical optimization + experiment design; raw material ordering and transport -> evaluation + planning; continuous cutting -> online integer optimization; Chinese medicine spectra -> preprocessing + feature engineering + classification.

本文件把国赛常见题型和算法族连接起来。生成器在拿到题面后，应先识别题型，再提出多条候选模型链，而不是直接套单一算法。

## 评价决策类

常见任务：

- 多方案排序
- 指标体系构建
- 综合评分

候选方法：

- AHP
- 熵权法
- TOPSIS
- 灰色关联分析
- PCA
- 模糊综合评价

论文结构：

指标筛选 -> 数据标准化 -> 权重确定 -> 综合评价 -> 稳健性分析。

## 数据分析与预测类

常见任务：

- 销量、流量、含沙量、价格预测
- 趋势/周期/突变分析

候选方法：

- 描述统计与可视化
- 相关分析
- 回归模型
- 时间序列模型
- GM(1,1)
- 小波变换
- M-K 检验
- R/S 分析
- 机器学习模型

论文结构：

数据清洗 -> 探索性分析 -> 模型选择 -> 预测结果 -> 误差检验 -> 决策应用。

## 优化规划类

常见任务：

- 布局优化
- 路径设计
- 补货/定价/排程
- 资源分配

候选方法：

- 线性规划
- 非线性规划
- 整数规划
- 多目标规划
- 遗传算法
- 模拟退火
- 粒子群
- 网格搜索

论文结构：

变量定义 -> 目标函数 -> 约束条件 -> 求解算法 -> 结果表 -> 敏感性分析。

## 几何与工程机理类

常见任务：

- 光线反射
- 覆盖宽度
- 空间轨迹
- 遮挡判定

候选方法：

- 坐标变换
- 向量几何
- 三角函数关系
- 离散仿真
- 递推法
- 网格搜索

论文结构：

坐标系 -> 物理/几何关系 -> 核心公式 -> 数值计算 -> 误差或稳定性验证。

## 生产计划与调度类

常见任务：

- 批次安排
- 空间利用率
- 周期生产
- 容量约束

候选方法：

- 整数规划
- 动态规划
- 遍历搜索
- 蒙特卡洛模拟
- 排队论

论文结构：

周期分析 -> 决策变量 -> 容量约束 -> 优化求解 -> 方案可视化。

## 图与网络类

常见任务：

- 最短路径
- 连通性
- 配送网络
- 交通网络

候选方法：

- Dijkstra
- Floyd
- 最小生成树
- 最大流
- 匹配模型
- 社区发现

论文结构：

网络建模 -> 节点边定义 -> 指标或目标 -> 算法求解 -> 路径/网络图展示。

## 仿真类

常见任务：

- 随机系统
- 排队系统
- 行人/交通/传播过程

候选方法：

- 蒙特卡洛
- 元胞自动机
- 多智能体仿真
- 微分方程
- 排队论

论文结构：

机制假设 -> 状态转移规则 -> 参数设定 -> 仿真结果 -> 稳健性分析。
