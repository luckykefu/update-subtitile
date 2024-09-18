import argparse
import os
from src.demo import demo_srt, demo_lrc2srt, demo_xstudio_lrc
from src.log import get_logger

logger = get_logger(__name__)
import gradio as gr

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def parse_arguments():

    # Parse command line arguments.
    parser = argparse.ArgumentParser(description=f"{__file__}")
    parser.add_argument(
        "--server_name", type=str, default="localhost", help="Server name"
    )
    parser.add_argument("--server_port", type=int, default=None, help="Server port")
    parser.add_argument("--root_path", type=str, default=None, help="Root path")
    return parser.parse_args()


def main():
    args = parse_arguments()

    with gr.Blocks() as demo:
        with gr.TabItem("Update Subtitle"):
            with gr.TabItem("SRT"):
                demo_srt()
        with gr.TabItem("LRC2SRT"):
            demo_lrc2srt()

        with gr.TabItem("X studiolrc"):
            demo_xstudio_lrc()

        demo.launch(
            server_name=args.server_name,
            server_port=args.server_port,
            root_path=args.root_path,
            show_api=False,
        )


if __name__ == "__main__":
    main()
