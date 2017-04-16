> Disclaimer: This project is intended to study the Scrapy Spider Framework and the MongoDB database, it cannot be used for commercial or other personal intentions. If used improperly, it will be the individuals bear.

* The project is mainly used for crawling PornHub, the largest adult site in the world. In doing so it retrieves video titles, duration, mp4 link, cover url and direct PornHub url.
* This project crawls PornHub.com quickly, but with a simple structure.
* This project can crawl up to 5 millon PornHub videos per day, depending on your personal network. Because of my slow bandwith my results are relatively slow.
* The crawler requests 10 threads at a time, and because of this can achieve the speed mentioned above. If your network is more performant you can request more threads and crawl a larger amount of videos per day. For the specific configuration see [pre-boot configuration]


## Environment, Architecture

Language: Python2.7

Environment: MacOS, 4G RAM

Database: MongoDB

* Mainly uses the scrapy reptile framework.
* Join to the Spider randomly by extracted from the Cookie pool and UA pool.
* Start_requests start five Request based on PornHub classification, and crawl the five categories at the same time.
* Support paging crawl data, and join to the queue.

## Instructions for use

### Pre-boot configuration

* Install MongoDB and start without configuration
* Install Scrapy
* Install Python dependent modules：pymongo, json, requests
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
    video_duration:  The length of the video, in seconds
    quality_480p:    Video 480p mp4 download address

## For Chinese

* QQ Group: 584296293

<img src="https://github.com/xiyouMc/PornHubBot/blob/master/img/WebHubCode2.png?raw=true" width = "700" height = "400" alt="图片名称" align=center />   
