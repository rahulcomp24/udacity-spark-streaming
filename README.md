1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
It changes `processedRowsPerSecond`,`numInputRows`.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

- `maxOffsetsPerTrigger` increasing this improved the `processedRowsPerSecond`
- `spark.executor.memory` increasing this also improved the `processedRowsPerSecond` because we had large watermark window so we more memory helped a lot.

## Screenshots
### Kafka Consumer
![Kafka Consumer](img/2021-06-06-05-31-02.png)
### Stream Spark DF
![Stream Table](img/2021-06-06-05-28-52.png)
### Stream Progress
![Stream Progress](img/2021-06-06-05-29-33.png)
### Spark UI
![Spark UI](img/2021-06-06-05-27-30.png)