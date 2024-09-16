############################################################
# TODO:extract_text from file

# from src.extract_text import extract_text
# if __name__ == '__main__':
#     file = r"D:\Music\男孩 (Live)\男孩 (Live).lrc"
#     extract_text(file)

############################################
# TODO:update_subtitle

from src.update_srt_with_new_subtitles import update_srt_with_new_subtitles
if __name__ == '__main__':
    srt_file = r"D:\Music\男孩 (Live).srt"
    new_subtitles_file = r"D:\Music\new_subtitles.txt"
    update_srt_with_new_subtitles(srt_file, new_subtitles_file)