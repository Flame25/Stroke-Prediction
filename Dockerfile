FROM tensorflow/serving:latest

COPY ./outputs/serving_model /models/stroke-detection-model

ENV MODEL_NAME=stroke-detection-model
ENV MONITORING_CONFIG="/model_config/prometheus.config"
ENV PORT=8501

RUN echo '#!/bin/bash \n\n\
    env\n\
    tensorflow_model_server --port=8500 --rest_api_port=${PORT} \
    --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} \
    "$@"' > /usr/bin/tf_serving_entrypoint.sh \
    && chmod +x /usr/bin/tf_serving_entrypoint.sh