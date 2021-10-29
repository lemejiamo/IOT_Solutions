#!/usr/bin/bash


curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":2.75, "user_id":"777", "date":"2021-10-10 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":3.75, "user_id":"777", "date":"2021-10-11 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":4.75, "user_id":"777", "date":"2021-10-12 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":5.75, "user_id":"777", "date":"2021-10-13 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":6.75, "user_id":"777", "date":"2021-10-14 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":7.75, "user_id":"777", "date":"2021-10-15 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":8.75, "user_id":"777", "date":"2021-10-16 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":9.75, "user_id":"777", "date":"2021-10-17 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":10.75, "user_id":"777", "date":"2021-10-18 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":9.75, "user_id":"777", "date":"2021-10-19 22:22:22"}'
curl -X POST 0.0.0.0:3001/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":8.75, "user_id":"777", "date":"2021-10-20 22:22:22"}'
# '{"device_id":1, "measure":2.75, "date":"2021-10-12 22:22:22"}'
# curl -X POST http://34.139.58.104:5000/api/v1/records/temp -H 'Content-Type: application/json' -d '{"device_id":1, "measure":50.75, "date":"2021-10-25 11:52:13"}'
