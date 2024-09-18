import gradio as gr
from .extract_text import extract_text
from .update_srt_with_new_subtitles import update_srt_with_new_subtitles
from .lrc2srt import lrc2srt
from .update_xstudio_lrc import update_xstudio_lrc


def demo_srt():
    with gr.Row():
        srt_file_path = gr.File(label="Upload SRT file", type="filepath")
    with gr.Row():
        srt_output1 = gr.Textbox(label="Original SRT text", lines=10, value="")
        text_input1 = gr.Textbox(label="Input new SRT text", lines=10, value="One subtitle per line")
        srt_output2 = gr.Textbox(label="Updated SRT", lines=10, value="")

    # When srt_file_path changes, automatically call the extract_text function
    srt_file_path.change(
        fn=extract_text,
        inputs=[srt_file_path],
        outputs=[srt_output1],
    )

    with gr.Row():
        update_srt_btn = gr.Button("Update SRT")
    with gr.Row():
        srt_output_path = gr.File(label="Output SRT file", type="filepath")
    with gr.Row():
        update_srt_btn.click(
            fn=update_srt_with_new_subtitles,
            inputs=[srt_file_path, text_input1],
            outputs=[srt_output_path, srt_output2],
        )


def demo_lrc2srt():
    with gr.Row():
        lrc_file_path = gr.File(label="Upload LRC file", type="filepath")
    lrc2srt_btn = gr.Button("RUN")
    with gr.Row():
        lrc_output1 = gr.Textbox(label="Original LRC text", lines=10, value="")
        text_input1 = gr.Textbox(label="Original LRC text", lines=10, value="")
    with gr.Row():
        lrc_output2 = gr.Textbox(label="New SRT text", lines=10, value="")
        text_input2 = gr.Textbox(label="New SRT text", lines=10, value="")
    with gr.Row():
        srt_file_out = gr.File(label="Output SRT file", type="filepath")
        text_file_output = gr.File(label="Output text file", type="filepath")

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


def demo_xstudio_lrc():
    with gr.Row():
        sc_lrc = gr.Textbox(label="sc_lrc", value="", lines=6)
        tgt_lrc = gr.Textbox(label="tgt_lrc", value="", lines=6)
    run_btn = gr.Button("Run")
    output_lrc = gr.Textbox(label="output_lrc", value="", lines=6)
    run_btn.click(fn=update_xstudio_lrc, inputs=[sc_lrc, tgt_lrc], outputs=[output_lrc])
