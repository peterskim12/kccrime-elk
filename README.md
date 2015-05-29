# kccrime-elk
This repo contains scripts and configs to help you get Kansas City crime data into Elasticsearch using Logstash.

* scripts/process.py: A Python script to convert the XML download of the crime data from the Open Data KC site to a more sensible JSON format.
* logstash.conf: The Logstash config file which helps parse and clean up the crime data
* index_template.json: An Elasticsearch index template for the crime data set. The Logstash config references this template in its elasticsearch output.

You will need to download the raw KC crime data files in XML format from the Open Data KC website: [https://data.kcmo.org/](https://data.kcmo.org/). You can find the crime data by searching for: crime <year> where year is the year of the crime data set you want. e.g. for the 2014 crime data set, search for: crime 2014.

The Open Data KC website seems to have crime data from 2009 to 2015.

You can learn more about the Elastic products here:

[https://www.elastic.co/products](https://www.elastic.co/products)

For technical documentation for Elasticsearch, Logstash, Kibana and others, go here:

[https://www.elastic.co/guide/index.html](https://www.elastic.co/guide/index.html)

Interact with the community of users on our forums:

[https://discuss.elastic.co/](https://discuss.elastic.co/)
