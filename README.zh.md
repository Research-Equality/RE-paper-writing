[English](README.md) | [简体中文](README.zh.md)

# RE-paper-writing

一个面向学术论文写作的权威 skills 仓库，覆盖论文规划、文献奠基、分节写作、修改润色，以及基于 LaTeX 的投稿准备流程。

这个仓库只保留与论文写作直接相关的 skill。唯一权威、可加载的技能集合位于 [`skills/`](skills/)；根目录中的其他项目目录保留为来源快照或上游参考，不是规范化后的 skill 目录。

多数项目只会用到其中一部分 skill。这个仓库应该被当作一个分阶段工作流，而不是每篇论文都要从头到尾全部调用一遍的清单。

## 仓库定位

- 只保留直接服务于论文规划、写作、文献综述、引用管理、表格生成、LaTeX 整理、自审、修改和 rebuttal 的 skill
- 将上游内容整理为可移植的仓库结构，去掉作者个人机器上的绝对路径依赖
- 把 [`skills/`](skills/) 作为后续论文写作相关 skill 的唯一权威目录

## 当前收录的 Skill

当前共收录 35 个 skill。

### 规划与文献奠基

- `research-planning`：把研究主题或初稿想法转成论文结构和任务计划
- `literature-search`：多源学术检索，输出结构化 JSONL
- `systematic-review`：可复用、产物驱动的系统综述流程
- `literature-review`：对已有文献集合做综合分析与梳理
- `source-material-ingestion`：把 PDF、DOCX、PPTX、XLSX 等源文件转换成可搜索的 Markdown 写作输入
- `citation-management`：校验、补全、修复和导出 BibTeX 引用
- `paper-memory-ledger`：跨会话保存论文项目的稳定事实、venue 约束、实验结论和写作约定

### 写作与稿件构建

- `experiment-report-bridge`：把本地实验产物整理成可直接喂给正式论文写作的 Markdown 报告
- `ml-paper-writing`：从研究仓库或成熟结果集合组织整篇论文初稿
- `latex-writeup-loop`：直接在 `template.tex` 中完成章节写作、补引和编译修复闭环
- `long-form-manuscript-polish`：把 bullet-heavy、像提纲或幻灯片的长文稿打磨成 prose-first 的正式论文
- `reverse-outline-flow-check`：用 reverse outline、段落角色和逻辑关系诊断 section flow
- `claim-evidence-map`：把论文主张映射到明确证据锚点，并下调没有支撑的表述
- `experiment-section-audit`：围绕 baseline、ablation 和 reviewer-facing 证据重构 Experiments
- `related-work-writing`：按主题组织、对比式写 Related Work
- `survey-generation`：基于文献语料生成 survey 稿件
- `paper-writing-section`：按章节撰写或重写论文段落
- `table-generation`：把结果文件转换成论文可用的 LaTeX 表格
- `paper-schematics`：生成图形摘要、方法流程图和其他概念型论文图示
- `academic-plotting`：生成数值型结果图和其他数据驱动的论文图表

### 投稿、评审与修改

- `paper-session-compaction`：把超长写作或改稿会话压缩成可靠的续写摘要
- `venue-submission-strategy`：按目标 venue 调整 framing、篇幅预算和 reviewer-facing 包装方式
- `reporting-guidelines-check`：核对稿件是否满足 CONSORT、STROBE、PRISMA 等报告规范
- `claim-rigor-audit`：检查论文主张是否超出了研究设计、证据强度或统计结果本身能支持的范围
- `manuscript-scorecard`：按维度给稿件打分，并跟踪不同修订版本的质量变化
- `latex-formatting`：按会议要求整理 LaTeX 格式
- `submission-qa-gate`：在导出前做最后一轮机械化投稿检查，包括标签、TODO、引用覆盖和编译就绪性
- `paper-compilation`：编译论文并定位 LaTeX 构建错误
- `paper-evidence-verifier`：核对论文中的数字与实验产物是否一致，防止结果造假或漂移
- `citation-verification-gate`：基于真实学术 API 校验引用并剔除幻觉文献
- `self-review`：投稿前结构化自审
- `review-ensemble`：使用多评审与元评审方式做更严格的稿件评估
- `paper-revision`：把评审意见映射到具体改稿动作
- `paper-redline-diff`：生成带修改痕迹的稿件 diff，用于改稿核对和 rebuttal 支撑
- `rebuttal-writing`：生成逐点回应的 rebuttal 文档

技能目录与简要路由见 [`skills/README.md`](skills/README.md)。

## 主流程

1. 先确定论文问题和证据底座：
   `research-planning` -> `literature-search` -> `systematic-review` 或 `literature-review`
2. 再整理输入材料并保持长期上下文：
   `source-material-ingestion` -> `paper-memory-ledger`
3. 如果实验已完成，先把实验结果整理成写作 handoff：
   `experiment-report-bridge`
4. 然后只选一个主写作入口：
   `ml-paper-writing` 负责整篇初稿，
   `latex-writeup-loop` 负责在现有 LaTeX 模板内原地写作，
   `paper-writing-section` / `related-work-writing` / `survey-generation` 负责分节写作
