> Disclaimer: This project is intended to study the Scrapy Spider Framework and the MongoDB database, can not be used for commercial or other personal intentions. If used improperly, it will be the individual bear.

* The project is mainly crawling the largest adult site int the world -- PornHub，contains video title、 duration、 mp4 link、 cover url and specific PornHub link.
* Project crawling PornHub.com with simple structure and fastly.
* Crawling PornHub video speed can reach 5 million / day or more. Specifically depending on the personal network, because I was a home network, so relatively slow.
* Request 10 threads at the same time can achieve the speed above. If the personal network environment is better, you can start more threads to request, the specific configuration see [pre-boot configuration].


## Environment, Architecture

Language: Python2.7

Environment: MacOS、4G RAM

Database: MongoDB

* Mainly use the scrapy reptile framework.
* Join to the Spider randomly by extracted from the Cookie pool and UA pool.
* Start_requests start five Request based on PorbHub classification, and crawl the five categories at the same time.
* Support paging crawl data, and join to the queue.

## Instructions for use

### Pre-boot configuration

* Install MongoDB and start without configuration
* Install Scrapy
* Install Python dependent modules：pymongo、json、requests
* Modify the configuration by needed, such as the interval time, the number of threads, etc.

### Start up

* cd PornHub
* python quickstart.py


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


## For Chinese

* QQGroup: 584296293

<img src="https://github.com/xiyouMc/PornHubBot/blob/master/img/WebHubCode.png?raw=true" width = "800" height = "400" alt="图片名称" align=center />


   