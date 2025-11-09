# LINE Bot 智能文件助手 📚

> 一個結合 LINE Bot 與 Google Gemini File Search 的智能文件問答機器人

<img width="1179" height="2556" alt="image" src="https://github.com/user-attachments/assets/4d5a4e0e-0eec-4753-a1b0-8b1e1e6d661a" />


## 🎯 這是什麼？

想像一下：你可以把任何 PDF、Word 文件、圖片傳給 LINE Bot，然後直接問它「這份文件在講什麼？」、「幫我整理重點」、「這張圖片裡有什麼？」，Bot 就會用 AI 幫你分析並回答！

這個專案讓你輕鬆打造一個專屬的文件智能助手，只要：
1. 📤 傳送文件或圖片給 Bot
2. 💬 用自然語言提問
3. 🤖 AI 立即分析並回答

## ✨ 功能特色

### 📁 支援多種檔案格式
- 📄 文件檔案：PDF、Word (DOCX)、純文字 (TXT) 等
  - 自動上傳到 File Search Store
  - 支援後續文字查詢
- 🖼️ 圖片檔案：JPG、PNG 等
  - 使用 Gemini 視覺理解能力即時分析
  - 無需上傳，直接回傳分析結果

### 🧠 AI 智能問答
- 使用 Google Gemini 2.5 Flash 模型
- 基於你上傳的文件內容回答問題
- 支援繁體中文、英文等多語言

### 👥 多人協作支援
- **1 對 1 聊天**：每個人有自己的文件庫（隔離的）
- **群組聊天**：群組成員共享文件庫（大家都能查詢）
- 自動識別對話類型，無需手動設定

### 📋 檔案管理功能
- **AI 口語化列表**：使用 Google ADK Agent 以自然對話方式介紹檔案
- **智能識別**：支援多種關鍵字（列出檔案、顯示檔案、list files 等）
- **Quick Reply 快速操作**：上傳成功後提供「生成摘要」、「重點整理」等快捷按鈕
- **明確檔案指定**：Quick Reply 自動帶入檔案名稱，避免混淆

### 🚀 部署簡單
- 支援 Docker 容器化部署
- 可部署到 Google Cloud Run
- 或在本地開發測試

## 📸 使用範例

### 📤 上傳文件並查詢

```
👤 你: [上傳一份會議記錄.pdf]
🤖 Bot: ✅ 檔案已成功上傳！
       檔案名稱：會議記錄.pdf

       現在您可以詢問我關於這個檔案的任何問題。

       [Quick Reply 按鈕]
       📝 生成檔案摘要 | 📌 重點整理 | 📋 列出檔案

👤 你: [點擊「📝 生成檔案摘要」]
     → 自動發送「請幫我生成「會議記錄.pdf」這個檔案的摘要」

🤖 Bot: 好的！這份會議記錄主要記錄了 2025 年第一季的營運會議...

       主要決議包括：
       1. 下季度預算增加 15%
       2. 新產品預計 6 月上市
       3. 人力資源部門將擴編 3 名員工
       ...
```

### 📋 列出檔案（AI 口語化）

```
👤 你: 列出檔案
🤖 Bot: 我看到你上傳了 3 個檔案唷！

       首先是「會議記錄.pdf」，這是在 1月8日下午2點半上傳的。
       接著是「技術文件.docx」，是在下午3點20分傳的。
       最後一個是「報告.txt」，這個是在下午4點10分上傳的。

       需要我幫你查詢哪個檔案的內容呢？😊
```

> 💡 **提示**：使用 Google ADK Agent 讓 AI 用自然對話方式介紹檔案，比傳統的清單或卡片更親切！

### 🖼️ 圖片分析

```
👤 你: [傳送圖片]
🤖 Bot: 正在分析您的圖片，請稍候...

🤖 Bot: 📸 圖片分析結果：

       這張圖片顯示了一個現代化的辦公室空間...
```

## 🛠️ 技術架構

- **Python 3.9+**
- **FastAPI** - 高效能異步 Web 框架
- **LINE Messaging API** - LINE Bot 介面（含 Quick Reply）
- **Google Gemini API** - 文件搜尋與 AI 問答
- **Google ADK (Agent Development Kit)** - 口語化檔案管理 Agent
- **Docker** - 容器化部署

## 📦 快速開始

### 1️⃣ 環境準備

