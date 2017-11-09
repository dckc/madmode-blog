# Making Secure IoT: seL4 on my Raspberry Pi 3B

I got seL4 running on my Raspberry Pi 3B tonight.

Even though I've worked with Dale Dougherty since the early '90s,
I've been on the sidelines of the whole maker thing until September when
Micro Center bundled a [Google AIY VOICE KIT with Raspberry Pi 3B for $35][AIY].

[AIY]: http://www.microcenter.com/site/content/google_aiy_preorder.aspx

<a data-flickr-embed="true" data-footer="true"
 href="https://www.flickr.com/photos/dckc/26502865629/in/album-72157690394355946/"
 title="AIY Kit"><img src="https://farm5.staticflickr.com/4517/26502865629_a8f62d67b5.jpg"
  width="500" height="305" alt="AIY Kit"></a>
  <script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

After I verified that it works as a voice device, I remembered the tantalizing
[seL4 on the Raspberry Pi 3][SR] item from early this year. The build dependencies
were greatly simplified by the [seL4 dockerfiles][DF]. Building the seL4-Test project
went without a hitch:

    mkdir sel4test && cd sel4test
    repo init --config-name -u git@github.com:seL4/sel4test-manifest.git
    repo sync
    make rpi3_debug_xml_defconfig && make
    ...
    [GEN_IMAGE] sel4test-driver-image-arm-bcm2837

[SR]: https://research.csiro.au/tsblog/sel4-raspberry-pi-3/
[DF]: https://github.com/SEL4PROJ/seL4-CAmkES-L4v-dockerfiles

The only way to see the seL4 test project do its thing is via the serial console.
Before I overwrote the working voice kit SD card, I wanted to test connectivity.
I have plenty of experience with RS-232 serial cables (I even had a job in high
school where I helped a tech by putting together serial terminal cables)
but [RS-232 vs. TTL serial](https://www.sparkfun.com/tutorials/215) is not just
a matter of wires and connectors; the voltage levels are different. USB to TTL cables
usually go for around $15, which is more than half of what I paid for the Pi!

Meanwhile, this summer Micro Center had a beaglebone green wireless, which
usually goes for around $50, on clearance for $20, and I couldn't pass it up.
The beaglebone uses the same TTL levels and works fine as an ssh server,
so I put together a cable

<a data-flickr-embed="true" data-footer="true"  href="https://www.flickr.com/photos/dckc/38223910826/in/album-72157690394355946/" title="IMG_20171106_212900488"><img src="https://farm5.staticflickr.com/4569/38223910826_a8fe8f7bdf.jpg" width="500" height="281" alt="IMG_20171106_212900488"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

After some `config-pin` tinkering, I confirmed that I could get
UART1 and UART2 on the beaglebone to talk to each other (UART0
is debug outputonly), but I couldn't get any console output from the Pi to show up.

After discovering a [JBtek Raspberry Pi USB to TTL Serial Cable](https://www.amazon.com/gp/product/B00QT7LQ88/)
on Amazon for $7, I ordered it and set the project aside.

That didn't work either until I connected an HDMI monitor and keyboard and
used `raspi-config` to enable the serial console. _I wonder if the beaglebone
would have worked given that fix._

With serial console hardware issues in hand, I loaded the SD card as instructed.
The first few boot stages worked, but I struggled to `Hit any key to stop autoboot`.
Minicom (remember minicom?) showed "Offline" so I turned off hardware flow control.
Bingo:

    U-Boot> fatls mmc 0
        50248   bootcode.bin
      2818372   start.elf
           35   config.txt
       393408   u-boot.bin
      4064956   sel4test-driver-image-arm-bcm2837
    U-Boot> fatload mmc 0 0x100000 sel4test-driver-image-arm-bcm2837
    reading sel4test-driver-image-arm-bcm2837
    4064956 bytes read in 328 ms (11.8 MiB/s)
    U-Boot> bootelf 0x100000
    ...
    Test suite passed. 119 tests passed. 42 tests disabled.
    All is well in the universe