5. 只在需要时插入局部专科：
   `reverse-outline-flow-check`、`long-form-manuscript-polish`、`claim-evidence-map`、`experiment-section-audit`、`table-generation`、`paper-schematics`、`academic-plotting`
6. 导出前运行可信度和合规性检查：
   `citation-management`、`paper-evidence-verifier`、`claim-rigor-audit`、`citation-verification-gate`、`reporting-guidelines-check`、`venue-submission-strategy`
7. 投稿前运行提交栈：
   `latex-formatting` -> `submission-qa-gate` -> `paper-compilation`
8. 收到评审后进入评审循环：
   `self-review` 或 `review-ensemble` -> `paper-revision` -> `paper-redline-diff` -> `rebuttal-writing`
9. 只有在跨会话工作时才启用连续性工具：
   `paper-session-compaction` 负责长线程 handoff，`paper-memory-ledger` 负责保存稳定事实

## 边界规则

- 同一时刻只选一个主写作入口，不要默认把 `ml-paper-writing`、`latex-writeup-loop`、`paper-writing-section` 混在同一步。
- `paper-schematics` 只管概念型、非数值型图；`academic-plotting` 只管数值型或数据驱动图。
- `claim-evidence-map` 负责论文正文可见的 claim-support 映射，`paper-evidence-verifier` 负责实验产物层面的数字核对，`claim-rigor-audit` 负责推断和论证强度。
- `submission-qa-gate` 负责整体就绪性；`paper-compilation` 只在 LaTeX 构建和报错排查本身是瓶颈时使用。
- `self-review` 用于快速单轮自审；`review-ensemble` 只在你需要更严格、更接近程序委员会的信号时使用。
- `paper-memory-ledger` 保存稳定的跨会话事实；`paper-session-compaction` 只处理单条超长线程的压缩 handoff。

共享产物约定：

- `outputs/<topic-slug>/search_results/*.jsonl`：原始检索结果
- `outputs/<topic-slug>/paper_db.jsonl`：共享文献语料库
- `outputs/<topic-slug>/reading_notes.md`、`synthesis.md`、`gaps.md`：综述中间产物
- `references.bib`：当前稿件引用库

## 仓库结构

```text
skills/
  citation-management/
  latex-formatting/
  literature-review/
  literature-search/
  source-material-ingestion/
  paper-memory-ledger/
  experiment-report-bridge/
  ml-paper-writing/
  latex-writeup-loop/
  long-form-manuscript-polish/
  reverse-outline-flow-check/
  claim-evidence-map/
  experiment-section-audit/
  paper-session-compaction/
  claim-rigor-audit/
  manuscript-scorecard/
  paper-schematics/
  reporting-guidelines-check/
  venue-submission-strategy/
  paper-evidence-verifier/
  submission-qa-gate/
  paper-compilation/
  paper-revision/
  paper-redline-diff/
  paper-writing-section/
  rebuttal-writing/
  related-work-writing/
  research-planning/
  review-ensemble/
  self-review/
  survey-generation/
  systematic-review/
  table-generation/
  academic-plotting/
  citation-verification-gate/
```

## 使用方式

以下命令默认在仓库根目录执行。

示例：构建一个可复用的文献语料库

```bash
python skills/systematic-review/scripts/search_semantic_scholar.py \
  --query "long-context reasoning agents" \
  --max-results 20 \
  --api-key "$S2_API_KEY" \
  -o outputs/long-context-reasoning-agents/search_results/s2.jsonl

python skills/systematic-review/scripts/bibtex_manager.py \
  --jsonl outputs/long-context-reasoning-agents/paper_db.jsonl \
  --output outputs/long-context-reasoning-agents/references.bib
```

推荐环境：

- Python 3.10+
- 可选环境变量：`S2_API_KEY`
- 可选依赖：`PyMuPDF`，用于 `self-review` 与 `systematic-review` 的 PDF 处理

## 收录规则

- skill 必须直接提升论文规划、写作质量、引用完整性、审稿质量或 LaTeX 投稿准备
- 实验执行、通用代码生成、GitHub 仓库挖掘、纯展示型流程不纳入当前整理范围
- 对于重复且脆弱的任务，优先保留可脚本化、可审计的 skill

## 来源说明

当前 `skills/` 下的整理结果主要来自本仓库中的 `agent-research-skills/`、`AI-research-SKILLs/20-ml-paper-writing/`、`ai-scientist/`、`AutoResearchClaw/`、`claude-scientific-skills/`、`claude-scientific-writer/`、`EvoScientist/`、`latex-document-skill/` 与 `Research-Paper-Writing-Skills/` 中和论文写作直接相关的部分，并已统一规范成可移植的权威目录。

本次整理的关键决策：

- 将 `deep-research` 重命名并收敛为 `systematic-review`
- 去除了硬编码的用户本地路径，统一改为仓库相对路径
- 只保留和论文写作直接相关的 skill；实验、代码和泛研究自动化能力不纳入当前目录
