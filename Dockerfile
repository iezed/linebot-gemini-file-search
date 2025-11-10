FROM python:3.10.17

# 設定工作目錄
WORKDIR /app

# 先複製 requirements.txt 並安裝依賴（利用 Docker cache）
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 再複製專案檔案
COPY . /app

EXPOSE 8080
CMD uvicorn main:app --host=0.0.0.0 --port=$PORT