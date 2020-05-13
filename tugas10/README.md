# Tugas 10
## Performance Test

Pada port 44444
| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 10 | 2.566 seconds | 1000 | 0 | 122000 bytes | 389.71 [#/sec] | 2.566 ms | 46.43 Kbytes/sec |
| 2 | 25 | 2.402 seconds | 1000 | 0 | 122000 bytes | 416.30 [#/sec] | 2.402 ms | 49.60 Kbytes/sec |
| 3 | 100 | 2.460 seconds | 1000 | 0 | 122000 bytes | 406.54 [#/sec] | 2.460 ms | 48.44 Kbytes/sec |
| 4 | 500 | 1.184 seconds | 1000 | 0 | 122000 bytes | 844.54 [#/sec] | 1.184 ms | 36.02 Kbytes/sec |
| 5 | 1000 | 0.902 seconds | 1000 | 0 | 122000 bytes | 1108.35 [#/sec] | 0.902 ms | 29.05 Kbytes/sec |

server_async_http.py pada port 45000
| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 10 | 8.085 seconds | 1000 | 0 | 122000 bytes | 123.68 [#/sec] | 8.085 ms | 14.74 Kbytes/sec |
| 2 | 25 | 7.555 seconds | 1000 | 0 | 122000 bytes | 132.37 [#/sec] | 7.555 ms | 15.77 Kbytes/sec |
| 3 | 100 | 2.440 seconds | 1000 | 0 | 122000 bytes | 243.998 [#/sec] | 2.440 ms | 48.83 Kbytes/sec |
| 4 | 500 | 0.731 seconds | 1000 | 0 | 122000 bytes | 1367.69 [#/sec] | 0.731 ms | 39.60 Kbytes/sec |
| 5 | 1000 | 1.193 seconds | 1000 | 0 | 122000 bytes | 838.52 [#/sec] | 1.193 ms | 38.76 Kbytes/sec |

server_thread_http.py pada port 46000
| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 10 | 1234.235 seconds | 1000 | 0 | 122000 bytes | 0.80 [#/sec] | 1242.235 ms | 0.10 Kbytes/sec |
| 2 | 25 | 918.018 seconds | 1000 | 0 | 122000 bytes | 1.09 [#/sec] | 918.018 ms | 0.13 Kbytes/sec |
| 3 | 100 | 1417.823 seconds | 1000 | 0 | 122000 bytes | 0.71 [#/sec] | 1417.823 ms | 0.08 Kbytes/sec |
| 4 | 500 | 26.511 seconds | 1000 | 0 | 122000 bytes | 37.72 [#/sec] | 26.511 ms | 1.36 Kbytes/sec |
| 5 | 1000 | 41.443 seconds | 1000 | 0 | 122000 bytes | 24.13 [#/sec] | 41.443 ms | 0.38 Kbytes/sec |