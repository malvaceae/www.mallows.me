FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir --upgrade \
    beautifulsoup4 \
    cssmin \
    jsmin \
    markdown \
    pelican \
    pelican-minify \
    pip \
    setuptools \
    typogrify \
    webassets \
    ;

CMD ["pelican", "-lr"]
