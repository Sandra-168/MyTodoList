import sys
import json

TODOS_FILE = "todos.json"


# === 資料存取 ===

def load_todos():
    """讀取 todos.json，回傳資料 dict。若檔案不存在則回傳初始結構。"""
    pass


def save_todos(data):
    """將資料 dict 寫入 todos.json。"""
    pass


# === 指令功能 ===

def add_todo(text):
    """Issue #1：新增一筆待辦事項。"""
    pass


def list_todos():
    """Issue #2：列出所有待辦事項。"""
    pass


def mark_done(todo_id):
    """Issue #3：將指定 ID 的待辦事項標記為完成。"""
    pass


def delete_todo(todo_id):
    """Issue #4：刪除指定 ID 的待辦事項。"""
    pass


def search_todos(keyword):
    """Issue #5：搜尋包含關鍵字的待辦事項。"""
    data = load_todos()
    results = [t for t in data["todos"] if keyword in t["text"]]
    if not results:
        print("找不到符合的待辦事項")
        return
    for t in results:
        status = "✅" if t["done"] else "⬜"
        print(f"[{t['id']}] {status} {t['text']}")


def show_stats():
    """Issue #6：顯示待辦事項統計資訊。"""
    pass


def edit_todo(todo_id, new_text):
    """Issue #7：編輯指定 ID 的待辦事項內容。"""
    pass


# === CLI 入口 ===

def main():
    """解析命令列參數並分派至對應的指令函式。"""
    args = sys.argv[1:]

    if not args:
        print("MyTodoList - 命令列待辦事項工具")
        print("Usage:")
        print('    python todo.py add "買牛奶"')
        print("    python todo.py list")
        print("    python todo.py done 1")
        print("    python todo.py delete 1")
        print('    python todo.py search "牛奶"')
        print("    python todo.py stats")
        print('    python todo.py edit 1 "新內容"')
        return

    command = args[0]

    if command == "hello":
        print("Hello! MyTodoList 環境設定成功 ✓")
    elif command == "add":
        add_todo(args[1])
    elif command == "list":
        list_todos()
    elif command == "done":
        mark_done(int(args[1]))
    elif command == "delete":
        delete_todo(int(args[1]))
    elif command == "search":
        search_todos(args[1])
    elif command == "stats":
        show_stats()
    elif command == "edit":
        edit_todo(int(args[1]), args[2])
    else:
        print(f"未知指令：{command}")


if __name__ == "__main__":
    main()
