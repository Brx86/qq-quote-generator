FROM python:3.11.8-slim-bullseye
EXPOSE 5000
WORKDIR /root
COPY app.py ascreenshot.py requirements.txt /root/
COPY templates /root/templates
RUN pip install -r /root/requirements.txt \
    && playwright install firefox \
    && playwright install-deps \
    && apt-get install wget -y \
    && wget -q -O- https://github.com/Brx86/yun/releases/download/2/noto_fonts.tar.gz|tar zxvf - -C /usr/share/fonts/ \
    && rm -rf /root/.cache/pip /var/lib/apt
CMD uvicorn app:app --host=0.0.0.0 --port=5000
