from instapy import InstaPy
import schedule
import time


def job():

        try:

                insta_username = ''
                insta_password = ''

                # if you want to run this script on a server, 
                # simply add nogui=True to the InstaPy() constructor
                session = InstaPy(username=insta_username, password=insta_password, nogui=True)
                session.login()

                # set up all the settings
                session.set_upper_follower_count(limit=5000)
                session.set_lower_follower_count(limit=1)
                session.set_do_comment(True, percentage=40)
                session.set_comments([u'Awesome post! :fire:', 'Love it! :heart_eyes:','Great post! :thumbsup:', 'Nice! Keep it up! :ok_hand: :100:'])
                session.set_dont_like(['male', 'gay', 'drugs', '420', 'sex', 'porn'])
                session.set_do_follow(enabled=True, percentage=10, times=1)
                session.unfollow_users(amount=40, onlyInstapyFollowed=True, onlyInstapyMethod = 'FIFO')
                # do the actual liking
                session.like_by_tags(['tag'], amount=100)
                session.like_by_locations(['242342160/wausau-wisconsin/', '222324874/appleton-wisconsin/'], amount=100, skip_top_posts=False)


                # end the bot session
                session.end()

        except:
                import traceback
                print(traceback.format_exc())
                
schedule.every(8).hours.do(job)

while True:
        schedule.run_pending()
        time.sleep(1)