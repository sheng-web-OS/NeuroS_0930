#!/usr/bin/env python3
"""Extract the Day 1 evidence table from the complete working document."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "day1-full-working-document.md"
OUTPUT = ROOT / "docs" / "day1" / "02-evidence" / "evidence-matrix.md"


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    start_marker = "## 3. Evidence Matrix"
    end_marker = "## 4. 手術不利條件矩陣"
    if start_marker not in text or end_marker not in text:
        raise SystemExit("Cannot find the expected Day 1 evidence section markers.")

    section = text.split(start_marker, 1)[1].split(end_marker, 1)[0].strip()
    header = """# Evidence Matrix｜C01–C49

> 這是查詢資料庫，不是順讀文章。請先由 [Evidence Map](evidence-map.md) 選擇問題，再回查 Evidence ID。完整工作稿保留於 [data/day1-full-working-document.md](../../../data/day1-full-working-document.md)。

## 使用規則

- 每列只引用一個主張。
- Guideline recommendation、observational association 與作者 synthesis 必須分開。
- `R/U` 分別代表 ruptured/unruptured。
- `G/RCT/C/N/Synthesis` 的能力邊界見 [source-roles.md](source-roles.md)。

---

"""
    OUTPUT.write_text(header + section + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
