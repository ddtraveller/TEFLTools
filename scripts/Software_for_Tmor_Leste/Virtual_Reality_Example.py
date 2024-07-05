import openvr
import pyglet
from pyglet.gl import *
import numpy as np
import ctypes

# Initialize OpenVR
openvr.init(openvr.VRApplication_Scene)
compositor = openvr.VRCompositor()

# Create a window
window = pyglet.window.Window(width=1280, height=720, caption='VR Mirror')

# Set up VR system
vr_system = openvr.VRSystem()

# Get recommended render target size
width, height = vr_system.getRecommendedRenderTargetSize()

# Create frame buffers and textures for left and right eyes
def create_framebuffer():
    framebuffer = GLuint()
    glGenFramebuffers(1, ctypes.byref(framebuffer))
    glBindFramebuffer(GL_FRAMEBUFFER, framebuffer)
    
    texture = GLuint()
    glGenTextures(1, ctypes.byref(texture))
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, None)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texture, 0)
    
    return framebuffer, texture

left_fb, left_texture = create_framebuffer()
right_fb, right_texture = create_framebuffer()

# Compile shaders
vertex_shader = """
#version 150
in vec3 position;
uniform mat4 mvp;
void main() {
    gl_Position = mvp * vec4(position, 1.0);
}
"""

fragment_shader = """
#version 150
out vec4 outColor;
void main() {
    outColor = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

def compile_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise RuntimeError(glGetShaderInfoLog(shader))
    return shader

vertex_shader = compile_shader(GL_VERTEX_SHADER, vertex_shader)
fragment_shader = compile_shader(GL_FRAGMENT_SHADER, fragment_shader)

# Link shaders
program = glCreateProgram()
glAttachShader(program, vertex_shader)
glAttachShader(program, fragment_shader)
glLinkProgram(program)
if not glGetProgramiv(program, GL_LINK_STATUS):
    raise RuntimeError(glGetProgramInfoLog(program))

glUseProgram(program)

# Create a simple cube
vertices = np.array([
    -0.5, -0.5, -0.5,
     0.5, -0.5, -0.5,
     0.5,  0.5, -0.5,
    -0.5,  0.5, -0.5,
    -0.5, -0.5,  0.5,
     0.5, -0.5,  0.5,
     0.5,  0.5,  0.5,
    -0.5,  0.5,  0.5,
], dtype=np.float32)

indices = np.array([
    0, 1, 2, 2, 3, 0,
    1, 5, 6, 6, 2, 1,
    5, 4, 7, 7, 6, 5,
    4, 0, 3, 3, 7, 4,
    3, 2, 6, 6, 7, 3,
    4, 5, 1, 1, 0, 4
], dtype=np.uint32)

# Create VAO and VBO
vao = GLuint()
glGenVertexArrays(1, ctypes.byref(vao))
glBindVertexArray(vao)

vbo = GLuint()
glGenBuffers(1, ctypes.byref(vbo))
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

ebo = GLuint()
glGenBuffers(1, ctypes.byref(ebo))
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

position_attrib = glGetAttribLocation(program, b"position")
glEnableVertexAttribArray(position_attrib)
glVertexAttribPointer(position_attrib, 3, GL_FLOAT, GL_FALSE, 0, 0)

# Main rendering loop
@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    for eye in range(2):
        glBindFramebuffer(GL_FRAMEBUFFER, left_fb if eye == 0 else right_fb)
        glViewport(0, 0, width, height)
        
        # Get eye transformation and projection
        eye_transform = vr_system.getEyeToHeadTransform(eye)
        proj_matrix = vr_system.getProjectionMatrix(eye, 0.1, 100.0)
        
        # Combine matrices
        mvp = np.dot(proj_matrix, np.linalg.inv(eye_transform))
        mvp_uniform = glGetUniformLocation(program, b"mvp")
        glUniformMatrix4fv(mvp_uniform, 1, GL_FALSE, mvp.flatten())
        
        # Draw cube
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
    
    # Submit frames to compositor
    compositor.submit(openvr.Eye_Left, openvr.Texture_t(handle=left_texture.value, eType=openvr.TextureType_OpenGL, eColorSpace=openvr.ColorSpace_Gamma))
    compositor.submit(openvr.Eye_Right, openvr.Texture_t(handle=right_texture.value, eType=openvr.TextureType_OpenGL, eColorSpace=openvr.ColorSpace_Gamma))
    
    # Render to window (mirror)
    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glViewport(0, 0, window.width, window.height)
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Here you would render the mirror view to the window

pyglet.app.run()

# Clean up
openvr.shutdown()