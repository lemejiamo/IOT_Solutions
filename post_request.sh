#!/usr/bin/bash

curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":2.75, "date":"2021-08-12 22:22:22"}'
