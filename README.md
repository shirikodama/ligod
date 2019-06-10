# Ligod
Ligod -- a very simple LIGO event listener and Django front end

## Introduction

LIGO, the way too cool gravity wave detector, created an API for sending out alerts when an event is detected. I'm guessing its main intent is for astromomers to point their telescopes at the events, but I was curious and bored... and voila.

The point of this project isn't to do anything interesting with the events themselves, but instead to do the grunt work of capturing the events, storing them in a database, and providing an ugly CRUD interface that can be fleshed out and beautified as needed. That is, I hope this can be a means to somebody else's ends.

## Installation

We assume you already have a working version of python and the Django library components necessary. In addition, you'll heed a couple of other packages:

```bash
pip install pygcn healpy
```

## Ligod Listener Setup

There are two separate components: the LIGO listener (ligod), and the Django front end. Ligod listens for the events as they happen and stores them in a simple sqlite3 database. There are a few parameters that are broken out, but mainly it's the XML from the event itself that is stored. There is no attempt to correlate the Gracedb_id's, but that could easily be done. The core of the code is the example code from the [LIGO API folks](https://emfollow.docs.ligo.org/userguide/tutorial/index.html).

Ligod can be called as a standalone daemon. I just put it into rc.local on my Ubuntu box, but you can fire it up any way you like. 

/home/mike/ligod/ligod -d '/home/mike/ligod/ligo.sq3'

LIGO sends out both real and test events. The test events are sent out about once an hour. By default, only the real events are stored. In addition, there is a test mode (-t) which uses a local test event so that you can more quickly iterate if you're debugging. Lastly, I added a mail-to feature if you'd like to be alerted in real time.