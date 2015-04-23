> This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
> Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
> Licensed to The Apache Software Foundation, http://www.apache.org/
> Benchmarking localhost (be patient).....done

Index or main Page (n 5 c 5 )
=====================================================


|      Variables          |     Value       |
|-------------------------|-----------------|
| Server Software:        | Werkzeug/0.10.4 |
| Server Hostname:        | localhost |
| Server Port:            | 5000 |
| Document Path:          | / |
| Document Length:        | 2030287 bytes |
| Concurrency Level:      | 5 |
| Time taken for tests:   | 0.749 seconds |
| Complete requests:      | 5 |
| Failed requests:        | 0 |
| Total transferred:      | 10152230 bytes |
| HTML transferred:       | 10151435 bytes |
| Requests per second:    | 6.68 [#/sec] (mean) |
| Time per request:       | 748.819 [ms] (mean) |
| Time per request:       | 149.764 [ms] (mean, across all concurrent requests) |
| Transfer rate:          | 13239.90 [Kbytes/sec] received |

### Connection Times (ms)
   Param.   | min |mean[+/-sd]|median | max
   ---------| ----|-----------|-------| ---
Connect:    |   0 |  0   0.1  |   0   |   0
Processing: | 161 |451 231.1  | 519   | 748
Waiting:    | 159 |449 231.1  | 518   | 747
Total:      | 161 |451 231.0  | 520   | 748

### Percentage of the requests served within a certain time (ms)
  %     | req. |
  ----- | ---- |
  50%   |449|
  66%   |590|
  75%   |590|
  80%   |748|
  90%   |748|
  95%   |748|
  98%   |748|
  99%   |748|
 100%   |748| (longest request)


Index or main Page (n 1000 c 1000)
=====================================================


|      Variables          |     Value       |
|-------------------------|-----------------|
| Server Software:        | Werkzeug/0.10.4 |
| Server Hostname:        | localhost |
| Server Port:            | 5000 |
| Document Path:          | / |
| Document Length:        | 2030287 bytes |
| Concurrency Level:      | 100 |
| Time taken for tests:   | 148.704 seconds |
| Complete requests:      | 1000 |
| Failed requests:        | 0 |
| Total transferred:      | 2030446000 bytes |
| HTML transferred:       | 2030287000 bytes |
| Requests per second:    | 6.72 [#/sec] (mean) |
| Time per request:       | 14870.368 [ms] (mean) |
| Time per request:       | 148.704 [ms] (mean, across all concurrent requests) |
| Transfer rate:          | 13334.29 [Kbytes/sec] received |

### Connection Times (ms)
   Param.   | min |mean[+/-sd]|median | max
   ---------| ----|-----------|-------| ---
Connect:    |   0 |   0   0.5  |   0  |    2
Processing: | 314 |14140 2528.9| 14796|  15550
Waiting:    | 312 |14138 2529.0| 14794|  15548
Total:      | 316 |14140 2528.5| 14796|  15551

### Percentage of the requests served within a certain time (ms)
  %     | req. |
  ----- | ---- |
  50% |14796|
  66% |14827|
  75% |14847|
  80% |14859|
  90% |14933|
  95% |15298|
  98% |15344|
  99% |15372|
 100% |15551| (longest request)

one request to GET 1 post (n 1000 c 100)
=====================================================


|      Variables          |     Value       |
|-------------------------|-----------------|
| Server Software:        | Werkzeug/0.10.4 |
| Server Hostname:        | localhost |
| Server Port:            | 5000 |
| Document Path:          | /iama/1 |
| Document Length:        | 265 bytes |
| Concurrency Level:      | 100 |
| Time taken for tests:   | 2.585 seconds |
| Complete requests:      | 1000 |
| Failed requests:        | 0 |
| Non-2xx responses:      | 1000 |
| Total transferred:      | 476000 bytes |
| HTML transferred:       | 265000 bytes |
| Requests per second:    | 386.80 [#/sec] (mean) |
| Time per request:       | 258.529 [ms] (mean) |
| Time per request:       | 2.585 [ms] (mean, across all concurrent requests) |
| Transfer rate:          | 179.80 [Kbytes/sec] received |

### Connection Times (ms)
   Param.   | min |mean[+/-sd]|median | max
   ---------| ----|-----------|-------| ---
Connect:    |   0 |   0   0.6  |   0  |    7
Processing: |  59 | 247  35.9  | 248  |  300
Waiting:    |  59 | 246  35.9  | 248  |  299
Total:      |  62 | 247  35.5  | 248  |  300

### Percentage of the requests served within a certain time (ms)
  %     | req. |
  ----- | ---- |
  50%   |248|
  66%   |257|
  75%   |262|
  80%   |267|
  90%   |291|
  95%   |294|
  98%   |295|
  99%   |297|
 100%   |300| (longest request)
