FROM python:3.10

RUN useradd -m bot
USER bot

WORKDIR /home/bot/app

COPY --chown=bot:bot requirements.txt .

RUN pip install -r requirements.txt

ENV PATH="/home/bot/.local/bin:${PATH}"

COPY --chown=bot:bot . .

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "src.wsgi:application" ]


