from spotify_local import (
    SpotifyLocal,
    start_spotify,
    start_spotify_web_helper,
    is_spotify_running,
    is_spotify_web_helper_running,
)
from time import sleep

# s = SpotifyLocal()


# @s.on("play_state_change")
# def test(status):
#     print("Play Pause Engaged")


# # @s.on("status_change")
# # def test1(status):
# #     print("new status")


# @s.on("track_change")
# def test2(status):
#     print("track changed")


# print(s._registered_events)

# s.listen(blocking=True)

# print("let's see if this prints out")

# sleep(120)


print(is_spotify_running())
print(is_spotify_web_helper_running())
# start_spotify_web_helper()
start_spotify()
