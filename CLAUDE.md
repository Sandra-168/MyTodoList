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

### 確認安裝成功
```bash
python3 --version
```

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
