# GitHub Upload

## 上傳前檢查

- [ ] 沒有病人姓名、病歷號、影像或其他 PHI。
- [ ] 沒有未獲授權的全文 PDF 或文獻圖表。
- [ ] `README.md` 的進度狀態正確。
- [ ] Day 2、Day 3 尚未完成的內容仍標示為待完成。
- [ ] Relative links 可正常開啟。

## 建立 repository

在此資料夾開啟 terminal：

```bash
git init
git add .
git commit -m "Build Day 1 intracranial aneurysm report structure"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

若 GitHub repository 已經存在，不要重複 `git init` 或覆蓋既有 history；把本資料夾內容合併到既有 repository 後再 commit。

## 建議首頁閱讀順序

GitHub 首頁只需要從 [README.md](README.md) 進入。口頭報告準備則直接開啟 [REPORT_OUTLINE.md](REPORT_OUTLINE.md)。
