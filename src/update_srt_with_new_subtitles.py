import os
import pysrt
from .log import get_logger
logger = get_logger(__name__)




def update_srt_with_new_subtitles(srt_file_path, text_input1):
    """
    从列表中读取新字幕，并更新 SRT 文件中的原有字幕。

    :param srt_file_path: SRT 文件的路径。
    :param text_input1: 包含新字幕文本的字符串。
    """
    new_subtitles = text_input1.split("\n")
    # 去除空白行
    new_subtitles = [line for line in new_subtitles if line.strip()]
    logger.info(f"New subtitles: {new_subtitles}")

    # 读取 SRT 文件
    subs = pysrt.open(srt_file_path, encoding="utf-8")

    # 初始化一个索引来跟踪新字幕列表
    new_subtitle_index = 0

    # 遍历 SRT 文件中的每个字幕条目
    for sub in subs:
        if new_subtitle_index < len(new_subtitles):
            # 使用新字幕替换原有字幕
            sub.text = new_subtitles[new_subtitle_index]
            new_subtitle_index += 1
        else:
            # 如果新字幕不足，则保留原有字幕
            pass

    # 构建更新后的 SRT 文件路径
    srt_output_path = os.path.splitext(srt_file_path)[0] + "_updated.srt"

    # 写回更新后的 SRT 文件
    subs.save(srt_output_path, encoding="utf-8")

    # 处理后的文本
    formatted_text = []
    for sub in subs:
        # 格式化每一行
        formatted_line = f"{sub.index}\n{sub.start} --> {sub.end}\n{sub.text}\n\n"
        formatted_text.append(formatted_line)

    # 输出处理后的文本
    formatted_text_str = "".join(formatted_text)
    logger.info(formatted_text_str)
    logger.info(f"Updated SRT file saved to {srt_output_path}")

    return srt_output_path, formatted_text_str
