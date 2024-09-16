############################################################
# TODO:extract_text from file

# from src.extract_text import extract_text
# if __name__ == '__main__':
#     file = r"D:\Music\男孩 (Live)\男孩 (Live).lrc"
#     extract_text(file)

############################################
# TODO:update_subtitle

# from src.update_srt_with_new_subtitles import update_srt_with_new_subtitles
# if __name__ == '__main__':
#     srt_file = r"test.srt"
#     new_subtitles_file = """
#     sldkjf
#     sldjf
# """
#     update_srt_with_new_subtitles(srt_file, new_subtitles_file)

#######################################################
# TODO:lrc2srt

# from src.lrc2srt import lrc2srt
# if __name__ == '__main__':
#     lrc_file = r"D:\Music\music\5_20AM(我在5_20睡觉13_14准时起) - 刀酱.txt"
#     lrc2srt(lrc_file)

########################################################
# TODO:update xstudio lrc

from src.update_xstudio_lrc import update_xstudio_lrc
if __name__ == '__main__':
    sc_lrc="""
sl ls lsfl sldk 
"""
    tgt_lrc="""
1 2 3 4
"""

    update_xstudio_lrc(sc_lrc, tgt_lrc)