首先，你需要準備這些：

**LINE Bot 設定**
1. 到 [LINE Developers Console](https://developers.line.biz/console/) 建立一個 Messaging API channel
2. 取得你的 `Channel Secret` 和 `Channel Access Token`

**Google Gemini API**
1. 到 [Google AI Studio](https://aistudio.google.com/app/apikey) 建立 API Key
2. 複製你的 `API Key`

### 2️⃣ 下載專案

```bash
git clone <你的 repo URL>
cd linebot-file-search-adk
```

### 3️⃣ 安裝套件

```bash
pip install -r requirements.txt
```

### 4️⃣ 設定環境變數

建立 `.env` 檔案或直接設定環境變數：

```bash
export ChannelSecret="你的 LINE Channel Secret"
export ChannelAccessToken="你的 LINE Channel Access Token"
export GOOGLE_API_KEY="你的 Google Gemini API Key"
```

### 5️⃣ 啟動服務

```bash
uvicorn main:app --reload
```

服務會在 `http://localhost:8000` 啟動

### 6️⃣ 設定 Webhook

如果在本地開發，使用 ngrok 來建立公開的網址：

```bash
ngrok http 8000
```

然後到 LINE Developers Console，把 Webhook URL 設定為：
```
https://你的-ngrok-網址.ngrok.io/
```

## 🎮 使用方式

### 📤 上傳檔案

**文件檔案（PDF、DOCX、TXT 等）：**
1. 直接在 LINE 聊天室傳送文件檔案
2. Bot 會回覆「正在處理您的檔案，請稍候...」
3. 上傳完成後會顯示「✅ 檔案已成功上傳！」
4. 現在可以開始提問關於文件的內容

**圖片檔案（JPG、PNG 等）：**
1. 直接在 LINE 聊天室傳送圖片
2. Bot 會回覆「正在分析您的圖片，請稍候...」
3. 立即收到圖片分析結果
4. 圖片不會儲存，每次都是即時分析

### 💬 開始提問

**文件查詢（需先上傳文件）：**

- 「這份文件的重點是什麼？」
- 「幫我整理成條列式」
- 「第三章在講什麼？」
- 「根據這份報告，我們應該注意什麼？」

**圖片分析（直接傳圖片）：**

- 傳送圖片後自動分析
- 會描述圖片的內容、場景、物品、文字等
- 無需額外提問

### 📋 管理已上傳的檔案

**列出檔案（AI 口語化）：**

支援多種關鍵字來查看已上傳的文件：
- 「列出檔案」或「列出文件」
- 「顯示檔案」或「查看檔案」
- 「我的檔案」或「檔案列表」
- 英文：「list files」、「show files」、「my files」

Bot 會用 **Google ADK Agent** 以自然對話方式介紹檔案：
- 🤖 口語化描述（而非條列式清單）
- 📅 自動格式化上傳時間
- 💬 友善親切的語氣
- 🎯 智能總結（檔案多時會挑重點說明）

**Quick Reply 快速操作：**

上傳檔案成功後，Bot 會提供快捷按鈕：
- 📝 **生成檔案摘要** - 自動帶入檔案名稱「請幫我生成『檔名』這個檔案的摘要」
- 📌 **重點整理** - 自動帶入檔案名稱「請幫我整理『檔名』的重點」
- 📋 **列出檔案** - 查看所有已上傳的文件

> 💡 **提示**：Quick Reply 會自動帶入剛上傳的檔案名稱，避免多檔案時的混淆！

### 📁 檔案管理方式

**文件檔案：**
- **個人聊天**：每個人有獨立的文件庫，只能查詢自己上傳的檔案
- **群組聊天**：所有群組成員共享同一個文件庫，任何人上傳的檔案都能被查詢
- 文件會持續保存在 File Search Store 中

**圖片檔案：**
- 不會儲存到 File Search Store
- 每次傳送都是即時分析
- 分析完成後圖片會自動清除

## 🐳 Docker 部署

### 建立映像檔

```bash
docker build -t linebot-file-search .
```

### 啟動容器

```bash
docker run -p 8000:8000 \
  -e ChannelSecret=你的SECRET \
  -e ChannelAccessToken=你的TOKEN \
  -e GOOGLE_API_KEY=你的API_KEY \
  linebot-file-search
```

## ☁️ 部署到 Google Cloud Run

### 步驟 1：安裝 Google Cloud SDK

參考[官方文件](https://cloud.google.com/sdk/docs/install)安裝

### 步驟 2：登入並設定專案

```bash
gcloud auth login
gcloud config set project 你的專案ID
```

### 步驟 3：建立並上傳 Docker 映像

```bash
gcloud builds submit --tag gcr.io/你的專案ID/linebot-file-search
```

### 步驟 4：部署到 Cloud Run

```bash
gcloud run deploy linebot-file-search \
  --image gcr.io/你的專案ID/linebot-file-search \
  --platform managed \
  --region asia-east1 \
  --allow-unauthenticated \
  --set-env-vars ChannelSecret=你的SECRET,ChannelAccessToken=你的TOKEN,GOOGLE_API_KEY=你的API_KEY
```

### 步驟 5：取得服務網址

```bash
gcloud run services describe linebot-file-search \
  --platform managed \
  --region asia-east1 \
  --format 'value(status.url)'
```

把這個網址設定到 LINE Bot 的 Webhook URL 就完成了！

## 🔒 安全性建議

**不要把敏感資訊寫進程式碼！** 建議使用 Google Secret Manager：

```bash
# 建立 secrets
echo -n "你的SECRET" | gcloud secrets create line-channel-secret --data-file=-
echo -n "你的TOKEN" | gcloud secrets create line-channel-token --data-file=-
echo -n "你的API_KEY" | gcloud secrets create google-api-key --data-file=-
```

部署時使用 secrets：

```bash
gcloud run deploy linebot-file-search \
  --image gcr.io/你的專案ID/linebot-file-search \
  --platform managed \
  --region asia-east1 \
  --allow-unauthenticated \
  --update-secrets=ChannelSecret=line-channel-secret:latest,ChannelAccessToken=line-channel-token:latest,GOOGLE_API_KEY=google-api-key:latest
```

## 📊 監控與除錯

部署後可以透過 Google Cloud Console 監控：

### 查看 Logs

```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=linebot-file-search" --limit 50
```

### 檢查服務狀態

直接到 [Cloud Run Console](https://console.cloud.google.com/run) 查看服務狀態、錯誤率、回應時間等指標

## 💡 使用小技巧

1. **上傳多份文件**：可以連續上傳多份文件，Bot 會記住所有文件並在查詢時搜尋
2. **圖片即時分析**：圖片不需要「上傳」，直接傳送就會立即分析並回覆
3. **文件持久化**：上傳的文件會持續保存在 File Search Store，可隨時查詢
4. **Quick Reply 快捷操作**：
   - 上傳檔案後立即使用 Quick Reply 按鈕（生成摘要、重點整理）
   - Quick Reply 會自動帶入檔案名稱，避免多檔案時混淆
   - 點擊按鈕比手動輸入更快速方便
5. **AI 口語化檔案列表**：
   - 輸入「列出檔案」會得到自然對話式的回應
   - AI 會用親切的語氣介紹每個檔案和上傳時間
   - 比傳統清單更友善、更易讀
6. **支援的檔案類型**：
   - 文件：取決於 Google Gemini File API 的支援
   - 圖片：JPG、JPEG、PNG、GIF、WebP

## 🤔 常見問題

**Q: 為什麼我問問題時 Bot 說「您還沒有上傳任何檔案」？**
A: 這個訊息是針對文件查詢。請先上傳文件檔案（PDF、DOCX 等），Bot 才能根據文件內容回答。如果您想分析圖片，請直接傳送圖片，無需上傳。

**Q: 圖片和文件的處理有什麼不同？**
A:
- **文件**：會上傳到 File Search Store，可以後續查詢，適合需要反覆查詢的資料
- **圖片**：即時分析後立即清除，適合快速了解圖片內容

**Q: 群組聊天中，其他人上傳的檔案我也能查詢嗎？**
A: 可以！群組中所有成員共享同一個文件庫（僅限文件檔案）。

**Q: 檔案會保存多久？**
A: 文件檔案會持續保存在 Google Gemini 的 File Search Store，圖片分析後會立即清除。

**Q: 支援哪些語言？**
A: Google Gemini 支援多種語言，包括繁體中文、簡體中文、英文、日文等。

**Q: 可以處理多大的檔案？**
A: 取決於 Google Gemini File API 的限制，一般文件都沒問題。圖片建議不超過 10MB。

**Q: Quick Reply 按鈕是什麼？**
A: Quick Reply 是上傳檔案成功後出現的快捷按鈕（📝 生成檔案摘要、📌 重點整理、📋 列出檔案）。點擊按鈕會自動發送完整問題，比手動輸入更方便，且會自動帶入檔案名稱避免混淆。

**Q: 為什麼列出檔案時不是顯示清單或卡片？**
A: 我們使用 Google ADK Agent 讓 AI 用自然對話方式介紹檔案，而非傳統的條列式清單或卡片。這樣的呈現更友善、更像真人對話，使用者體驗更好。AI 會根據檔案數量智能調整說明方式。

**Q: 如何自訂 Quick Reply 按鈕的文字？**
A: 在 `main.py` 的 `handle_document_message()` 函數中可以修改 Quick Reply 的設定。你可以調整按鈕的 `label`（顯示文字）和 `text`（發送內容）。

## 🔧 進階設定

### 修改 AI 模型

在 `main.py` 第 51 行可以修改使用的模型：

```python
MODEL_NAME = "gemini-2.5-flash"  # 可改成其他 Gemini 模型
```

### 調整文件查詢的回應溫度

在 `main.py` 約第 220 行可以調整 AI 的創意程度：

```python
temperature=0.7,  # 0.0 = 保守精確, 1.0 = 創意發散
```

### 自訂圖片分析的提示詞

在 `main.py` 約第 270 行可以修改圖片分析的提示：

```python
contents=["請詳細描述這張圖片的內容，包括主要物品、場景、文字等資訊。", image],
```

可以改成：
- `"請用英文描述這張圖片"` - 英文回應
- `"這張圖片中有哪些文字？"` - 專注於 OCR
- `"這張圖片的主題是什麼？"` - 摘要式回應

### 自訂 Quick Reply 按鈕

在 `main.py` 的檔案上傳成功處理部分（約第 447-452 行）：

```python
quick_reply = QuickReply(items=[
    QuickReplyButton(action=MessageAction(
        label="📝 生成檔案摘要",
        text=f"請幫我生成「{file_name}」這個檔案的摘要"
    )),
    QuickReplyButton(action=MessageAction(
        label="📌 重點整理",
        text=f"請幫我整理「{file_name}」的重點"
    )),
    QuickReplyButton(action=MessageAction(
        label="📋 列出檔案",
        text="列出檔案"
    )),
])
```

你可以：
- 修改 `label` 來改變按鈕顯示文字
- 修改 `text` 來改變點擊後發送的內容
- 新增或移除按鈕（LINE 限制最多 13 個）
- 使用 `{file_name}` 變數來自動帶入檔案名稱

### 自訂 FileManagerAgent 的語氣和風格

在 `file_manager_agent/agent.py` 中修改 agent instruction（約第 24-33 行）：

```python
instruction="""你是一個友善的檔案管理助手。

當使用者要求列出檔案時：
1. 使用 list_files tool 來取得檔案清單
2. 用口語化、友善的方式呈現結果
3. 不要使用條列式或表格，用自然的對話方式說明
4. 例如：「我看到你上傳了 3 個檔案唷！首先是『會議記錄.pdf』...」
5. 語氣要輕鬆、親切

回應時請用繁體中文。"""
```

你可以調整：
- **語氣風格**：從「親切」改為「專業」、「幽默」等
- **語言**：改為英文或其他語言
- **呈現方式**：要求 AI 用特定格式（如分類、排序等）
- **細節程度**：決定要說明到多詳細

## 📝 授權條款

MIT License - 歡迎自由使用、修改、分享！

## 🙌 貢獻

歡迎提交 Issue 或 Pull Request！

## 📚 相關連結

- [Google Gemini File Search 官方文件](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-tw)
- [Google ADK (Agent Development Kit) 文件](https://ai.google.dev/gemini-api/docs/adk)
- [LINE Messaging API 文件](https://developers.line.biz/en/docs/messaging-api/)
- [LINE Messaging API - Quick Reply](https://developers.line.biz/en/docs/messaging-api/using-quick-reply/)
- [FastAPI 文件](https://fastapi.tiangolo.com/)

---

⭐ 如果這個專案對你有幫助，請給個 Star 支持一下！
