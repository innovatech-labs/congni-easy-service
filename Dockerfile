FROM public.ecr.aws/lambda/python:3.8

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY "${OPENAI_API_KEY}"

COPY . .
RUN pip install -r ./requirements.txt
CMD ["main.handler"]