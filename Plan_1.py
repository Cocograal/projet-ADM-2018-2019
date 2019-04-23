"""
Created for the ungratful William by my humble self

-Diana
"""

def chart(canvas):
    obstacles = []
    obstacles.append(canvas.create_rectangle(120,180,125,460, fill='tan1', outline='tan2')) 
    obstacles.append(canvas.create_rectangle(120,180,125,460, fill='tan1', outline='tan2')) 
    obstacles.append(canvas.create_rectangle(480,180,560,185, fill='chocolate1',outline='chocolate2'))
    obstacles.append(canvas.create_rectangle(480,180,560,185, fill='chocolate1',outline='chocolate2'))
    obstacles.append(canvas.create_rectangle(475,180,480,460, fill='chocolate1', outline='chocolate2'))
    obstacles.append(canvas.create_rectangle(475,180,480,460, fill='chocolate1', outline='chocolate2'))
    obstacles.append(canvas.create_oval(280,134,320,439, fill='lightseagreen', outline='lightseagreen'))
    obstacles.append(canvas.create_rectangle(40,455,120,460, fill='tan1', outline='tan2'))
    obstacles.append(canvas.create_rectangle(40,455,120,460, fill='tan1', outline='tan2'))
    
    return obstacles