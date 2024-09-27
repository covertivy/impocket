import cmd2

HIST_LEN = 10_000

class PocketCMD(cmd2.Cmd):
    def __init__(
        self,
    ) -> None:
        super().__init__(
            persistent_history_file=None,
            persistent_history_length=HIST_LEN,
            startup_script=None,
            silence_startup_script=True,
            include_py=False,
            include_ipy=False,
            allow_cli_args=False,
            transcript_files=None,
            allow_redirection=False,
            multiline_commands=False,
            terminators=None,
            shortcuts=None,
            command_sets=None,
            auto_load_commands=True
        )
        pass