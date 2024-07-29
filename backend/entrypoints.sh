#!/bin/sh

echo "Waiting for MongoDBs to start..."
./wait-for $HOST_DB1:$PORT_DB1
echo "DB1 started"
./wait-for $HOST_DB2:$PORT_DB2
echo "DB2 started"

echo "Starting services"
uvicorn main:app --host 0.0.0.0 --port 3000