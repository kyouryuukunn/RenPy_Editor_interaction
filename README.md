This is a test for communication between Ren'Py and an editor.
This is mainly intended to do real time preview in Ren'Py like lightvn

 youtube samples:
 <https://www.youtube.com/watch?v=Wf6O4PFkL2w>

1. Place editor_interaction.rpy into your game directory.
2. Set your Editor to edit interaction_file and write the code which is done by Ren'Py.

This example is vim script

		"" auto warp
		let g:interaction_pass="E:/Soft/renpy/the_question/game/interaction_file"
		
		function! WarpToCurrentLine()
		    if &modified
		        return
		    endif
		
		    let file_path = expand("%:p")
		    let file_path = split(expand("%:p"), "game")[-1][1:]
		    let line_number = line('.')
		    let warp_to_line = "renpy.warp_to_line('".file_path.":".line_number."')"
		    "" write 'renpy.warp_to_line("<current file>:<current line number>")' on temp file.
		    call writefile([warp_to_line], g:interaction_pass)
		endfunction
		
		augroup renpy
			autocmd!
		    "" WarpToCurrentLine function is called per cursor move.
			autocmd CursorMoved *rpy call WarpToCurrentLine()
		augroup END



3. launch the game and set _editor_interaction.interaction_on = 1 then communication with the editor starts.

