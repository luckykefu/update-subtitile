import os
import re
from .log import get_logger
logger = get_logger(__name__)




def parse_lrc_time(line):
    """解析 LRC 时间标签"""
    time_pattern = re.compile(r"\[(\d+):(\d+)\.(\d+)\]")
    time_match = time_pattern.match(line)
    if time_match:
        minutes = int(time_match.group(1))
        seconds = int(time_match.group(2))
        milliseconds = int(time_match.group(3)) * 100  # 转换成毫秒
        return f"{minutes:02}:{seconds:02}.{milliseconds:03}"
    return None


def extract_timestamps_and_texts(lines):
    """提取所有时间戳和文本"""
    timestamps = []
    texts = []

    for line in lines:
        parsed_time = parse_lrc_time(line)
        if parsed_time:
            text = re.sub(r"\[\d+:\d+\.\d+\]", "", line).strip()
            timestamps.append(parsed_time)
            texts.append(text)

    return timestamps, texts


def generate_srt_content(timestamps, texts):
    """生成 SRT 文件内容"""
    srt_content = []
    index = 1

    for i in range(len(timestamps)):
        start_time = timestamps[i]
        end_time = (
            timestamps[i + 1]
            if i < len(timestamps) - 1
            else calculate_end_time(start_time)
        )

        srt_content.append(f"{index}\n{start_time} --> {end_time}\n{texts[i]}\n")
        index += 1

    return srt_content


def calculate_end_time(start_time):
    """计算最后一个时间戳的结束时间，默认持续两秒"""
    try:
        parts = start_time.replace(",", ":").split(":")
        if len(parts) != 3:
            logger.error(f"Invalid time format: {start_time}")
            return start_time  # 返回原始时间戳作为默认值

        minutes = int(parts[0])
        seconds = float(parts[1])
        milliseconds = int(float(parts[2]))

        end_seconds = seconds + 2
        end_minutes = minutes

        if end_seconds >= 60:
            end_seconds -= 60
            end_minutes += 1

        return f"{end_minutes:02}:{int(end_seconds):02},{milliseconds:03}"
    except ValueError as e:
        logger.error(f"Failed to parse time '{start_time}': {e}")
        return start_time  # 返回原始时间戳作为默认值


def write_files(srt_content, pure_text):
    """写入 SRT 和纯文本文件"""
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    srt_file_path = os.path.join(temp_dir, "output.srt")
    text_file_path = os.path.join(temp_dir, "pure_text.txt")

    with open(srt_file_path, "w", encoding="utf-8") as srt_file:
        srt_file.write("\n".join(srt_content))

    with open(text_file_path, "w", encoding="utf-8") as text_file:
        text_file.write("\n".join(pure_text))

    return srt_file_path, text_file_path


def extract_lyrics_from_lrc(lrc_content):
    """
    从 LRC 文件内容中提取纯文本歌词。

    :param lrc_content: LRC 文件的内容。
    :return: 纯文本歌词。
    """
    try:
        # 日志记录开始
        logger.info("Starting extract_lyrics_from_lrc function.")

        # 使用正则表达式移除时间标签
        logger.info("Extracting pure text from LRC content.")
        time_pattern = re.compile(r"\[\d+:\d+\.\d+\]")
        lyrics = []

        lines = lrc_content.split("\n")
        for line in lines:
            # 移除时间标签
            pure_text = time_pattern.sub("", line).strip()
            if pure_text:
                lyrics.append(pure_text)

        # 日志记录结束
        logger.info("extract_lyrics_from_lrc function completed successfully.")
        return "\n".join(lyrics)

    except Exception as e:
        logger.error(f"An error occurred during LRC extraction: {e}")
        raise


def lrc2srt(lrc_file):
    """
    将 LRC 文件转换为 SRT 文件。

    :param lrc_file: LRC 文件的路径。
    :return: SRT 文件的路径。
    """
    try:
        # 读取 LRC 文件
        logger.info("Reading LRC file...")
        with open(lrc_file, "r", encoding="utf-8") as file:
            lrc_content = file.read()
        lrc_pure_text = extract_lyrics_from_lrc(lrc_content)
        # 解析 LRC 文件
        logger.info("Parsing LRC file...")
        lines = lrc_content.split("\n")
        timestamps, texts = extract_timestamps_and_texts(lines)

        # 生成 SRT 内容
        logger.info("Generating SRT content...")
        srt_content = generate_srt_content(timestamps, texts)

        # 写入 SRT 和纯文本文件
        logger.info("Writing files...")
        srt_file_path, text_file_path = write_files(srt_content, texts)

        logger.info("LRC to SRT conversion complete.")
        return (
            lrc_content,
            lrc_pure_text,
            "\n".join(srt_content),
            "\n".join(texts),
            srt_file_path,
            text_file_path,
        )

    except Exception as e:
        logger.error(f"An error occurred during LRC to SRT conversion: {e}")
        raise


# 示例调用
# result = lrc2srt("path/to/lrc_file.lrc")
# print(result)
