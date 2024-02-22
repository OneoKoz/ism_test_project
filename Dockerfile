FROM python:3.11-slim

ENV GRADIO_SERVER_PATH 0.0.0.0
ENV GRADIO_SERVER_PORT=7860

COPY . .
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]