from instapy import InstaPy
import pickle
import schedule
import time

def job():
    try:

        insta_username = ''
        insta_password = ''

        # if you want to run this script on a server, 
        #simply add nogui=True to the InstaPy() constructor 
        session = InstaPy(username=insta_username, password=insta_password, nogui=True)
        #session.login()
        session.browser.get("https://www.instagram.com")
        for cookie in pickle.load(open("instacookiespowerful.pkl", "rb")):
        session.browser.add_cookie(cookie)

        # set up all the settings
        session.set_upper_follower_count(limit=5000)
        session.set_lower_follower_count(limit=10)
        session.set_do_comment(True, percentage=50)
        session.set_comments([u'Awesome post! :fire: Keep it up :punch: :100:', u'Love it! :heart_eyes:', u'Great post! :thumbsup: :smiley:', u'Nice! :ok_hand: :100:'])
        session.set_dont_like(['male', 'gay', 'drugs', '420', 'sex', 'porn', 'naked', 'boy', 'body'])
        session.set_do_follow(enabled=True, percentage=10, times=1)
        session.unfollow_users(amount=50, onlyInstapyFollowed=True, onlyInstapyMethod = 'FIFO')
        # do the actual liking
        session.like_by_tags(['highprotein', 'postworkoutmeal', 'fitfood'], amount=50)
        # session.like_by_locations(['242342160/wausau-wisconsin/', '222324874/appleton-wisconsin/', '214788051/madison-wisconsin/'], amount=100, skip_top_posts=False)


        # end the bot session
        session.end()
    except:
        import traceback
        print(traceback.format_exc())
        
schedule.every(6).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

                
