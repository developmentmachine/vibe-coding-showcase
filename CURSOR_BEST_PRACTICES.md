# Cursor Vibe Coding 最佳实践指南

虽然 Gemini CLI 是一个强大的终端 Agent，但 **Cursor** 是目前最流行的可视化 AI 编程 IDE。Cursor 的底层逻辑依然是 Vibe Coding（用结构和上下文约束 AI），但它有着自己独特的交互哲学。

在 Cursor 中，“优雅”不仅仅体现在 `.cursorrules`，更体现在**动态上下文的精准投喂**上。

---

## 一、 动态上下文控制术：`@` 机制的艺术

Cursor 的灵魂在于其 `@` 引用机制。不要指望 AI 自己去“读懂”整个数万行的代码库，**显式投喂永远优于隐式猜测**。

* ✅ **`@Files` (精准打击)**：当你要修改 `analyzer.py` 时，不要光说“帮我改这个文件”，应该说：“参考 `@golden_service.py` 的错误处理逻辑，重构 `@analyzer.py`。”
* ✅ **`@Folders` (划定知识区)**：遇到编译错误时，说：“请在这个错误栈的基础上，检查 `@src/` 目录下的所有文件，寻找类型不匹配的地方。”
* ✅ **`@Docs` (注入外部真理)**：如果要用一个相对冷门或较新的库（比如 Pydantic V2 的最新特性），通过 `@Docs` 引入官方文档，能瞬间消除 AI 的幻觉。
* ✅ **`@Codebase` (慎用，仅限架构级提问)**：只有在问“我们的项目中哪里实现了重试逻辑？”这类宏观问题时才使用，否则会引入极大的“上下文噪音”。

---

## 二、 `.cursorrules` 的正确打开方式

Cursor 在每次对话时都会将 `.cursorrules` 作为最高优先级的 System Prompt 拼接到你的提问前。
**黄金法则：保持简短（控制在 150 行以内），只写“红线”，不写“业务逻辑”。**

**优秀的 CursorRules 结构：**
1. **Persona（角色设定）**：例如“你是一个资深的 Python 架构师”。
2. **Tech Stack（技术栈锁定）**：明确版本，如“React 18, Next.js 14, TailwindCSS”。
3. **Negative Constraints（红线禁区）**：例如“不要使用 any”、“不要修改 package.json 除非我明确要求”。
4. **Code Style（格式要求）**：例如“使用 Early Return（提前返回）”、“所有函数必须有完整的 Docstring”。

---

## 三、 上下文洁癖：被忽视的 `.cursorignore`

在 Vibe Coding 中，**不让 AI 看什么，比让它看什么更重要**。
如果 Cursor 的索引引擎把旧的日志、编译产物或巨大的 JSON 文件读了进去，AI 就会开始“胡言乱语”。

在项目根目录建立 `.cursorignore`，写入：
```text
# 严禁 AI 读取以下文件产生幻觉或浪费 Token
.venv/
node_modules/
dist/
build/
*.log
*.sqlite3
coverage/
```
*这相当于给 AI 戴上了眼罩，屏蔽了所有的“脏数据”。*

---

## 四、 双流协同：Cmd+L (Chat) 与 Cmd+I (Composer)

Cursor 提供了两种截然不同的 AI 交互模式，不要混用：

* **🔍 Cmd+L (Chat) - 负责“思考与探索”**
  * **作用**：研究代码、解释报错、生成测试计划、询问“我该怎么实现这个功能”。
  * **心态**：把它当成一个坐你旁边的资深同事，你们在白板前画图讨论。

* **🛠️ Cmd+I (Composer) - 负责“干脏活与多文件修改”**
  * **作用**：你已经在 Chat 里得到了方案，或者你心里已经有了明确的“指令”。打开 Composer，直接下达：“按照刚才讨论的方案，修改 `@schemas.py` 并在 `@analyzer.py` 中实现，同时在 `@test_analyzer.py` 中补充测试。”
  * **心态**：把它当成你的打字机。它会自动为你一次性修改跨越多个目录的文件。

---

## 五、 “一句话”高杠杆 Prompt 模板

在完善了 `.cursorrules` 和 Schema 后，你在 Cursor 里最常使用的完美 Prompt 应该长这样：

> "请实现 `@analyzer.py` 的核心逻辑，输入输出必须严格遵守 `@schemas.py`，遇到异常请参考 `@golden_service.py` 抛出自定义异常。确保 `@test_analyzer.py` 中的测试全部变绿。"

**解析**：没有任何一句废话，没有去解释业务是什么。你只是用 `@` 把“规则”、“输入输出”和“验收标准”像锁链一样扣在了一起，然后按下回车，享受 Vibe Coding 的快感。
