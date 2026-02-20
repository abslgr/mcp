import sqlite3
from datetime import date, datetime
from fastmcp import FastMCP
import csv
import os

mcp = FastMCP(name="expense server")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "expenses.db")

# ---------------- DB INIT ----------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        expense_date TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- TOOLS ----------------
@mcp.tool
def add_expense(amount: float, category: str, description: str, expense_date: str | None = None) -> str:
    """Add expense with optional date"""

    if not expense_date:
        expense_date = date.today().isoformat()

    try:
        datetime.strptime(expense_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format YYYY-MM-DD"

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
    "INSERT INTO expenses (amount, category, description, expense_date) VALUES (?, ?, ?, ?)",
        (amount, category, description, expense_date)
    )

    conn.commit()
    conn.close()

    return f"Expense added for {expense_date}"

@mcp.tool()
def list_expenses() -> list:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return rows

@mcp.tool()
def delete_expense(expense_id: int) -> str:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()
    return "Expense deleted"

@mcp.tool()
def summarize_expenses() -> dict:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    total = cur.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]
    by_cat = cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category").fetchall()
    conn.close()
    return {"total": total or 0, "by_category": by_cat}

@mcp.tool()
def get_expense_by_id(expense_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM expenses WHERE id=?", (expense_id,)).fetchone()
    conn.close()
    return row

@mcp.tool()
def update_expense(expense_id: int, amount: float):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE expenses SET amount=? WHERE id=?", (amount, expense_id))
    conn.commit()
    conn.close()
    return "Expense updated"

@mcp.tool()
def list_categories():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    rows = cur.execute("SELECT DISTINCT category FROM expenses").fetchall()
    conn.close()
    return rows

@mcp.tool()
def monthly_summary(month: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    rows = cur.execute(
        f"SELECT category, SUM(amount) FROM expenses WHERE expense_date LIKE ? GROUP BY category",
        (f"{month}%",)
    ).fetchall()
    conn.close()
    return rows

@mcp.tool()
def export_expenses_csv(filename: str = "expenses.csv"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM expenses").fetchall()
    cols = [c[1] for c in cur.execute("PRAGMA table_info(expenses)").fetchall()]
    conn.close()

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(cols)
        writer.writerows(rows)

    return f"Exported to {filename}"

@mcp.tool()
def clear_all_expenses():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses")
    conn.commit()
    conn.close()
    return "All expenses cleared"

@mcp.tool
def drop_table(table_name: str = "expenses", confirm: bool = False) -> str:
    """
    Drop a table from the database.
    ⚠️ confirm must be True to execute
    """

    if not confirm:
        return "Drop table aborted. Set confirm=True to proceed."

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(f"DROP TABLE IF EXISTS {table_name}")

    conn.commit()
    conn.close()

    return f"Table {table_name} dropped successfully"

# ---------------- RESOURCES ----------------
@mcp.resource(uri="resource://expenses/db-info", name="expenses_db_info", mime_type="application/json")
def expenses_db_info() -> dict:
    return {"db": DB_PATH, "table": "expenses"}

@mcp.resource(uri="resource://expenses/categories", name="categories_resource", mime_type="application/json")
def categories_resource() -> list:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    rows = cur.execute("SELECT DISTINCT category FROM expenses").fetchall()
    conn.close()
    return rows

@mcp.tool
def get_expenses_db_info() -> dict:
    return expenses_db_info()

@mcp.tool
def get_categories_resource() -> list:
    return categories_resource()

# ---------------- PROMPTS ----------------
@mcp.prompt(description="Analyze expenses")
def expense_analysis_prompt() -> str:
    return "Analyze my spending pattern and suggest savings tips."

@mcp.prompt(description="Monthly report")
def monthly_report_prompt(month: str) -> str:
    return f"Generate spending report for {month}"

@mcp.tool
def run_expense_analysis_prompt() -> str:
    return expense_analysis_prompt()

@mcp.tool
def run_monthly_report_prompt(month: str) -> str:
    return monthly_report_prompt(month)

# ---------------- SCHEMA TOOLS ----------------
@mcp.tool
def show_table_schema(table_name: str = "expenses") -> list:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    rows = cur.execute(f"PRAGMA table_info({table_name})").fetchall()
    conn.close()
    return rows

@mcp.tool
def run_sql(query: str) -> list:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(query)
    try:
        rows = cur.fetchall()
    except:
        rows = []
    conn.commit()
    conn.close()
    return rows

# ---------------- RUN ----------------
if __name__ == "__main__":
    mcp.run()