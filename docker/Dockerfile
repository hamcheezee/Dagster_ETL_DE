FROM python:3.11-slim

# Change working directory
WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app

# Install ODBC dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install dagit dagster-webserver dagster-postgres

# Install DuckDB dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libboost-all-dev

# Clone and build DuckDB
RUN git clone https://github.com/duckdb/duckdb.git
WORKDIR duckdb/build
RUN cmake ..
RUN make
RUN make install

# Install Python bindings for DuckDB
RUN pip install duckdb

# Install pyodbc and other Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY docker/dagster.yaml workspace.yaml .
COPY . .

EXPOSE 3000

# Copy the libodbc.2.dylib library
# COPY /opt/homebrew/opt/unixodbc/lib/libodbc.2.dylib .

CMD ["dagster-webserver", "-h", "workspace.yaml", "-h", "0.0.0.0", "-p", "3000"]
