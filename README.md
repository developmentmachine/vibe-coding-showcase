# Vibe Coding Showcase: A-Share Sentiment Agent

这是一个为你量身定制的 Vibe Coding 架构示例。基于你工作区中的 `agent-platform`、`A-shares-hot` 以及现代 Python 栈（uv/Pydantic/Pytest）的使用习惯，我设计了这个微缩版的架构。

在这里，你不需要给 AI 写长篇大论的“需求文档”，而是通过 **6个维度的硬契约** 来锁死 AI 的输出边界。

## 目录结构映射的 6 大原则：

1. **环境与依赖声明 (Environment Constraints)**
   👉 `pyproject.toml`
   *AI 看到这个文件后，绝不敢乱引入 `requests` 或 `pandas`，它会严格使用 `httpx` 和 `pydantic>=2.0`。*

2. **结构化蓝图 (Schema & API)**
   👉 `src/schemas.py`
   *用 Pydantic V2 锁死了输入输出的字段和类型。AI 不需要猜“股票代码是 string 还是 int”，Schema 就是法律。*

3. **终极硬契约 (Test-Driven)**
   👉 `tests/test_analyzer.py`
   *TDD 驱动。测试用例里写明了“遇到异常代码必须抛出 404 错误”。这强迫 AI 必须处理边界（快乐路径陷阱），否则 CI 标红。*

4. **示例驱动 (Golden Examples)**
   👉 `examples/golden_service.py`
   *AI 的“字帖”。你不需要在规则里写“请使用 logging，并且捕获异常后要封装为自定义异常”，AI 只要看了这个文件，就会自动模仿这种完美的错误处理和依赖注入风格。*

5. **宏观规则与负向约束 (Context Control & Rules)**
   👉 `.cursorrules` 和 隐式的 `.cursorignore`（未建但概念一致）
   *定海神针，防止框架级别的幻觉（例如混淆 Pydantic V1/V2 语法）。*

6. **状态流转 (State/Git)**
   *(本目录假设为一个干净的起点)*

---
**接下来，你可以尝试对 AI 说：**
> "参考 `examples/golden_service.py` 的风格和 `src/schemas.py` 的结构，帮我在 `src/analyzer.py` 中实现测试用例 `tests/test_analyzer.py` 中要求的逻辑。"
