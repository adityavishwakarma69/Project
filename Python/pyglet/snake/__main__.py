import pyglet

window = pyglet.window.Window()

rectimg = lambda width, height, color: pyglet.image.create(width, height, pyglet.image.SolidColorImagePattern(color))

@window.event
def on_draw():
    window.clear()

    rectimg(20, 20, (255, 255, 255, 0)).blit(20, 20)


pyglet.app.run()
