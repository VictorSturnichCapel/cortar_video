import yt_dlp
from moviepy.video.io.VideoFileClip import VideoFileClip

def download_video(url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_filename = ydl.prepare_filename(info_dict)
    return video_filename

def create_clips(video_path, clip_duration=25):
    video = VideoFileClip(video_path)
    video_duration = int(video.duration)
    for start_time in range(0, video_duration, clip_duration):
        end_time = min(start_time + clip_duration, video_duration)
        clip = video.subclip(start_time, end_time)
        clip_filename = f"{video_path[:-4]}_clip_{start_time}_{end_time}.mp4"
        clip.write_videofile(clip_filename, codec='libx264')
        print(f"Created clip: {clip_filename}")

url = 'link_do_video'
output_path = "caminho_de_saida"
video_filename = download_video(url, output_path)
create_clips(video_filename)
