init python in _editor_interaction:
    interaction_filepass = "interaction_file"
    last_mtime = None
    interaction_on = 0

init python hide:
    def editor_interaction():
        if not _editor_interaction.interaction_on:
            return
        if _editor_interaction.interaction_filepass:
            fn = renpy.loader.get_path(_editor_interaction.interaction_filepass)
            next_mtime = renpy.loader.auto_mtime(fn)
            if next_mtime:
                if _editor_interaction.last_mtime is None:
                    _editor_interaction.last_mtime = next_mtime
                elif next_mtime > _editor_interaction.last_mtime:
                    _editor_interaction.last_mtime = next_mtime
                    f = open(fn)
                    code = f.read()
                    f.close()
                    if code:
                        renpy.python.py_eval(code[:-1])
            else:
                _editor_interaction.last_mtime = next_mtime

    config.periodic_callback = editor_interaction
