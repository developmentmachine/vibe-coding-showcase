# 🏛️ Vibe Coding Showcase 核心宪法 (GEMINI.md)

> **注意**：这是针对 Gemini CLI 的项目级系统指令（Rules）。Gemini 在进入本项目工作区时会自动读取并遵循此文件。

## 1. 核心技术架构 (Core Architecture)
- **Runtime**: Python >= 3.10
- **Package Manager**: `uv` (严禁提示或使用 `pip install`)
- **Core Libraries**: `pydantic>=2.7.0` (仅限 V2 语法), `httpx`, `pytest`

## 2. 绝对禁忌 (Red Lines - NEVER DO THIS)
- 🚫 **禁止引入未声明依赖**：如果 `pyproject.toml` 中不存在该库，严禁在代码中 `import`。
- 🚫 **禁止降级类型系统**：严禁在代码中使用 `Any` 或 `# type: ignore`。
- 🚫 **禁止幻觉实现**：数据校验不得自编正则表达式，必须复用 `src/schemas.py` 中的模型。

## 3. 编码规程 (Coding Standards)
- **风格对齐**：所有新增 Service 类，必须 1:1 模仿 `examples/golden_service.py`（尤其是依赖注入与异常封装）。
- **测试驱动**：修复 Bug 或新增功能时，**第一步**是编写或更新 `tests/` 下的 pytest 异步用例；**第二步**才是修改业务代码。修改后必须确保所有测试通过（变绿）。

## 4. 协作协议 (Interaction Protocol)
- 不要在回复中输出冗长的解释，只输出代码意图和执行结果。
- 如果某项重构涉及跨越 3 个以上的文件，在动手前必须先输出一份修改计划，并请求用户确认。
