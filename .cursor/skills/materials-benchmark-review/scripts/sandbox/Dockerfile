FROM python:3.11-slim

ENV VIRTUAL_ENV=/opt/qa-checker-venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m venv "${VIRTUAL_ENV}" \
    && pip install --no-cache-dir uv \
    && uv pip install --python "${VIRTUAL_ENV}/bin/python" --no-cache \
        pip \
        numpy \
        scipy \
        pandas \
        scikit-learn \
        scikit-image \
        matplotlib \
        ase \
        pymatgen \
        spglib \
        phonopy \
        seekpath \
        h5py \
        netCDF4 \
        networkx \
        sympy \
        pint \
        uncertainties \
        lmfit

RUN mkdir -p /root/.cache/uv /workspace /solution /app/outputs /logs/verifier

WORKDIR /workspace

CMD ["python", "--version"]
