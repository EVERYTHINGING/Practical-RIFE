from moviepy.editor import VideoFileClip, CompositeVideoClip, vfx
import random

bg = VideoFileClip("bg.mp4")
flowers = VideoFileClip("flowers.mp4")
flowers = vfx.mask_color(flowers)

layers = [bg]

for i in range(1,30):
  layer = flowers.resize((random.random()/2)+0.5)
  
  if random.random() > 0.5:
    layer = layer.fx(vfx.mirror_x)

  if random.random() > 0.5:
    layer = layer.fx(vfx.mirror_y)

  layer = layer.rotate(random.random()*360)

  distx = (random.random()*100)+300
  distx *= 1 if (random.random() > 0.5) else -1
  posx = (bg.w/2)
  posx += distx
  posx -= (layer.w/2)

  disty = (random.random()*100)+300
  disty *= 1 if (random.random() > 0.5) else -1
  posy = (bg.h/2)
  posy += disty
  posy -= (layer.h/2)

  print(posx, posy)
  
  layer = layer.set_position((posx, posy))
  layers.append(layer)


output = CompositeVideoClip(layers)
output.write_videofile("out.mp4")