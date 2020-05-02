title: Pebble beats out Garmin Vivofit for my wrist
published: true
date: 2014-12-19
tags: [mobile, health, javascript, android]
summary: extending the open web platform to my wrist

My wife, big on walking but not usually a gadget freak, got so
addicted to tracking with her Nike+ that when the web site stopped
working, it was a major problem. She asked for a fitbit for her
birthday.

The sleep tracking would be a nice bonus.

She talked about getting me one for my birthday too so that I could
join her fitbit friends leaderboard.

Why not a smartwatch while I'm at it?

I have been tracking the market for years, but the Casio 3090 that I
already have is good enough that it would take something pretty
special to get me to switch:

  1. At about $50, I can afford to replace it every five years or so when I
     break it or lose it.
  2. It's maintenance free. It sets itself from WWV radio every night;
     it's water resistant; and it's solar powered, so it **never needs
     charging**.
  3. It does one thing really well: keeps time. To the small
     part of a second. And date. And weekday. And timezones.

A smartwatch that I have to charge every night loses out to the fitbit
on sleep tracking. That and the price rules out the current crop
(Android Wear, Apple Watch).

A friend recommended the Garmin Vivofit ($75). It interoperates with
the fitbit web site, tells time, and claims a battery life of around a
year.

Another acquaintance loves his Pebble ($100). So do lots of other
reviewers, while some gripe about style and some report its fitness
tracking features don't really cut it.

I ordered them both to see which one I like better. I opened the
Pebble first.

  * It's not as big or bulky as I expected. It's actually smaller and
    lighter than my Casio.
  * Sleep tracking just works. The fitbit took a few nights of
    fidgeting to figure out how to get it in and out of sleep tracking
    mode. The Pebble featured a MisFit app when I turned it on. I said
    sure, go ahead. That night I didn't bother to figure out how to
    turn on sleep tracking, but when I awoke, lo, there were the data.

I did hit one glitch where the sleep tracker kicked in when I was
watching a movie. And there's no web site integration; Android sync is
["coming soon"][6].

[6]: https://apps.getpebble.com/applications/53a898a2cfee2a02c900006c

Speaking of sleep, I didn't get much that first night because...

  * **Developer support is amazing**. I knew about their open platform
    with a C SDK, but what blew me away was [Pebble.js][1] and
    [CloudPebble][2]. Zero install. Just sign up, grab the example
    javascript, and hit *Install and Run*, and there it is, running on
    your watch. It seems like magic, but it's all just open source.

Two hours later, I had a [working prototype][3] of an app I've been
thinking about since I re-joined the world of commuting: *On my way
home, figure out my ETA and send it to my wife so she can figure it in
to dinner plans.* And if I weren't new to ordinary stuff like
[javascript date handling][js], the [geolocation API][geo], and the
[google maps API][maps], it would have been a lot less than two hours.

[js]: http://stackoverflow.com/a/1197947/846824
[geo]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation
[maps]: https://developers.google.com/maps/documentation/directions/

Quite a contrast from trying out
[IntelliJ's IDE support for Cordova][4]; two hours wasn't even enough
to get the underlying Android SDK installed. I ran out of space on my
devtools and had to grow it. Twice.

While I have the ETA on the Pebble now, I haven't figured out how to
actually send it. I can see how to do it with Ajax to a service like
twilo, but that seems silly; surely I can just get the phone to send
the text.

I might build an app to sync my MisFit data to the fitbit API (though
I'd rather somebody else did that for me). And I'm itching to try
embedded app development with [RustyPebble][], too.

[1]: http://developer.getpebble.com/guides/js-apps/pebble-js/
[2]: https://cloudpebble.net/
[3]: https://github.com/dckc/watch1
[4]: http://blog.jetbrains.com/idea/2014/09/developer-tools-for-phonegap-cordova-and-ionic-in-intellij-idea-14/
[RustyPebble]: https://github.com/franc0is/RustyPebble

Anyway, it's game over. I returned the Vivofit without even opening
it. The Pebble beat out my Casio watch too:

  1. It's a good value, though if I lost or broke it, I'm not sure
     whether I'd replace it right away or make do with the old watch
     for a while. Time will tell.
  2. It's pretty low maintenance. It charges quickly enough that
     there's no conflict with sleep tracking. I just charge it for an
     hour or so every few days while I commute or while I'm at my
     desk. The defaults for notifications were a little overwhelming,
     but it's fine now that I played with the options a bit.
  3. It tells time and date, plus the weather and steps and sleep and
     appointments texts and email and anything else developers like me
     can dream up. Once a boring email message got in the way of job 1
     when I looked for the time. But I'm happy with the trade. I never
     miss a phone call now. And thanks to Android Smart Lock
     integration, it saves me keying in my PIN but about once a day.
 
