# Intracranial Aneurysm Report｜顱內動脈瘤文獻報告資料庫

這不是一篇連續文章，而是一個**報告組裝系統**。閱讀順序不由檔案長度決定，而由臨床決策層級決定：

1. 先判斷 **ruptured 或 unruptured**。
2. 再判斷是否需要 **立即 securing、血腫清除或減壓**。
3. 再比較 **clipping、endovascular treatment、observation** 的淨效益。
4. 最後才進入 **coil、BAC、SAC、FD、WEB** 與術後抗血小板策略。

> 核心警語：不要用下一層的裝置名稱，替上一層尚未回答的治療問題作答。

---

## 快速入口

| 使用目的 | 從這裡開始 | 產出 |
|---|---|---|
| 準備口頭報告 | [REPORT_OUTLINE.md](REPORT_OUTLINE.md) | 12 張投影片的問題、結論與來源 |
| 完成 Day 1 | [docs/day1/README.md](docs/day1/README.md) | 手術不利條件與 clipping/endovascular 骨架 |
| 追查 01–33 任務 | [docs/day1/task-index.md](docs/day1/task-index.md) | 每一題對應到實際檔案 |
| 回查單一證據 | [docs/day1/02-evidence/evidence-matrix.md](docs/day1/02-evidence/evidence-matrix.md) | C01–C49 evidence claims |
| 查核心文獻 | [references/core-sources.md](references/core-sources.md) | 文獻角色、可支持與不可支持的命題 |
| 查看三日全計畫 | [planning/99-core-tasks.md](planning/99-core-tasks.md) | 99 項任務、時間與驗收標準 |
| 新增子問題 | [templates/subquestion-template.md](templates/subquestion-template.md) | 固定的報告型資料格式 |

---

## 資料夾邏輯

| 層級 | 功能 | 閱讀原則 |
|---|---|---|
| `docs/day1/01-framing/` | 固定報告問題、族群與名詞 | 沒有固定邊界，不進入證據比較 |
| `docs/day1/02-evidence/` | 文獻角色與 evidence matrix | 只放可回查的主張，不承擔敘事 |
| `docs/day1/03-surgical-selection/` | 拆解手術相對不利的真正機轉 | 位置只是代理變項，必須回到走廊、分支、血腫與病人耐受性 |
| `docs/day1/04-synthesis/` | 把證據轉成投影片、矩陣與病例 | 每項結論必須附反例與停止點 |
| `docs/day2/` | 裝置選擇系統 | Day 1 完成後才進入 |
| `docs/day3/` | 藥物與術後照護 | 必須依 device 與 rupture status 分層 |
| `data/` | 完整工作稿與可稽核底稿 | 不建議作為口頭報告的第一入口 |

---

## 目前進度

| 區塊 | 狀態 | 說明 |
|---|---|---|
| Day 1：問題、證據、手術決策 | **已完成** | 49 條 evidence claims；任務 01–32 完成，任務 33 已有講稿、待本人計時 |
| Day 2：五種裝置比較 | 尚未完成 | 目前只有任務入口與預定產出 |
| Day 3：藥物與術後照護 | 尚未完成 | 目前只有任務入口與預定產出 |

---

## 報告使用規則

- **投影片只放結論、比較軸與決策後果。**完整數字留在 evidence matrix。
- **觀察性關聯不可寫成術式因果比較。**尤其 UIA 的 pooled complication rates。
- **coiling 不等於所有 endovascular devices。**AHA/ASA 對 primary coiling 的推薦不可自動外推至 SAC 或 FD。
- **不確定性不是待刪除的雜訊。**會改變治療方向的未知，必須留在 [uncertainty-log.md](docs/day1/04-synthesis/uncertainty-log.md)。

## 版本邊界

本資料庫用於 clerk 以上的神經外科／神經介入文獻報告。單一病人的實際治療仍需完整 angiography、clinical grade、hematoma、branch/perforator anatomy、病人耐受性及 multidisciplinary discussion。
