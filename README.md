# pTIPS-ContextCamera
A zoom tool for live-streaming a play session


### To Run with Zoom:

*NOTE:* This will not work on a local machine (IP firewalls are too weird). Run the docker setup in Digital Ocean or some kind of public VPS

Prestep for DigitalOcean:
  * apt update
  * apt install -y docker.io docker-compose git
  
* Move the local files to the DO droplet `scp -r /Users/jspann/Documents/research/bai_lab/ptips_zoom_contextcamera/full_rtmp_zoom root@159.203.189.56:~` (replace the IP with your DO droplet's IP)
* ssh into Digital Ocean
* `cd full_rtmp_zoom`
* `docker-compose up --build`
* Run "zoom_builder.py" locally
* Open the Host URL that comes up in the terminal output
* When the zoom meeting opens, click "More">"Livestream">"Live on custom livestream service"
* If asked, enter the streaming info
  * **Streaming URL:** `rtmp://192.168.50.91:1935/live` (replace the IP with your DO droplet's IP)
  * **Session Key:** `stream`
  * "Live streaming page URL": Whatever you want



### To test with OBS:
* Install OBS locally
* "Settings" -> "Stream"
* Give Zoom your credentials
* **Streaming URL:** `rtmp://192.168.50.91:1935/live` (replace the IP with your local device IP)
* **Session Key:** `stream`



### Tips:
Use `curl ifconfig.me` to get the public IP on DigitalOcean or your local device
