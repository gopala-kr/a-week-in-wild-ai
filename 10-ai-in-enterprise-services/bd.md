



----

![4th](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/10-ai-in-enterprise-services/imgs/4th.PNG)

-------

![3765_02_06](https://www.packtpub.com/graphics/9781784396688/graphics/3765_02_06.jpg)



-----------

![hadoop-ecosystem](https://mydataexperiments.files.wordpress.com/2017/04/hadoop-ecosystem.png)

-------



![data-lake-architecture](https://www.searchtechnologies.com/images/blog-graphics/data-lake-architecture.jpg)

---------

![60_s](https://sonra.io/wp-content/uploads/2017/06/graphic_0619_2-1024x585.png)

-----------




- [Big data architecture: Hadoop and Data Lake- 1](https://www.slideshare.net/welkaim/big-data-architecture-hadoop-and-data-lake-part-1)
- [Data lake: a new ideology in big data era ](https://www.itm-conferences.org/articles/itmconf/pdf/2018/02/itmconf_wcsn2018_03025.pdf)
- [A Data Lake Architecture with Hadoop and Open Source Search Engines](https://www.searchtechnologies.com/blog/search-data-lake-with-big-data)
- [Big data architecture: BI and Analytics (Part 2)](https://www.slideshare.net/welkaim/big-data-architecture-bi-and-analytics-part-2)
- [Big data architecture: Technologies (Part 3)](https://www.slideshare.net/welkaim/big-data-architecture-technologies-part-3)


---------


<table id="custom-table-sonra-style">
<tbody>
<tr>
<th></th>
<th>Open Source</th>
<th>Amazon AWS</th>
<th>Microsoft Azure</th>
<th>Google Cloud</th>
</tr>
<tr>
<th>Batch Ingest</th>
<td>Sqoop<br />
File Transfer<br />
Flume<br />
StreamSets</td>
<td>AWS Data Transfer Services (various options)</td>
<td>Import/Export Service<br />
Data Factory</td>
<td>Cloud DataFlow</td>
</tr>
<tr>
<th>Streaming Ingest</th>
<td>Flume<br />
StreamSets</td>
<td>Amazon Kinesis Firehose</td>
<td>Event Hubs<br />
IOT Hub</td>
<td>Cloud DataFlow</td>
</tr>
<tr>
<th>Persistent Storage</th>
<td>HDFS<br />
RDBMS</td>
<td>S3, Glacier<br />
RDS</td>
<td>Storage Blob<br />
HDFS<br />
SQL Database</td>
<td>Persistent Disk<br />
Google Cloud Storage<br />
Cloud SQL</td>
</tr>
<tr>
<th>Transient Storage</th>
<td>Kafka</td>
<td>Kinesis</td>
<td>Event Hubs<br />
IOT Hub<br />
HDInsight (Kafka)</td>
<td>Cloud Pub/Sub<br />
Cloud IoT Core</td>
</tr>
<tr>
<th>Batch Processing</th>
<td>Hive<br />
Flink, Spark<br />
MapReduce<br />
PostgreSQL</td>
<td>EMR Spark<br />
EMR Hadoop<br />
EMR Presto<br />
AWS Batch<br />
Redshift</td>
<td>Azure Batch<br />
HDInisght (Spark/Map Reduce)<br />
SQL Data Warehouse<br />
Data Lake Analytics<br />
Azure Functions</td>
<td>Cloud Dataflow (open source Apache Beam)<br />
Cloud DataProc (Spark, Hadoop)</td>
</tr>
<tr>
<th>Stream Processing</th>
<td>Flink<br />
Spark<br />
Beam</td>
<td>Amazon Kinesis Streams<br />
Amazon Kinesis Analytics<br />
EMR Spark</td>
<td>Stream Analytics<br />
HDInsight (Storm, Spark)</td>
<td>Cloud Dataflow (open source Apache Beam)<br />
DataProc (Spark, Hadoop)</td>
</tr>
<tr>
<th>Machine Learning</th>
<td>Scikit<br />
Tensorflow<br />
Spark MLLib<br />
TensorFlow etc.<br />
Huge number of libraries</td>
<td>Lex<br />
Polly<br />
Recognition<br />
Amazon Machine Learning</td>
<td>Azure ML<br />
Cognitive Services</td>
<td>Natural Language<br />
SpeechTranslation<br />
Vision<br />
Video<br />
ML Engine</td>
</tr>
<tr>
<th>Serving Storage Graph</th>
<td>JanusGraph</td>
<td>Neptune</td>
<td>CosmosDB</td>
<td>N/A</td>
</tr>
<tr>
<th>Serving Storage BI/EDW</th>
<td>Impala + Kudu</td>
<td>Redshift<br />
Athena</td>
<td>SQL Data Warehouse<br />
Analysis Services (OLAP Cubes)</td>
<td>BigQuery</td>
</tr>
<tr>
<th>Serving Storage Search (keywords + facets)</th>
<td>Solr</td>
<td>Amazon CloudSearch<br />
Amazon Elasticsearch</td>
<td>Azure Search</td>
<td>N/A Marketplace, e.g. Solr</td>
</tr>
<tr>
<th>Serving Storage RDBMS</th>
<td>PostgreSQL</td>
<td>RDS</td>
<td>SQL DB</td>
<td>Cloud SQL</td>
</tr>
<tr>
<th>Serving Storage NoSQL</th>
<td>HBase</td>
<td>DynamoDB</td>
<td>HDInsight (HBase)<br />
CosmosDB</td>
<td>BigTable<br />
Spanner<br />
DataStore</td>
</tr>
<tr>
<th>Sandboxes Notebook</th>
<td>Zeppelin</td>
<td>EMR Zeppelin</td>
<td>Azure Notebooks</td>
<td>Cloud Datalab</td>
</tr>
<tr>
<th>Sandboxes Data Science or Preparation Platform</th>
<td>Dataiku DSS Community Edition (not open source)</td>
<td>N/A Marketplace only, e.g. Dataiku DSS</td>
<td>N/A Marketplace only, e.g. Dataiku DSS</td>
<td>Cloud DataPrep (beta). Under the hood this is Trifacta.</td>
</tr>
<tr>
<th>Clients/Data Apps</th>
<td>Superset (BI)</td>
<td>Quicksight</td>
<td>PowerBI</td>
<td>Google Data Studio</td>
</tr>
<tr>
<th>Orchestration</th>
<td>Airflow</td>
<td>AWS Data Pipeline</td>
<td>Data Factory</td>
<td>N/A Marketplace</td>
</tr>
<tr>
<th>ETL Tool</th>
<td>N/A</td>
<td>AWS Glue</td>
<td>Data Factory</td>
<td>N/A Marketplace</td>
</tr>
<tr>
<th>MDM Hub</th>
<td>N/A</td>
<td>N/A Marketplace</td>
<td>N/A Marketplace</td>
<td>N/A Marketplace</td>
</tr>
<tr>
<th>Lineage</th>
<td>N/A</td>
<td>AWS Glue</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<th>Catalog</th>
<td>N/A</td>
<td>AWS Glue</td>
<td>Data Catalog</td>
<td>N/A Marketplace</td>
</tr>
</tbody>
</table>

-----
