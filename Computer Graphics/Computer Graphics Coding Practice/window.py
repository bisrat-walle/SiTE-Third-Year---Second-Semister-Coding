import glfw

if not glfw.init():
    raise Exception("GLFW cannot be initialized")

window = glfw.create_window(1000, 600, "MY FIRST EVER GRAPHICAL WINDOW", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window cannot be created!")

glfw.set_window_pos(window, 400, 200)
glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()

