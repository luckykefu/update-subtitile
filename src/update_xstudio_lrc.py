# 假设 `logger` 已经正确配置
from .log import get_logger

logger = get_logger(__name__)


def update_xstudio_lrc(sc_lrc=None, tgt_lrc=None):
    """
    更新 XStudio LRC 文件中的字符。

    :param sc_lrc: 原始 LRC 文件内容（带有时间戳）
    :param tgt_lrc: 目标 LRC 文件内容（仅包含文本）
    :return: 更新后的 LRC 文件内容
    """
    try:
        # 日志记录开始
        logger.info("Starting update_xstudio_lrc function.")

        # 检查输入参数是否为空
        if not sc_lrc or not tgt_lrc:
            logger.error("Input parameters cannot be empty.")
            raise ValueError("Input parameters cannot be empty.")

        # 读取原有歌词
        logger.info("Removing newline characters from input strings.")
        tgt_lrc = tgt_lrc.replace("\n", "").replace(" ", "")
        sc_lrc = sc_lrc.replace("\n", " ")

        # 将目标歌词分割为字符列表
        logger.info("Converting target lyrics into character list.")
        tgt_lrc_char_list = list(tgt_lrc)

        # 将原始 LRC 文件分割为空间分隔的字符列表
        logger.info("Splitting source LRC into space-separated character list.")
        sc_lrc_char_list = sc_lrc.split(" ")

        # 替换字符
        logger.info("Replacing characters in the source LRC list.")
        min_length = min(len(sc_lrc_char_list), len(tgt_lrc_char_list))
        for i in range(min_length):
            sc_lrc_char_list[i] = tgt_lrc_char_list[i]

        # 将列表中的元素用空格连接起来
        logger.info("Joining the updated character list.")
        updated_sc_lrc = " ".join(sc_lrc_char_list)
        logger.info(f"Updated LRC: {updated_sc_lrc}")
        # 日志记录结束
        logger.info("update_xstudio_lrc function completed successfully.")
        return updated_sc_lrc

    except Exception as e:
        logger.error(f"An error occurred during LRC update: {e}")
        raise


# 示例调用
# result = update_xstudio_lrc(sc_lrc="00:01.000 [hello world]", tgt_lrc="你好 世界")
# print(result)
