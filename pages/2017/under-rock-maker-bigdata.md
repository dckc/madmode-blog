I'm coming out from under a rock with a beaglebone and spark.

Even though I've worked with Dale Dougherty since the early '90s, I've been on the sidelines of the whole maker thing.
Corbin / Monte talked about putting beaglebones all around his house. At $60, I stayed on the sideline, but
when microcenter had it on clearance for $20, I couldn't pass up.

#swig - amazing: plug it in and voiala, web server with cloud9 IDE
earlier episode:
http://dm93.org/2005/0501pchw/index.html

project ideas:
  - Amazon Echo (or google thingy? "tell me about my day" bedside thingy)
  - car computer?

Hadoop is a decade old already!
Our upstream provider switched from Oracle to Microsoft Sql Server without notice. The up-side: a good use to try out spark.
Moved ~150GB in ~1day, and I think that was without parallelism. "Failure is normal" quote vs. Oracle all-or-nothing
transactional rollback.
Ugh! spark security!

looked into tftp boot today. found the image I built earlier:

```
Jul 29 22:19:38 <DanC>	hm. they provide a docker build environment. that's attractive from a "what happens in docker stays in docker" perspective
Jul 29 22:21:36 <DanC>	especially since last time I played with seL4, I ended up in a twisty maze of haskell dependencies
Jul 29 22:26:57 <DanC>	hm. AM335x doesn't occur on https://qemu.weilnetz.de/doc/qemu-doc.html#ARM-System-emulator
Jul 29 22:35:34 <DanC>	Hello, welcome to the sel4/CAmkES/L4v docker build environment
Jul 29 22:35:34 <DanC>	connolly@in-container:/host$ 
Jul 29 22:46:21 <DanC>	[elfloader] done.
Jul 29 22:46:21 <DanC>	[GEN_IMAGE] sel4test-driver-image-arm-am335x
```

But

  - [setting up tftp boot](http://www.embeddedhobbyist.com/2013/06/beaglebone-black-network-boot/) involves editing `uEnv.txt` and it's not obvious how to recover if it doesn't work
  - [seL4 on the BeagleBone](https://wiki.sel4.systems/Hardware/Beaglebone) requires a serial cable, which I don't have - at $9.95, it's half the price of the computer itself!
