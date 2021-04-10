# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:2.4.1

USER root

SHELL ["/bin/bash", "-c"]

RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  build-essential && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN python -m nltk.downloader stopwords

RUN python -m spacy download en_core_web_sm

COPY . .

VOLUME ["/app/actions","/app/similarity"]

EXPOSE 5055

#ENTRYPOINT ["./entrypoint.sh"]

#CMD ["start", "--actions", "actions.actions"]

USER 1001