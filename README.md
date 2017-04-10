> Disclaimer: This project is intended to study the Scrapy Spider Framework and the MongoDB database, can not be used for commercial and personal other intentions. If used improperly, by the individual bear.

* The project is mainly crawling the world's largest adult site PornHub，contains video title、 duration、 mp4 link、 cover url and specific PornHub link.
* Project crawling PornHub.com, simple structure, fastly.
* Crawling PornHub video speed can reach 5 million / day or more. Specifically depending on the personal network, because I was a home network, so relatively slow.
* 10 threads at the same time request, can achieve the above speed. If the personal network environment is better, you can start more threads to request, the specific configuration see [pre-boot configuration].


## Environment, Architecture

Language: Python2.7

Environment: MacOS、4G RAM

Database: MongoDB

* Mainly use the scrapy reptile framework
* Extract a join to the Spider randomly from the Cookie pool and UA pool
* Start_requests based on PorbHub classification, started five Request, while the five categories to crawl.
* And support paging crawl data, and join the queue to be queued.

## Instructions for use

### Pre-boot configuration

* Install MongoDB and start without configuration
* Install Scrapy
* Install Python dependent modules：pymongo、json、requests
* According to their own need to modify the Scrapy on the interval time, start Requests the number of threads and so on the configuration

### Start up

* python PornHub/quickstart.py

## Run screenshots
![](https://github.com/xiyouMc/PornHubBot/blob/master/img/running.png?raw=true)
![](https://github.com/xiyouMc/PornHubBot/blob/master/img/mongodb.png?raw=true)

## Database description

The table in the database that holds the data is PhRes. The following is a field description:

#### PhRes table：
	
	video_title:     The title of the video, and as a unique.
	link_url:        Video jump to PornHub`s link
	image_url:       Video cover link
	video_duration:  The length of the video, in s
	quality_480p:    Video 480p mp4 download address
