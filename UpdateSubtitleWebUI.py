import argparse
from src.update_xstudio_lrc import update_xstudio_lrc
from src.extract_text import extract_text
from src.lrc2srt import lrc2srt
from src.update_srt_with_new_subtitles import (
    update_srt_with_new_subtitles,
)
from src.log import logger
import gradio as gr


with gr.Blocks() as demo:
    with gr.TabItem("Update Subtitle"):
        with gr.TabItem("SRT"):
            with gr.Row():
                srt_file_path = gr.File(label="上传srt文件", type="filepath")
            with gr.Row():
                srt_output1 = gr.Textbox(label="原srt文本", lines=10, value="")
                text_input1 = gr.Textbox(
                    label="输入新srt文本", lines=10, value="每行一个字幕"
                )
                srt_output2 = gr.Textbox(label="更新srt", lines=10, value="")

            # 当 srt_file_path 发生变化时，自动调用 extract_text 函数
            srt_file_path.change(
                fn=extract_text,
                inputs=[srt_file_path],
                outputs=[srt_output1],
            )

            with gr.Row():
                update_srt_btn = gr.Button("更新srt")
            with gr.Row():
                srt_output_path = gr.File(label="输出srt文件", type="filepath")
            with gr.Row():
                update_srt_btn.click(
                    fn=update_srt_with_new_subtitles,
                    inputs=[srt_file_path, text_input1],
                    outputs=[srt_output_path, srt_output2],
                )

        with gr.TabItem("LRC2SRT"):
            with gr.Row():
                lrc_file_path = gr.File(label="上传lrc文件", type="filepath")
            lrc2srt_btn = gr.Button("RUN")
            with gr.Row():
                lrc_output1 = gr.Textbox(label="原lrc文本", lines=10, value="")
                text_input1 = gr.Textbox(label="原lrc文本", lines=10, value="")
            with gr.Row():
                lrc_output2 = gr.Textbox(label="新srt文本", lines=10, value="")
                text_input2 = gr.Textbox(label="新srt文本", lines=10, value="")
            with gr.Row():
                srt_file_out = gr.File(label="输出srt文件", type="filepath")
                text_file_output = gr.File(label="输出text文件", type="filepath")

            lrc2srt_btn.click(
                fn=lrc2srt,
                inputs=[lrc_file_path],
                outputs=[
                    lrc_output1,
                    text_input1,
                    lrc_output2,
                    text_input2,
                    srt_file_out,
                    text_file_output,
                ],
            )

        with gr.TabItem("X studiolrc"):
            with gr.Row():
                sc_lrc = gr.Textbox(label="sc_lrc", value="", lines=6)
                tgt_lrc = gr.Textbox(label="tgt_lrc", value="", lines=6)
            run_btn = gr.Button("run")
            output_lrc = gr.Textbox(label="output_lrc", value="", lines=6)
            run_btn.click(
                fn=update_xstudio_lrc, inputs=[sc_lrc, tgt_lrc], outputs=[output_lrc]
            )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo")
    parser.add_argument(
        "--server_name", type=str, default="localhost", help="server name"
    )
    parser.add_argument("--server_port", type=int, default=8080, help="server port")
    parser.add_argument("--root_path", type=str, default=None, help="root path")
    args = parser.parse_args()

    demo.launch(
        server_name=args.server_name,
        server_port=args.server_port,
        root_path=args.root_path,
        show_api=False,
    )
