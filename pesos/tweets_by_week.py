'''tweets_by_week -- toward 'week in review' PESOS

cf. https://indieweb.org/User:Madmode.com#Dan_Connolly
'''

TEMPLATE = u"""
<div>
  <a href="http://twitter.com/{user}">Twitter</a>: {user}<br>
  {tweet_text}<br>
  <a href="http://twitter.com/{user}/statuses/{status_id}">Posted {tweet_created}</a>

<pre>
{raw}
</pre>

</div>
"""


def main(argv, stdout, environ, Api):
    user_id = argv[1]

    [CONSUMER_KEY,
     CONSUMER_SECRET,
     ACCESS_KEY,
     ACCESS_SECRET] = [
         environ[k] for k in
         '''CONSUMER_KEY
         CONSUMER_SECRET
         ACCESS_KEY
         ACCESS_SECRET'''.split()]

    api = Api(CONSUMER_KEY,
              CONSUMER_SECRET,
              ACCESS_KEY,
              ACCESS_SECRET)

    statuses = api.GetUserTimeline(user_id=user_id)
    # elif kwargs['screenname'] is not None:
    #    statuses = api.GetUserTimeline(screen_name=kwargs['screenname'])

    for status in statuses:
        print >>stdout, (
            TEMPLATE.format(user=status.user.screen_name,
                            tweet_text=status.text,
                            status_id=status.id,
                            raw=status.AsJsonString(),
                            tweet_created=status.created_at)).encode('utf-8')

if __name__ == '__main__':
    def _script():
        from os import environ
        from sys import argv, stdout

        from twitter import Api

        main(argv, stdout, environ, Api)
    _script()
