# Streaming On PiCamera

## Code for recording for few seconds

For this, you just must have a Rasberry Pi 3 and a Pi Camera (For me it's "noIR Camera V2")

The code is in the "camera.py" file 

PS : This code not filming, it's just to see in the camera in a few time 

If you want, you can change the time recording in the code (It's in seconds)

## Streaming remote

For streaming remote, you must have vlc on your raspberry and the device where you want to watch the streaming

So install vlc with 

```console
sudo apt-get install vlc
```

You must be connected to a network too (a LAN -> https://en.wikipedia.org/wiki/LAN_(disambiguation) )

Then test if you have raspivid ( https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md )

Finnaly, use:

```console
raspivid -o - -t 0 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264 --rtsp-host=<your-ip-address>
```

To get your IP address you can use:
```console
ifconfig
```
It depends on your network interface: ETH0 or WLAN0.

Then connect your other device with vlc and it should work 

:)

