# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案說明

**MyTodoList** 是一個 Python 命令列待辦事項工具，供團隊練習 GitHub 協作流程（Issue → Branch → PR → Review → Merge）。

遠端倉庫：https://github.com/Sandra-168/MyTodoList.git

## 語言與溝通偏好

- 繁體中文回應
- commit message 使用繁體中文
- 程式碼註解與 docstring 使用繁體中文
- 程式碼本體保留英文

## 環境需求

需要 **Python 3.6+**，不需安裝任何額外套件。

### 安裝 Python 3（Windows）

至 https://www.python.org/downloads/ 下載安裝檔，安裝時勾選「Add Python to PATH」。

### 安裝 Git（Windows）

至 https://git-scm.com/downloads 下載安裝檔，安裝時選項維持預設即可。

### 安裝 Claude Code（Windows）

開啟 PowerShell 執行：

```powershell
irm https://claude.ai/install.ps1 | iex
```


### 確認安裝成功

```bash
python --version
git --version
claude --version
```

---

## 開始使用

### Clone 專案

```bash
git clone https://github.com/Sandra-168/MyTodoList.git
cd MyTodoList
```

### 開啟 Claude Code

在專案目錄下執行：

```bash
claude
```

### 切換 Model 為 Sonnet

進入 Claude Code 後輸入 `/model`，從清單中選擇 Sonnet，按 Enter 確認。

---

## 開發指令

開啟「命令提示字元（cmd）」或「PowerShell」，切換至專案目錄後執行：

```bash
cd 你的專案路徑\MyTodoList

# 確認環境是否設定成功
python todo.py hello

# 執行程式
python todo.py

# 各指令範例
python todo.py add "買牛奶"
python todo.py list
python todo.py done 1
python todo.py delete 1
python todo.py search "牛奶"
python todo.py stats
python todo.py edit 1 "新內容"
```

## 架構說明

所有邏輯集中在單一檔案 `todo.py`，內部依職責分為三個區塊：

```
# === 資料存取 ===
load_todos()      # 讀取 todos.json，回傳 dict
save_todos()      # 將 dict 寫入 todos.json

# === 指令功能 ===
add_todo(text)    # Issue #1：新增待辦事項
list_todos()      # Issue #2：列出所有待辦事項
mark_done(id)     # Issue #3：標記完成
delete_todo(id)   # Issue #4：刪除待辦事項
search_todos(kw)  # Issue #5：搜尋功能
show_stats()      # Issue #6：統計功能
edit_todo(id, text) # Issue #7：編輯待辦事項

# === CLI 入口 ===
main()            # 解析 sys.argv 並分派至對應函式
```

## 資料儲存

資料存於本機 `todos.json`（已加入 `.gitignore`，不進 repo）。

資料結構：

```json
{
  "next_id": 6,
  "todos": [
    { "id": 1, "text": "買牛奶", "done": true },
    { "id": 2, "text": "寫週報", "done": false }
  ]
}
```

- `next_id`：遞增計數器，確保 ID 唯一不重複
- 刪除後 ID 不補位（保留原始編號）

## 協作分工

每個 Issue 對應 `todo.py` 中的一個函式，認領後只需實作該函式，不影響其他人的工作範圍。

### 如何認領 Issue

1. 到 https://github.com/Sandra-168/MyTodoList/issues 查看所有 Issue
2. 點進想做的 Issue，在下方留言「我來做」
3. 開一個新 branch，命名格式為 `feature/issue-1-add-todo`（數字和名稱對應你的 Issue）
4. 完成後 commit、push，到 GitHub 開 Pull Request
5. PR 標題格式：`feat: 新增待辦事項 (closes #1)`（#1 換成你的 Issue 編號）
6. 找隊友 Code Review，通過後 merge 進 main
