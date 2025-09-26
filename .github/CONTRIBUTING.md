# 🤝 协作指南（CONTRIBUTING.md）

## 💡 分支命名规范
- 功能开发：`feature/<功能名>`  例如 `feature/login-form`
- Bug 修复：`fix/<描述>`        例如 `fix/overflow-error`
- 文档更新：`docs/<内容>`       例如 `docs/setup-instructions`

## 🧱 工作流程
1. 开始前：切换主分支并更新
git switch main
git pull
2. 创建新分支：
git switch -c feature/xxx

3. 修改代码、写注释、提交：
git add .
git commit -m "feat(xxx): 简要描述"
git push -u origin feature/xxx

4. 打开 Pull Request（PR），等待审查通过后合并！
<类型>(<作用域>): <简短描述>
## ✍️ 提交信息格式建议

例如：
feat(auth): add login endpoint
fix(ui): fix dropdown bug on mobile
docs(readme): add setup instructions


## ✅ 合并要求
- 所有改动必须通过 Pull Request 合并
- 禁止直接推送 `main` 分支（系统已限制）
- 每个 PR 至少一个 reviewer 审核通过才能合并
