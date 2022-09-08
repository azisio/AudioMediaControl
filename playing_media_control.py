import asyncio
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager

# 現在再生中の曲情報
async def get_all_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
            info = await current_session.try_get_media_properties_async()
            info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}
            info_dict['genres'] = list(info_dict['genres'])
            return info_dict
    raise Exception('現在再生中のプロセスが存在しません')

# 再生中のメディアを停止
async def stop_current_media():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        current_session.try_stop_async()
        return
    raise Exception('現在再生中のプロセスが存在しません')

# 再生中のメディアを一時停止
async def pause_current_media():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        current_session.try_pause_async()
        return        
    raise Exception('現在再生中のプロセスが存在しません')

# 再生中のメディアを再生
async def play_current_media():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        current_session.try_play_async()
        return        
    raise Exception('現在再生中のプロセスが存在しません')

# 再生中のメディアのシャッフル機能を有効/無効
async def shuffle_current_media(enable:bool):
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        current_session.try_change_shuffle_active_async(enable)
        return        
    raise Exception('現在再生中のプロセスが存在しません')

# 次のトラックを再生
async def skip_next_current_media():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        current_session.try_skip_next_async()
        return        
    raise Exception('現在再生中のプロセスが存在しません')

# 前のトラックを再生
async def skip_previous_current_media():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        current_session.try_skip_previous_async()
        return        
    raise Exception('現在再生中のプロセスが存在しません')

if __name__ == '__main__':
    current_media_info = asyncio.run(get_all_media_info())
    print(current_media_info)

    # asyncio.run(pause_current_media())
    # asyncio.run(play_current_media())
    # asyncio.run(stop_current_media())
    # asyncio.run(shuffle_current_media(True))
    # asyncio.run(shuffle_current_media(False))
    # asyncio.run(skip_next_current_media())
    # asyncio.run(skip_previous_current_media())