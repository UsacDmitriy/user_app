FROM python:3.9 AS base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin


RUN PIP_USER=1 pip install --upgrade pip
RUN PIP_USER=1 pip install pipenv
COPY Pipfile* ./
RUN PIP_USER=1 pipenv install --system --deploy --ignore-pipfile

FROM python:3.9

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN groupadd myapp && useradd -G myapp user -u 1234
COPY --chown=user:myapp --from=base ${PYROOT}/ ${PYROOT}/


RUN mkdir -p /usr/scr/app
WORKDIR /usr/src/

COPY --chown=user:myapp app ./app
USER user

CMD ["groups"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]


