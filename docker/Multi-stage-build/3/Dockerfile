ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim
RUN adduser --system --no-create-home appuser
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY app.py /app
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD [ "python","app.py" ]