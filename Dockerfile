# Extend the official Rasa SDK image
FROM rasa/rasa:2.4.3-full
USER root

SHELL ["/bin/bash", "-c"]

WORKDIR /app

#EXPOSE 5055

#ENTRYPOINT ["./entrypoint.sh"]

#CMD ["start", "--actions", "actions.actions"]

USER 1001