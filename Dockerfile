FROM quay.io/astronomer/astro-runtime:12.6.0
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
CMD astro dev start
