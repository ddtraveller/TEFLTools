from PIL import Image, ImageDraw
import math

def create_spiral(size, filename):
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    
    center_x, center_y = size // 2, size // 2
    radius = 0
    angle = 0
    
    while radius < size // 2:
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        draw.point((x, y), fill="black")
        
        radius += 0.1
        angle += 0.1
    
    image.save(filename, "JPEG")

def create_branching(size, filename):
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    
    def draw_branch(start_x, start_y, length, angle):
        if length < 5:
            return
        
        end_x = start_x + int(length * math.cos(angle))
        end_y = start_y + int(length * math.sin(angle))
        
        draw.line((start_x, start_y, end_x, end_y), fill="black", width=2)
        
        draw_branch(end_x, end_y, length * 0.7, angle + math.pi / 6)
        draw_branch(end_x, end_y, length * 0.7, angle - math.pi / 6)
    
    draw_branch(size // 2, size, size // 3, -math.pi / 2)
    
    image.save(filename, "JPEG")

def create_waves(size, filename):
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    
    for y in range(0, size, 20):
        for x in range(size):
            offset = int(25 * math.sin(x * 0.05 + y * 0.1))
            draw.point((x, y + offset), fill="black")
    
    image.save(filename, "JPEG")

def create_tessellations(size, filename):
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    
    hexagon_size = 20
    hexagon_height = int(hexagon_size * math.sqrt(3) / 2)
    
    for y in range(0, size, hexagon_height):
        for x in range(0, size, hexagon_size):
            if y % (2 * hexagon_height) < hexagon_height:
                offset = hexagon_size // 2
            else:
                offset = 0
            
            draw.regular_polygon((x + offset, y, hexagon_size), 6, fill="black")
    
    image.save(filename, "JPEG")

# Generate the example images
create_spiral(500, "spiral.jpg")
create_branching(500, "branching.jpg")
create_waves(500, "waves.jpg")
create_tessellations(500, "tessellations.jpg")