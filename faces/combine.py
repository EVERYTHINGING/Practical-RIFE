from moviepy.editor import VideoFileClip, CompositeVideoClip, vfx
bg = VideoFileClip("bg.mp4")
flowers = VideoFileClip("flowers.mp4")
flowers = vfx.mask_color(flowers)

layers = [bg]

for i in range(1,5):
  layer = flowers.resize(1/i)
  layer.set_position((500, 500))
  layers.append(layer)


output = CompositeVideoClip(layers)
output.write_videofile("out.mp4")